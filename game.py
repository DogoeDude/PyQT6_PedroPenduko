from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, 
                            QVBoxLayout, QHBoxLayout, QLabel, QFrame, QProgressBar)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap, QPalette, QColor
import sys
import os
from story_content import story_content, StoryNode
from audio_manager import AudioManager
from player import Player
from combat_manager import CombatManager
import random

class StoryGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Legacy of the Digital Penduko")
        self.setMinimumSize(1024, 768)  # Increased size for better visibility
        
        # Initialize story state
        self.current_dimension = 0
        self.current_text_index = 0
        self.text_animation_speed = 50
        self.is_animating = False
        
        # Define background image sets FIRST
        self.backgrounds = {
            'forest': [
                "diwata_forest.jpg",
                "forest_structures.jpg",
                "sacred_grove.jpg",
                "unstable_forest.jpg"
            ],
            'lake': [
                "lawa_background.jpg",
                "chaos_energy.jpg"
            ],
            'ritual': [
                "ritual_clearing.jpg",
                "prophecy_chamber.jpg"
            ],
            'village': [
                "diwata_village.jpg",
                "ancestral_memories.png"
            ],
            'final': [
                "bulkan_background.jpg",
                "patay_background.jpg"
            ],
            'main': [
                "start.jpg",
                "intro_background.jpg"
            ],
            'tech': [
                "magical_terminal.jpg",
                "terminal_active.jpg",
                "digital_awakening.jpg"
            ],
            # Numbered backgrounds for rotation
            'numbered': [
                "n1.jpg", "n2.jpg", "n3.jpg", "n4.jpg", "n5.jpg",
                "n6.jpg", "n7.jpg", "n8.jpg", "n9.jpg", "n10.jpg"
            ]
        }
        
        # Boss battle backgrounds
        self.boss_backgrounds = {
            "Engkanto Twins": "engkanto_twins.jpg",
            "Guardian of the Abyss": "dimensional_patterns.jpg",
            "Corrupted Dilim": "chaos_energy.jpg",
            "Molten Tikbalang": "molten_tikbalang.jpg"
        }
        
        # Image handling - SIMPLIFIED
        self.image_folder = "images"  # Just one folder for all images
        self.default_image = "ancestral_memories.png"
        
        # Initialize audio manager
        self.audio = AudioManager()
        
        # Initialize player first
        self.player = Player()
        
        # Initialize combat manager
        self.combat = CombatManager(self.player)
        
        # Setup UI
        self.setup_ui()
        
        # Initialize story content
        self.story_content = story_content
        self.current_node = "start"
        self.story_history = []
        
        # Define training nodes
        self.training_nodes = {
            "power_strike_training",
            "defense_training",
            "magic_practice",
            "code_magic",
            "time_mastery",
            "skill_mastery",
            "combat_basics",
            "magic_basics"
        }
        
        # Add tracking for last boss
        self.last_boss_node = None  # Track the last boss node we encountered
        
        # Start the game
        self.show_current_scene()

    def setup_ui(self):
        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        
        # Create game area
        game_area = QWidget()
        game_layout = QHBoxLayout(game_area)
        
        # Background image
        self.background_label = QLabel()
        self.background_label.setMinimumSize(800, 600)
        self.background_label.setScaledContents(True)
        
        # Story text display
        self.text_display = QLabel()
        self.text_display.setWordWrap(True)
        self.text_display.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.text_display.setStyleSheet("""
            QLabel {
                background-color: rgba(0, 0, 0, 180);
                color: white;
                padding: 20px;
                border-radius: 10px;
                font-size: 16px;
                margin: 20px;
            }
        """)
        
        # Stack text over background
        stack_layout = QVBoxLayout()
        stack_layout.addWidget(self.background_label)
        stack_layout.addWidget(self.text_display)
        stack_layout.setAlignment(self.text_display, Qt.AlignmentFlag.AlignBottom)
        
        # Choice buttons
        button_layout = QHBoxLayout()
        self.left_button = QPushButton("Choice 1")
        self.right_button = QPushButton("Choice 2")
        
        self.left_button.setMinimumWidth(200)
        self.right_button.setMinimumWidth(200)
        
        self.left_button.clicked.connect(lambda: self.make_choice(0))
        self.right_button.clicked.connect(lambda: self.make_choice(1))
        
        button_layout.addWidget(self.left_button)
        button_layout.addWidget(self.right_button)
        
        # Add boss return button (initially hidden)
        self.boss_return_button = QPushButton("Return to Boss")
        self.boss_return_button.clicked.connect(lambda: self.make_choice(2))  # Third choice
        self.boss_return_button.hide()
        button_layout.addWidget(self.boss_return_button)
        
        # Control buttons
        control_layout = QHBoxLayout()
        self.back_button = QPushButton("Back")
        self.skip_button = QPushButton("Skip")
        
        self.back_button.clicked.connect(self.go_back)
        self.skip_button.clicked.connect(self.skip_animation)
        
        control_layout.addWidget(self.back_button)
        control_layout.addWidget(self.skip_button)
        
        # Stats display
        self.stats_frame = QFrame()
        stats_layout = QVBoxLayout(self.stats_frame)
        
        self.hp_label = QLabel(f"HP: {self.player.stats.hp}/{self.player.stats.max_hp}")
        self.level_label = QLabel(f"Level: {self.player.stats.level}")
        self.exp_label = QLabel(f"EXP: {self.player.stats.exp}/{self.player.stats.exp_to_next}")
        
        stats_layout.addWidget(self.hp_label)
        stats_layout.addWidget(self.level_label)
        stats_layout.addWidget(self.exp_label)
        
        self.stats_frame.setStyleSheet("""
            QFrame {
                background-color: rgba(0, 0, 0, 180);
                border-radius: 10px;
                padding: 10px;
            }
            QLabel {
                color: white;
                font-size: 14px;
            }
        """)
        
        # Add potion buttons
        potion_layout = QHBoxLayout()
        self.minor_potion_btn = QPushButton("Use Minor Potion")
        self.major_potion_btn = QPushButton("Use Major Potion")
        self.full_potion_btn = QPushButton("Use Full Potion")
        
        self.minor_potion_btn.clicked.connect(lambda: self.use_potion("Minor Healing Potion"))
        self.major_potion_btn.clicked.connect(lambda: self.use_potion("Major Healing Potion"))
        self.full_potion_btn.clicked.connect(lambda: self.use_potion("Full Restore Potion"))
        
        potion_layout.addWidget(self.minor_potion_btn)
        potion_layout.addWidget(self.major_potion_btn)
        potion_layout.addWidget(self.full_potion_btn)
        
        # Add boss HP bar (initially hidden)
        boss_layout = QHBoxLayout()
        self.boss_name_label = QLabel("")
        self.boss_hp_label = QLabel("")
        
        # Style the boss HP bar
        self.boss_hp_bar = QProgressBar()
        self.boss_hp_bar.setMinimum(0)
        self.boss_hp_bar.setMaximum(100)
        self.boss_hp_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid grey;
                border-radius: 5px;
                text-align: center;
                background-color: #333333;
            }
            QProgressBar::chunk {
                background-color: #8B0000;  /* Dark red for boss HP */
            }
        """)
        
        boss_layout.addWidget(self.boss_name_label)
        boss_layout.addWidget(self.boss_hp_bar)
        boss_layout.addWidget(self.boss_hp_label)
        
        # Hide boss UI initially
        self.boss_name_label.hide()
        self.boss_hp_bar.hide()
        self.boss_hp_label.hide()
        
        # Add boss layout to main layout (before the potion buttons)
        main_layout.addLayout(boss_layout)
        
        # Combine layouts
        main_layout.addLayout(stack_layout)
        main_layout.addLayout(button_layout)
        main_layout.addLayout(control_layout)
        main_layout.addWidget(self.stats_frame)
        main_layout.addLayout(potion_layout)
        
        # Style buttons
        self.style_buttons()
        
        # Add sound effects to buttons
        self.left_button.clicked.connect(lambda: self.audio.play_sfx("button_click"))
        self.right_button.clicked.connect(lambda: self.audio.play_sfx("button_click"))
        self.back_button.clicked.connect(lambda: self.audio.play_sfx("button_click"))
        self.skip_button.clicked.connect(lambda: self.audio.play_sfx("button_click"))

    def load_image(self, image_name):
        """Load image from images folder with error handling and logging"""
        image_path = os.path.join(self.image_folder, image_name)
        print(f"Attempting to load image: {image_path}")  # Debug print
        
        if not os.path.exists(image_path):
            print(f"Warning: Image not found: {image_path}")  # Debug print
            image_path = os.path.join(self.image_folder, self.default_image)
            if not os.path.exists(image_path):
                print(f"Error: Default image not found: {image_path}")  # Debug print
                # Create a colored background as fallback
                pixmap = QPixmap(800, 600)
                pixmap.fill(QColor(53, 53, 53))
                return pixmap
        
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print(f"Error: Failed to load image: {image_path}")  # Debug print
            # Create a colored background as fallback
            pixmap = QPixmap(800, 600)
            pixmap.fill(QColor(53, 53, 53))
        
        return pixmap

    def show_current_scene(self):
        """Display the current story node"""
        current_node = self.story_content[self.current_node]
        
        # Track boss encounters for return button
        if hasattr(current_node, 'boss') and current_node.boss:
            self.last_boss_node = self.current_node
        
        # Add "Return to Boss" option if we're in a training node and have a boss pending
        if self.current_node in self.training_nodes and self.last_boss_node:
            current_choices = list(current_node.choices)
            current_choices.append(("Return to Boss", self.last_boss_node))
            current_node.choices = current_choices
            
            # Update button text for all choices
            if len(current_choices) > 2:
                self.left_button.setText(current_choices[0][0])
                self.right_button.setText(current_choices[1][0])
                self.boss_return_button.setText(current_choices[2][0])
                self.boss_return_button.show()
            else:
                self.boss_return_button.hide()
        
        print(f"Current node: {self.current_node}")
        print(f"Background setting: {current_node.background}")  # Debug what background is set
        bg_name = self.get_background(current_node.background)
        print(f"Selected background: {bg_name}")  # Debug what background was selected
        
        # Get background image
        bg_name = self.get_background(current_node.background)
        image_path = os.path.join(self.image_folder, bg_name)
        
        print(f"Loading image: {image_path}")  # Debug print
        
        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                self.background_label.setPixmap(pixmap.scaled(self.background_label.size(), Qt.AspectRatioMode.KeepAspectRatio))
            else:
                print(f"Error loading image: {image_path}")
                self.background_label.setPixmap(QPixmap(os.path.join(self.image_folder, self.default_image)))
        else:
            print(f"Image not found: {image_path}")
            self.background_label.setPixmap(QPixmap(os.path.join(self.image_folder, self.default_image)))
        
        # Enhanced music selection based on scene context
        if hasattr(current_node, 'boss') and current_node.boss:
            self.audio.play_bgm("boss_battle")
        elif "battle" in current_node.text.lower() or "combat" in current_node.text.lower():
            self.audio.play_bgm("battle")
        elif "victory" in current_node.text.lower() or "success" in current_node.text.lower():
            self.audio.play_bgm("victory")
        elif current_node.dimension == "Bayan ng Diwata":
            self.audio.play_bgm("diwata_forest")
        elif self.current_node == "start":
            self.audio.play_bgm("main_menu")
        else:
            self.audio.play_bgm("forest")
        
        # Update choices
        if current_node.choices:
            self.left_button.setText(current_node.choices[0][0])
            self.right_button.setText(current_node.choices[1][0])
            self.left_button.setEnabled(True)
            self.right_button.setEnabled(True)
        else:
            self.left_button.setEnabled(False)
            self.right_button.setEnabled(False)
        
        # Start text animation
        self.animate_text(current_node.text)

    def style_buttons(self):
        button_style = """
            QPushButton {
                background-color: rgba(60, 60, 60, 200);
                color: white;
                border: 2px solid #555555;
                border-radius: 10px;
                padding: 15px;
                font-size: 14px;
                margin: 10px;
            }
            QPushButton:hover {
                background-color: rgba(80, 80, 80, 200);
                border: 2px solid #666666;
            }
            QPushButton:pressed {
                background-color: rgba(40, 40, 40, 200);
            }
            QPushButton:disabled {
                background-color: rgba(40, 40, 40, 100);
                border: 2px solid #333333;
                color: #888888;
            }
        """
        
        for button in [self.left_button, self.right_button, 
                      self.back_button, self.skip_button]:
            button.setStyleSheet(button_style)

    def animate_text(self, text):
        self.full_text = text
        self.current_text_index = 0
        self.is_animating = True
        self.text_display.setText("")
        self.animation_timer = QTimer()
        self.animation_timer.timeout.connect(self.update_text_animation)
        self.animation_timer.start(self.text_animation_speed)

    def update_text_animation(self):
        if self.current_text_index < len(self.full_text):
            self.text_display.setText(self.full_text[:self.current_text_index + 1])
            self.current_text_index += 1
        else:
            self.animation_timer.stop()
            self.is_animating = False

    def skip_animation(self):
        if self.is_animating:
            self.animation_timer.stop()
            self.text_display.setText(self.full_text)
            self.is_animating = False

    def check_boss_readiness(self, boss_name: str) -> bool:
        """Check if player is ready for a boss fight"""
        min_levels = {
            "Engkanto Twins": 1,    # Starting boss
            "Guardian of the Abyss": 3,
            "Corrupted Dilim": 5
        }
        return self.player.stats.level >= min_levels.get(boss_name, 1)

    def proceed_to_node(self, next_node: str):
        """Handle proceeding to the next story node"""
        next_node_data = self.story_content[next_node]
        
        # Check if entering boss battle
        if hasattr(next_node_data, 'boss') and next_node_data.boss:
            # Only start combat if boss hasn't been defeated
            if next_node_data.boss not in self.player.defeated_bosses:
                self.current_node = next_node
                # Reset any existing combat
                self.combat = CombatManager(self.player)  # Create fresh combat manager
                combat_text = self.combat.start_combat(next_node_data.boss)
                self.update_combat_ui(combat_text)
                self.left_button.setText("Attack")
                self.right_button.setText("Defend")
                self.boss_return_button.hide()
                self.audio.play_bgm("boss_battle")
                return
        
        # If not a boss or boss already defeated, proceed normally
        if self.current_node not in self.training_nodes:
            self.story_history.append(self.current_node)
        self.current_node = next_node
        self.show_current_scene()

    def make_choice(self, choice_idx):
        """Handle player choice"""
        if self.is_animating:
            self.skip_animation()
            return
            
        self.audio.play_sfx("button_click")
        current_node = self.story_content[self.current_node]
        
        # Check if we're in combat
        if self.combat.current_enemy:  # Changed condition to check if combat is active
            # Combat handling code
            if choice_idx == 0:  # Attack
                combat_text = self.combat.player_attack()
                if self.combat.current_enemy and self.combat.current_enemy.hp > 0:
                    # Enemy still alive, counter-attack
                    combat_text += "\n" + self.combat.enemy_attack()
                self.update_combat_ui(combat_text)
                return  # Stay in combat
            else:  # Defend
                # Defend action reduces damage
                self.player.stats.defense += 5  # Temporary defense boost
                combat_text = self.combat.enemy_attack()
                self.player.stats.defense -= 5  # Remove temporary defense
                self.update_combat_ui(combat_text)
                return  # Stay in combat
            
        # Normal story progression
        if choice_idx < len(current_node.choices):
            next_node = current_node.choices[choice_idx][1]
            self.proceed_to_node(next_node)

    def go_back(self):
        if self.story_history:
            self.current_node = self.story_history.pop()
            self.show_current_scene()

    def handle_victory(self):
        """Handle victory scenario with appropriate music"""
        self.audio.play_bgm("victory")
        # Record the defeated boss
        if self.combat.current_enemy:
            self.player.defeated_bosses.add(self.combat.current_enemy.name)
        # After 2:37, switch back to appropriate background music
        QTimer.singleShot(157000, lambda: self.return_to_ambient_music())

    def return_to_ambient_music(self):
        """Return to appropriate background music after victory"""
        node = self.story_content[self.current_node]
        if node.dimension == "Bayan ng Diwata":
            self.audio.play_bgm("diwata_forest")
        else:
            self.audio.play_bgm("forest")

    def update_stats_display(self):
        """Update the display of player stats"""
        self.hp_label.setText(f"HP: {self.player.stats.hp}/{self.player.stats.max_hp}")
        self.level_label.setText(f"Level: {self.player.stats.level}")
        self.exp_label.setText(f"EXP: {self.player.stats.exp}/{self.player.stats.exp_to_next}")

    def update_combat_ui(self, combat_text: str):
        """Update UI during combat"""
        self.text_display.setText(combat_text)
        self.update_stats_display()
        
        # Update boss HP if in combat
        if self.combat.current_enemy:
            self.update_boss_hp_display()
            
        # Check for victory or death
        if self.combat.current_enemy and self.combat.current_enemy.hp <= 0:
            victory_text = self.handle_victory()
            self.text_display.setText(victory_text)
            self.hide_boss_hp()
            self.proceed_after_combat()
        elif self.player.stats.hp <= 0:
            self.handle_player_death()

    def update_boss_hp_display(self):
        """Update the boss HP bar"""
        enemy = self.combat.current_enemy
        if enemy:
            # Show boss UI
            self.boss_name_label.show()
            self.boss_hp_bar.show()
            self.boss_hp_label.show()
            
            # Update values
            self.boss_name_label.setText(enemy.name)
            hp_percent = (enemy.hp / enemy.max_hp) * 100
            self.boss_hp_bar.setValue(int(hp_percent))
            self.boss_hp_label.setText(f"{enemy.hp}/{enemy.max_hp}")

    def hide_boss_hp(self):
        """Hide the boss HP bar when not in combat"""
        self.boss_name_label.hide()
        self.boss_hp_bar.hide()
        self.boss_hp_label.hide()

    def proceed_after_combat(self):
        """Proceed to next story node after combat"""
        if self.combat.current_enemy and self.combat.current_enemy.hp <= 0:
            # Only proceed if boss is actually defeated
            self.current_node = self.story_content[self.current_node].choices[0][1]
            self.show_current_scene()
            # Return to appropriate background music
            self.return_to_ambient_music()

    def handle_player_death(self):
        """Handle what happens when player dies"""
        self.text_display.setText("Game Over! You have been defeated...")
        self.left_button.setEnabled(False)
        self.right_button.setEnabled(False)
        
        # Add a restart button or other game over options
        self.back_button.setText("Restart")
        self.back_button.clicked.disconnect()
        self.back_button.clicked.connect(self.restart_game)

    def restart_game(self):
        """Reset the game to starting state"""
        self.player = Player()
        self.combat = CombatManager(self.player)
        self.current_node = "start"
        self.story_history = []
        self.update_stats_display()
        self.show_current_scene()
        
        # Reset back button
        self.back_button.setText("Back")
        self.back_button.clicked.disconnect()
        self.back_button.clicked.connect(self.go_back)

    def use_potion(self, potion_type: str):
        """Handle potion usage during combat"""
        success, message = self.player.use_potion(potion_type)
        if success:
            self.text_display.setText(message)
            self.update_stats_display()
            # Enemy still gets their turn after potion use
            enemy_message = self.combat.enemy_attack()
            self.text_display.setText(f"{message}\n{enemy_message}")
            self.update_stats_display()

    def get_background(self, path: str) -> str:
        """Get appropriate background image based on context"""
        if path == "main":
            return random.choice(["start.jpg", "intro_background.jpg"])
            
        elif path == "forest":
            return random.choice([
                "diwata_forest.jpg",
                "forest_structures.jpg",
                "sacred_grove.jpg",
                "unstable_forest.jpg"
            ])
            
        elif path == "lake":
            return "lawa_background.jpg"
            
        elif path == "tech":
            return random.choice([
                "magical_terminal.jpg",
                "terminal_active.jpg",
                "digital_awakening.jpg"
            ])
            
        elif path == "village":
            return "diwata_village.jpg"
            
        elif path == "twin":
            return "engkanto_twins.jpg"
            
        elif path == "guardian":
            return "dimensional_patterns.jpg"
            
        elif path == "dilim":
            return "chaos_energy.jpg"
            
        elif path == "ritual":
            return "ritual_clearing.jpg"
            
        elif path == "final":
            return random.choice([
                "bulkan_background.jpg",
                "patay_background.jpg"
            ])
            
        # Default fallback
        return "ancestral_memories.png"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle("Fusion")
    
    # Create dark palette
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
    dark_palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)
    
    app.setPalette(dark_palette)
    
    window = StoryGame()
    window.show()
    sys.exit(app.exec()) 