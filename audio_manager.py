from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl
import os

class AudioManager:
    def __init__(self):
        # Create players for different audio types
        self.bgm_player = QMediaPlayer()
        self.sfx_player = QMediaPlayer()
        
        # Create audio outputs
        self.bgm_output = QAudioOutput()
        self.sfx_output = QAudioOutput()
        
        # Set audio outputs for players
        self.bgm_player.setAudioOutput(self.bgm_output)
        self.sfx_player.setAudioOutput(self.sfx_output)
        
        # Set default volumes
        self.bgm_output.setVolume(0.5)  # 50% volume for background music
        self.sfx_output.setVolume(0.7)  # 70% volume for sound effects
        
        # Track current BGM
        self.current_bgm = None
        
        # Audio file paths
        self.bgm_folder = "audio/bgm"
        self.sfx_folder = "audio/sfx"
        
        # Define available audio
        self.bgm = {
            "main_menu": "main_theme.mp3",
            "forest": "forest_ambient.mp3",
            "battle": "battle_regular.mp3",
            "boss_battle": "boss_theme.mp3",
            "diwata_forest": "magical_forest.mp3",
            "victory": "victory.mp3"
        }
        
        self.sfx = {
            "button_click": "button_click.wav",
            "magic_cast": "spell_cast.wav",
            "text_blip": "text_sound.wav",
            "item_get": "item_acquire.wav"
        }

        # BGM mapping for dimensions and battles
        self.bgm_tracks = {
            "start": "title_theme.mp3",
            "Bayan ng Diwata": "diwata_forest.mp3",
            "Lawa ng Walang Hanggan": "lake_theme.mp3",
            "The Convergence": "final_area.mp3",
            "boss_battle": "boss_battle.mp3",
            "victory": "victory.mp3"
        }

    def play_bgm(self, track_name):
        """Play background music with automatic looping"""
        if track_name in self.bgm:
            file_path = os.path.join(self.bgm_folder, self.bgm[track_name])
            if os.path.exists(file_path):
                url = QUrl.fromLocalFile(file_path)
                if self.current_bgm != track_name:
                    self.bgm_player.setSource(url)
                    self.bgm_player.play()
                    self.current_bgm = track_name
                    
                    # Only set up looping for non-victory music
                    if track_name != "victory":
                        self.bgm_player.mediaStatusChanged.connect(self._loop_bgm)

    def play_sfx(self, sound_name):
        """Play a sound effect once"""
        if sound_name in self.sfx:
            file_path = os.path.join(self.sfx_folder, self.sfx[sound_name])
            if os.path.exists(file_path):
                url = QUrl.fromLocalFile(file_path)
                self.sfx_player.setSource(url)
                self.sfx_player.play()

    def _loop_bgm(self, status):
        """Internal method to handle BGM looping"""
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.bgm_player.setPosition(0)
            self.bgm_player.play()

    def stop_bgm(self):
        """Stop the current background music"""
        self.bgm_player.stop()
        self.current_bgm = None

    def pause_bgm(self):
        """Pause the current background music"""
        self.bgm_player.pause()

    def resume_bgm(self):
        """Resume the current background music"""
        self.bgm_player.play()

    def set_bgm_volume(self, volume):
        """Set BGM volume (0.0 to 1.0)"""
        self.bgm_output.setVolume(volume)

    def set_sfx_volume(self, volume):
        """Set SFX volume (0.0 to 1.0)"""
        self.sfx_output.setVolume(volume) 