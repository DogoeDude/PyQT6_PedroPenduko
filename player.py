from dataclasses import dataclass
from typing import Dict, List

@dataclass
class PlayerStats:
    hp: int
    max_hp: int
    attack: int
    defense: int
    magic: int
    level: int
    exp: int
    exp_to_next: int
    items: List[str]
    skills: List[str]

class Player:
    def __init__(self):
        self.stats = PlayerStats(
            hp=100,
            max_hp=100,
            attack=10,
            defense=5,
            magic=8,
            level=1,
            exp=0,
            exp_to_next=100,
            items=[],
            skills=["Basic Attack"]
        )
        
    def take_damage(self, damage: int) -> int:
        """Returns actual damage taken after defense calculation"""
        actual_damage = max(1, damage - self.stats.defense)
        self.stats.hp = max(0, self.stats.hp - actual_damage)
        return actual_damage
    
    def heal(self, amount: int):
        self.stats.hp = min(self.stats.max_hp, self.stats.hp + amount)
    
    def gain_exp(self, exp: int) -> bool:
        """Returns True if leveled up"""
        self.stats.exp += exp
        if self.stats.exp >= self.stats.exp_to_next:
            self.level_up()
            return True
        return False
    
    def level_up(self):
        self.stats.level += 1
        self.stats.max_hp += 20
        self.stats.hp = self.stats.max_hp
        self.stats.attack += 5
        self.stats.defense += 3
        self.stats.magic += 4
        self.stats.exp -= self.stats.exp_to_next
        self.stats.exp_to_next = int(self.stats.exp_to_next * 1.5) 