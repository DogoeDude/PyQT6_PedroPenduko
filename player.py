from dataclasses import dataclass
from typing import Dict, List, Tuple

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
    gold: int = 100  # Starting gold
    items: List[str] = None
    potions: Dict[str, int] = None  # Count of each potion type

class Player:
    def __init__(self):
        self.stats = PlayerStats(
            hp=300,
            max_hp=300,
            attack=35,
            defense=20,
            magic=25,
            level=1,
            exp=0,
            exp_to_next=100,
            gold=200,
            items=[],
            potions={
                "Minor Healing Potion": 3,
                "Major Healing Potion": 1,
                "Full Restore Potion": 0
            }
        )
        # Add a set to track defeated bosses
        self.defeated_bosses = set()
        self.training_bonuses = {
            "power_strike_training": False,
            "defense_training": False,
            "magic_practice": False,
            "code_magic": False,
            "time_mastery": False,
            "skill_mastery": False
        }
        self.equipment = {
            "weapon": None,
            "armor": None
        }
        
    def take_damage(self, damage: int) -> int:
        """Returns actual damage taken after defense calculation"""
        # New defense formula that scales better
        defense_reduction = min(0.75, self.stats.defense / 100)  # Cap at 75% reduction
        actual_damage = max(1, int(damage * (1 - defense_reduction)))
        self.stats.hp = max(0, self.stats.hp - actual_damage)
        
        # Check for death
        if self.stats.hp <= 0:
            return -1  # Signal death to combat system
            
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
        self.stats.max_hp += 50
        self.stats.hp = self.stats.max_hp
        self.stats.attack += 15
        self.stats.defense += 10
        self.stats.magic += 12
        self.stats.exp -= self.stats.exp_to_next
        self.stats.exp_to_next = int(self.stats.exp_to_next * 1.5) 
    
    def use_potion(self, potion_type: str) -> Tuple[bool, str]:
        """Use a potion to heal. Returns (success, message)"""
        if self.stats.potions.get(potion_type, 0) <= 0:
            return False, f"No {potion_type} remaining!"
            
        heal_amounts = {
            "Minor Healing Potion": 30,
            "Major Healing Potion": 75,
            "Full Restore Potion": self.stats.max_hp
        }
        
        heal_amount = heal_amounts.get(potion_type, 0)
        if heal_amount > 0:
            self.stats.potions[potion_type] -= 1
            old_hp = self.stats.hp
            self.heal(heal_amount)
            actual_heal = self.stats.hp - old_hp
            return True, f"Used {potion_type}! Healed for {actual_heal} HP!"
            
        return False, "Invalid potion type!"

    def buy_potion(self, potion_type: str) -> Tuple[bool, str]:
        """Try to buy a potion. Returns (success, message)"""
        costs = {
            "Minor Healing Potion": 50,
            "Major Healing Potion": 100,
            "Full Restore Potion": 200
        }
        
        cost = costs.get(potion_type)
        if cost is None:
            return False, "Invalid potion type!"
            
        if self.stats.gold < cost:
            return False, "Not enough gold!"
            
        self.stats.gold -= cost
        self.stats.potions[potion_type] = self.stats.potions.get(potion_type, 0) + 1
        return True, f"Purchased {potion_type} for {cost} gold!"

    def apply_training_effect(self, training_type: str) -> str:
        """Apply permanent stat bonuses from training"""
        if training_type in self.training_bonuses and not self.training_bonuses[training_type]:
            self.training_bonuses[training_type] = True
            
            # Different training types give different bonuses
            bonuses = {
                "power_strike_training": {
                    "attack": 15,
                    "message": "Power Strike mastered! Attack increased by 15!"
                },
                "defense_training": {
                    "defense": 10,
                    "max_hp": 50,
                    "message": "Defense mastered! Defense +10, Max HP +50!"
                },
                "magic_practice": {
                    "magic": 15,
                    "attack": 10,
                    "message": "Magic practice complete! Magic +15, Attack +10!"
                },
                "code_magic": {
                    "magic": 20,
                    "defense": 5,
                    "message": "Code magic mastered! Magic +20, Defense +5!"
                },
                "time_mastery": {
                    "attack": 20,
                    "magic": 20,
                    "message": "Time magic mastered! Attack and Magic +20!"
                },
                "skill_mastery": {
                    "attack": 25,
                    "defense": 15,
                    "max_hp": 75,
                    "message": "Skills mastered! Attack +25, Defense +15, Max HP +75!"
                }
            }

            if training_type in bonuses:
                bonus = bonuses[training_type]
                if "attack" in bonus:
                    self.stats.attack += bonus["attack"]
                if "defense" in bonus:
                    self.stats.defense += bonus["defense"]
                if "magic" in bonus:
                    self.stats.magic += bonus["magic"]
                if "max_hp" in bonus:
                    self.stats.max_hp += bonus["max_hp"]
                    self.stats.hp += bonus["max_hp"]  # Heal by the amount of max HP increase
                return bonus["message"]
            
        return "No new training effect."

    def equip_item(self, item_type: str, item_name: str) -> str:
        """Equip an item and return status message"""
        if item_type == "weapon":
            stats = {
                "Tech Blade": {"attack": 25},
                "Spirit Staff": {"magic": 25},
                "Power Gauntlets": {"attack": 20, "defense": 10}
            }
        elif item_type == "armor":
            stats = {
                "Digital Armor": {"defense": 25},
                "Spirit Robe": {"magic": 15, "defense": 15},
                "Power Shield": {"defense": 30}
            }
        else:
            return "Invalid item type!"
            
        if item_name in stats:
            self.equipment[item_type] = item_name
            for stat, value in stats[item_name].items():
                setattr(self.stats, stat, getattr(self.stats, stat) + value)
            return f"Equipped {item_name}!"
            
        return "Invalid item!"