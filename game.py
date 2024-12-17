from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, 
                            QVBoxLayout, QHBoxLayout, QLabel, QFrame)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap, QPalette, QColor
import sys
import os
from story_content import story_content, StoryNode
from audio_manager import AudioManager
from player import Player
from combat_manager import CombatManager

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
        
        # Image handling
        self.image_folder = "images"
        self.default_image = "default_background.jpg"
        
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
        
        # Combine layouts
        main_layout.addLayout(stack_layout)
        main_layout.addLayout(button_layout)
        main_layout.addLayout(control_layout)
        main_layout.addWidget(self.stats_frame)
        
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
        node = self.story_content[self.current_node]
        
        # Enhanced music selection based on scene context
        if hasattr(node, 'boss') and node.boss:
            self.audio.play_bgm("boss_battle")
        elif "battle" in node.text.lower() or "combat" in node.text.lower():
            self.audio.play_bgm("battle")
        elif "victory" in node.text.lower() or "success" in node.text.lower():
            self.audio.play_bgm("victory")
        elif node.dimension == "Bayan ng Diwata":
            self.audio.play_bgm("diwata_forest")
        elif self.current_node == "start":
            self.audio.play_bgm("main_menu")
        else:
            self.audio.play_bgm("forest")
        
        # Update background
        pixmap = self.load_image(node.background)
        self.background_label.setPixmap(pixmap)
        
        # Update choices
        if node.choices:
            self.left_button.setText(node.choices[0][0])
            self.right_button.setText(node.choices[1][0])
            self.left_button.setEnabled(True)
            self.right_button.setEnabled(True)
        else:
            self.left_button.setEnabled(False)
            self.right_button.setEnabled(False)
        
        # Start text animation
        self.animate_text(node.text)

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

    def make_choice(self, choice_index):
        if self.is_animating:
            self.skip_animation()
            return
            
        self.audio.play_sfx("button_click")
        current_node = self.story_content[self.current_node]
        
        if current_node.choices:
            self.story_history.append(self.current_node)
            next_node = current_node.choices[choice_index][1]
            
            # Check if entering combat
            if hasattr(current_node, 'boss') and current_node.boss:
                combat_text = self.combat.start_combat(current_node.boss)
                self.update_combat_ui(combat_text)
                self.audio.play_bgm("boss_battle")
            else:
                self.current_node = next_node
                self.show_current_scene()

    def go_back(self):
        if self.story_history:
            self.current_node = self.story_history.pop()
            self.show_current_scene()

    def handle_victory(self):
        """Handle victory scenario with appropriate music"""
        self.audio.play_bgm("victory")
        # After 2:37, switch back to appropriate background music
        QTimer.singleShot(157000, lambda: self.return_to_ambient_music())  # 157000ms = 2:37
        
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
        """Update UI after combat actions"""
        self.text_display.setText(combat_text)
        self.update_stats_display()
        
        # Check if player died
        if self.player.stats.hp <= 0:
            self.handle_player_death()

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