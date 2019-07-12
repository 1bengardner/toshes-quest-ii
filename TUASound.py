"""
File: TUASound.py
Author: Ben Gardner
Created: September 6, 2013
Revised: December 30, 2015
"""


from pygame import mixer


class Sound:
    """Plays music."""
    
    def __init__(self):
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
        
        mixer.init(frequency=44100, size=-8, channels=2, buffer=2048)
        self.currentSong = None
        self.previousSong = None    # For returning to the previous song after an event

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
        mixer.music.load("audio\\%s.ogg" % self.currentSong)
        mixer.music.play(-1, 0.05)

    def stopMusic(self):
        """Stop music playback."""
        mixer.music.stop()

    def queueMusic(self, songName=None):
        """Queue a song to play."""
        if songName:
            self.currentSong = songName
        mixer.music.queue("audio\\%s.ogg" % self.currentSong)

    def isPlaying(self):
        """Determine whether music is playing."""
        return mixer.music.get_busy()

    def isInstantPlay(self, songName=None):
        """Determine whether music should start immediately."""
        if not self.isPlaying():
            return True
