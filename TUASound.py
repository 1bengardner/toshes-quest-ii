"""
File: TUASound.py
Author: Ben Gardner
Created: September 6, 2013
Revised: November 8, 2022
"""


import pickle
from pygame import mixer

from TUAPreferences import Preferences


class Sound:
    """Plays music."""
    
    MUSIC_VOLUME = 0.7
    
    def __init__(self):
        self.path = "audio\\%s.ogg"
        self.songs = {"Intro Theme": "Daring Feat",
                      "Game Over Theme": "Overcast",
                      "Mob Battle": "Mosquitoes",
                      "Important Battle": "Dungeon Escape",
                      "Canonical Battle": "Fearless Fighter",
                      "Rival Battle": "Tango Town",
                      "Tomas Battle": "Escape Route",
                      "Guardian Battle": "Space Traveller",
                      "Final Battle": "Grandpa's Gardens",
                      "Niplin Battle": "Niplin",
                      "Crayon Battle": "RUF"
                     }
        self.sounds = {"Level Up": "FX-Dream",
                       "Get Item": "FX-Collect",
                       "Mercenary Up": "FX-Discover",
                       "New Skill": "FX-Discover",
                       "Deal Damage": "FX-Hit",
                       "Take Damage": "FX-Struck",
                       "Heal": "FX-Rise",
                       "Critical Strike": "FX-Critical",
                       "Critical Injury": "FX-Injured",
                       "Block": "FX-Brush",
                       "Flee": "FX-Flee",
                       "Kill": "FX-Activate",
                       "Dead": "FX-Dead",
                       "Drink": "FX-Bubble",
                       "Move": "FX-Step",
                       "Select Option": "FX-Select",
                       "Inventory": "FX-Switch",
                       "Return": "FX-Toss",
                       "Select Item": "FX-Touch",
                       "Equip": "FX-Equip",
                       "Buy": "FX-Collect",
                       "Sell": "FX-Sell",
                       "Increase Stat": "FX-Upgrade",
                       "Save": "FX-Activate",
                       "Load": "FX-Switch",
                       "Low HP": "FX-Alert",
                       "Mark Map": "FX-Touch",
                       "Warp": "FX-Thud",
                       "Open Dialog": "FX-Touch",
                       "Menu": "FX-Cluck"
                      }
        
        mixer.init(frequency=44100, size=-8, channels=2, buffer=2048)
        self.currentSong = None
        self.previousSong = None    # For returning to the previous song after an event
        self.sfxMuted = False
        mixer.music.set_volume(Sound.MUSIC_VOLUME)

    def isNewSong(self, songName):
        """Check if the given song is different from the current one."""
        if songName != self.currentSong:
            return True

    def fadeoutMusic(self, fadeoutTime):
        """Fade out the current song."""
        mixer.music.fadeout(fadeoutTime)

    def playMusic(self, songName):
        """Play the specified song."""
        mixer.music.stop()
        if songName:
            self.currentSong = songName
            mixer.music.load(self.path % self.currentSong)
            mixer.music.play(-1)

    def stopMusic(self):
        """Stop music playback."""
        mixer.music.stop()

    def queueMusic(self, songName=None):
        """Queue a song to play."""
        if songName:
            self.currentSong = songName
            mixer.music.queue(self.path % self.currentSong)

    def isPlaying(self):
        """Determine whether music is playing."""
        return mixer.music.get_busy()

    def isInstantPlay(self, songName=None):
        """Determine whether music should start immediately."""
        if not self.isPlaying():
            return True
            
    def playSound(self, soundName, count=1):
        if not self.sfxMuted and count > 0:
            mixer.Sound(self.path % soundName).play(loops=count - 1)
            
    def muteSfx(self):
        if self.sfxMuted:
            self.sfxMuted = False
            self.playSound("FX-Activate")
        else:
            self.playSound("FX-Toss")
            self.sfxMuted = True
        self.writePreferences()
        
    def muteMusic(self):
        mixer.music.set_volume(0 if mixer.music.get_volume() > 0 else Sound.MUSIC_VOLUME)
        self.writePreferences()
        
    def writePreferences(self):
        with open("preferences.tqp", "w") as config:
            preferences = Preferences()
            preferences.musicOn = mixer.music.get_volume() > 0
            preferences.sfxOn = not self.sfxMuted
            pickle.dump(preferences, config)
