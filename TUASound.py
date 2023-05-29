"""
File: TUASound.py
Author: Ben Gardner
Created: September 6, 2013
Revised: May 28, 2023
"""


import pickle
from pygame import mixer

from TUAPreferences import Preferences


class Sound:
    """Plays music."""
    
    MUSIC_VOLUME = 0.6
    
    def __init__(self):
        self.path = "audio\\%s.ogg"
        self.songs = {"Intro Theme": "Daring Feat",
                      "Game Over Theme": "Overcast",
                      "Mob Battle": "Mosquitoes",
                      "Coliseum Battle": "Nemea",
                      "Important Battle": "Dungeon Escape",
                      "Canonical Battle": "Fearless Fighter",
                      "Rival Battle": "Tango Town",
                      "Tomas Battle": "Escape Route",
                      "Guardian Battle": "Space Traveller",
                      "Final Battle": "Grandpa's Gardens",
                      "Niplin Battle": "Niplin",
                      "Riplin Battle": "Grandpa's Gardens",
                      "Crayon Battle": "Boiling Over",
                      "Wisp Battle": "RUF",
                     }
        self.sounds = {"Level Up": "FX-Dream",
                       "Mercenary Up": "FX-Frolic",
                       "Get Item": "FX-Collect",
                       "New Skill": "FX-Discover",
                       "Power Up": "FX-Discover",
                       "Forge Upgrade": "FX-Discover",
                       "Deal Damage": "FX-Hit",
                       "Wand Attack": "FX-Cast",
                       "Bow Attack": "FX-Shoot",
                       "Gun Attack": "FX-Bullet",
                       "Take Damage": "FX-Struck",
                       "Heal": "FX-Bless",
                       "Critical Strike": "FX-Critical",
                       "Critical Injury": "FX-Injured",
                       "Defend": "FX-Tap",
                       "No Damage": "FX-Tick",
                       "Miss": "FX-Miss",
                       "Block": "FX-Ping",
                       "Boost": "FX-Brush",
                       "Flee": "FX-Flee",
                       "Kill": "FX-Activate",
                       "Dead": "FX-Dead",
                       "Drink": "FX-Bubble",
                       "Move": "FX-Step",
                       "Select Option": "FX-Select",
                       "Inventory": "FX-Switch",
                       "Return": "FX-Toss",
                       "Cancel": "FX-Toss",
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
                       "Open Dialog": "FX-Question",
                       "Menu": "FX-Cluck",
                       "New Quest": "FX-Scribble",
                       "Quest Complete": "FX-Gracious",
                       "Quest Ready": "FX-Surprise",
                       "Open Log": "FX-Touch",
                       "Sleep": "FX-Bless",
                       "Jackpot": "FX-Sell",
                       "Grounded": "FX-Ground",
                       "Frozen": "FX-Freeze",
                       "Poisoned": "FX-Poison",
                       "Paralyzed": "FX-Paralyze",
                       "Burning": "FX-Burn",
                       "Petrified": "FX-Petrify",
                       "Drowned": "FX-Drown",
                       "Break Free": "FX-Rise",
                       "Remove Armour": "FX-Toss",
                       "Place on Anvil": "FX-Thud",
                       "Strike Anvil": [
                           ("FX-Smith-%s" % i) for i in range(11)
                       ],
                       "Crucible": "FX-Select",
                       "Hammer": "FX-Cast",
                       "Failed Upgrade": "FX-Ground",
                      }
        
        mixer.init(frequency=44100, size=-16, channels=2, buffer=2048)
        self.currentSong = None
        self.previousSong = None    # For returning to the previous song after an event
        self.sfxMuted = False
        mixer.music.set_volume(Sound.MUSIC_VOLUME)
        mixer.set_reserved(1)   # Reserve channel 0

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
            
    def playSound(self, soundName, count=1, pan=None, interruptible=False):
        if not self.sfxMuted and count > 0:
            sound = mixer.Sound(self.path % soundName)
            if pan is None and not interruptible:
                sound.play(loops=count - 1)
            else:
                if interruptible:
                    channel = mixer.Channel(0)
                else:
                    channel = mixer.find_channel(True)
                if pan:
                    channel.set_volume(*pan)
                channel.play(sound, loops=count - 1)
            
    def muteSfx(self):
        if self.sfxMuted:
            self.sfxMuted = False
            self.playSound("FX-Touch")
        else:
            self.sfxMuted = True
        self.writePreferences()
        
    def muteMusic(self):
        mixer.music.set_volume(0 if mixer.music.get_volume() > 0 else Sound.MUSIC_VOLUME)
        self.writePreferences()
        
    def writePreferences(self):
        try:
            with open("prefs\\preferences.tqp", "r") as existingPreferences:
                preferences = pickle.load(existingPreferences)
        except IOError:
            preferences = Preferences()
        preferences.musicOn = mixer.music.get_volume() > 0
        preferences.sfxOn = not self.sfxMuted
        with open("prefs\\preferences.tqp", "w") as preferencesFile:
            pickle.dump(preferences, preferencesFile)
