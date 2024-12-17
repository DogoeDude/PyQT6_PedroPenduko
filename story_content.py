from dataclasses import dataclass
from typing import List, Tuple, Optional

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
        text="In the mystical realm of the Philippines, where technology and magic intertwine, you discover your destiny as the Digital Penduko. Your birthmark glows with an otherworldly power...",
        choices=[
            ("Examine the mysterious birthmark", "examine_mark"),
            ("Explore the surrounding forest", "explore_forest")
        ],
        background="start.jpg"
    ),
    
    "explore_forest": StoryNode(
        text="As you venture deeper into the luminous forest, you discover ancient techno-organic structures pulsing with energy. The trees themselves seem to hum with digital frequencies...",
        choices=[
            ("Investigate the structures", "investigate_structures"),
            ("Follow the humming sound", "follow_sound")
        ],
        background="forest_structures.jpg",
        dimension="Bayan ng Diwata"
    ),
    
    "examine_mark": StoryNode(
        text="As you look at your birthmark, it pulses with increasing intensity. Ancient knowledge floods your mind - you are the descendant of Pedro Penduko...",
        choices=[
            ("Accept your destiny", "accept_destiny"),
            ("Resist the calling", "resist_destiny")
        ],
        background="birthmark.jpg"
    ),
    
    "accept_destiny": StoryNode(
        text="As you embrace your role, the Diwatas of Luntiang Kanlungan appear before you. They speak of the Engkanto Twins who have corrupted their sacred forest's technomagical grid.",
        choices=[
            ("Help the Diwatas", "help_diwatas"),
            ("Seek more information", "seek_info")
        ],
        background="diwata_forest.jpg",
        dimension="Bayan ng Diwata"
    ),

    "resist_destiny": StoryNode(
        text="You try to resist the calling, but the power within you grows stronger. The forest around you responds to your denial, the digital energies becoming unstable...",
        choices=[
            ("Embrace the power", "accept_destiny"),
            ("Continue resisting", "resistance_consequences")
        ],
        background="unstable_forest.jpg"
    ),

    "resistance_consequences": StoryNode(
        text="Your resistance triggers a surge of chaotic energy. The Diwatas appear, warning that your denial could fracture the realms...",
        choices=[
            ("Finally accept your role", "accept_destiny"),
            ("Seek a different path", "alternative_path")
        ],
        background="chaos_energy.jpg"
    ),

    "investigate_structures": StoryNode(
        text="The ancient structures reveal themselves as magical terminals, their surfaces covered in glowing sigils that match your birthmark...",
        choices=[
            ("Interface with the terminal", "terminal_interface"),
            ("Search for more structures", "structure_search")
        ],
        background="magical_terminal.jpg"
    ),

    "follow_sound": StoryNode(
        text="The humming leads you to a clearing where the Engkanto Twins are performing a ritual, their powers affecting the forest's technomagical grid...",
        choices=[
            ("Confront the twins", "twin_confrontation"),
            ("Observe secretly", "secret_observation")
        ],
        background="ritual_clearing.jpg"
    ),

    "help_diwatas": StoryNode(
        text="The Diwatas guide you to their sacred grove, where they begin teaching you how to harness your inherited powers...",
        choices=[
            ("Learn light magic", "light_training"),
            ("Study tech manipulation", "tech_training")
        ],
        background="sacred_grove.jpg",
        items=["Diwata's Token"]
    ),

    "seek_info": StoryNode(
        text="The Diwatas share ancient prophecies about the Digital Penduko and the five dimensions that need saving...",
        choices=[
            ("Ask about the first trial", "first_trial"),
            ("Learn about the enemies", "enemy_info")
        ],
        background="prophecy_chamber.jpg"
    ),

    "terminal_interface": StoryNode(
        text="The terminal activates, downloading ancient knowledge directly into your mind. You learn about the five dimensions and their guardians...",
        choices=[
            ("Process the information", "knowledge_processing"),
            ("Search for more terminals", "terminal_search")
        ],
        background="terminal_active.jpg"
    ),

    "twin_confrontation": StoryNode(
        text="The Engkanto Twins turn to face you, their forms shifting between light and shadow. They seem to have been expecting you...",
        choices=[
            ("Attempt diplomacy", "twin_diplomacy"),
            ("Prepare for battle", "twin_battle")
        ],
        background="engkanto_twins.jpg",
        boss="Engkanto Twins"
    ),

    "knowledge_processing": StoryNode(
        text="The ancient knowledge reveals the true nature of your quest and the importance of balancing technology with magic...",
        choices=[
            ("Begin your journey", "first_trial"),
            ("Seek more knowledge", "terminal_search")
        ],
        background="knowledge_vision.jpg"
    ),

    "first_trial": StoryNode(
        text="Your first trial begins - you must restore balance to the forest's technomagical grid while dealing with the Engkanto Twins...",
        choices=[
            ("Face the twins", "twin_confrontation"),
            ("Search for allies", "seek_allies")
        ],
        background="trial_begins.jpg"
    ),

    "light_training": StoryNode(
        text="The Diwatas teach you to harness light energy, showing how it interacts with both magical and technological systems...",
        choices=[
            ("Practice light manipulation", "light_practice"),
            ("Learn about light's history", "light_history")
        ],
        background="n3.jpg"
    ),

    "tech_training": StoryNode(
        text="You begin learning how to interface with the forest's ancient technology, discovering how it merges with magical energies...",
        choices=[
            ("Study the interfaces", "tech_study"),
            ("Experiment with devices", "tech_experiment")
        ],
        background="n2.jpg"
    ),

    "structure_search": StoryNode(
        text="You discover more ancient structures throughout the forest, each pulsing with a different frequency of techno-magical energy...",
        choices=[
            ("Analyze the patterns", "pattern_analysis"),
            ("Follow the energy flow", "energy_tracking")
        ],
        background="n1.jpg"
    ),

    "secret_observation": StoryNode(
        text="Hidden from view, you watch as the twins perform their ritual. Their powers seem to be causing instability in the forest's grid...",
        choices=[
            ("Continue watching", "gather_intelligence"),
            ("Intervene now", "twin_confrontation")
        ],
        background="n4.jpg"
    ),

    "twin_diplomacy": StoryNode(
        text="You attempt to reason with the Engkanto Twins, sensing that their actions might have a deeper purpose...",
        choices=[
            ("Offer to help them", "twin_alliance"),
            ("Demand explanations", "twin_negotiation")
        ],
        background="n5.jpg"
    ),

    "twin_battle": StoryNode(
        text="The twins unleash their combined powers of light and shadow, creating a spectacular display of techno-magical combat...",
        choices=[
            ("Focus on defense", "defensive_battle"),
            ("Counter-attack", "offensive_battle")
        ],
        background="n6.jpg"
    ),

    "terminal_search": StoryNode(
        text="You search for more terminals, each one containing fragments of ancient knowledge about the five dimensions...",
        choices=[
            ("Connect the fragments", "knowledge_synthesis"),
            ("Seek specific information", "targeted_search")
        ],
        background="n7.jpg"
    ),

    "enemy_info": StoryNode(
        text="The Diwatas reveal information about the various beings who have been corrupted by the dimensional instability...",
        choices=[
            ("Learn about defenses", "defense_training"),
            ("Study their weaknesses", "weakness_analysis")
        ],
        background="n8.jpg"
    ),

    "seek_allies": StoryNode(
        text="You search for potential allies among the forest's inhabitants, each with their own unique powers and knowledge...",
        choices=[
            ("Approach the nature spirits", "spirit_allies"),
            ("Seek tech-savvy beings", "tech_allies")
        ],
        background="n9.jpg"
    ),

    "alternative_path": StoryNode(
        text="Your resistance leads you down a different path, but you soon realize all paths converge toward the same destiny...",
        choices=[
            ("Accept the inevitable", "accept_destiny"),
            ("Find a compromise", "path_compromise")
        ],
        background="n10.jpg"
    ),

    "path_compromise": StoryNode(
        text="You seek a way to fulfill your destiny while maintaining your autonomy, discovering that being the Digital Penduko allows for personal interpretation...",
        choices=[
            ("Forge your own path", "custom_destiny"),
            ("Return to tradition", "accept_destiny")
        ],
        background="n1.jpg"
    ),

    "custom_destiny": StoryNode(
        text="You begin to shape your role as Digital Penduko in your own way, combining traditional knowledge with your personal approach...",
        choices=[
            ("Start your journey", "first_trial"),
            ("Seek more guidance", "seek_info")
        ],
        background="n2.jpg"
    ),

    "defensive_battle": StoryNode(
        text="You focus on defending against the twins' attacks, looking for patterns in their assault...",
        choices=[
            ("Look for an opening", "counter_opportunity"),
            ("Maintain defense", "wear_down")
        ],
        background="n3.jpg"
    ),

    "offensive_battle": StoryNode(
        text="You take the offensive against the twins, forcing them to react to your attacks...",
        choices=[
            ("Press the advantage", "press_attack"),
            ("Fall back", "defensive_battle")
        ],
        background="n4.jpg"
    ),

    "counter_opportunity": StoryNode(
        text="You spot a weakness in the twins' attack pattern and prepare to counter...",
        choices=[
            ("Strike decisively", "battle_victory"),
            ("Offer peace", "twin_diplomacy")
        ],
        background="n5.jpg"
    ),

    "battle_victory": StoryNode(
        text="Your successful counter-attack disrupts the twins' ritual, forcing them to acknowledge your power...",
        choices=[
            ("Show mercy", "twin_alliance"),
            ("Demand surrender", "twin_submission")
        ],
        background="n6.jpg"
    ),

    "twin_alliance": StoryNode(
        text="The Engkanto Twins reveal they were testing your worthiness. They offer to teach you the secrets of balancing light and shadow...",
        choices=[
            ("Accept their teaching", "twin_training"),
            ("Remain cautious", "cautious_alliance")
        ],
        background="n7.jpg",
        items=["Twin's Amulet"]
    ),

    "twin_submission": StoryNode(
        text="The twins bow before your power, but their defeat creates an imbalance in the forest's energy grid...",
        choices=[
            ("Help restore balance", "grid_restoration"),
            ("Seek their knowledge", "forced_teaching")
        ],
        background="n8.jpg"
    ),

    "twin_training": StoryNode(
        text="Under the twins' guidance, you learn to manipulate both light and shadow energies, discovering their complementary nature...",
        choices=[
            ("Master light powers", "light_mastery"),
            ("Focus on shadow arts", "shadow_mastery")
        ],
        background="n9.jpg",
        items=["Light Essence", "Shadow Essence"]
    ),

    "light_practice": StoryNode(
        text="You channel pure light energy, creating dazzling displays of power that interface with the forest's tech grid...",
        choices=[
            ("Experiment further", "light_experiment"),
            ("Apply to combat", "light_combat")
        ],
        background="n10.jpg"
    ),

    "light_history": StoryNode(
        text="The Diwatas share ancient tales of light wielders and their role in maintaining the balance between technology and magic...",
        choices=[
            ("Learn traditional techniques", "traditional_training"),
            ("Develop new methods", "innovative_approach")
        ],
        background="n1.jpg"
    ),

    "tech_study": StoryNode(
        text="You delve deep into the forest's technological systems, discovering they're powered by a fusion of digital and magical energy...",
        choices=[
            ("Optimize the system", "system_optimization"),
            ("Search for vulnerabilities", "security_analysis")
        ],
        background="n2.jpg",
        items=["Tech Manual"]
    ),

    "tech_experiment": StoryNode(
        text="Your experiments with the ancient tech reveal unexpected interactions with your inherited powers...",
        choices=[
            ("Push the limits", "power_surge"),
            ("Document findings", "research_focus")
        ],
        background="n3.jpg"
    ),

    "pattern_analysis": StoryNode(
        text="The energy patterns form a complex network, suggesting a larger purpose behind the forest's techno-magical infrastructure...",
        choices=[
            ("Map the network", "grid_mapping"),
            ("Trace power sources", "source_tracking")
        ],
        background="n4.jpg"
    ),

    "gather_intelligence": StoryNode(
        text="As you observe, you notice the twins are trying to stabilize a dangerous fluctuation in the forest's energy grid...",
        choices=[
            ("Offer assistance", "cooperative_approach"),
            ("Learn their technique", "study_method")
        ],
        background="n5.jpg"
    ),

    "grid_mapping": StoryNode(
        text="Your mapping reveals five major power nodes, each corresponding to a different dimension's influence...",
        choices=[
            ("Visit first node", "node_one_exploration"),
            ("Study the connections", "connection_analysis")
        ],
        background="n6.jpg",
        items=["Grid Map"]
    ),

    "power_surge": StoryNode(
        text="Your experiment triggers a massive surge of power, awakening dormant systems throughout the forest...",
        choices=[
            ("Control the surge", "containment_effort"),
            ("Channel the energy", "power_channeling")
        ],
        background="n7.jpg"
    ),

    "light_mastery": StoryNode(
        text="You achieve remarkable control over light energy, able to create complex techno-magical constructs...",
        choices=[
            ("Create defensive systems", "defense_creation"),
            ("Develop healing abilities", "healing_development")
        ],
        background="n8.jpg",
        items=["Light Master's Ring"]
    ),

    "shadow_mastery": StoryNode(
        text="The shadow arts reveal new aspects of your power, including the ability to navigate between dimensional boundaries...",
        choices=[
            ("Explore dimensions", "dimension_walking"),
            ("Strengthen barriers", "barrier_reinforcement")
        ],
        background="n9.jpg",
        items=["Shadow Walker's Cloak"]
    ),

    "dimension_walking": StoryNode(
        text="You discover the ability to glimpse other dimensions, seeing how they're all connected through the forest's energy grid...",
        choices=[
            ("Enter second dimension", "dimension_two_entry"),
            ("Strengthen your connection", "connection_strengthening")
        ],
        background="n10.jpg"
    ),

    "dimension_two_entry": StoryNode(
        text="You step into the Lake of Infinity, where time flows like water and reality shifts like waves...",
        choices=[
            ("Navigate time streams", "time_navigation"),
            ("Seek the Guardian", "lake_guardian_encounter")
        ],
        background="n1.jpg",
        dimension="Lawa ng Walang Hanggan"
    ),

    "lake_guardian_encounter": StoryNode(
        text="The Guardian of the Abyss emerges, its fluid form containing countless possible futures...",
        choices=[
            ("Challenge the Guardian", "guardian_battle"),
            ("Seek knowledge", "temporal_wisdom")
        ],
        background="n2.jpg",
        boss="Guardian of the Abyss"
    ),

    "temporal_wisdom": StoryNode(
        text="The Guardian shares visions of possible futures, showing the consequences of your choices across dimensions...",
        choices=[
            ("Accept guidance", "future_guidance"),
            ("Forge own path", "independent_future")
        ],
        background="n3.jpg",
        items=["Temporal Crystal"]
    ),

    "future_guidance": StoryNode(
        text="The Guardian reveals a path through time that leads to the Volcano of Wrath, where the Molten Tikbalang awaits...",
        choices=[
            ("Enter the volcano", "volcano_entry"),
            ("Prepare further", "temporal_training")
        ],
        background="n4.jpg",
        items=["Time Shard"]
    ),

    "temporal_training": StoryNode(
        text="You learn to manipulate the flow of time itself, a skill that will prove crucial in the trials ahead...",
        choices=[
            ("Master time dilation", "time_mastery"),
            ("Practice time viewing", "future_sight")
        ],
        background="n5.jpg",
        items=["Chronometer"]
    ),

    "volcano_entry": StoryNode(
        text="The Bulkan ng Galit looms before you, its peaks crackling with techno-magical lightning. The heat is almost unbearable...",
        choices=[
            ("Use tech to cool down", "tech_cooling"),
            ("Channel protective magic", "heat_shield")
        ],
        background="n6.jpg",
        dimension="Bulkan ng Galit"
    ),

    "tech_cooling": StoryNode(
        text="You activate your tech systems, creating a cooling field. Suddenly, you detect multiple heat signatures approaching...",
        choices=[
            ("Analyze signatures", "heat_analysis"),
            ("Prepare for combat", "volcanic_battle")
        ],
        background="n7.jpg",
        items=["Cooling Module"]
    ),

    "heat_shield": StoryNode(
        text="Your magical shield glows as it deflects the intense heat. A deep laugh echoes through the volcanic chambers...",
        choices=[
            ("Track the sound", "tikbalang_encounter"),
            ("Strengthen defenses", "shield_enhancement")
        ],
        background="n8.jpg"
    ),

    "tikbalang_encounter": StoryNode(
        text="The Molten Tikbalang emerges from a lava pool, its form blazing with power. 'So, the Digital Penduko dares to enter my domain...'",
        choices=[
            ("Challenge directly", "tikbalang_battle"),
            ("Attempt negotiation", "tikbalang_parley")
        ],
        background="n9.jpg",
        boss="Molten Tikbalang"
    ),

    "tikbalang_battle": StoryNode(
        text="The battle begins! The Tikbalang summons waves of lava and rains of molten metal...",
        choices=[
            ("Use time powers", "temporal_combat"),
            ("Combine tech and magic", "fusion_attack")
        ],
        background="n10.jpg"
    ),

    "fusion_attack": StoryNode(
        text="You merge your technological cooling systems with magical energy, creating a devastating frost-fire attack...",
        choices=[
            ("Full power", "decisive_strike"),
            ("Strategic blast", "tactical_approach")
        ],
        background="n1.jpg",
        items=["Frost-Fire Core"]
    ),

    "forge_quest": StoryNode(
        text="You discover an ancient forge deep within the volcano. The spirits of master craftsmen still linger here...",
        choices=[
            ("Learn crafting", "ancient_crafting"),
            ("Seek rare materials", "material_hunt")
        ],
        background="n2.jpg"
    ),

    "ancient_crafting": StoryNode(
        text="The spirit of a master craftsman offers to teach you the art of forging techno-magical weapons...",
        choices=[
            ("Forge a weapon", "weapon_creation"),
            ("Create armor", "armor_crafting")
        ],
        background="n3.jpg",
        items=["Spirit Hammer"]
    ),

    "weapon_creation": StoryNode(
        text="You begin the complex process of forging a weapon that can channel both technological and magical energies...",
        choices=[
            ("Forge sword", "penduko_blade"),
            ("Create staff", "tech_staff")
        ],
        background="n4.jpg"
    ),

    "penduko_blade": StoryNode(
        text="The blade takes form, its edge gleaming with digital runes and magical sigils. It hums with power...",
        choices=[
            ("Test the blade", "weapon_testing"),
            ("Add enhancements", "blade_upgrade")
        ],
        background="n5.jpg",
        items=["Digital Blade"]
    ),

    "time_trial": StoryNode(
        text="A mysterious door appears, offering a challenge: Complete a series of tasks before time runs out...",
        choices=[
            ("Accept challenge", "trial_start"),
            ("Prepare more", "trial_preparation")
        ],
        background="n6.jpg"
    ),

    "trial_start": StoryNode(
        text="The trial begins! You must navigate through shifting rooms while solving techno-magical puzzles...",
        choices=[
            ("Focus on speed", "speed_run"),
            ("Solve carefully", "careful_approach")
        ],
        background="n7.jpg",
        items=["Trial Token"]
    ),

    "wear_down": StoryNode(
        text="You maintain your defensive stance, gradually wearing down the twins' energy...",
        choices=[
            ("Launch counter-attack", "counter_opportunity"),
            ("Call for surrender", "offer_peace")
        ],
        background="n8.jpg"
    ),

    "press_attack": StoryNode(
        text="You press your advantage, forcing the twins to separate as they try to avoid your assault...",
        choices=[
            ("Focus on light twin", "light_twin_battle"),
            ("Target shadow twin", "shadow_twin_battle")
        ],
        background="n9.jpg"
    ),

    "light_experiment": StoryNode(
        text="Your experiments with light energy reveal new possibilities for combining magic and technology...",
        choices=[
            ("Create light construct", "construct_creation"),
            ("Enhance existing tech", "tech_enhancement")
        ],
        background="n10.jpg"
    ),

    "light_combat": StoryNode(
        text="You practice combat applications of light magic, learning to create weapons and shields...",
        choices=[
            ("Focus on offense", "light_weapons"),
            ("Master defense", "light_shields")
        ],
        background="n1.jpg"
    ),

    "traditional_training": StoryNode(
        text="The ancient techniques of light manipulation prove to be more powerful than you expected...",
        choices=[
            ("Master basics", "basic_mastery"),
            ("Learn advanced forms", "advanced_training")
        ],
        background="n2.jpg"
    ),

    "innovative_approach": StoryNode(
        text="You begin developing new ways to use light energy, combining traditional knowledge with modern tech...",
        choices=[
            ("Test new technique", "technique_testing"),
            ("Document findings", "research_documentation")
        ],
        background="n3.jpg"
    ),

    "system_optimization": StoryNode(
        text="You work on improving the efficiency of the forest's techno-magical systems...",
        choices=[
            ("Upgrade hardware", "hardware_enhancement"),
            ("Refine energy flow", "energy_optimization")
        ],
        background="n4.jpg"
    ),

    "security_analysis": StoryNode(
        text="Your investigation reveals potential vulnerabilities in the forest's defensive systems...",
        choices=[
            ("Strengthen defenses", "defense_upgrade"),
            ("Set up monitoring", "security_monitoring")
        ],
        background="n5.jpg"
    ),

    "research_focus": StoryNode(
        text="You carefully document your findings about the interaction between technology and magic...",
        choices=[
            ("Continue research", "deep_research"),
            ("Apply findings", "practical_application")
        ],
        background="n6.jpg"
    ),

    "source_tracking": StoryNode(
        text="You follow the energy sources, discovering a complex network of power distribution...",
        choices=[
            ("Map the network", "network_mapping"),
            ("Investigate anomalies", "anomaly_research")
        ],
        background="n7.jpg"
    ),

    "cooperative_approach": StoryNode(
        text="You step forward to help the twins stabilize the energy grid...",
        choices=[
            ("Share your power", "power_sharing"),
            ("Offer technical help", "tech_assistance")
        ],
        background="n8.jpg"
    ),

    "study_method": StoryNode(
        text="You observe the twins' technique, learning how they manipulate the forest's energy...",
        choices=[
            ("Try their method", "technique_practice"),
            ("Develop improvement", "technique_enhancement")
        ],
        background="n9.jpg"
    ),

    "containment_effort": StoryNode(
        text="You work to contain the power surge, preventing it from destabilizing the forest...",
        choices=[
            ("Channel excess power", "power_channeling"),
            ("Create containment field", "field_creation")
        ],
        background="n10.jpg"
    ),

    "power_channeling": StoryNode(
        text="You begin channeling the excess energy into useful applications...",
        choices=[
            ("Power up systems", "system_enhancement"),
            ("Store for later", "energy_storage")
        ],
        background="n1.jpg"
    ),

    "defense_creation": StoryNode(
        text="You work on creating defensive systems using your mastery of light energy...",
        choices=[
            ("Build barriers", "barrier_construction"),
            ("Create wards", "ward_creation")
        ],
        background="n2.jpg"
    ),

    "healing_development": StoryNode(
        text="You discover how to use light energy for healing and restoration...",
        choices=[
            ("Practice healing", "healing_practice"),
            ("Study restoration", "restoration_study")
        ],
        background="n3.jpg"
    ),

    "connection_strengthening": StoryNode(
        text="You work on strengthening your connection to the dimensional energies...",
        choices=[
            ("Deepen bond", "bond_strengthening"),
            ("Expand awareness", "awareness_expansion")
        ],
        background="n4.jpg"
    ),

    "time_navigation": StoryNode(
        text="You learn to navigate the complex currents of time in the Lake of Infinity...",
        choices=[
            ("Explore future", "future_exploration"),
            ("Study past", "past_investigation")
        ],
        background="n5.jpg"
    ),

    "guardian_battle": StoryNode(
        text="You engage in combat with the Guardian of the Abyss, dodging its temporal attacks...",
        choices=[
            ("Use time powers", "temporal_combat"),
            ("Physical assault", "direct_combat")
        ],
        background="n6.jpg"
    ),

    "independent_future": StoryNode(
        text="You choose to forge your own path through time, seeking your own answers...",
        choices=[
            ("Explore dimensions", "dimension_exploration"),
            ("Seek knowledge", "knowledge_quest")
        ],
        background="n7.jpg"
    ),

    "time_mastery": StoryNode(
        text="Your practice with time manipulation grows stronger, allowing greater control...",
        choices=[
            ("Speed mastery", "acceleration_mastery"),
            ("Slow mastery", "deceleration_mastery")
        ],
        background="n8.jpg"
    ),

    "future_sight": StoryNode(
        text="You develop the ability to glimpse possible futures, seeing the consequences of choices...",
        choices=[
            ("Study visions", "vision_analysis"),
            ("Test predictions", "prediction_testing")
        ],
        background="n9.jpg"
    ),

    "heat_analysis": StoryNode(
        text="Your analysis reveals multiple heat signatures moving through the volcanic chambers...",
        choices=[
            ("Track movements", "signature_tracking"),
            ("Prepare defenses", "defense_preparation")
        ],
        background="n10.jpg"
    ),

    "volcanic_battle": StoryNode(
        text="You engage in combat with volcanic creatures, their bodies made of living magma...",
        choices=[
            ("Use cooling tech", "tech_combat"),
            ("Magic defense", "magic_shield")
        ],
        background="n1.jpg"
    ),

    "shield_enhancement": StoryNode(
        text="You strengthen your magical shields against the intense volcanic heat...",
        choices=[
            ("Layer defenses", "shield_layering"),
            ("Add tech support", "tech_integration")
        ],
        background="n2.jpg"
    ),

    "tikbalang_parley": StoryNode(
        text="You attempt to negotiate with the Molten Tikbalang, sensing a deeper reason for its actions...",
        choices=[
            ("Offer alliance", "tikbalang_alliance"),
            ("Seek compromise", "peaceful_resolution")
        ],
        background="n3.jpg"
    ),

    "temporal_combat": StoryNode(
        text="You use your time manipulation powers in combat, creating temporal advantages...",
        choices=[
            ("Slow time", "time_slow"),
            ("Speed self", "time_acceleration")
        ],
        background="n4.jpg"
    ),

    "decisive_strike": StoryNode(
        text="You channel all your power into a single, devastating attack...",
        choices=[
            ("Full force", "maximum_power"),
            ("Precise strike", "targeted_attack")
        ],
        background="n5.jpg"
    ),

    "tactical_approach": StoryNode(
        text="You carefully plan your attack, looking for the most efficient way to succeed...",
        choices=[
            ("Find weakness", "weakness_exploitation"),
            ("Create opening", "opportunity_creation")
        ],
        background="n6.jpg"
    ),

    "material_hunt": StoryNode(
        text="You search the volcanic chambers for rare materials needed for crafting...",
        choices=[
            ("Mine resources", "resource_gathering"),
            ("Search secrets", "secret_discovery")
        ],
        background="n7.jpg"
    ),

    "armor_crafting": StoryNode(
        text="You begin the process of creating techno-magical armor...",
        choices=[
            ("Focus protection", "defensive_armor"),
            ("Add enhancements", "enhanced_armor")
        ],
        background="n8.jpg"
    ),

    "weapon_testing": StoryNode(
        text="You test your newly forged weapon, discovering its unique properties...",
        choices=[
            ("Combat practice", "combat_training"),
            ("Power testing", "power_testing")
        ],
        background="n9.jpg"
    ),

    "blade_upgrade": StoryNode(
        text="You work on enhancing your weapon with additional features...",
        choices=[
            ("Add tech", "tech_enhancement"),
            ("Enhance magic", "magic_enhancement")
        ],
        background="n10.jpg"
    ),

    "trial_preparation": StoryNode(
        text="You prepare yourself for the upcoming time trial...",
        choices=[
            ("Study patterns", "pattern_study"),
            ("Practice skills", "skill_practice")
        ],
        background="n1.jpg"
    ),

    "speed_run": StoryNode(
        text="You focus on completing the trial as quickly as possible...",
        choices=[
            ("Take risks", "risky_approach"),
            ("Efficient path", "optimal_route")
        ],
        background="n2.jpg"
    ),

    "careful_approach": StoryNode(
        text="You take your time to ensure each step is correct...",
        choices=[
            ("Analyze patterns", "pattern_recognition"),
            ("Safe progress", "methodical_advance")
        ],
        background="n3.jpg"
    ),

    "construct_creation": StoryNode(
        text="You focus your light energy to create solid constructs of pure energy...",
        choices=[
            ("Create weapon", "light_weapon_creation"),
            ("Form shield", "light_shield_creation")
        ],
        background="n4.jpg"
    ),

    "tech_enhancement": StoryNode(
        text="You begin integrating light energy into your existing technology...",
        choices=[
            ("Enhance defenses", "defense_enhancement"),
            ("Upgrade weapons", "weapon_enhancement")
        ],
        background="n5.jpg"
    ),

    "light_weapons": StoryNode(
        text="You learn to form weapons from pure light energy...",
        choices=[
            ("Practice accuracy", "accuracy_training"),
            ("Increase power", "power_training")
        ],
        background="n6.jpg"
    ),

    "light_shields": StoryNode(
        text="Your defensive light constructs grow stronger with practice...",
        choices=[
            ("Reinforce shields", "shield_reinforcement"),
            ("Add counter-measures", "shield_offense")
        ],
        background="n7.jpg"
    ),

    "basic_mastery": StoryNode(
        text="The fundamental techniques of light manipulation become second nature...",
        choices=[
            ("Perfect basics", "basic_perfection"),
            ("Move to advanced", "advanced_transition")
        ],
        background="n8.jpg"
    ),

    "advanced_training": StoryNode(
        text="You begin learning more complex light manipulation techniques...",
        choices=[
            ("Focus on control", "control_mastery"),
            ("Expand power", "power_expansion")
        ],
        background="n9.jpg"
    ),

    "technique_testing": StoryNode(
        text="You carefully test your new approach to light manipulation...",
        choices=[
            ("Refine technique", "technique_refinement"),
            ("Push boundaries", "boundary_testing")
        ],
        background="n10.jpg"
    ),

    "research_documentation": StoryNode(
        text="You document your discoveries about combining traditional and modern techniques...",
        choices=[
            ("Analyze results", "result_analysis"),
            ("Plan improvements", "improvement_planning")
        ],
        background="n1.jpg"
    ),

    "hardware_enhancement": StoryNode(
        text="You work on upgrading the physical components of the forest's tech...",
        choices=[
            ("Install upgrades", "system_upgrade"),
            ("Test stability", "stability_check")
        ],
        background="n2.jpg"
    ),

    "energy_optimization": StoryNode(
        text="You fine-tune the energy flow through the forest's systems...",
        choices=[
            ("Balance flows", "flow_balancing"),
            ("Increase efficiency", "efficiency_boost")
        ],
        background="n3.jpg"
    ),

    "defense_upgrade": StoryNode(
        text="You begin strengthening the weaknesses in the forest's defenses...",
        choices=[
            ("Reinforce barriers", "barrier_upgrade"),
            ("Add new systems", "system_addition")
        ],
        background="n4.jpg"
    ),

    "security_monitoring": StoryNode(
        text="You set up systems to monitor and respond to threats...",
        choices=[
            ("Configure alerts", "alert_setup"),
            ("Create responses", "response_planning")
        ],
        background="n5.jpg"
    ),

    "deep_research": StoryNode(
        text="Your continued research reveals deeper mysteries about tech-magic fusion...",
        choices=[
            ("Study patterns", "pattern_study"),
            ("Test theories", "theory_testing")
        ],
        background="n6.jpg"
    ),

    "practical_application": StoryNode(
        text="You begin applying your research findings to real-world problems...",
        choices=[
            ("Test solutions", "solution_testing"),
            ("Gather data", "data_collection")
        ],
        background="n7.jpg"
    ),

    "network_mapping": StoryNode(
        text="You create a detailed map of the forest's energy network...",
        choices=[
            ("Analyze patterns", "pattern_analysis"),
            ("Identify nodes", "node_identification")
        ],
        background="n8.jpg"
    ),

    "anomaly_research": StoryNode(
        text="You investigate unusual patterns in the energy distribution...",
        choices=[
            ("Study effects", "effect_analysis"),
            ("Trace sources", "source_tracing")
        ],
        background="n9.jpg"
    ),

    "power_sharing": StoryNode(
        text="You share your power with the twins to help stabilize the grid...",
        choices=[
            ("Maintain balance", "balance_maintenance"),
            ("Guide energy", "energy_guidance")
        ],
        background="n10.jpg"
    ),

    "tech_assistance": StoryNode(
        text="You offer your technical expertise to help with the stabilization...",
        choices=[
            ("Repair systems", "system_repair"),
            ("Optimize flow", "flow_optimization")
        ],
        background="n1.jpg"
    ),

    "energy_tracking": StoryNode(
        text="You follow the energy flows through the forest, discovering how they connect different areas of the techno-magical grid...",
        choices=[
            ("Map the flows", "energy_mapping"),
            ("Study patterns", "energy_patterns")
        ],
        background="n3.jpg"
    ),

    "energy_mapping": StoryNode(
        text="Your mapping reveals a complex network of energy channels, some leading to previously unknown areas...",
        choices=[
            ("Follow new paths", "explore_channels"),
            ("Document findings", "record_discoveries")
        ],
        background="n4.jpg"
    ),

    "energy_patterns": StoryNode(
        text="The energy patterns show regular fluctuations, suggesting a deeper order to the forest's power grid...",
        choices=[
            ("Analyze rhythm", "study_fluctuations"),
            ("Search source", "locate_source")
        ],
        background="n5.jpg"
    ),

    "light_weapon_creation": StoryNode(
        text="You focus your energy into forming a weapon of pure light, its form shifting based on your thoughts...",
        choices=[
            ("Form blade", "light_blade"),
            ("Create bow", "light_bow")
        ],
        background="n6.jpg"
    ),

    "light_shield_creation": StoryNode(
        text="The light coalesces into a protective barrier, responding to your will and strengthening your defenses...",
        choices=[
            ("Reinforce shield", "strengthen_defense"),
            ("Add counter", "reactive_shield")
        ],
        background="n7.jpg"
    ),

    "defense_enhancement": StoryNode(
        text="You work on improving your defensive capabilities, combining technology with light magic...",
        choices=[
            ("Test defenses", "defense_testing"),
            ("Add features", "defense_upgrade")
        ],
        background="n8.jpg"
    ),

    "weapon_enhancement": StoryNode(
        text="Your weapons grow stronger as you integrate new techno-magical improvements...",
        choices=[
            ("Test power", "power_testing"),
            ("Fine-tune", "weapon_tuning")
        ],
        background="n9.jpg"
    ),

    "accuracy_training": StoryNode(
        text="You practice your aim with the light weapons, learning to hit increasingly difficult targets...",
        choices=[
            ("Continue practice", "advanced_accuracy"),
            ("Try new techniques", "new_methods")
        ],
        background="n10.jpg"
    ),

    "power_training": StoryNode(
        text="Your training focuses on increasing the raw power of your light-based attacks...",
        choices=[
            ("Push limits", "power_limits"),
            ("Control output", "power_control")
        ],
        background="n1.jpg"
    ),

    "shield_reinforcement": StoryNode(
        text="You strengthen your light shields, making them more resilient against both physical and magical attacks...",
        choices=[
            ("Test strength", "shield_testing"),
            ("Add layers", "shield_layers")
        ],
        background="n2.jpg"
    ),

    "shield_offense": StoryNode(
        text="You develop ways to use your shields offensively, turning defense into attack...",
        choices=[
            ("Practice technique", "offensive_shield"),
            ("Refine control", "shield_mastery")
        ],
        background="n3.jpg"
    ),

    "explore_channels": StoryNode(
        text="You venture into the newly discovered energy channels, finding strange artifacts and ancient technology...",
        choices=[
            ("Study artifacts", "artifact_analysis"),
            ("Follow deeper", "deep_exploration")
        ],
        background="n4.jpg"
    ),

    "record_discoveries": StoryNode(
        text="You carefully document your findings about the energy network, uncovering patterns that suggest a greater purpose...",
        choices=[
            ("Research patterns", "pattern_research"),
            ("Share findings", "knowledge_share")
        ],
        background="n5.jpg"
    ),

    "study_fluctuations": StoryNode(
        text="The rhythm of the energy fluctuations seems to match an ancient prophecy about the Digital Penduko...",
        choices=[
            ("Study prophecy", "prophecy_research"),
            ("Monitor changes", "energy_monitoring")
        ],
        background="n6.jpg"
    ),

    "locate_source": StoryNode(
        text="You track the energy patterns to their source, finding a massive ancient terminal pulsing with power...",
        choices=[
            ("Access terminal", "terminal_access"),
            ("Scan area", "area_scan")
        ],
        background="n7.jpg"
    )
} 