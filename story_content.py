from dataclasses import dataclass
from typing import List, Tuple, Optional
import random

@dataclass
class StoryNode:
    text: str
    choices: List[Tuple[str, str]]
    background: str
    dimension: Optional[str] = None
    boss: Optional[str] = None
    items: List[str] = None

story_content = {
    "start": StoryNode(
        text="You begin your journey...",
        choices=[
            ("Enter Diwata Forest", "sacred_grove"),
            ("Prepare first", "initial_preparation")
        ],
        background="main"
    ),

    # First Dimension - Bayan ng Diwata
    "sacred_grove": StoryNode(
        text="You enter the Sacred Grove of the Diwata Forest, where technology and nature intertwine...",
        choices=[
            ("Explore grove", "grove_exploration"),
            ("Study surroundings", "forest_study")
        ],
        background="forest"
    ),

    "grove_exploration": StoryNode(
        text="Ancient techno-organic structures pulse with energy. The trees themselves hum with digital frequencies...",
        choices=[
            ("Investigate structures", "tech_study"),
            ("Follow the humming", "energy_trace")
        ],
        background="forest"
    ),

    "tech_study": StoryNode(
        text="You examine the ancient technological structures...",
        choices=[
            ("Test systems", "system_test"),
            ("Return to grove", "grove_exploration")
        ],
        background="tech"
    ),

    "energy_trace": StoryNode(
        text="You follow the mysterious energy signatures...",
        choices=[
            ("Track source", "twin_search"),
            ("Study energy", "energy_study")
        ],
        background="forest"
    ),

    "forest_study": StoryNode(
        text="You study the forest's unique fusion of technology and nature...",
        choices=[
            ("Learn tech-magic", "magic_study"),
            ("Track twins", "twin_search")
        ],
        background="forest"
    ),

    "magic_study": StoryNode(
        text="You learn about the forest's techno-magical properties...",
        choices=[
            ("Practice magic", "magic_practice"),
            ("Track twins", "twin_search")
        ],
        background="tech"
    ),

    "twin_search": StoryNode(
        text="You follow traces of the Engkanto Twins' power through the forest...",
        choices=[
            ("Confront twins", "twin_battle"),
            ("Observe more", "twin_observation")
        ],
        background="forest"
    ),

    "twin_battle": StoryNode(
        text="The Engkanto Twins unleash their combined power...",
        choices=[
            ("Continue", "twin_aftermath"),
            ("Proceed", "twin_aftermath")
        ],
        background="twin"
    ),

    "twin_aftermath": StoryNode(
        text="With the Engkanto Twins defeated, you sense a dark presence from the Lake of Infinity. But you may need more preparation...",
        choices=[
            ("Enter Lake portal", "lake_warning"),
            ("Train in village", "luntiang_kanlungan")
        ],
        background="portal.jpg",
        dimension="Bayan ng Diwata"
    ),

    "lake_warning": StoryNode(
        text="The portal's energy feels overwhelming. The Guardian's power might be too much for your current strength...",
        choices=[
            ("Enter anyway", "lake_entrance"),
            ("Return to train", "luntiang_kanlungan")
        ],
        background="lake/lake1.jpg"
    ),

    # Second Dimension - Lawa ng Walang Hanggan
    "lake_entrance": StoryNode(
        text="The infinite lake stretches before you. The Guardian's power is palpable...",
        choices=[
            ("Face Guardian", "guardian_check"),
            ("Study waters", "lake_study"),
            ("Retreat", "lake_retreat")
        ],
        background="lake"
    ),

    "guardian_check": StoryNode(
        text="The Guardian's power is immense. Without proper training, this battle could be fatal...",
        choices=[
            ("Fight anyway", "abyss_battle"),
            ("Retreat to train", "lake_retreat")
        ],
        background="lake"
    ),

    "lake_retreat": StoryNode(
        text="You wisely choose to retreat and prepare further. The Guardian can wait...",
        choices=[
            ("Return to village", "luntiang_kanlungan"),
            ("Train nearby", "lakeside_training")
        ],
        background="lake"
    ),

    "lake_study": StoryNode(
        text="You study the time-warped waters, learning their temporal properties...",
        choices=[
            ("Practice time magic", "time_magic"),
            ("Seek Guardian", "guardian_search")
        ],
        background="lake"
    ),

    "time_magic": StoryNode(
        text="You practice manipulating the temporal energies...",
        choices=[
            ("Master time", "time_mastery"),
            ("Face Guardian", "abyss_battle")
        ],
        background="lake"
    ),

    "guardian_search": StoryNode(
        text="You search for signs of the Guardian in the infinite waters...",
        choices=[
            ("Confront Guardian", "abyss_battle"),
            ("Study more", "lake_study")
        ],
        background="lake"
    ),

    "abyss_battle": StoryNode(
        text="The Guardian of the Abyss emerges from the infinite lake, distorting time itself...",
        choices=[
            ("Continue", "abyss_aftermath"),
            ("Proceed", "abyss_aftermath")
        ],
        background="guardian"
    ),

    "abyss_aftermath": StoryNode(
        text="The Guardian is defeated, but Corrupted Dilim's power feels overwhelming. Rushing in would be suicide...",
        choices=[
            ("Face Dilim", "final_warning"),
            ("Final preparations", "preparation_choice")
        ],
        background="lake"
    ),

    "final_warning": StoryNode(
        text="Corrupted Dilim's power is beyond anything you've faced. Without maximum preparation, death is certain...",
        choices=[
            ("Fight anyway", "final_battle"),
            ("Prepare more", "preparation_choice")
        ],
        background="final"
    ),

    "preparation_choice": StoryNode(
        text="You must prepare thoroughly for the final battle...",
        choices=[
            ("Master powers", "final_training"),
            ("Gather resources", "resource_gathering"),
            ("Study enemy", "dilim_research")
        ],
        background="final"
    ),

    # Final Dimension - The Convergence
    "final_dimension": StoryNode(
        text="You enter the Convergence, where all dimensions meet. Corrupted Dilim awaits...",
        choices=[
            ("Face Dilim", "final_battle"),
            ("Final preparation", "ultimate_preparation")
        ],
        background="final"
    ),

    "final_battle": StoryNode(
        text="Corrupted Dilim emerges, wielding the twisted power of all dimensions...",
        choices=[
            ("Continue", "final_aftermath"),
            ("Proceed", "final_aftermath")
        ],
        background="dilim"
    ),

    "final_aftermath": StoryNode(
        text="Victory! The dimensions stabilize as balance is restored. Your legend as the Digital Penduko is complete...",
        choices=[
            ("Begin new journey", "start"),
            ("Continue watching", "start")
        ],
        background="final"
    ),

    # Preparation and Training Nodes
    "initial_preparation": StoryNode(
        text="You prepare for your journey into the mystical digital forest...",
        choices=[
            ("Basic training", "basic_training"),
            ("Study lore", "initial_research")
        ],
        background="main"
    ),

    "basic_training": StoryNode(
        text="You focus on mastering your newfound powers...",
        choices=[
            ("Combat training", "combat_training"),
            ("Magic practice", "magic_practice")
        ],
        background="main"
    ),

    "combat_training": StoryNode(
        text="The ancient warrior spirit teaches you combat techniques...",
        choices=[
            ("Learn Power Strike", "power_strike_training"),
            ("Learn Defense", "defense_training")
        ],
        background="main"
    ),

    "magic_practice": StoryNode(
        text="You study the fusion of technology and magic...",
        choices=[
            ("Learn Tech-Magic", "techno_magic"),
            ("Study Ancient Code", "code_magic")
        ],
        background="tech"
    ),

    "lake_preparation": StoryNode(
        text="You prepare to enter the Lake of Infinity...",
        choices=[
            ("Study time magic", "time_study"),
            ("Enter lake", "lake_entrance")
        ],
        background="lake"
    ),

    "final_preparation": StoryNode(
        text="You make your final preparations before facing Corrupted Dilim...",
        choices=[
            ("Power meditation", "power_focus"),
            ("Face destiny", "final_battle")
        ],
        background="final"
    ),

    "ultimate_preparation": StoryNode(
        text="You gather all your power and knowledge for the final confrontation...",
        choices=[
            ("Ready", "final_battle"),
            ("Meditate more", "power_focus")
        ],
        background="final"
    ),

    "advanced_training": StoryNode(
        text="You undergo more intensive training...",
        choices=[
            ("Enter forest", "sacred_grove"),
            ("Perfect skills", "skill_mastery")
        ],
        background="main"
    ),

    "initial_research": StoryNode(
        text="You delve deeper into the ancient digital lore...",
        choices=[
            ("Study more", "knowledge_mastery"),
            ("Begin journey", "sacred_grove")
        ],
        background="main/deep_research.jpg",
        items=["Advanced Lore"]
    ),

    "time_study": StoryNode(
        text="You study the principles of time manipulation...",
        choices=[
            ("Practice control", "time_magic"),
            ("Enter lake", "lake_entrance")
        ],
        background="time_study.jpg"
    ),

    "power_focus": StoryNode(
        text="You focus your powers through meditation...",
        choices=[
            ("Face destiny", "final_battle"),
            ("Continue focus", "deep_focus")
        ],
        background="power_meditation.jpg"
    ),

    # Add missing study and practice nodes
    "system_test": StoryNode(
        text="You run diagnostics on the ancient systems...",
        choices=[
            ("Apply findings", "tech_study"),
            ("Return to grove", "grove_exploration")
        ],
        background="system_test.jpg"
    ),

    "energy_study": StoryNode(
        text="You analyze the mysterious energy patterns...",
        choices=[
            ("Follow source", "twin_search"),
            ("Study more", "energy_trace")
        ],
        background="energy_study.jpg"
    ),

    "techno_magic": StoryNode(
        text="You study the fusion of technology and magic...",
        choices=[
            ("Learn Tech-Magic", "techno_magic"),
            ("Study Ancient Code", "code_magic")
        ],
        background="tech"
    ),

    "twin_observation": StoryNode(
        text="You observe the twins' movements carefully...",
        choices=[
            ("Engage twins", "twin_battle"),
            ("Study more", "twin_search")
        ],
        background="twin_observe.jpg"
    ),

    "time_mastery": StoryNode(
        text="You begin to master temporal manipulation...",
        choices=[
            ("Face Guardian", "abyss_battle"),
            ("Practice more", "time_magic")
        ],
        background="time_mastery.jpg"
    ),

    "skill_mastery": StoryNode(
        text="You perfect all your combat and magical abilities...",
        choices=[
            ("Test powers", "final_training"),
            ("Return", "preparation_choice")
        ],
        background="final/skill_mastery.jpg",
        items=["Ultimate Mastery"]
    ),

    "deep_research": StoryNode(
        text="You delve deeper into the ancient digital lore...",
        choices=[
            ("Study more", "knowledge_mastery"),
            ("Begin journey", "sacred_grove")
        ],
        background="main/deep_research.jpg",
        items=["Advanced Lore"]
    ),

    "deep_focus": StoryNode(
        text="You focus your mind and spirit for the challenges ahead...",
        choices=[
            ("Complete meditation", "power_focus"),
            ("Return", "final_preparation")
        ],
        background="final/deep_focus.jpg",
        items=["Mental Focus"]
    ),

    # Add village nodes for Bayan ng Diwata
    "luntiang_kanlungan": StoryNode(
        text="The Diwata village offers various opportunities to grow stronger...",
        choices=[
            ("Train abilities", "village_training"),
            ("Help villagers", "village_quests"),
            ("Visit shops", "village_shops")
        ],
        background="village"
    ),

    "village_training": StoryNode(
        text="The village masters can teach you different skills...",
        choices=[
            ("Combat training", "advanced_combat"),
            ("Magic studies", "advanced_magic"),
            ("Return to village", "luntiang_kanlungan")
        ],
        background="village"
    ),

    "village_quests": StoryNode(
        text="Several villagers need help:\n- Missing child in the forest\n- Corrupted forest spirits\n- Malfunctioning defense grid",
        choices=[
            ("Find child", "rescue_mission"),
            ("Help spirits", "spirit_cleansing"),
            ("Fix grid", "grid_repair")
        ],
        background="forest/village_square.jpg",
        items=["Village Map", "Spirit Detector"]
    ),

    # Add village nodes for Lawa ng Walang Hanggan
    "baybay_ng_tala": StoryNode(
        text="You arrive at Baybay ng Tala, where time flows unevenly along the infinite shore...",
        choices=[
            ("Collect crystals", "crystal_gathering"),
            ("Help villagers", "temporal_repairs")
        ],
        background="star_shore.jpg",
        dimension="Lawa ng Walang Hanggan"
    ),

    "crystal_gathering": StoryNode(
        text="You search for Temporal Crystals to enhance your Infinity Stopwatch...",
        choices=[
            ("Return to village", "baybay_ng_tala"),
            ("Study crystals", "crystal_study")
        ],
        background="crystal_field.jpg"
    ),

    # Add village nodes for The Convergence
    "final_sanctuary": StoryNode(
        text="You find a hidden sanctuary in the Convergence, a last bastion before the final battle...",
        choices=[
            ("Prepare equipment", "final_upgrades"),
            ("Face destiny", "final_battle")
        ],
        background="sanctuary.jpg",
        dimension="The Convergence"
    ),

    "final_upgrades": StoryNode(
        text="You make final modifications to your equipment using knowledge from all dimensions...",
        choices=[
            ("Return to sanctuary", "final_sanctuary"),
            ("Test power", "power_testing")
        ],
        background="upgrade_chamber.jpg"
    ),

    "forest_exploration": StoryNode(
        text="As you explore, you notice the forest's corruption spreading. Time might be running out...",
        choices=[
            ("Track corruption", "corruption_study"),
            ("Help creatures", "creature_rescue"),
            ("Find source", "corruption_source")
        ],
        background="forest/corrupted_grove.jpg",
        items=["Corruption Sample"]
    ),

    # Add missing training/learning nodes
    "power_strike_training": StoryNode(
        text="You practice advanced combat techniques, focusing on power and precision...",
        choices=[
            ("Continue training", "advanced_combat"),
            ("Return to village", "luntiang_kanlungan")
        ],
        background="forest/power_training.jpg",
        items=["Power Strike Mastery"]
    ),

    "defense_training": StoryNode(
        text="You learn to perfect your defensive stances and techniques...",
        choices=[
            ("Continue training", "advanced_combat"),
            ("Return to village", "luntiang_kanlungan")
        ],
        background="forest/defense_training.jpg",
        items=["Defense Mastery"]
    ),

    "magic_practice": StoryNode(
        text="You delve into the mysteries of techno-magic...",
        choices=[
            ("Continue practice", "advanced_magic"),
            ("Return to village", "luntiang_kanlungan")
        ],
        background="forest/magic_practice.jpg",
        items=["Magic Mastery"]
    ),

    "code_magic": StoryNode(
        text="You study the ancient code patterns that control magical energy...",
        choices=[
            ("Practice coding", "code_practice"),
            ("Return to village", "luntiang_kanlungan")
        ],
        background="forest/code_magic.jpg",
        items=["Code Mastery"]
    ),

    "time_mastery": StoryNode(
        text="You learn to manipulate the flow of time itself...",
        choices=[
            ("Continue mastery", "time_magic"),
            ("Return to lake", "lake_entrance")
        ],
        background="lake/time_mastery.jpg",
        items=["Time Mastery"]
    ),

    "skill_mastery": StoryNode(
        text="You perfect all your combat and magical abilities...",
        choices=[
            ("Test powers", "final_training"),
            ("Return", "preparation_choice")
        ],
        background="final/skill_mastery.jpg",
        items=["Ultimate Mastery"]
    ),

    # Additional Training/Study Nodes
    "combat_basics": StoryNode(
        text="You learn the fundamental combat techniques...",
        choices=[
            ("Power training", "power_strike_training"),
            ("Defense training", "defense_training")
        ],
        background="main/combat_basics.jpg",
        items=["Basic Combat Training"]
    ),

    "magic_basics": StoryNode(
        text="You study the basics of magical manipulation...",
        choices=[
            ("Practice magic", "magic_practice"),
            ("Study code magic", "code_magic")
        ],
        background="main/magic_basics.jpg",
        items=["Basic Magic Training"]
    ),

    "elder_wisdom": StoryNode(
        text="The village elder shares ancient knowledge and techniques...",
        choices=[
            ("Learn wisdom", "knowledge_mastery"),
            ("Return to village", "luntiang_kanlungan")
        ],
        background="forest/elder_wisdom.jpg",
        items=["Elder's Teaching"]
    ),

    # Shop/Quest Nodes
    "potion_shop": StoryNode(
        text="The alchemist offers various healing potions:\n- Minor Healing Potion (50 gold)\n- Major Healing Potion (100 gold)\n- Full Restore Potion (200 gold)",
        choices=[
            ("Buy potions", "buy_potions"),
            ("Return to shops", "village_shops")
        ],
        background="village"
    ),

    "equipment_shop": StoryNode(
        text="The village craftsman offers various equipment...",
        choices=[
            ("View weapons", "weapon_shop"),
            ("View armor", "armor_shop"),
            ("Return to shops", "village_shops")
        ],
        background="village"
    ),

    "village_help": StoryNode(
        text="The villagers gather to assist in the search...",
        choices=[
            ("Organize search", "search_party"),
            ("Search alone", "forest_search")
        ],
        background="forest/village_help.jpg"
    ),

    # Battle/Preparation Nodes
    "ultimate_preparation": StoryNode(
        text="You make your final preparations before facing Corrupted Dilim...",
        choices=[
            ("Face destiny", "final_battle"),
            ("Train more", "final_training")
        ],
        background="final/ultimate_prep.jpg",
        items=["Ultimate Power"]
    ),

    "abyss_battle": StoryNode(
        text="The Guardian of the Abyss emerges from the infinite waters...",
        choices=[
            ("Fight", "guardian_battle"),
            ("Retreat", "lake_retreat")
        ],
        background="lake/abyss_battle.jpg",
        boss="Guardian of the Abyss"
    ),

    "final_training": StoryNode(
        text="You undergo intense training to prepare for the final battle...",
        choices=[
            ("Master combat", "skill_mastery"),
            ("Master magic", "magic_mastery"),
            ("Return", "preparation_choice")
        ],
        background="final/final_training.jpg",
        items=["Ultimate Training Scroll"]
    ),

    "magic_mastery": StoryNode(
        text="You focus on mastering advanced magical techniques...",
        choices=[
            ("Continue practice", "final_training"),
            ("Test powers", "magic_test")
        ],
        background="final/magic_mastery.jpg",
        items=["Advanced Magic Mastery"]
    ),

    "knowledge_mastery": StoryNode(
        text="The elder's ancient knowledge reveals powerful secrets...",
        choices=[
            ("Apply knowledge", "power_boost"),
            ("Study more", "deep_knowledge")
        ],
        background="forest/knowledge_master.jpg",
        items=["Ancient Wisdom"]
    ),

    "basic_training": StoryNode(
        text="You begin with fundamental combat and magic training...",
        choices=[
            ("Combat basics", "power_strike_training"),
            ("Magic basics", "magic_practice")
        ],
        background="main/basic_training.jpg",
        items=["Basic Training Complete"]
    ),

    "initial_research": StoryNode(
        text="You study the basics of the Digital World's lore...",
        choices=[
            ("Learn more", "knowledge_mastery"),
            ("Begin journey", "sacred_grove")
        ],
        background="main/initial_research.jpg",
        items=["Basic Lore"]
    ),

    # Add Village/Quest Related Nodes
    "weapon_shop": StoryNode(
        text="The weaponsmith offers various magical weapons:\n- Tech Blade (2000 gold)\n- Spirit Staff (1800 gold)\n- Power Gauntlets (1500 gold)",
        choices=[
            ("Purchase weapon", "weapon_purchase"),
            ("Return to shop", "buy_equipment")
        ],
        background="forest/weapon_shop.jpg"
    ),

    "armor_shop": StoryNode(
        text="The armorsmith displays protective gear:\n- Digital Armor (2000 gold)\n- Spirit Robe (1800 gold)\n- Power Shield (1500 gold)",
        choices=[
            ("Purchase armor", "armor_purchase"),
            ("Return to shop", "buy_equipment")
        ],
        background="forest/armor_shop.jpg"
    ),

    "child_rescue": StoryNode(
        text="You find the child trapped in corrupted vines...",
        choices=[
            ("Use magic", "magic_rescue"),
            ("Use strength", "force_rescue")
        ],
        background="forest/child_rescue.jpg",
        items=["Child's Gratitude"]
    ),

    "village_quests": StoryNode(
        text="The village has several requests for help...",
        choices=[
            ("Help villagers", "village_tasks"),
            ("Hunt corrupted", "corruption_hunt"),
            ("Return", "luntiang_kanlungan")
        ],
        background="forest/village_quests.jpg"
    ),

    # Add Resource/Research Related Nodes
    "material_gathering": StoryNode(
        text="You gather rare materials for the final battle...",
        choices=[
            ("Search forest", "forest_materials"),
            ("Search lake", "lake_materials"),
            ("Return", "resource_gathering")
        ],
        background="final/material_gather.jpg",
        items=["Rare Materials"]
    ),

    "pattern_study": StoryNode(
        text="You analyze Corrupted Dilim's attack patterns...",
        choices=[
            ("Study more", "dilim_research"),
            ("Test theory", "pattern_test")
        ],
        background="final/pattern_study.jpg",
        items=["Pattern Analysis"]
    ),

    # Add Combat/Boss Related Nodes
    "twin_observation": StoryNode(
        text="You observe the Engkanto Twins' movements and patterns...",
        choices=[
            ("Study more", "twin_search"),
            ("Confront", "twin_battle")
        ],
        background="forest/twin_observe.jpg",
        items=["Twin Pattern Data"]
    ),

    "system_test": StoryNode(
        text="You test the ancient technological systems...",
        choices=[
            ("Run diagnostics", "tech_study"),
            ("Power systems", "power_test")
        ],
        background="tech/system_test.jpg",
        items=["System Data"]
    ),

    "energy_study": StoryNode(
        text="You study the mysterious energy patterns...",
        choices=[
            ("Analyze flow", "energy_trace"),
            ("Test energy", "energy_experiment")
        ],
        background="forest/energy_study.jpg",
        items=["Energy Data"]
    ),

    # Add Cleansing/Ritual Related Nodes
    "cleansing_ritual": StoryNode(
        text="You perform the grand cleansing ritual...",
        choices=[
            ("Channel power", "ritual_power"),
            ("Focus energy", "ritual_focus")
        ],
        background="ritual_clearing.jpg",
        items=["Ritual Success"]
    ),

    "spirit_cleansing": StoryNode(
        text="You begin the spirit cleansing process...",
        choices=[
            ("Use code", "code_cleanse"),
            ("Use energy", "energy_cleanse")
        ],
        background="forest/spirit_cleanse.jpg",
        items=["Cleansed Spirit"]
    ),

    # Combat/Battle Related Nodes
    "guardian_battle": StoryNode(
        text="The Guardian of the Abyss unleashes temporal powers...",
        choices=[
            ("Continue", "abyss_aftermath"),
            ("Proceed", "abyss_aftermath")
        ],
        background="bosses/guardian.jpg",
        boss="Guardian of the Abyss"
    ),

    "magic_test": StoryNode(
        text="You test your newly mastered magical abilities...",
        choices=[
            ("Continue training", "magic_mastery"),
            ("Return", "final_training")
        ],
        background="final/magic_test.jpg",
        items=["Magic Test Results"]
    ),

    "power_test": StoryNode(
        text="You test the ancient power systems...",
        choices=[
            ("Continue testing", "system_test"),
            ("Return", "tech_study")
        ],
        background="tech/power_test.jpg",
        items=["Power Test Data"]
    ),

    "energy_experiment": StoryNode(
        text="You conduct experiments with the mysterious energy...",
        choices=[
            ("Continue research", "energy_study"),
            ("Apply findings", "energy_trace")
        ],
        background="forest/energy_experiment.jpg",
        items=["Energy Research"]
    ),

    # Training/Study Related Nodes
    "code_practice": StoryNode(
        text="You practice coding ancient magical algorithms...",
        choices=[
            ("Debug code", "code_debugging"),
            ("Test spells", "magic_application")
        ],
        background="forest/code_practice.jpg",
        items=["Code Practice Results"]
    ),

    "power_boost": StoryNode(
        text="You channel the ancient knowledge into raw power...",
        choices=[
            ("Master power", "skill_mastery"),
            ("Study more", "knowledge_mastery")
        ],
        background="forest/power_boost.jpg",
        items=["Ancient Power"]
    ),

    "deep_knowledge": StoryNode(
        text="You delve deeper into the ancient wisdom...",
        choices=[
            ("Apply wisdom", "knowledge_mastery"),
            ("Share knowledge", "elder_wisdom")
        ],
        background="forest/deep_knowledge.jpg",
        items=["Deep Wisdom"]
    ),

    "buy_potions": StoryNode(
        text="The alchemist prepares your chosen potions...",
        choices=[
            ("Buy more", "potion_shop"),
            ("Return to shops", "village_shops")
        ],
        background="village/alchemy_shop.jpg"
    ),

    # Village/Quest Related Nodes
    "village_tasks": StoryNode(
        text="The villagers need help with various tasks...",
        choices=[
            ("Help children", "child_rescue"),
            ("Help elders", "elder_tasks"),
            ("Return", "village_quests")
        ],
        background="forest/village_tasks.jpg",
        items=["Villager's Gratitude"]
    ),

    "corruption_hunt": StoryNode(
        text="You track corrupted creatures in the forest...",
        choices=[
            ("Hunt creatures", "creature_battle"),
            ("Study corruption", "corruption_study"),
            ("Return", "village_quests")
        ],
        background="forest/corruption_hunt.jpg",
        items=["Corruption Samples"]
    ),

    "magic_rescue": StoryNode(
        text="You use magic to carefully free the child...",
        choices=[
            ("Complete rescue", "rescue_complete"),
            ("Check child", "child_safety")
        ],
        background="forest/magic_rescue.jpg",
        items=["Rescue Success"]
    ),

    "force_rescue": StoryNode(
        text="You carefully break apart the corrupted vines...",
        choices=[
            ("Free child", "rescue_complete"),
            ("Check safety", "child_safety")
        ],
        background="forest/force_rescue.jpg",
        items=["Rescue Success"]
    ),

    "weapon_purchase": StoryNode(
        text="You select a weapon to purchase...",
        choices=[
            ("Confirm purchase", "equipment_shop"),
            ("Browse more", "weapon_shop")
        ],
        background="forest/weapon_purchase.jpg"
    ),

    "armor_purchase": StoryNode(
        text="You select armor to purchase...",
        choices=[
            ("Confirm purchase", "equipment_shop"),
            ("Browse more", "armor_shop")
        ],
        background="forest/armor_purchase.jpg"
    ),

    # Resource/Research Related Nodes
    "forest_materials": StoryNode(
        text="You gather rare materials from the ancient forest...",
        choices=[
            ("Continue gathering", "material_gathering"),
            ("Study materials", "material_study")
        ],
        background="forest/material_gather.jpg",
        items=["Forest Materials"]
    ),

    "lake_materials": StoryNode(
        text="You collect unique materials from the temporal waters...",
        choices=[
            ("Continue gathering", "material_gathering"),
            ("Study materials", "material_study")
        ],
        background="lake/material_gather.jpg",
        items=["Lake Materials"]
    ),

    "pattern_test": StoryNode(
        text="You test your theories about corruption patterns...",
        choices=[
            ("Continue testing", "pattern_study"),
            ("Apply findings", "dilim_research")
        ],
        background="final/pattern_test.jpg",
        items=["Pattern Test Results"]
    ),

    # Ritual/Cleansing Related Nodes
    "ritual_power": StoryNode(
        text="You channel power into the cleansing ritual...",
        choices=[
            ("Complete ritual", "cleansing_complete"),
            ("Adjust power", "ritual_adjustment")
        ],
        background="forest/ritual_power.jpg",
        items=["Ritual Power"]
    ),

    "ritual_focus": StoryNode(
        text="You focus the energies of the cleansing ritual...",
        choices=[
            ("Complete ritual", "cleansing_complete"),
            ("Adjust focus", "ritual_adjustment")
        ],
        background="forest/ritual_focus.jpg",
        items=["Ritual Focus"]
    ),

    "code_cleanse": StoryNode(
        text="You use coded spells to cleanse the spirit...",
        choices=[
            ("Complete cleansing", "spirit_purified"),
            ("Adjust code", "code_adjustment")
        ],
        background="forest/code_cleanse.jpg",
        items=["Code Cleanse"]
    ),

    "energy_cleanse": StoryNode(
        text="You channel pure energy to cleanse the spirit...",
        choices=[
            ("Complete cleansing", "spirit_purified"),
            ("Adjust energy", "energy_adjustment")
        ],
        background="forest/energy_cleanse.jpg",
        items=["Energy Cleanse"]
    ),

    # Lake/Time Related Nodes
    "lakeside_training": StoryNode(
        text="You train near the temporal waters...",
        choices=[
            ("Practice time magic", "time_magic"),
            ("Study waters", "lake_study"),
            ("Return", "lake_retreat")
        ],
        background="lake/lakeside_training.jpg",
        items=["Time Training"]
    ),

    "time_flow": StoryNode(
        text="You study the flow of time itself...",
        choices=[
            ("Adjust flow", "flow_adjustment"),
            ("Return", "time_magic")
        ],
        background="lake/time_flow.jpg",
        items=["Time Flow Study"]
    ),

    "crystal_experiment": StoryNode(
        text="You experiment with temporal crystals...",
        choices=[
            ("Continue tests", "crystal_testing"),
            ("Apply findings", "time_mastery")
        ],
        background="lake/crystal_experiment.jpg",
        items=["Crystal Data"]
    ),

    # Analysis/Study Related Nodes
    "corruption_study": StoryNode(
        text="You analyze the nature of the corruption...",
        choices=[
            ("Continue study", "sample_analysis"),
            ("Apply findings", "corruption_cleansing")
        ],
        background="forest/corruption_study.jpg",
        items=["Corruption Analysis"]
    ),

    "corruption_tracking": StoryNode(
        text="You track the spread of corruption...",
        choices=[
            ("Update map", "spread_mapping"),
            ("Study patterns", "pattern_analysis")
        ],
        background="forest/corruption_tracking.jpg",
        items=["Tracking Data"]
    ),

    "creature_healing": StoryNode(
        text="You attempt to heal corrupted creatures...",
        choices=[
            ("Continue healing", "healing_ritual"),
            ("Study effects", "effect_study")
        ],
        background="forest/creature_healing.jpg",
        items=["Healing Progress"]
    ),

    "corruption_effects": StoryNode(
        text="You document the effects of corruption...",
        choices=[
            ("Continue study", "effect_study"),
            ("Apply findings", "corruption_cleansing")
        ],
        background="forest/corruption_effects.jpg",
        items=["Effects Study"]
    ),

    "source_analysis": StoryNode(
        text="You analyze the source of corruption...",
        choices=[
            ("Continue analysis", "pattern_analysis"),
            ("Track source", "corruption_source")
        ],
        background="forest/source_analysis.jpg",
        items=["Source Data"]
    ),

    # Initial/Preparation Nodes
    "initial_preparation": StoryNode(
        text="You prepare for your journey into the mystical digital forest...",
        choices=[
            ("Basic training", "basic_training"),
            ("Study lore", "initial_research")
        ],
        background="main"
    ),

    "deep_research": StoryNode(
        text="You delve deeper into the ancient digital lore...",
        choices=[
            ("Study more", "knowledge_mastery"),
            ("Begin journey", "sacred_grove")
        ],
        background="main/deep_research.jpg",
        items=["Advanced Lore"]
    ),

    "deep_focus": StoryNode(
        text="You focus your mind and spirit for the challenges ahead...",
        choices=[
            ("Complete meditation", "power_focus"),
            ("Return", "final_preparation")
        ],
        background="final/deep_focus.jpg",
        items=["Mental Focus"]
    ),

    # Training/Combat Nodes
    "advanced_combat": StoryNode(
        text="You learn advanced combat techniques from the village masters...",
        choices=[
            ("Power training", "power_strike_training"),
            ("Defense training", "defense_training"),
            ("Return", "village_training")
        ],
        background="forest/advanced_combat.jpg",
        items=["Advanced Combat Scroll"]
    ),

    "advanced_magic": StoryNode(
        text="The elder teaches you advanced magical techniques...",
        choices=[
            ("Practice spells", "magic_practice"),
            ("Study code magic", "code_magic"),
            ("Return", "village_training")
        ],
        background="forest/advanced_magic.jpg",
        items=["Advanced Magic Scroll"]
    ),

    "code_debugging": StoryNode(
        text="You debug the ancient magical code...",
        choices=[
            ("Fix code", "grid_repair"),
            ("Test spells", "magic_application")
        ],
        background="forest/code_debug.jpg",
        items=["Debug Tools"]
    ),

    "magic_application": StoryNode(
        text="You apply your magical knowledge to practical use...",
        choices=[
            ("Test spells", "code_practice"),
            ("Return", "advanced_magic")
        ],
        background="forest/magic_apply.jpg",
        items=["Spell Application"]
    ),

    "material_study": StoryNode(
        text="You study the magical materials you've gathered...",
        choices=[
            ("Continue study", "resource_gathering"),
            ("Apply knowledge", "item_crafting")
        ],
        background="forest/material_study.jpg",
        items=["Material Knowledge"]
    ),

    # Village/Quest Nodes
    "rescue_mission": StoryNode(
        text="You prepare to rescue the trapped villagers...",
        choices=[
            ("Use magic", "magic_rescue"),
            ("Use strength", "force_rescue")
        ],
        background="forest/rescue_mission.jpg",
        items=["Rescue Kit"]
    ),

    "grid_repair": StoryNode(
        text="You work on repairing the damaged magical grid...",
        choices=[
            ("Debug code", "code_debugging"),
            ("Channel power", "power_channeling")
        ],
        background="forest/grid_repair.jpg",
        items=["Grid Tools"]
    ),

    "elder_tasks": StoryNode(
        text="The village elders need help with various magical tasks...",
        choices=[
            ("Help with magic", "magic_tasks"),
            ("Help with study", "lore_study")
        ],
        background="forest/elder_tasks.jpg",
        items=["Elder's Gratitude"]
    ),

    "creature_battle": StoryNode(
        text="You face the corrupted forest creatures...",
        choices=[
            ("Fight", "combat_sequence"),
            ("Try healing", "creature_healing")
        ],
        background="forest/creature_battle.jpg",
        items=["Creature Sample"]
    ),

    "rescue_complete": StoryNode(
        text="You successfully complete the rescue mission...",
        choices=[
            ("Check victims", "child_safety"),
            ("Return to village", "village_quests")
        ],
        background="forest/rescue_complete.jpg",
        items=["Rescue Badge"]
    ),

    "child_safety": StoryNode(
        text="You ensure the rescued child is safe and well...",
        choices=[
            ("Return child", "village_return"),
            ("Check for others", "rescue_mission")
        ],
        background="forest/child_safety.jpg",
        items=["Safety Token"]
    ),

    "buy_equipment": StoryNode(
        text="The village craftsman displays their wares...",
        choices=[
            ("Buy weapons", "weapon_shop"),
            ("Buy armor", "armor_shop"),
            ("Return", "village_shops")
        ],
        background="village/equipment_shop.jpg"
    ),

    # Lake/Time Nodes
    "temporal_repairs": StoryNode(
        text="You work on repairing temporal distortions...",
        choices=[
            ("Adjust time", "time_flow"),
            ("Study effects", "temporal_study")
        ],
        background="lake/temporal_repairs.jpg",
        items=["Time Tools"]
    ),

    "crystal_study": StoryNode(
        text="You study the mysterious temporal crystals...",
        choices=[
            ("Analyze power", "crystal_experiment"),
            ("Test effects", "time_magic")
        ],
        background="lake/crystal_study.jpg",
        items=["Crystal Knowledge"]
    ),

    "flow_adjustment": StoryNode(
        text="You carefully adjust the flow of time...",
        choices=[
            ("Continue adjusting", "time_flow"),
            ("Study effects", "temporal_study")
        ],
        background="lake/flow_adjust.jpg",
        items=["Flow Control"]
    ),

    # Cleansing/Ritual Nodes
    "cleansing_complete": StoryNode(
        text="The cleansing ritual is successfully completed...",
        choices=[
            ("Study effects", "effect_study"),
            ("Return", "village_quests")
        ],
        background="forest/cleansing_complete.jpg",
        items=["Cleansing Success"]
    ),

    "ritual_adjustment": StoryNode(
        text="You make careful adjustments to the ritual...",
        choices=[
            ("Channel power", "ritual_power"),
            ("Focus energy", "ritual_focus")
        ],
        background="forest/ritual_adjust.jpg",
        items=["Ritual Tools"]
    ),

    "spirit_purified": StoryNode(
        text="The spirit is successfully purified...",
        choices=[
            ("Study results", "effect_study"),
            ("Return", "village_quests")
        ],
        background="forest/spirit_pure.jpg",
        items=["Pure Spirit"]
    ),

    "code_adjustment": StoryNode(
        text="You adjust the cleansing code patterns...",
        choices=[
            ("Test code", "code_cleanse"),
            ("Debug more", "code_debugging")
        ],
        background="forest/code_adjust.jpg",
        items=["Code Tools"]
    ),

    "energy_adjustment": StoryNode(
        text="You adjust the flow of cleansing energy...",
        choices=[
            ("Test energy", "energy_cleanse"),
            ("Study flow", "energy_study")
        ],
        background="forest/energy_adjust.jpg",
        items=["Energy Tools"]
    ),

    # Research/Analysis Nodes
    "corruption_cleansing": StoryNode(
        text="You work on cleansing the corruption...",
        choices=[
            ("Use ritual", "cleansing_ritual"),
            ("Study more", "corruption_study")
        ],
        background="forest/corruption_cleanse.jpg",
        items=["Cleansing Tools"]
    ),

    "corruption_source": StoryNode(
        text="You investigate the source of corruption...",
        choices=[
            ("Study more", "source_analysis"),
            ("Track source", "corruption_tracking")
        ],
        background="forest/corruption_source.jpg",
        items=["Source Data"]
    ),

    "creature_rescue": StoryNode(
        text="You attempt to rescue corrupted creatures...",
        choices=[
            ("Heal creature", "creature_healing"),
            ("Study corruption", "corruption_study")
        ],
        background="forest/creature_rescue.jpg",
        items=["Rescue Tools"]
    ),

    "sample_collection": StoryNode(
        text="You carefully collect corruption samples...",
        choices=[
            ("Study samples", "sample_analysis"),
            ("Track source", "corruption_tracking")
        ],
        background="forest/sample_collection.jpg",
        items=["Corruption Samples"]
    ),

    # Combat/Battle Flow Nodes
    "combat_sequence": StoryNode(
        text="You engage in combat with the corrupted creatures...",
        choices=[
            ("Continue fight", "creature_battle"),
            ("Try healing", "creature_healing")
        ],
        background="forest/combat_sequence.jpg",
        items=["Combat Experience"]
    ),

    "guardian_battle": StoryNode(
        text="The Guardian of the Abyss unleashes its full power...",
        choices=[
            ("Continue", "abyss_aftermath"),
            ("Proceed", "abyss_aftermath")
        ],
        background="bosses/guardian.jpg",
        boss="Guardian of the Abyss"
    ),

    # Village/Training Nodes
    "village_training": StoryNode(
        text="The village masters offer different types of training...",
        choices=[
            ("Combat training", "advanced_combat"),
            ("Magic training", "advanced_magic"),
            ("Return", "luntiang_kanlungan")
        ],
        background="village/village_training.jpg"
    ),

    "village_return": StoryNode(
        text="You return to the village with those you've rescued...",
        choices=[
            ("Report success", "village_quests"),
            ("Check for more", "rescue_mission")
        ],
        background="forest/village_return.jpg",
        items=["Village Gratitude"]
    ),

    "village_shops": StoryNode(
        text="The village marketplace bustles with activity...",
        choices=[
            ("Equipment shop", "buy_equipment"),
            ("Potion shop", "potion_shop"),
            ("Return", "luntiang_kanlungan")
        ],
        background="village/village_shops.jpg"
    ),

    "power_focus": StoryNode(
        text="You focus your power through deep meditation...",
        choices=[
            ("Continue focus", "deep_focus"),
            ("Return", "final_preparation")
        ],
        background="final/power_focus.jpg",
        items=["Focused Power"]
    ),

    "power_channeling": StoryNode(
        text="You channel power into the damaged grid...",
        choices=[
            ("Continue channeling", "grid_repair"),
            ("Adjust flow", "energy_adjustment")
        ],
        background="forest/power_channeling.jpg",
        items=["Channeling Mastery"]
    ),

    "magic_tasks": StoryNode(
        text="The elders need help with various magical tasks...",
        choices=[
            ("Help with rituals", "cleansing_ritual"),
            ("Help with studies", "lore_study")
        ],
        background="forest/magic_tasks.jpg",
        items=["Elder's Wisdom"]
    ),

    "lore_study": StoryNode(
        text="You study ancient lore with the village elders...",
        choices=[
            ("Continue study", "knowledge_mastery"),
            ("Help with tasks", "magic_tasks"),
            ("Return", "elder_tasks")
        ],
        background="forest/lore_study.jpg",
        items=["Ancient Knowledge"]
    ),

    # Resource/Crafting Nodes
    "item_crafting": StoryNode(
        text="You work on crafting magical items...",
        choices=[
            ("Craft equipment", "equipment_crafting"),
            ("Study materials", "material_study")
        ],
        background="forest/item_crafting.jpg",
        items=["Crafted Item"]
    ),

    "temporal_study": StoryNode(
        text="You study the effects of temporal distortions...",
        choices=[
            ("Continue study", "time_magic"),
            ("Apply knowledge", "temporal_repairs")
        ],
        background="lake/temporal_study.jpg",
        items=["Temporal Knowledge"]
    ),

    "code_practice": StoryNode(
        text="You practice coding magical algorithms...",
        choices=[
            ("Debug code", "code_debugging"),
            ("Test spells", "magic_application")
        ],
        background="forest/code_practice.jpg",
        items=["Code Practice"]
    ),

    # Final Battle Preparation Nodes
    "final_preparation": StoryNode(
        text="You make your final preparations...",
        choices=[
            ("Meditate", "power_focus"),
            ("Face destiny", "final_battle")
        ],
        background="final/preparation.jpg",
        items=["Final Preparation"]
    ),

    "final_sanctuary": StoryNode(
        text="You reach a sacred place to gather your strength...",
        choices=[
            ("Meditate", "power_focus"),
            ("Test power", "power_testing")
        ],
        background="final/sanctuary.jpg",
        items=["Sacred Power"]
    ),

    "power_testing": StoryNode(
        text="You test the limits of your power...",
        choices=[
            ("Continue testing", "final_sanctuary"),
            ("Ready for battle", "final_battle")
        ],
        background="final/power_testing.jpg",
        items=["Power Mastery"]
    ),

    # Search/Rescue Nodes
    "search_party": StoryNode(
        text="You organize villagers to help with the search...",
        choices=[
            ("Lead search", "forest_search"),
            ("Split up", "rescue_mission")
        ],
        background="forest/search_party.jpg",
        items=["Search Organization"]
    ),

    "forest_search": StoryNode(
        text="You search through the dangerous forest...",
        choices=[
            ("Continue search", "rescue_mission"),
            ("Return to village", "village_return")
        ],
        background="forest/forest_search.jpg",
        items=["Search Results"]
    ),

    # Effect/Study Nodes
    "effect_study": StoryNode(
        text="You study the effects of corruption and healing...",
        choices=[
            ("Document findings", "corruption_effects"),
            ("Continue healing", "healing_ritual")
        ],
        background="forest/effect_study.jpg",
        items=["Effect Analysis"]
    ),

    "sample_analysis": StoryNode(
        text="You analyze the collected corruption samples...",
        choices=[
            ("Study patterns", "pattern_analysis"),
            ("Continue collection", "sample_collection")
        ],
        background="forest/sample_analysis.jpg",
        items=["Analysis Results"]
    ),

    "spread_mapping": StoryNode(
        text="You map the corruption's spread patterns...",
        choices=[
            ("Update map", "corruption_tracking"),
            ("Study patterns", "pattern_analysis")
        ],
        background="forest/spread_mapping.jpg",
        items=["Corruption Map"]
    ),

    "healing_ritual": StoryNode(
        text="You perform healing rituals on corrupted beings...",
        choices=[
            ("Continue healing", "creature_healing"),
            ("Study effects", "effect_study")
        ],
        background="forest/healing_ritual.jpg",
        items=["Healing Knowledge"]
    ),

    # Equipment/Shop Nodes
    "equipment_crafting": StoryNode(
        text="You craft magical equipment using gathered materials...",
        choices=[
            ("Craft weapon", "weapon_crafting"),
            ("Craft armor", "armor_crafting")
        ],
        background="forest/equipment_craft.jpg",
        items=["Crafted Equipment"]
    ),

    "buy_potions": StoryNode(
        text="You browse the available healing potions...",
        choices=[
            ("Purchase", "confirm_purchase"),
            ("Return", "potion_shop")
        ],
        background="village/potion_shop.jpg"
    ),

    # Combat/Battle Nodes
    "final_battle": StoryNode(
        text="You face Corrupted Dilim in the final confrontation...",
        choices=[
            ("Continue", "final_aftermath"),
            ("Proceed", "final_aftermath")
        ],
        background="bosses/corrupted_dilim.jpg",
        boss="Corrupted Dilim"
    ),

    "crystal_testing": StoryNode(
        text="You test the properties of temporal crystals...",
        choices=[
            ("Continue tests", "crystal_experiment"),
            ("Study results", "crystal_study")
        ],
        background="lake/crystal_test.jpg",
        items=["Crystal Data"]
    ),

    # Additional nodes found from thorough scan
    "weapon_crafting": StoryNode(
        text="You craft powerful weapons...",
        choices=[
            ("Continue crafting", "equipment_crafting"),
            ("Test weapon", "combat_training")
        ],
        background="forest/weapon_craft.jpg",
        items=["Crafted Weapon"]
    ),

    "armor_crafting": StoryNode(
        text="You craft protective armor...",
        choices=[
            ("Continue crafting", "equipment_crafting"),
            ("Test armor", "defense_training")
        ],
        background="forest/armor_craft.jpg",
        items=["Crafted Armor"]
    ),

    "confirm_purchase": StoryNode(
        text="Confirm your purchase of potions...",
        choices=[
            ("Buy more", "buy_potions"),
            ("Return", "village_shops")
        ],
        background="village/shop_purchase.jpg"
    ),

    "techno_magic": StoryNode(
        text="You study the fusion of technology and magic...",
        choices=[
            ("Practice spells", "magic_practice"),
            ("Study code", "code_magic")
        ],
        background="forest/techno_magic.jpg",
        items=["Tech-Magic Manual"]
    ),

    "deep_focus": StoryNode(
        text="You enter a deep meditative state...",
        choices=[
            ("Continue focus", "power_focus"),
            ("Return", "final_preparation")
        ],
        background="final/deep_focus.jpg",
        items=["Enhanced Focus"]
    ),

    "time_flow": StoryNode(
        text="You study the flow of temporal energies...",
        choices=[
            ("Adjust flow", "flow_adjustment"),
            ("Study more", "time_magic")
        ],
        background="lake/time_flow.jpg",
        items=["Time Flow Data"]
    ),

    "corruption_source": StoryNode(
        text="You discover the source of corruption...",
        choices=[
            ("Investigate", "source_analysis"),
            ("Prepare cleansing", "corruption_cleansing")
        ],
        background="forest/corruption_source.jpg",
        items=["Source Location"]
    ),

    # Missing Combat/Training Nodes
    "combat_training": StoryNode(
        text="You test your combat skills with the new weapon...",
        choices=[
            ("Continue training", "power_strike_training"),
            ("Return", "weapon_crafting")
        ],
        background="forest/combat_train.jpg",
        items=["Combat Experience"]
    ),

    "final_aftermath": StoryNode(
        text="With Corrupted Dilim defeated, peace returns to the digital world...",
        choices=[
            ("Celebrate victory", "victory_celebration"),
            ("Return home", "game_end")
        ],
        background="final/aftermath.jpg",
        items=["Hero's Medal"]
    ),

    # Missing Village/Quest Nodes
    "luntiang_kanlungan": StoryNode(
        text="The peaceful village of Luntiang Kanlungan welcomes you...",
        choices=[
            ("Visit shops", "village_shops"),
            ("Train", "village_training"),
            ("Accept quests", "village_quests")
        ],
        background="forest/village_main.jpg"
    ),

    # Missing Flow/Study Nodes
    "flow_adjustment": StoryNode(
        text="You carefully adjust the temporal flow...",
        choices=[
            ("Continue adjusting", "time_flow"),
            ("Study effects", "temporal_study")
        ],
        background="lake/flow_adjust.jpg",
        items=["Flow Control"]
    ),

    # Missing End Game Nodes
    "victory_celebration": StoryNode(
        text="The village celebrates your victory over Corrupted Dilim...",
        choices=[
            ("Join celebration", "celebration_feast"),
            ("Reflect quietly", "peaceful_end")
        ],
        background="final/celebration.jpg",
        items=["Victory Token"]
    ),

    "game_end": StoryNode(
        text="Your journey as the Digital Penduko comes to an end...",
        choices=[
            ("New Game", "start"),
            ("Exit", "exit_game")
        ],
        background="final/end_screen.jpg"
    ),

    # Missing Celebration Nodes
    "celebration_feast": StoryNode(
        text="The village holds a grand feast in your honor...",
        choices=[
            ("Thank everyone", "peaceful_end"),
            ("Share stories", "story_sharing")
        ],
        background="final/feast.jpg",
        items=["Feast Medal"]
    ),

    "peaceful_end": StoryNode(
        text="Peace returns to the digital world thanks to your efforts...",
        choices=[
            ("New Journey", "start"),
            ("Rest", "game_end")
        ],
        background="final/peace.jpg",
        items=["Peace Token"]
    ),

    "story_sharing": StoryNode(
        text="You share tales of your adventures with the villagers...",
        choices=[
            ("Continue sharing", "celebration_feast"),
            ("End story", "peaceful_end")
        ],
        background="final/story_share.jpg",
        items=["Story Token"]
    ),

    # Resource/Gathering Related Nodes
    "resource_gathering": StoryNode(
        text="You gather resources for the final battle...",
        choices=[
            ("Gather materials", "material_gathering"),
            ("Study resources", "material_study"),
            ("Return", "preparation_choice")
        ],
        background="forest/resource_gather.jpg",
        items=["Rare Resources"]
    ),

    "item_crafting": StoryNode(
        text="You craft items from gathered materials...",
        choices=[
            ("Craft weapons", "weapon_crafting"),
            ("Craft armor", "armor_crafting"),
            ("Return", "material_study")
        ],
        background="forest/item_craft.jpg",
        items=["Crafted Items"]
    ),

    # Combat/Training Related Nodes
    "magic_test": StoryNode(
        text="You test your mastered magical abilities...",
        choices=[
            ("Continue practice", "magic_mastery"),
            ("Return", "final_training")
        ],
        background="final/magic_test.jpg",
        items=["Magic Test Results"]
    ),

    "power_test": StoryNode(
        text="You test the ancient power systems...",
        choices=[
            ("Continue testing", "system_test"),
            ("Return", "tech_study")
        ],
        background="tech/power_test.jpg",
        items=["Power Test Data"]
    ),

    "energy_experiment": StoryNode(
        text="You conduct experiments with the mysterious energy...",
        choices=[
            ("Continue research", "energy_study"),
            ("Apply findings", "energy_trace")
        ],
        background="forest/energy_experiment.jpg",
        items=["Energy Research"]
    ),

    # Village/Quest Related Nodes
    "magic_tasks": StoryNode(
        text="You assist with various magical tasks...",
        choices=[
            ("Help with rituals", "cleansing_ritual"),
            ("Study with elders", "lore_study"),
            ("Return", "village_quests")
        ],
        background="forest/magic_tasks.jpg",
        items=["Task Completion"]
    ),

    "lore_study": StoryNode(
        text="You study ancient lore with the village elders...",
        choices=[
            ("Continue study", "knowledge_mastery"),
            ("Help with tasks", "magic_tasks"),
            ("Return", "elder_tasks")
        ],
        background="forest/lore_study.jpg",
        items=["Ancient Knowledge"]
    ),

    "equipment_shop": StoryNode(
        text="The village craftsman displays their wares...",
        choices=[
            ("Buy weapons", "weapon_shop"),
            ("Buy armor", "armor_shop"),
            ("Return", "village_shops")
        ],
        background="village/equipment_shop.jpg"
    ),

    "potion_shop": StoryNode(
        text="The alchemist offers various healing potions...",
        choices=[
            ("Browse potions", "buy_potions"),
            ("Return", "village_shops")
        ],
        background="village/potion_shop.jpg"
    ),

    # Final Battle Related Nodes
    "exit_game": StoryNode(
        text="Thank you for playing Digital Penduko!",
        choices=[
            ("New Game", "start"),
            ("Exit", "exit_game")
        ],
        background="main/exit_screen.jpg"
    ),

    "final_upgrades": StoryNode(
        text="You make final improvements to your abilities...",
        choices=[
            ("Test power", "power_testing"),
            ("Face destiny", "final_battle")
        ],
        background="final/upgrades.jpg",
        items=["Final Power-up"]
    ),

    # Study/Analysis Related Nodes
    "pattern_analysis": StoryNode(
        text="You analyze the corruption patterns...",
        choices=[
            ("Study more", "spread_mapping"),
            ("Track source", "corruption_source")
        ],
        background="forest/pattern_analysis.jpg",
        items=["Pattern Data"]
    ),

    "corruption_effects": StoryNode(
        text="You study the effects of corruption...",
        choices=[
            ("Continue study", "effect_study"),
            ("Begin cleansing", "cleansing_ritual")
        ],
        background="forest/corruption_effects.jpg",
        items=["Effects Data"]
    ),

    # Ritual/Cleansing Related Nodes
    "cleansing_ritual": StoryNode(
        text="You perform the cleansing ritual...",
        choices=[
            ("Channel power", "ritual_power"),
            ("Focus energy", "ritual_focus")
        ],
        background="ritual_clearing.jpg",
        items=["Ritual Components"]
    )
}

# Update all background paths to use existing images
def update_all_backgrounds():
    """Update all node backgrounds to use correct identifiers"""
    for node in story_content.values():
        # Main/Starting areas
        if "start" in node.text.lower():
            node.background = "main"
            
        # Forest/Grove areas
        elif "forest" in node.text.lower() or "grove" in node.text.lower():
            node.background = "forest"
            
        # Lake/Water areas
        elif "lake" in node.text.lower() or "water" in node.text.lower():
            node.background = "lake"
            
        # Tech/Terminal areas
        elif "tech" in node.text.lower() or "terminal" in node.text.lower():
            node.background = "tech"
            
        # Village areas
        elif "village" in node.text.lower():
            node.background = "village"
            
        # Boss battles
        elif "twin" in node.text.lower():
            node.background = "twin"
        elif "guardian" in node.text.lower():
            node.background = "guardian"
        elif "dilim" in node.text.lower():
            node.background = "dilim"
            
        # Ritual areas
        elif "ritual" in node.text.lower():
            node.background = "ritual"
            
        # Final areas
        elif "final" in node.text.lower():
            node.background = "final"
            
        # Default
        else:
            node.background = "ancestral_memories.jpg"

# Run the update
update_all_backgrounds()