"""
File: TUAMountOlympus.py
Author: Ben Gardner
Created: April 29, 2023
Revised: May 19, 2023
"""


import random


class MountOlympus:

    name = "Mount Olympus"
    audio = "The Price of Glory"

    def generateMap(self, mapName="Spiral"):
        sacredSpots = (
            None,
            self.maverick,
            self.forge,
            self.ointment,
            self.entrance,
            self.forgeEntrance,
        )

        def generateEnemyLocations():
            chance = 0.2
            candidates = []
            for y in range(len(self.spots)):
                for x in range(len(self.spots[0])):
                    if any(self.spots[y][x] == spot for spot in sacredSpots):
                        continue
                    candidates.append((x, y))
            return [candidate for candidate in candidates if random.randint(1, 100) <= chance * 100]

        def replaceRandomSpot(spots, replacement, locations):
            candidates = []
            for y in range(len(self.spots)):
                for x in range(len(self.spots[0])):
                    if any(self.spots[y][x] == spot for spot in sacredSpots):
                        continue
                    candidates.append((x, y))
            x, y = random.choice(candidates)
            self.spots[y][x] = replacement
            locations.append((x, y))

        mavr = self.maverick
        forg = self.forge
        oint = self.ointment
        entr = self.entrance
        ltRt = self.leftRight
        upDn = self.upDown
        upRt = self.upRight
        upLt = self.upLeft
        dnRt = self.downRight
        dnLt = self.downLeft
        upD2 = self.upDown2
        dist = self.somethingInTheDistance
        towr = self.tower
        forE = self.forgeEntrance

        if "Mount Olympus Map" not in self.c.flags:
            self.c.flags['Mount Olympus Map'] = {}
            self.c.flags['Mount Olympus Map']['Events'] = []
        eventLocations = self.c.flags['Mount Olympus Map']['Events']

        if mapName == "Spiral":
            self.audio = "The Price of Glory"
            def warp():
                X = 7
                Y = 15
                return self.actions({'area': "Mount Olympus",
                                     'coordinates': (X, Y)})
            self.spots = [
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
[None, forg, None, None, None, dnRt, ltRt, dist, ltRt, dnLt, None, None, None, None, None],
[None, None, None, None, dnRt, upLt, None, None, None, upRt, dnLt, None, None, None, None],
[None, None, None, dnRt, upLt, None, None, None, None, None, upRt, dnLt, None, None, None],
[None, None, dnRt, upLt, None, None, dnRt, ltRt, dnLt, None, None, upRt, dnLt, None, None],
[None, None, upDn, None, None, dnRt, upLt, None, upRt, dnLt, None, None, upDn, None, None],
[None, dnRt, upLt, None, dnRt, upLt, None, None, None, upRt, dnLt, None, upRt, dnLt, None],
[None, upDn, None, None, upDn, None, None, forE, None, None, upD2, None, None, upD2, None],
[None, upRt, dnLt, None, upRt, dnLt, None, towr, None, None, upDn, None, None, upDn, None],
[None, None, upDn, None, None, upRt, ltRt, upLt, None, dnRt, upLt, None, dnRt, upLt, None],
[None, None, upRt, dnLt, None, None, None, None, None, upDn, None, None, upDn, None, None],
[None, None, None, upRt, ltRt, dnLt, None, dnRt, ltRt, upLt, None, dnRt, upLt, None, None],
[None, None, None, None, None, upRt, ltRt, upLt, None, None, None, upDn, None, None, None],
[None, None, None, None, None, None, None, None, None, None, dnRt, upLt, None, None, None],
[None, None, None, None, None, None, None, dnRt, dist, ltRt, upLt, None, None, None, None],
[None, None, None, None, None, None, None, entr, None, None, None, None, None, None, None],
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            ]
        elif mapName == "Blob":
            self.audio = "Groundhog"
            def warp():
                X = 6
                Y = 12
                return self.actions({'area': "Mount Olympus",
                                     'coordinates': (X, Y)})
            self.spots = [
[None, None, None, None, None, None, None, None, None, None, None, None, None],
[None, forg, None, None, dnRt, ltRt, dist, ltRt, dnLt, None, None, None, None],
[None, None, None, dnRt, upDn, ltRt, upD2, ltRt, upDn, dnLt, None, None, None],
[None, None, dnRt, upDn, ltRt, upD2, ltRt, upD2, ltRt, upDn, dnLt, None, None],
[None, None, upD2, ltRt, upDn, ltRt, upD2, ltRt, upDn, ltRt, upD2, None, None],
[None, dnRt, ltRt, upD2, ltRt, upDn, ltRt, upDn, ltRt, upD2, ltRt, dnLt, None],
[None, upD2, upDn, ltRt, upDn, ltRt, upD2, ltRt, upDn, ltRt, upDn, upD2, None],
[None, upRt, ltRt, upD2, ltRt, upDn, ltRt, upDn, ltRt, upD2, ltRt, upLt, None],
[None, None, upD2, ltRt, upDn, ltRt, upD2, ltRt, upDn, ltRt, upD2, None, None],
[None, None, upRt, upDn, ltRt, upD2, ltRt, upD2, ltRt, upDn, upLt, None, None],
[None, None, None, upRt, upDn, ltRt, upD2, ltRt, upDn, upLt, None, None, None],
[None, None, None, None, upRt, upD2, ltRt, upD2, upLt, None, None, None, None],
[None, None, None, None, None, None, entr, None, None, None, None, None, None],
[None, None, None, None, None, None, None, None, None, None, None, None, None],
            ]
            if eventLocations:
                self.spots[eventLocations[0][1]][eventLocations[0][0]] = mavr
                self.spots[eventLocations[1][1]][eventLocations[1][0]] = oint
                self.spots[eventLocations[2][1]][eventLocations[2][0]] = forE
            else:
                replaceRandomSpot(self.spots, mavr, eventLocations)
                replaceRandomSpot(self.spots, oint, eventLocations)
                replaceRandomSpot(self.spots, forE, eventLocations)
        elif mapName == "Snake":
            self.audio = "Hummingbird"
            def warp():
                X = 5
                Y = 19
                return self.actions({'area': "Mount Olympus",
                                     'coordinates': (X, Y)})
            self.spots = [
[None, None, None, None, None, None, None, None, None, None, None],
[None, forg, None, None, None, forE, None, None, None, None, None],
[None, None, None, None, dnRt, towr, None, None, None, None, None],
[None, None, None, dnRt, ltRt, upLt, None, None, None, None, None],
[None, None, dnRt, ltRt, upLt, None, None, None, None, None, None],
[None, dnRt, ltRt, upLt, None, None, None, None, None, None, None],
[None, upD2, upDn, None, None, None, None, None, None, None, None],
[None, upRt, ltRt, dnLt, None, None, None, None, None, None, None],
[None, None, upRt, ltRt, dnLt, None, None, None, None, None, None],
[None, None, None, upRt, ltRt, dnLt, None, None, None, None, None],
[None, None, None, None, upRt, ltRt, dnLt, None, None, None, None],
[None, None, None, None, None, upRt, ltRt, dnLt, None, None, None],
[None, None, None, None, None, None, upRt, ltRt, dnLt, None, None],
[None, None, None, None, None, None, None, upRt, ltRt, dnLt, None],
[None, None, None, None, None, None, None, None, upDn, upD2, None],
[None, None, None, None, None, None, None, dnRt, ltRt, upLt, None],
[None, None, None, None, None, None, dnRt, ltRt, upLt, None, None],
[None, None, None, None, None, dnRt, ltRt, upLt, None, None, None],
[None, None, None, None, None, upRt, upLt, None, None, None, None],
[None, None, None, None, None, entr, None, None, None, None, None],
[None, None, None, None, None, None, None, None, None, None, None],
            ]
            if eventLocations:
                self.spots[eventLocations[0][1]][eventLocations[0][0]] = mavr
                self.spots[eventLocations[1][1]][eventLocations[1][0]] = oint
            else:
                replaceRandomSpot(self.spots, mavr, eventLocations)
                replaceRandomSpot(self.spots, oint, eventLocations)
        if "Enemies" not in self.c.flags['Mount Olympus Map']:
            self.c.flags['Mount Olympus Map']['Enemies'] = generateEnemyLocations()
        self.spots[-2][-2] = warp
        self.c.flags['Last Mount Olympus'] = mapName

    def __init__(self, character):
        def getNextMapName(currentName):
            if currentName == "Spiral":
                return "Blob"
            elif currentName == "Blob":
                return "Snake"
            elif currentName == "Snake":
                return "Spiral"

        self.view = None
        self.imageIndex = None
        self.text = None
        self.menu = None
        self.helpText = None
        self.tempFlag = None
        self.c = character
        self.movementVerb = "walk"
        
        if "Mount Olympus Ascensions" not in self.c.flags:
            self.c.flags['Mount Olympus Ascensions'] = 0
        
        if "Mount Olympus Map" in self.c.flags:
            self.generateMap(self.c.flags['Last Mount Olympus'])
        elif "Last Mount Olympus" in self.c.flags:
            self.generateMap(getNextMapName(self.c.flags['Last Mount Olympus']))
        else:
            self.generateMap()

        self.encounters = None

    def movementActions(self):
        pass

    def actions(self, newActions=None):
        def enemyEncounter():
            def getRandomName():
                prefixes = [
                    "A",
                    "Acti",
                    "Aero",
                    "Aetheri",
                    "Alcyono",
                    "Amphi",
                    "Angio",
                    "Arche",
                    "Bio",
                    "Bryo",
                    "Calypto",
                    "Cata",
                    "Chrono",
                    "Chryso",
                    "Cosmo",
                    "Cyano",
                    "Dendro",
                    "Deutero",
                    "Dia",
                    "Diplo",
                    "Dra",
                    "Eo",
                    "Epi",
                    "Erythro",
                    "Eu",
                    "Exo",
                    "Geo",
                    "Gnatho",
                    "Haplo",
                    "Helico",
                    "Hemo",
                    "Hi",
                    "Holo",
                    "Hyalo",
                    "Hyper",
                    "Ido",
                    "Iso",
                    "Kine",
                    "Litho",
                    "Lycano",
                    "Macro",
                    "Manu",
                    "Mega",
                    "Melano",
                    "Meso",
                    "Meta",
                    "Mono",
                    "Morpho",
                    "Muco",
                    "Myko",
                    "Neo",
                    "Neuro",
                    "Odyne",
                    "Onco",
                    "Onycho",
                    "Ophi",
                    "Oro",
                    "Pachy",
                    "Phobo",
                    "Phylo",
                    "Platy",
                    "Poly",
                    "Pro",
                    "Proto",
                    "Psilo",
                    "Ptero",
                    "Rhegma",
                    "Rhodo",
                    "Sauro",
                    "Soma",
                    "Sy",
                    "Taxo",
                    "Telo",
                    "Tere",
                    "Thana",
                    "Trocho",
                    "Xeno",
                    "Xipho",
                    "Zelo",
                ]
                suffixes = [
                    "blast",
                    "chet",
                    "chrome",
                    "drome",
                    "gen",
                    "gist",
                    "hedr",
                    "l",
                    "log",
                    "mer",
                    "metr",
                    "mir",
                    "n",
                    "phor",
                    "seism",
                    "sm",
                    "st",
                    "stom",
                    "therm",
                    "thes",
                    "thyre",
                    "troph",
                    "tom",
                    "tox",
                    "xes",
                    "zizyph",
                    "zon",
                ]
                diminutives = [
                    "ides",
                    "idas",
                    "ion",
                    "ios",
                    "ius",
                    "os",
                    "us",
                    "ianos",
                ]
                rc = random.choice
                return rc(prefixes) + rc(suffixes) + rc(diminutives)
                
            enemyLevels = {
                "Nemean Lion": 5,
                "Teumessian Fox": 5,
                "Stymphalian Bird": 5,
                "Hydra": 4,
                "Chimera": 4,
                "Cerberus": 4,
                "Cychreides": 3,
                "Skolopendra": 3,
                "Pterripus": 3,
                "Gorgon": 2,
                "Harpy": 2,
                "Minotaur": 2,
                "Centaur": 1,
                "Satyr": 1,
                "Siren": 1,
            }
            for x, y in self.c.flags['Mount Olympus Map']['Enemies']:
                if x == self.c.x and y == self.c.y:
                    self.c.flags['Mount Olympus Map']['Enemies'].remove((x, y))
                    stats = {}
                    random.seed(x + y * 100 + self.c.flags['Mount Olympus Ascensions'] * 10000)
                    enemy = random.choice(enemyLevels.keys())
                    stats['NAME'] = getRandomName()
                    stats['SUBNAME'] = enemy
                    if self.c.level > 30:
                        stats['LEVEL'] = self.c.level + enemyLevels[enemy]
                        stats['XP'] = 1 + ((self.c.level - 30) ** 1.5 / 200)
                        stats['maxHp'] = 1 + ((self.c.level - 30) ** 2.0 / 200)
                        stats['damage'] = 1 + ((self.c.level - 30) * 0.1)
                        stats['defence'] = 1 + ((self.c.level - 30) * 0.1)
                    modifiers = {
                        'Multiplicative': True,
                        'Stats': stats}
                    return {
                        'view': "battle",
                        'enemy': enemy,
                        'enemy modifiers': modifiers,
                        'mercenaries': self.c.mercenaries,}
            return {}

        actions = {'view': self.view,
                   'image index': self.imageIndex,
                   'text': self.text,
                   'menu': self.menu,
                   'italic text': self.helpText}
        if "Mount Olympus Map" in self.c.flags:
            actions.update(enemyEncounter())
        if newActions:
            actions.update(newActions)
        return actions

    def maverick(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 0
        self.text = ""
        self.helpText = None
        self.menu = []
        skill1 = "Expunging Lunge"
        skill2 = "Reckless Rack"
        skill3 = "Battery Cage"
        price1 = 10000
        price2 = 20000
        price3 = 30000
        self.menu = [
            "Speak to Maverick.",
            "Learn %s (%s euros)." % (skill1, price1),
            "Learn %s (%s euros)." % (skill2, price2),
            "Learn %s (%s euros)." % (skill3, price3),
        ]
        if selectionIndex == 0:
            textOptions = []
            textOptions.append("Maverick: Have you enhanced your gear at the forge? Enhance far enough, and your equipment will change form.")
            textOptions.append("Maverick: The minotaur below the city will test your might. Yes, I have defeated it many times. You may want to have a go at it--to learn, foremost--but also to have a chance at acquiring its horn, which is a potent and empowering item at the anvil.")
            textOptions.append("Maverick: It is a cold and solemn life I lead. But I must do it. Someone has to do it, and it's me. Yes, I am the one who must stand atop this mountain to teach warriors the final three skills. Why couldn't they have assigned me somewhere nice, like Pristina? Oh, that's right: Raoul had to take that spot.")
            if self.c.equippedWeapon.CATEGORY in ("Bow", "Wand"):
                textOptions.append("Maverick: Well, I don't know about that wooden weapon of yours.")
            if self.c.strength > 50:
                textOptions.append("Maverick: Hail, fellow.")
            if self.c.hasMercenary("Qendresa"):
                textOption = "Maverick: Now, what is such a pretty lady doing gallivanting around this highly dangerous, yet completely isolated and--"
                textOption += "\nQendresa grips the hilt of her espadon."
                textOption += "\nMaverick: Oh, I meant no harm!"
                textOption += "\nMaverick raises his hands slightly and takes a half step backward."
                textOption += "\nQendresa: Oh, you could not cause any."
                if self.c.hasMercenary("Barrie"):
                    textOption += "\nBarrie: Watch out dude, she's got 'tude."
                textOptions.append(textOption)
            
            self.text = random.choice(textOptions)
        elif selectionIndex == 1:
            return self.actions({'skill': skill1,
                                 'cost': price1})
        elif selectionIndex == 2:
            return self.actions({'skill': skill2,
                                 'cost': price2})
        elif selectionIndex == 3:
            return self.actions({'skill': skill3,
                                 'cost': price3})
        else:
            if "Maverick" not in self.c.flags:
                self.text = "You confront a warrior standing stoically upon an outcrop. He rests his swords at his sides as you draw near."
            self.text += "\nMaverick: Greetings, explorer. I am Maverick. I am protector of Olympus. And, I am teacher to only the most talented pupils."
            self.text = self.text.strip()
        return self.actions()

    def forge(self, selectionIndex=None):
        self.view = "forge"
        self.imageIndex = 1
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            if "Just Forged" in self.c.flags:
                self.c.flags['Mount Olympus Ascensions'] += 1
                del self.c.flags['Just Forged']
                del self.c.flags['Mount Olympus Map']
                del self.c.flags['Marked Areas'][self.name]
                del self.c.flags['Discovered Areas'][self.name]
                if "Olympian Treasure" in self.c.flags:
                    del self.c.flags['Olympian Treasure']
                self.__init__(self.c)
                X = 1
                Y = 5
                return self.actions({'area': "Litochoro",
                                     'coordinates': (X, Y)})
            else:
                for y in range(len(self.spots)):
                    for x in range(len(self.spots[0])):
                        if self.spots[y][x] == self.forgeEntrance:
                            X, Y = x, y
                            return self.actions({'area': "Mount Olympus",
                                                 'coordinates': (X, Y)})
        if "Just Forged" in self.c.flags:
            self.view = "forge done"
            self.text = "You enter the Forge of Hephaestus. The flame burns low."
            self.menu = ["Return to Litochoro.",]
        else:
            if "Mount Olympus Complete" in self.c.flags:
                self.text = "You enter the Forge of Hephaestus once again, hammer at the ready."
            else:
                self.text = ("Inside the forge is a massive anvil, with a burning crucible as its heat source. Alongside it lies a solid obsidian blacksmith's hammer." +
                "\nToshe: This must be the ancient forge that belonged to Hephaestus." +
                "\nYou lift the hammer and prepare to work.")
            self.menu = ["Leave the forge.",]
        return self.actions()

    def ointment(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0 and "Olympian Treasure" not in self.c.flags:
            self.text = ("You collect a vial of Olympian Ointment!")
            self.c.flags['Olympian Treasure'] = True
            return self.actions({'item': "Olympian Ointment"})
        if "Olympian Treasure" not in self.c.flags:
            self.imageIndex = 2
            self.text = "You come across an ornate jar on the ground in seemingly pristine condition. It is too heavy to lift."
            self.menu = ["Take some of what's in the jar.",]
        return self.actions()

    def entrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 3
        self.text = None
        self.helpText = None
        self.menu = []
        if selectionIndex == 0:
            X = 1
            Y = 5
            return self.actions({'area': "Litochoro",
                                 'coordinates': (X, Y)})
        self.text = "You arrive at the base of Mount Olympus."
        if "Mount Olympus Base" not in self.c.flags:
            self.c.flags['Mount Olympus Base'] = True
            if self.c.hasMercenary("Barrie"):
                self.text += "\nBarrie: The home of the gods!"
            if self.c.hasMercenary("Qendresa"):
                self.text += "\nQendresa: This mountain is quite astonishing...and treacherous!"
                self.text += "\nQendresa points to a immense creature in the distance."
                if self.c.hasMercenary("Barrie"):
                    self.text += "\nBarrie: Pfft. We can take 'em on."
        self.menu = ["Return to Litochoro.",]
        return self.actions()

    def leftRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 4
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def upDown(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 5
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def upRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 6
        self.helpText = None
        self.menu = []
        return self.actions()

    def upLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 7
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def downRight(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 8
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def downLeft(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 9
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def upDown2(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 10
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def somethingInTheDistance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 11
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def tower(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 12
        self.text = None
        self.helpText = None
        self.menu = []
        return self.actions()

    def forgeEntrance(self, selectionIndex=None):
        self.view = "travel"
        self.imageIndex = 13
        self.text = None
        self.helpText = None
        if "Mount Olympus Complete" in self.c.flags:
            self.text = "You approach the Forge of Hephaestus."
            self.menu = ["Enter the Forge of Hephaestus."]
        else:
            self.text = "You approach a colossal forge."
            self.menu = ["Enter the forge."]
        if selectionIndex == 0:
            X = 1
            Y = 1
            return self.actions({'area': "Mount Olympus",
                                 'coordinates': (X, Y)})
        return self.actions()
