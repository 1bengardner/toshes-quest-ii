"""
File: TUAFartooqHold.py
Author: Ben Gardner
Created: May 1, 2017
Revised: November 14, 2022
"""


from TUAStatics import Static


class FartooqHold:
    
    name = "Fartooq Hold"
    audio = "On Thinner Ice"

    def __init__(self, character):
        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"

        wrp1 = self.galijula
        cav1 = self.cave1
        cav2 = self.cave2
        cav3 = self.cave3
        cav4 = self.cave4
        cav5 = self.cave5
        nooE = self.nookEntrance
        cav6 = self.cave6
        cav7 = self.cave7
        fork = self.fork
        pth1 = self.path1
        pth2 = self.path2
        pth3 = self.path3
        pth4 = self.path4
        orbb = self.orb
        ltRt = self.leftRight
        bend = self.bend
        pol1 = self.pool1
        watr = self.water
        pol2 = self.pool2
        tunl = self.tunnel
        pilr = self.pillar
        nook = self.nook
        
        
        self.spots = [
            [None, None, None, None, None, None, None, None],
            [None, watr, None, None, orbb, None, pilr, None],
            [None, None, None, None, pth4, None, tunl, None],
            [None, None, None, None, pth3, None, pol2, None],
            [None, None, None, None, pth2, None, None, None],
            [None, None, None, None, pth1, None, pol1, None],
            [None, None, None, None, fork, ltRt, bend, None],
            [None, nook, None, None, cav7, None, None, None],
            [None, None, None, None, cav6, None, None, None],
            [None, nooE, cav5, cav4, cav1, cav2, cav3, None],
            [None, None, None, None, wrp1, None, None, None],
            [None, None, None, None, None, None, None, None]
            ]
        
        e = {'Horn Dog': 10,
             'Horn Beast': 10,
             'Ice Spawn': 5}
             
        self.encounters = {wrp1: {},
                           cav1: {},
                           cav2: e,
                           cav3: e,
                           cav4: e,
                           cav5: e,
                           nooE: e,
                           cav6: e,
                           cav7: e,
                           fork: e,
                           pth1: e,
                           pth2: e,
                           pth3: e,
                           pth4: e,
                           orbb: e,
                           ltRt: e,
                           bend: e,
                           pol1: e,
                           watr: {},
                           pol2: e,
                           tunl: {},
                           pilr: {},
                           nook: {},
                           }
    
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
    
    def hasGainedPowerOf(self, animal):
        return "Animal Powers" in self.c.flags and animal in self.c.flags['Animal Powers']
    
    def galijula(self, selectionIndex=None):
        X = 4
        Y = 2
        return self.actions({'area': "Galijula",
                             'coordinates': (X, Y)})
    
    def cave1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = None
        self.helpText = None
        self.menu = []
        if "Fartooq Hold" not in self.c.flags:
            if self.c.hasMercenary("Qendresa"):
                self.text = ("Qendresa: It is far too cold here.")
                if self.c.hasMercenary("Barrie"):
                    self.text += ("\nBarrie: As an Albanian homebody," +
                                  " I'm surprised you knew that." +
                                  "\nQendresa has a puzzled expression.")
            self.c.flags['Fartooq Hold'] = True
        return self.actions()
    
    def cave2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def cave3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 2
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def cave4(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def cave5(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def nookEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            return Static.ICA_DATA['Ica 6']
        if self.c.dexterity >= 75:
            self.text = ("You come across a gap in the wall that "+
                         "you could crouch into.")
            self.menu = ["Enter the gap."]
        else:
            self.text = ("You come across a gap in the wall that "+
                         "you could maybe crouch into, were you more "+
                         "dextrous.")
        return self.actions()
    
    def cave6(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def cave7(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def fork(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def path1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def path2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def path3(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()
    
    def path4(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def orb(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 13
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            self.imageIndex = 14
            self.text = "You grab the orb and feel its powerful presence."
            return self.actions({'item': "Oracular Orb"})
        
        if (self.c.hasItem("Oracular Orb") or
            "Placed Oracular Orb" in self.c.flags):
            self.imageIndex = 14
        else:
            self.text = "Toshe: Holy shit! What the fuck is that?"
            self.menu = ["Take the magical object."]
        return self.actions()

    def leftRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 15
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def bend(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 16
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def pool1(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 17
        self.text = None
        self.helpText = None
        if selectionIndex == 0:
            X = 1
            Y = 1
            return self.actions({'area': "Fartooq Hold",
                                 'coordinates': (X, Y)})
            
        if "Fartooq Alcove" not in self.c.flags:
            self.text = ("You come across a deep pool of water in an" +
                         " alcove.")
            if self.c.hasMercenary("Qendresa"):
                self.text += ("\nQendresa: There is water? What" +
                              " keeps it from freezing?")
            self.c.flags['Fartooq Alcove'] = True
        self.menu = ["Enter the water."]
        return self.actions()

    def water(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 18
        self.text = None
        self.helpText = None
        self.menu = []
        self.text = "You dive into the pool."
        
        if selectionIndex == 0:
            X = 6
            Y = 3
            return self.actions({'area': "Fartooq Hold",
                                 'coordinates': (X, Y)})
        if selectionIndex == 1:
            X = 6
            Y = 5
            return self.actions({'area': "Fartooq Hold",
                                 'coordinates': (X, Y)})
        
        if ( "Fartooq Ambush" not in self.c.flags and
             not self.c.hasItem("Oracular Orb")):
            self.c.flags['Fartooq Ambush'] = True
            self.view = "battle"
            return self.actions({'enemy': "Ice Guardian",
                                 'mercenaries': self.c.mercenaries})
        elif ("Fartooq Ambush" not in self.c.flags):
            self.text = ""
            if "Ice Guardian Legion" not in self.c.flags:
                self.c.flags['Ice Guardian Legion'] = True
                self.text = "An endless legion of ice guardians approaches."
            self.view = "battle"
            return self.actions({'enemy': "Ice Guardian",
                                 'mercenaries': self.c.mercenaries})            

        if "Fartooq Water" not in self.c.flags:
            self.text = ("The ice guardian vanishes." +
                         "\nToshe: I don't like the looks of this place.")
            self.c.flags['Fartooq Water'] = True
        self.menu = ["Swim forward.",
                     "Swim back."]
        return self.actions()

    def pool2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 19
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 1
            Y = 1
            return self.actions({'area': "Fartooq Hold",
                                 'coordinates': (X, Y)})
        
        if "Fartooq Surface" not in self.c.flags:
            self.text = ("You surface to find yourself facing" +
                         " the entrance to a dark cave.")
            self.c.flags['Fartooq Surface'] = True
        self.menu = ["Enter the water."]
        return self.actions()

    def tunnel(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 20
        self.text = None
        self.helpText = None
        self.menu = []
        if "Farooq Moonlight" not in self.c.flags:
            self.text = ("Moonlight from outside illuminates the tunnel.")
            self.c.flags['Farooq Moonlight'] = True
        elif ("Placed Oracular Orb" in self.c.flags and
              "Aldreed" not in self.c.flags['Kills'] and
              "Hiding from Aldreed" not in self.c.flags):
            self.text = ("Toshe: I'm not fighting that thing!")
            self.c.flags['Hiding from Aldreed'] = True
        return self.actions()

    def pillar(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 21
        self.text = None
        self.helpText = None
        self.menu = []
        if ("Placed Oracular Orb" not in self.c.flags):
            self.text = ("You reach the edge of the mountain. You see a" +
                         " pedestal with a spherical indentation on top.")

        if ("Mountaintop" not in self.c.flags):
            self.text += ("\nToshe: What is this place? It looks all messed up.")
            if self.c.hasMercenary("Qendresa"):
                self.text += ("\nQendresa: Yes, the pillar's shadow appears" +
                              " to be facing the wrong direction or something.")
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: It just looks like some crappy" +
                              " Photoshop job by an unpaid developer who" +
                              " couldn't finish in time.")
                if self.c.hasMercenary("Qendresa"):
                    self.text += ("\nQendresa: Are you referring to only this" +
                                  " scene? They all look like that.")
            self.c.flags['Mountaintop'] = True
        if ( selectionIndex == 0 and
             self.c.hasItem("Oracular Orb")):
            self.c.flags['New Song'] = "Drat"
            self.tempFlag = {'New Song': self.audio}
            self.imageIndex = 22
            self.c.removeItem(self.c.indexOfItem("Oracular Orb"))
            self.c.flags['Placed Oracular Orb'] = True
            self.text = ("You place the orb atop the pillar." +
                         "\nThe mountaintop rumbles. The moon appears to" +
                         " flash for a brief moment." +
                         "\nA terrifying beast swoops down and perches on" +
                         " a peak above." +
                         "\nAldreed: Graaagh!!")
            self.menu = ["Face Aldreed."]
        elif (self.c.hasItem("Oracular Orb")):
            self.menu = ["Place the orb upon the pedestal."]
        elif ("Placed Oracular Orb" in self.c.flags and
              "Aldreed" not in self.c.flags['Kills']):
            self.imageIndex = 22
            self.view = "battle"
            return self.actions({'enemy': "Aldreed",
                                 'mercenaries': self.c.mercenaries})
        elif ("Aldreed" in self.c.flags['Kills'] and
              "Aldreed Aftermath" not in self.c.flags):
            self.text = "The pedestal has disappeared."
            self.text += "\nToshe: Not bad."
            if self.c.hasMercenary("Barrie"):
                self.text += ("\nBarrie: That was fantastic!")
            if self.c.hasMercenary("Qendresa"):
                self.text += ("\nQendresa: Now can we go back down?")
            self.c.flags['Aldreed Aftermath'] = True
        elif selectionIndex == 0:
            self.c.flags['Sliding Down'] = True
            X = 6
            Y = 16
            return self.actions({'area': "Adriatic Sea",
                                 'coordinates': (X, Y)})
        if ("Aldreed Aftermath" in self.c.flags):
            self.imageIndex = 23
            self.menu = ["Slide down the mountainside."]
            
        return self.actions()

    def nook(self, selectionIndex=None):
        thisIca = "Ica 5"
        self.c.flags[thisIca] = True
        self.view = "store"
        self.imageIndex = 24
        self.text = None
        self.helpText = None
        npc = "Ica"
        skill1 = "Death Dart"
        skillPrice1 = 5000
        tunic = "Water Tunic"
        self.menu = ["Leave."]
        ableToLearn = self.hasGainedPowerOf("Giant Seal2") or self.hasGainedPowerOf("Giant Shark2")
        if ableToLearn:
            self.menu = ["Learn %s (%s euros)." % (skill1, skillPrice1)] + self.menu
        if any(ica != thisIca and ica in self.c.flags for ica in Static.ICAS):
            self.menu += ["Travel to the next nook."]
        if selectionIndex == 0 and ableToLearn:
            return self.actions({'skill': skill1,
                                 'cost': skillPrice1,
                                 'items for sale': [tunic]+[None]*8})
        elif selectionIndex == 1 and ableToLearn or selectionIndex == 0:
            X = 1
            Y = 9
            return self.actions({'area': "Fartooq Hold",
                                 'coordinates': (X, Y)})
        elif selectionIndex == 2 and ableToLearn or selectionIndex == 1:
            self.c.flags['Nooking'] = True
            i = Static.ICAS.index(thisIca)
            nextIca = [ica for ica in Static.ICAS[i+1:] + Static.ICAS[:i]
                       if ica in self.c.flags][0]
            return self.actions(Static.ICA_DATA[nextIca])
        elif "Nooking" in self.c.flags:
            self.text = (npc+" transports you to the next nook.")
            del self.c.flags['Nooking']
        elif npc not in self.c.flags:
            self.text = ("You crawl through the gap and find yourself "+
                         "in a dark, damp nook. To your surprise, there's "+
                         "someone else inside."+
                         "\nWoman: Quick, get in here. It is not safe outside. "+
                         "There are monsters."+
                         "\nToshe: Yeah, I noticed. Who are you?"+
                         "\n"+npc+": I am "+npc+". I take refuge in the "+
                         "trees. I protect the peace and serenity of the "+
                         "forest. I craft special tunics for use by fellow "+
                         "archers. I can teach you the way of the bow.")
            self.c.flags['Ica'] = True
        elif not ableToLearn:
            self.text = "\n"+npc+": Archer, you must make peace with an aquatic beast. Then, I can teach you a devastating technique in this keep."
        else:
            self.text = ("You crawl through the gap and find yourself "+
                         "in a dark, damp nook."+
                         "\n"+npc+": What do you seek today, archer?")
        return self.actions({'items for sale': [tunic]+[None]*8})
