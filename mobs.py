class Dimension:
    def __init__(self, name, mechanics, lore, village_name, village_description, activities):
        self.name = name
        self.mechanics = mechanics
        self.lore = lore
        self.village = Village(village_name, village_description, activities)

    def display_info(self):
        return f"Dimension: {self.name}\nLore: {self.lore}\nMechanics: {self.mechanics}"


class Village:
    def __init__(self, name, description, activities):
        self.name = name
        self.description = description
        self.activities = activities

    def display_info(self):
        return f"Village: {self.name}\nDescription: {self.description}\nActivities: {', '.join(self.activities)}"


class Boss:
    def __init__(self, name, virtue, special_ability):
        self.name = name
        self.virtue = virtue
        self.special_ability = special_ability

    def display_info(self):
        return f"Boss: {self.name}\nVirtue: {self.virtue}\nSpecial Ability: {self.special_ability}"


class SubBoss:
    def __init__(self, name, challenge_type, reward):
        self.name = name
        self.challenge_type = challenge_type
        self.reward = reward

    def display_info(self):
        return f"Sub-Boss: {self.name}\nChallenge: {self.challenge_type}\nReward: {self.reward}"


class Item:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats

    def upgrade(self, enhancement):
        for stat, value in enhancement.items():
            if stat in self.stats:
                self.stats[stat] += value

    def display_info(self):
        return f"Item: {self.name}\nStats: {self.stats}"


# All Dimensions
dimensions = [
    Dimension(
        name="Bayan ng Diwata (City of the Fairies)",
        mechanics="Maze navigation using programming logic",
        lore="A radiant forest of magical light and advanced tech.",
        village_name="Luntiang Kanlungan (Green Haven)",
        village_description="A bustling, nature-integrated village where Diwatas live in harmony with technology.",
        activities=[
            "Upgrade magical tools using forest materials",
            "Complete side quests to learn coding-based spells",
            "Solve environmental puzzles"
        ]
    ),
    Dimension(
        name="Lawa ng Walang Hanggan (Lake of Infinity)",
        mechanics="Battle mechanics slow down time, requiring precise actions.",
        lore="A shimmering, endless lake where time flows differently.",
        village_name="Baybay ng Tala (Shore of Stars)",
        village_description="A serene lakeside village where time flows unevenly.",
        activities=[
            "Collect Temporal Crystals to create or upgrade the Infinity Stopwatch",
            "Debug 'time distortions' in villagers' temporal devices",
            "Participate in races against time anomalies"
        ]
    ),
    Dimension(
        name="Bulkan ng Galit (Volcano of Wrath)",
        mechanics="Heat damage over time; solve equations to cool the environment.",
        lore="A fiery domain ruled by angered elemental spirits.",
        village_name="Pugon ng Lakas (Forge of Strength)",
        village_description="A volcanic settlement where blacksmiths use molten lava to forge magical weapons.",
        activities=[
            "Trade rare ores to craft Kapre's Smoke Filter and Volcano Core",
            "Learn combat techniques from fire-wielding NPCs",
            "Solve mini-games involving managing heat levels"
        ]
    ),
    Dimension(
        name="Patay na Lupa (Dead Lands)",
        mechanics="Stealth-based gameplay and resource management.",
        lore="A barren wasteland crawling with corrupted spirits.",
        village_name="Silungan ng Kaluluwa (Refuge of Souls)",
        village_description="A hidden settlement protected by ghostly wards.",
        activities=[
            "Collect spectral energy to reinforce Shadow Cloak",
            "Restore magical barriers by completing stealth missions",
            "Decode ancient texts to unlock Lake’s Tear"
        ]
    ),
    Dimension(
        name="Bilangguan ng Anino (Prison of Shadows)",
        mechanics="Light-based puzzles and memory-based challenges.",
        lore="A dimension of illusions where nothing is as it seems.",
        village_name="Liwayway ng Liwanag (Dawn of Light)",
        village_description="A settlement combating shadow creatures using light-based technologies.",
        activities=[
            "Build and upgrade Light Prism Lens using collected shards",
            "Assist villagers in crafting light-based traps",
            "Solve shadow puzzles to uncover secrets about the final boss"
        ]
    )
]

# All Main Bosses
bosses = [
    Boss("Haraya", "Imagination", "Generates illusions to confuse the player"),
    Boss("Sigla", "Energy", "Auras that sap the protagonist's stamina over time"),
    Boss("Karunungan", "Wisdom", "Counters programming solutions by corrupting code"),
    Boss("Tapang", "Courage", "Resistance to damage until specific puzzles are solved"),
    Boss("Pag-asa", "Hope", "Periodically heals unless disrupted"),
    Boss("Liwanag", "Light", "Switches between light and dark forms, altering attack patterns"),
    Boss("Dilim", "Darkness", "Combines all other bosses' powers into one")
]

# All Sub-Bosses
sub_bosses = [
    SubBoss("Engkanto Twins", "Harmonize light patterns", "Diwata's Token"),
    SubBoss("Molten Tikbalang", "Test fire-resistance tactics", "Volcano Core"),
    SubBoss("Tiyanak General", "Requires stealth and strategy", "Shadow Cloak")
]

# All Unique Items
items = [
    Item("Agimat Compiler", {"execution_speed": 10, "cooldown_reduction": 5}),
    Item("Diwata's Token", {"invincibility_duration": 5}),
    Item("Kapre's Smoke Filter", {"environmental_damage_reduction": 20}),
    Item("Tikbalang's Talisman", {"stamina_boost": 15, "speed_boost": 10}),
    Item("Lake’s Tear", {"health_restoration": 100}),
    Item("Light Prism Lens", {"illusion_detection": 20}),
    Item("Volcano Core", {"fire_resistance": 30}),
    Item("Shadow Cloak", {"stealth_duration": 10}),
    Item("Infinity Stopwatch", {"time_freeze_duration": 5}),
    Item("Penduko's Legacy", {"ultimate_skill_power": 50})
]

# Displaying All Data
print("=== Dimensions ===")
for dimension in dimensions:
    print(dimension.display_info())
    print(dimension.village.display_info(), "\n")

print("=== Bosses ===")
for boss in bosses:
    print(boss.display_info(), "\n")

print("=== Sub-Bosses ===")
for sub_boss in sub_bosses:
    print(sub_boss.display_info(), "\n")

print("=== Items ===")
for item in items:
    print(item.display_info(), "\n")

print(len(items))
print(len(sub_bosses))
print(len(bosses))
print(len(dimensions))