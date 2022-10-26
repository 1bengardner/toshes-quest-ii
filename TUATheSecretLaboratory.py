"""
File: TUATheSecretLaboratory.py
Author: Ben Gardner
Created: September 8, 2013
Revised: October 26, 2022
"""


from random import choice


class TheSecretLaboratory:

    name = "The Secret Laboratory"
    audio = "Groovy Detective"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        entr = self.entrance
        rDor = self.redDoor # These colours do not make sense because I
                            # incorrectly planned the number of rooms
        bDor = self.blueDoor
        gDor = self.greenDoor
        yDor = self.yellowDoor
        oDor = self.orangeDoor
        swt1 = self.switch1
        swt2 = self.switch2
        swt3 = self.switch3
        swt4 = self.switch4
        swt5 = self.switch5
        swt6 = self.switch6
        swt7 = self.switch7
        swt8 = self.switch8
        dead = self.deadEnd
        boss = self.boss
        levr = self.leverRoom

        self.spots = [
            [None, None, None, None, None],
            [None, None, dead, None, None],
            [None, None, None, None, None],
            [None, swt5, oDor, swt2, None],
            [None, None, None, None, None],
            [None, swt7, yDor, swt8, None],
            [None, None, None, None, None],
            [None, swt5, gDor, swt6, None],
            [None, None, None, None, None],
            [None, swt3, bDor, swt4, None],
            [None, None, None, None, None],
            [None, swt1, rDor, swt2, None],
            [None, None, entr, None, None],
            [None, None, None, None, None],
            [None, boss, None, levr, None],
            [None, None, None, None, None]]
             
        self.encounters = {}

        self.madScientistPhrases = [
            "Don't touch that!",
            "What do you think you're doing?",
            "You'll pay for that...in blood!",
            "Prepare to be fried!",
            "You're a troublemaker!",
            "Keep your hands to yourself!",
            "Get out of here!",
            "That's not a toy!",
            "You're dealing with the wrong scientist!",
            "I hope you like electrocution!"]
    
    def movementActions(self):
        pass

    def actions(self, newActions=None):
        actions = {'view': self.view,
                   'image index': self.imageIndex,
                   'text': self.text,
                   'menu': self.menu,
                   'italic text': self.helpText}
        if newActions:
            actions.update(newActions)
        return actions

    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 4
            Y = 5
            return self.actions({'area': "Western Kosovo",
                                 'coordinates': (X, Y)})
            
        if "Secret Lab Entrance" not in self.c.flags:
            self.text = ("You enter the stone tower and step onto a long, "+
                         "dark corridor.")
            self.c.flags['Secret Lab Entrance'] = True
        self.menu = ["Leave."]
        return self.actions()

    def redDoor(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.c.flags['Room Hop'] = True
            X = 2
            Y = 9
            return self.actions({'area': "The Secret Laboratory",
                                 'coordinates': (X, Y)})
        
        if "Red Door Open" in self.c.flags:
            self.imageIndex = 2
            self.menu = ["Hop into the next room."]

        if "Room Hop" in self.c.flags:
            self.text = ("You hop into a different room.")
            del self.c.flags['Room Hop']
            
        if "Secret Lab Door Room" not in self.c.flags:
            self.text = ("As you proceed down the hall, you walk into a "+
                         "room with control panels and bright lights. There "+
                         "are activation cores on each side."+
                         "\nToshe: This looks like fun.")
            self.c.flags['Secret Lab Door Room'] = True
            
        return self.actions()

    def blueDoor(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0 and "Blue Door Open" in self.c.flags:
            self.c.flags['Room Hop'] = True
            X = 2
            Y = 7
            return self.actions({'area': "The Secret Laboratory",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 0 or selectionIndex == 1:
            self.c.flags['Room Hop'] = True
            X = 2
            Y = 11
            return self.actions({'area': "The Secret Laboratory",
                                 'coordinates': (X, Y)})
        
        if "Blue Door Open" in self.c.flags:
            self.imageIndex = 4
            self.menu += ["Hop into the next room."]

        if "Red Door Open" in self.c.flags:
            self.menu += ["Hop into the previous room."]

        if "Room Hop" in self.c.flags:
            self.text = ("You hop into a different room.")
            del self.c.flags['Room Hop']
            
        return self.actions()

    def greenDoor(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0 and "Green Door Open" in self.c.flags:
            self.c.flags['Room Hop'] = True
            X = 2
            Y = 5
            return self.actions({'area': "The Secret Laboratory",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 0 or selectionIndex == 1:
            self.c.flags['Room Hop'] = True
            X = 2
            Y = 9
            return self.actions({'area': "The Secret Laboratory",
                                 'coordinates': (X, Y)})
        
        if "Green Door Open" in self.c.flags:
            self.imageIndex = 6
            self.menu += ["Hop into the next room."]

        if "Blue Door Open" in self.c.flags:
            self.menu += ["Hop into the previous room."]

        if "Room Hop" in self.c.flags:
            self.text = ("You hop into a different room.")
            del self.c.flags['Room Hop']
            
        return self.actions()

    def yellowDoor(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0 and "Yellow Door Open" in self.c.flags:
            self.c.flags['Room Hop'] = True
            X = 2
            Y = 3
            return self.actions({'area': "The Secret Laboratory",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 0 or selectionIndex == 1:
            self.c.flags['Room Hop'] = True
            X = 2
            Y = 7
            return self.actions({'area': "The Secret Laboratory",
                                 'coordinates': (X, Y)})
        
        if "Yellow Door Open" in self.c.flags:
            self.imageIndex = 8
            self.menu += ["Hop into the next room."]

        if "Green Door Open" in self.c.flags:
            self.menu += ["Hop into the previous room."]

        if "Room Hop" in self.c.flags:
            self.text = ("You hop into a different room.")
            del self.c.flags['Room Hop']
            
        return self.actions()

    def orangeDoor(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0 and (("Red Door Open" in self.c.flags
                                     and "Green Door Open" not in self.c.flags)
                                    or ("Red Door Open" not in self.c.flags
                                        and "Green Door Open" in self.c.flags)):
            X = 2
            Y = 1
            return self.actions({'area': "The Secret Laboratory",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 0 or selectionIndex == 1:
            self.c.flags['Room Hop'] = True
            X = 2
            Y = 5
            return self.actions({'area': "The Secret Laboratory",
                                 'coordinates': (X, Y)})
        
        if ("Red Door Open" in self.c.flags
            and "Green Door Open" not in self.c.flags) or (
            "Red Door Open" not in self.c.flags
            and "Green Door Open" in self.c.flags):
            self.imageIndex = 10
            self.menu += ["Hop into the next room."]

        if "Yellow Door Open" in self.c.flags:
            self.menu += ["Hop into the previous room."]

        if "Room Hop" in self.c.flags:
            self.text = ("You hop into a different room.")
            del self.c.flags['Room Hop']
            
        return self.actions()

    def switch1(self, selectionIndex=None):
        return self.switchTemplate(selectionIndex, "Red", "left")

    def switch2(self, selectionIndex=None):
        return self.switchTemplate(selectionIndex, "Blue", "right")

    def switch3(self, selectionIndex=None):
        return self.switchTemplate(selectionIndex, "Green", "left")

    def switch4(self, selectionIndex=None):
        return self.switchTemplate(selectionIndex, "Yellow", "right")

    def switch5(self, selectionIndex=None):
        return self.switchTemplate(selectionIndex, "Yellow", "left")

    def switch6(self, selectionIndex=None):
        return self.switchTemplate(selectionIndex, "Red", "right")

    def switch7(self, selectionIndex=None):
        return self.switchTemplate(selectionIndex, "Blue", "left")

    def switch8(self, selectionIndex=None):
        return self.switchTemplate(selectionIndex, "Green", "right")

    def switchTemplate(self, selectionIndex, color, side):
        self.view = "travel"
        self.imageIndex = 13
        if side == "right":
            self.imageIndex = 14
        self.text = None
        self.helpText = None
        self.menu = []
        clicks = "one click"
        if color in ("Red", "Green"):
            clicks = "two clicks"
        if selectionIndex == 0:
            if ("%s Door Open" % color) not in self.c.flags:
                self.c.flags[('%s Door Open' % color)] = True
                self.text = ("You activate the %s core. You hear %s."
                             % (color.lower(), clicks))
            else:
                del self.c.flags[('%s Door Open' % color)]
                self.text = ("You deactivate the %s core. You hear %s."
                             % (color.lower(), clicks))
            self.view = "battle"
            self.text += ("\nMad Scientist: "+choice(self.madScientistPhrases))
            return self.actions({'enemy': "Mad Scientist",
                                 'mercenaries': self.c.mercenaries})
        if "Secret Switch" not in self.c.flags:
            self.text = ("You see some controls with a large activation panel.")
            self.c.flags['Secret Switch'] = True
        if ("%s Door Open" % color) not in self.c.flags:
            self.menu = [("Activate the %s core." % color.lower())]
        else:
            self.menu = [("Deactivate the %s core." % color.lower())]
        return self.actions()

    def deadEnd(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 15
        self.text = None
        self.helpText = None
        self.menu = []
        if ('Secret Lab Boss' not in self.c.flags and
            'Secret Lab Lever' not in self.c.flags):
            if selectionIndex == 0:
                X = 1
                Y = 14
                return self.actions({'area': "The Secret Laboratory",
                                     'coordinates': (X, Y)})
            if selectionIndex == 1:
                X = 3
                Y = 14
                return self.actions({'area': "The Secret Laboratory",
                                     'coordinates': (X, Y)})
            if selectionIndex == 2:
                self.c.flags['Room Hop'] = True
                X = 2
                Y = 3
                return self.actions({'area': "The Secret Laboratory",
                                     'coordinates': (X, Y)})
                
            self.text = ("You enter the final room and see two switches: a "+
                         "keyboard with a power button and a large lever at "+
                         "the back of the room. Between these is a tube "+
                         "containing a massive creature you've never "+
                         "seen before."+
                         "\nToshe: This must be where Tomas generates all the "+
                         "monsters. One of these has got to be a killswitch.")
            self.menu = ["Press the button (game will be saved).",
                         "Pull the lever (game will be saved).",
                         "Hop into the previous room."]
        else:
            X = 3
            Y = 14
            return self.actions({'area': "The Secret Laboratory",
                                 'coordinates': (X, Y)})
        return self.actions()

    def boss(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 15
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.view = "battle"
            self.text = "Nameless Beast: Mmmuuuunnnlgh."
            self.c.flags['Secret Lab Boss'] = True
            return self.actions({'enemy': "Nameless Beast",
                                 'mercenaries': self.c.mercenaries})
        elif 'Secret Lab Boss' not in self.c.flags:
            self.c.flags['New Song'] = "Drat"
            self.text = ("You approach the keyboard and quickly press the "+
                         "power button."+
                         "\nThe floor shakes as the glass from the tube is "+
                         "slowly lowered to the ground. You feel the urge to "+
                         "run but your feet are stuck in pure fear."+
                         "\nToshe: Wh-what the fuck is happening?!"+
                         "\nVesicles pop on the skin of the unknown creature "+
                         "and eventually settle. Its eyes open and you "+
                         "realize the beast is alive."+
                         "\nToshe: Holy shit...")
            self.menu = ["Brace yourself."]
            return self.actions({'save': True})
        else:
            X = 2
            Y = 1
            return self.actions({'area': "The Secret Laboratory",
                                 'coordinates': (X, Y)})

    def leverRoom(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 16
        self.text = None
        self.helpText = None
        self.menu = ["Hop into the previous room."]
        if selectionIndex == 0:
            self.c.flags['Room Hop'] = True
            X = 2
            Y = 3
            return self.actions({'area': "The Secret Laboratory",
                                 'coordinates': (X, Y)})
            
        elif ("Secret Lab Boss" in self.c.flags and
              "Secret Lab Lever" not in self.c.flags and not selectionIndex):
            self.text = ("Toshe: Wow. How did I survive?")
            self.menu += ["Pull the lever (game will save)."]
            
        elif "Secret Lab Lever" not in self.c.flags:
            self.text = ("You slowly pull down the lever until you hear a "+
                         "click."+
                         "\nToshe: That must've done it."+
                         "\n70-M45: System deactivated."+
                         "\nToshe: Yes!"+
                         "\n70-M45: Using emergency power supply: Stone "+
                         "of Macedonia."+
                         "\nToshe: No! What the fuck? How? This place uses the "+
                         "power of the Stone of Macedonia?..."+
                         "\n...I've gotta get the Key to Macedonia from the "+
                         "president. He must be somewhere nearby. I can't "+
                         "be too far from Macedonia now. Shit. I need to "+
                         "hurry.")
            self.c.flags['Secret Lab Lever'] = True
            return self.actions({'save': True})
        
        else:
            self.text = ("You see a pulled down lever.")
            
        return self.actions()
