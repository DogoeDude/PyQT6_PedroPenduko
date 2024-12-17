from dataclasses import dataclass
from typing import Dict, Optional
import random

@dataclass
class Enemy:
    name: str
    hp: int
    max_hp: int
    attack: int
    defense: int
    exp_reward: int
    item_drop: Optional[str] = None

class CombatManager:
    def __init__(self, player):
        self.player = player
        self.current_enemy: Optional[Enemy] = None
        
        self.enemies = {
            "Engkanto Twin": Enemy(
                name="Engkanto Twin",
                hp=80,
                max_hp=80,
                attack=15,
                defense=8,
                exp_reward=50,
                item_drop="Light Essence"
            ),
            "Molten Tikbalang": Enemy(
                name="Molten Tikbalang",
                hp=150,
                max_hp=150,
                attack=25,
                defense=15,
                exp_reward=100,
                item_drop="Volcano Core"
            ),
            # Add more enemies...
        }
    
    def start_combat(self, enemy_name: str) -> str:
        """Start combat with an enemy, returns initial combat message"""
        if enemy_name in self.enemies:
            self.current_enemy = self.enemies[enemy_name]
            return f"Combat started with {enemy_name}!"
        return "Enemy not found!"
    
    def player_attack(self) -> str:
        """Process player's attack, returns combat message"""
        if not self.current_enemy:
            return "No enemy to attack!"
            
        damage = max(1, self.player.stats.attack - self.current_enemy.defense)
        self.current_enemy.hp -= damage
        
        if self.current_enemy.hp <= 0:
            return self.handle_victory()
            
        return f"You deal {damage} damage to {self.current_enemy.name}!"
    
    def enemy_attack(self) -> str:
        """Process enemy's attack, returns combat message"""
        if not self.current_enemy:
            return "No enemy attacking!"
            
        damage = self.player.take_damage(self.current_enemy.attack)
        return f"{self.current_enemy.name} deals {damage} damage to you!"
    
    def handle_victory(self) -> str:
        """Handle victory conditions and rewards"""
        if not self.current_enemy:
            return "No enemy defeated!"
            
        exp_gained = self.current_enemy.exp_reward
        leveled_up = self.player.gain_exp(exp_gained)
        
        message = f"Victory! Defeated {self.current_enemy.name}!\n"
        message += f"Gained {exp_gained} EXP!\n"
        
        if self.current_enemy.item_drop:
            self.player.stats.items.append(self.current_enemy.item_drop)
            message += f"Obtained {self.current_enemy.item_drop}!\n"
            
        if leveled_up:
            message += f"Level Up! Now level {self.player.stats.level}!"
            
        self.current_enemy = None
        return message 