"""
File: TUASound.py
Author: Ben Gardner
Created: September 6, 2013
Revised: August 21, 2022
"""


from pygame import mixer


class Sound:
    """Plays music."""
    
    def __init__(self):
        self.path = "audio\\%s.ogg"
        self.songs = {"Intro Theme": "Daring Feat",
                      "Game Over Theme": "Overcast",
                      "Wizard Theme": "Buddha",
                      "Mob Battle": "Mosquitoes",
                      "Important Battle": "Dungeon Escape",
                      "Canonical Battle": "Fearless Fighter",
                      "Rival Battle": "Tango Town",
                      "Tomas Battle": "Escape Route",
                      "Guardian Battle": "Space Traveller",
                      "Final Battle": "Grandpa's Gardens",
                      "Riplin Battle": "Grandpa's Grandpa",
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
                       "Move": "FX-Step",
                       "Select": "FX-Select",
                       "Inventory": "FX-Switch",
                       "Return": "FX-Toss",
                       "Equip": "FX-Equip",
                       "Increase Stat": "FX-Upgrade",
                       "Save": "FX-Activate",
                       "Load": "FX-Switch",
                      }
        
        mixer.init(frequency=44100, size=-8, channels=2, buffer=2048)
        self.currentSong = None
        self.previousSong = None    # For returning to the previous song after an event
        self.sfxMuted = False
        mixer.music.set_volume(1)

    def isNewSong(self, songName):
        """Check if the given song is different from the current one."""
        if songName != self.currentSong:
            return True

    def fadeoutMusic(self, fadeoutTime):
        """Fade out the current song."""
        mixer.music.fadeout(fadeoutTime)

    def playMusic(self, songName=None):
        """Play the specified song. If none specified, play the current song."""
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
            
    def playSound(self, soundName):
        if not self.sfxMuted:
            mixer.Sound(self.path % soundName).play()
            
    def muteSfx(self):
        self.sfxMuted = not self.sfxMuted
        if not self.sfxMuted:
            self.playSound("FX-Hit")
        
    def muteMusic(self):
        mixer.music.set_volume((mixer.music.get_volume() + 1) % 2)
