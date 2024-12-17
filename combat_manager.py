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
    special_moves: Dict[str, Dict] = None

class CombatManager:
    def __init__(self, player):
        self.player = player
        self.current_enemy: Optional[Enemy] = None
        
        self.enemies = {
            "Engkanto Twins": Enemy(
                name="Engkanto Twins",
                hp=250,
                max_hp=250,
                attack=45,
                defense=15,
                exp_reward=300,
                item_drop="Twin Essence",
                special_moves={
                    "Dual Strike": {"damage": 65, "chance": 0.3},
                    "Light Shield": {"defense_boost": 10, "chance": 0.2}
                }
            ),
            
            "Guardian of the Abyss": Enemy(
                name="Guardian of the Abyss",
                hp=400,
                max_hp=400,
                attack=60,
                defense=25,
                exp_reward=500,
                item_drop="Time Crystal",
                special_moves={
                    "Time Warp": {"damage": 85, "chance": 0.3},
                    "Temporal Shield": {"heal": 60, "chance": 0.25}
                }
            ),
            
            "Corrupted Dilim": Enemy(
                name="Corrupted Dilim",
                hp=600,
                max_hp=600,
                attack=75,
                defense=30,
                exp_reward=1000,
                item_drop="Balance Stone",
                special_moves={
                    "Dimension Crush": {"damage": 100, "chance": 0.35},
                    "Void Shield": {"defense_boost": 20, "heal": 75, "chance": 0.25}
                }
            )
        }
    
    def start_combat(self, enemy_name: str) -> str:
        """Start combat with an enemy, returns initial combat message"""
        if enemy_name in self.enemies:
            self.current_enemy = self.enemies[enemy_name]
            return f"Combat started with {enemy_name}!"
        return "Enemy not found!"
    
    def player_attack(self) -> str:
        """Enhanced player attack with critical hits and combos"""
        if not self.current_enemy:
            return "No enemy to attack!"
            
        # Critical hit system with improved chances and damage
        critical_chance = random.random()
        base_damage = self.player.stats.attack * random.uniform(0.9, 1.3)  # Increased variance
        
        if critical_chance > 0.85:  # 15% crit chance
            damage = int(base_damage * 2.0)  # Increased crit multiplier
            message = "Critical hit! "
        else:
            damage = int(base_damage)
            message = ""
            
        # Improved damage calculation against defense
        defense_reduction = self.current_enemy.defense * 0.7  # Reduced defense effectiveness
        actual_damage = max(1, damage - defense_reduction)
        self.current_enemy.hp -= actual_damage
        
        if self.current_enemy.hp <= 0:
            return self.handle_victory()
            
        return f"{message}You deal {actual_damage} damage to {self.current_enemy.name}!"
    
    def enemy_attack(self) -> str:
        """Enhanced enemy AI with improved special moves"""
        if not self.current_enemy:
            return "No enemy attacking!"
            
        # More aggressive special move usage when HP is low
        hp_percentage = self.current_enemy.hp / self.current_enemy.max_hp
        special_chance_boost = 1.0 + (1.0 - hp_percentage) * 0.5  # Up to 50% increased chance
            
        # Check for special moves with boosted chance
        for move_name, effects in self.current_enemy.special_moves.items():
            if random.random() < effects["chance"] * special_chance_boost:
                return self.execute_special_move(move_name, effects)
        
        # Enhanced regular attack with better randomization
        base_damage = self.current_enemy.attack * random.uniform(0.9, 1.4)  # Increased variance
        damage = self.player.take_damage(int(base_damage))
        return f"{self.current_enemy.name} deals {damage} damage to you!"
    
    def execute_special_move(self, move_name: str, effects: Dict) -> str:
        """Execute enemy special move"""
        message = f"{self.current_enemy.name} uses {move_name}! "
        
        if "damage" in effects:
            damage = self.player.take_damage(effects["damage"])
            message += f"Deals {damage} damage! "
            
        if "defense_boost" in effects:
            self.current_enemy.defense += effects["defense_boost"]
            message += f"Defense increased by {effects['defense_boost']}! "
            
        if "heal" in effects:
            heal_amount = min(effects["heal"], 
                            self.current_enemy.max_hp - self.current_enemy.hp)
            self.current_enemy.hp += heal_amount
            message += f"Heals for {heal_amount} HP! "
            
        return message
    
    def handle_victory(self) -> str:
        """Handle victory with balanced rewards"""
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