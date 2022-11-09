# -*- coding: utf-8 -*-
#Toshe's Underwater Adventures 1.1

"""
File: Toshe's Quest II.py
Author: Ben Gardner
Created: December 25, 2012
Revised: November 8, 2022
"""

 
from Tkinter import *
import tkFont
import tkMessageBox
from TUAMain import Main
from TUADialog import OpenFileDialog
from TUAStatics import Static
import random
from datetime import datetime
import pickle


class Window:
    """Contains the game window."""

    def __init__(self, master):
        self.gameFrame = Frame(master, bg=DEFAULT_BG, relief=SUNKEN, bd=4)
        self.gameFrame.grid(row=0)
        
        self.levelUpFrame = Frame(master, bg=LEVEL_UP_BG, relief=RIDGE, bd=10)
        self.levelUpFrame.grid(row=0)
        self.levelUpFrame.grid_remove()

        self.mercenaryUpFrame = Frame(master, bg=MERCENARY_UP_BG,
                                      relief=RIDGE, bd=10)
        self.mercenaryUpFrame.grid(row=0)
        self.mercenaryUpFrame.grid_remove()
        
        self.lootFrame = Frame(master, bg=LOOT_BG, relief=RIDGE, bd=10)
        self.lootFrame.grid(row=0)
        self.lootFrame.grid_remove()
        
        self.powerUpFrame = Frame(master, bg=MYSTIC_BG, relief=RIDGE, bd=10)
        self.powerUpFrame.grid(row=0)
        self.powerUpFrame.grid_remove()
        
        self.newSkillFrame = Frame(master, bg=SKILL_BG, relief=RIDGE, bd=10)
        self.newSkillFrame.grid(row=0)
        self.newSkillFrame.grid_remove()
        
        self.levelUpLabel = Label(self.levelUpFrame, text="LEVEL UP!",
                                  font=font5, bg=LEVEL_UP_BG, fg=LEVEL_UP_FG)
        self.levelUpLabel.grid()
        self.levelUpLabel.bind("<Button-1>", self.removeLevelUpFrame)
        
        self.mercenaryUpLabel = Label(self.mercenaryUpFrame,
                                 text="MERC. UP!",
                                 font=font7,
                                 bg=MERCENARY_UP_BG, fg=MERCENARY_UP_FG)
        self.mercenaryUpLabel.grid()
        self.mercenaryUpLabel.bind("<Button-1>", self.removeMercenaryUpFrame)
        
        lootLabel = Label(self.lootFrame, text="LOOT!", font=font5,
                          bg=LOOT_BG, fg=LOOT_FG)
        lootLabel.grid()
        lootLabel.bind("<Button-1>", self.removeLootFrame)
        
        self.powerUpLabel = Label(self.powerUpFrame, text="POWER UP!",
                                  font=font5, bg=MYSTIC_BG, fg=MYSTIC_FG2)
        self.powerUpLabel.grid()
        self.powerUpLabel.bind("<Button-1>", self.removePowerUpFrame)
        
        self.newSkillLabelBottom = Label(self.newSkillFrame,
                                         text="PUMMELER'S PRECISION!",
                                         wraplength=WINDOW_WIDTH,
                                         font=font7,
                                         bg=SKILL_BG, fg=SKILL_FG)
        self.newSkillLabelBottom.grid(row=0, rowspan=2, pady=16)
        self.newSkillLabelBottom.bind("<Button-1>", self.removeNewSkillFrame)
        self.newSkillLabelTop = Label(self.newSkillFrame,
                                         text="New Skill",
                                         font=font8,
                                         bg=SKILL_BG, fg=SKILL_FG)
        self.newSkillLabelTop.grid(row=0, sticky=N)
        self.newSkillLabelTop.bind("<Button-1>", self.removeNewSkillFrame)
        
        self.makeChildren(self.gameFrame)

    def makeChildren(self, master):
        self.topFrame = TopFrame(master)
        self.bottomFrame = BottomFrame(master)
        
    def gridLevelUpFrame(self):
        self.levelUpFrame.grid()
        root.after(4000, window.removeLevelUpFrame)

    def removeLevelUpFrame(self, event=None):
        self.levelUpFrame.grid_remove()

    def gridMercenaryUpFrame(self, name):
        self.mercenaryUpLabel.config(text="%s UP!" % name.upper())
        self.mercenaryUpFrame.grid()
        root.after(3000, window.removeMercenaryUpFrame)

    def removeMercenaryUpFrame(self, event=None):
        self.mercenaryUpFrame.grid_remove()
        
    def gridLootFrame(self):
        self.lootFrame.grid()
        root.after(2500, window.removeLootFrame)

    def removeLootFrame(self, event=None):
        self.lootFrame.grid_remove()
        
    def gridPowerUpFrame(self):
        self.powerUpFrame.grid()
        root.after(3500, window.removePowerUpFrame)

    def removePowerUpFrame(self, event=None):
        self.powerUpFrame.grid_remove()
        
    def gridnewSkillFrame(self, skillName):
        self.newSkillLabelBottom.config(text="%s!" % skillName.upper())
        self.newSkillFrame.grid()
        root.after(3000, window.removeNewSkillFrame)
        
    def removeNewSkillFrame(self, event=None):
        self.newSkillFrame.grid_remove()


class TopFrame:
    """Contains the upper portion of the game window."""

    def __init__(self, master):
        frameA = Frame(master, bg=DEFAULT_BG)
        frameA.grid()
        self.makeChildren(frameA)

    def makeChildren(self, master):        
        self.topLeftFrame = TopLeftFrame(master)
        self.topCenterFrame = TopCenterFrame(master)
        self.topRightFrame = TopRightFrame(master)
    

class BottomFrame:
    """Contains the lower portion of the game window."""

    def __init__(self, master):
        frameB = Frame(master, bg=DEFAULT_BG)
        frameB.grid()
        self.makeChildren(frameB)

    def makeChildren(self, master):
        self.bottomLeftFrame = BottomLeftFrame(master)
        self.bottomRightFrame = BottomRightFrame(master)


class TopLeftFrame:
    """Contains frames for vital stats and inventory.

    Only one is displayed at a time.
    """

    def __init__(self, master):
        frameC = Frame(master, width=FRAME_C_WIDTH, height=FRAME_C_HEIGHT,
                       bg=DEFAULT_BG)
        frameC.grid()
        frameC.grid_propagate(0)
        self.makeFrameElements(frameC)

    def makeFrameElements(self, master):
        """Creates labelframes for vital stats and inventory.

        Vital stats displays: character name, level, XP, HP, EP
        Inventory displays: items, item stats for selected item, equip button
        """
        self.vitalStats = LabelFrame(master, text="Vital Stats", font=font3,
                                     width=FRAME_C_WIDTH, height=FRAME_C_HEIGHT,
                                     bg=DEFAULT_BG)
        self.vitalStats.grid()
        self.vitalStats.grid_propagate(0)
    
        self.levelLabel = Label(self.vitalStats, text="1", font=font2,
                                width=2, bg=DEFAULT_BG, relief=RIDGE)
        self.levelLabel.grid(column=1, padx=10, pady=10, sticky=E)
        self.nameLabel = Label(self.vitalStats, text="Toshe", font=italicFont4,
                               fg=BLACK, bg=DEFAULT_BG)
        self.nameLabel.grid(row=0, column=0, columnspan=2)
        self.xpBarLabel = Label(self.vitalStats, image=xpBars[6], bg=YELLOW,
                                relief=SUNKEN, bd=1, compound=CENTER,
                                font=font8, fg=WHITE)
        self.xpBarLabel.grid(row=1, columnspan=2)
        self.spBarLabel = Label(self.vitalStats, image=spBars[34],
                                bg=DEFAULT_BG, relief=SUNKEN, bd=1)
        self.spBarLabel.grid(row=3, columnspan=2)
        self.spLabel = Label(self.vitalStats, text="80",
                             bg=DEFAULT_BG, font=font1, bd=0)
        self.spLabel.grid(row=4, sticky=W+N)
        self.spWord = Label(self.vitalStats, text="Mystic 2", fg=MYSTIC_FG,
                            bg=MYSTIC_BG, font=font1, relief=RIDGE)
        self.spWord.grid(row=4, column=1, padx=1, ipadx=4, ipady=1, sticky=E)
        self.tosheLabel = Label(self.vitalStats, image=tosheImage, bg=BROWN,
                                relief=RIDGE, bd=4)
        self.tosheLabel.grid(columnspan=2, pady=20)
        self.hpWord = Label(self.vitalStats, text="HP",
                            bg=DEFAULT_BG, font=font1, bd=0)
        self.hpWord.grid(column=0, sticky=W)
        self.hpLabel = Label(self.vitalStats, text="100/100",
                                  bg=DEFAULT_BG, font=font1, bd=0)
        self.hpLabel.grid(row=6, column=1, sticky=E)
        self.hpBarLabel = Label(self.vitalStats, image=hpBars[4], bg=DEFAULT_BG,
                                relief=SUNKEN, bd=1)
        self.hpBarLabel.grid(columnspan=2)
        self.epBarLabel = Label(self.vitalStats, image=epBars[2], bg=DEFAULT_BG,
                                relief=SUNKEN, bd=1)
        self.epBarLabel.grid(row=8, columnspan=2)
        self.epWord = Label(self.vitalStats, text="EP",
                            bg=DEFAULT_BG, font=font1, bd=0)
        self.epWord.grid(column=0, sticky=W)
        self.epLabel = Label(self.vitalStats, text="100/100",
                                  bg=DEFAULT_BG, font=font1, bd=0)
        self.epLabel.grid(row=9, column=1, sticky=E)


        self.inventory = LabelFrame(master, text="Inventory", font=font3,
                                    width=FRAME_C_WIDTH, height=FRAME_C_HEIGHT,
                                    bg=DEFAULT_BG)
        self.inventory.grid(row=0)
        self.inventory.grid_propagate(0)

        # Inventory checkbutton variable
        self.v1 = IntVar()
        self.itemButtons = makeItemButtons(self.inventory, self.v1, 0)
        self.itemNameLabel = Label(self.inventory, text="Name", font=font2,
                                   bg=DEFAULT_BG)
        self.itemNameLabel.grid(columnspan=3, sticky=W)
        self.itemCategoryLabel = Label(self.inventory, text="Category",
                                       font=font2, bg=DEFAULT_BG)
        self.itemCategoryLabel.grid(columnspan=3, sticky=W)
        self.itemValueLabel = Label(self.inventory, text="X Euros", font=font1,
                                    bg=DEFAULT_BG)
        self.itemValueLabel.grid(columnspan=3, sticky=W)
        self.itemRequirementLabel = Label(self.inventory, text="Requires X Y",
                                          font=font1, bg=DEFAULT_BG)
        self.itemRequirementLabel.grid(columnspan=3, sticky=W)
        self.itemQualityLabel = Label(self.inventory,
                                      text="X Power/X Defence", font=font1,
                                      bg=DEFAULT_BG)
        self.itemQualityLabel.grid(columnspan=3, sticky=W)
        self.itemCBRateLabel = Label(self.inventory, text=
                                     "X% Critical Chance/X% Block Chance",
                                     font=font1, bg=DEFAULT_BG)
        # CB represents critical/block
        self.itemCBRateLabel.grid(columnspan=3, sticky=W)
        self.itemElementLabel = Label(self.inventory,
                                      text=
                                      "Imbued with X/Reduces X Damage by Y%",
                                      font=font1, bg=DEFAULT_BG)
        self.itemElementLabel.grid(columnspan=3, sticky=W)
        self.equipButton = Button(self.inventory, text="Equip", font=font2,
                                  fg=BUTTON_FG, bg=BUTTON_BG,
                                  command=self.clickEquipButton)
        self.equipButton.grid(columnspan=3, sticky=E+W)
        self.sellButton = Button(self.inventory, text="Sell", font=font2,
                                 fg=BUTTON_FG, bg=BUTTON_BG,
                                 command=self.clickSellButton)
        self.sellButton.grid(row=10, columnspan=3, sticky=E+W)
        self.sellButton.grid_remove()
        self.dropButton = Button(self.inventory, text="Drop", font=font2,
                                 fg=BUTTON_FG, bg=BUTTON_BG,
                                 command=self.clickDropButton)
        self.dropButton.grid(row=10, columnspan=3, sticky=E+W)
        self.dropButton.grid_remove()

    def clickEquipButton(self):
        main.character.equip(self.v1.get())
        window.topFrame.topRightFrame.updateOtherStats()
        self.equipButton['state'] = DISABLED
        self.updateInventory()
        if main.view == "battle":
            interfaceActions = main.equipItem()
            window.bottomFrame.bottomRightFrame.clickBackButton()
            updateInterface(interfaceActions)
        main.sound.playSound(main.sound.sounds['Equip'])
        
    def clickSellButton(self):
        main.sell(self.v1.get())
        self.sellButton['state'] = DISABLED
        self.updateInventory()
        window.topFrame.topRightFrame.buyButton['state'] = DISABLED
        window.topFrame.topRightFrame.updateStore()

    def clickDropButton(self):
        if self.v1.get() in main.character.equippedItemIndices.values():
            main.character.equip(self.v1.get())
        main.character.removeItem(self.v1.get())
        main.character.addItem(main.tempItem)
        window.bottomFrame.bottomRightFrame.clickCancelDropButton()

    def updateVitalStats(self):
        """Change the current level, xp, hp and ep of the character shown in the
        Vital Stats frame to correspond to the character's actual values of
        these stats.
        """
        c = main.character
        
        self.levelLabel['text'] = c.level
        if c.xp > c.xpTnl:
            self.xpBarLabel['image'] = xpBars[-1]
        else:
            self.xpBarLabel['image'] = xpBars[int(float(c.xp) / c.xpTnl *
                                                  (NUMBER_OF_BARS - 1))]
        self.xpBarLabel['text'] = "%d%%" % (100 * c.xp / c.xpTnl)
        self.xpBarLabel['fg'] = WHITE if (100 * c.xp / c.xpTnl < 45) else NAVY
        if hasattr(c, 'specialization'):
            self.spWord['text'] = "%s %s" % (c.specialization, c.ub205e2nmzfwi)
            if c.sp > c.spTnl:
                self.spBarLabel['image'] = spBars[-1]
            else:
                self.spBarLabel['image'] = spBars[int(float(c.sp) / c.spTnl *
                                                      (NUMBER_OF_BARS - 1))]
            self.spLabel['text'] = c.sp
        if c.hp <= 0:
            self.hpBarLabel['image'] = hpBars[0]
        elif float(c.hp) < float(c.maxHp) / NUMBER_OF_BARS:
            self.hpBarLabel['image'] = hpBars[1]
        else:
            self.hpBarLabel['image'] = hpBars[int(float(c.hp) / c.maxHp *
                                                  (NUMBER_OF_BARS - 1))]
        self.hpBarLabel['text'] = "%d/%d" % (c.hp, c.maxHp)
        self.hpLabel['text'] = "%d/%d" % (c.hp, c.maxHp)
        if c.ep <= 0:
            self.epBarLabel['image'] = epBars[0]
        elif float(c.ep) < float(c.maxEp) / NUMBER_OF_BARS:
            self.epBarLabel['image'] = epBars[1]
        else:
            self.epBarLabel['image'] = epBars[int(float(c.ep) / c.maxEp *
                                                  (NUMBER_OF_BARS - 1))]
        self.epBarLabel['text'] = "%d/%d" % (c.ep, c.maxEp)
        self.epLabel['text'] = "%d/%d" % (c.ep, c.maxEp)

    def updateInventory(self):
        """Show the current images for the character's inventory in the
        Inventory frame.
        """
        clearItemStats(self, store=False)
        self.v1.set(-1)
        for i in range(0, 3):
            for j in range(0, 3):
                if not main.character.items[i*3+j]:
                    self.itemButtons[i*3+j].config(image=noItemImage,
                                                   state=DISABLED,
                                                   bg=BLACK)
                elif i*3+j in main.character.equippedItemIndices.values():
                    try:
                        itemImage = itemImages[
                            main.character.items[i*3+j].IMAGE_NAME]
                    except KeyError as e:
                        print "Missing image: %s" % e
                        itemImage = defaultImage
                    self.itemButtons[i*3+j].config(image=itemImage,
                                                   state=NORMAL,
                                                   bg=LIGHTCYAN)
                elif i*3+j not in main.character.equippedItemIndices.values():
                    try:
                        itemImage = itemImages[
                            main.character.items[i*3+j].IMAGE_NAME]
                    except KeyError as e:
                        print "Missing image: %s" % e
                        itemImage = defaultImage
                    self.itemButtons[i*3+j].config(image=itemImage,
                                                   state=NORMAL,
                                                   bg=BLACK)
        self.equipButton['text'] = "Equip"

        
class TopCenterFrame:
    """Displays title, area image and map."""

    def __init__(self, master):
        frameD = Frame(master, width=348, height=FRAME_C_HEIGHT, bg=DEFAULT_BG)
        frameD.grid(row=0, column=1)
        frameD.grid_columnconfigure(0, weight=1)
        frameD.grid_rowconfigure(0, weight=3)
        frameD.grid_rowconfigure(1, weight=1)
        frameD.grid_propagate(0)
        self.makeFrameElements(frameD)

    def makeFrameElements(self, master):
        self.playMusic = BooleanVar(value=True)
        self.musicButton = Checkbutton(master, indicatoron=False, bg=DEFAULT_BG,
                                     relief=SUNKEN, image=musicImage,
                                     variable=self.playMusic,
                                     command=main.sound.muteMusic)
        self.musicButton.grid(row=0, padx=16, sticky=W)
        self.playSfx = BooleanVar(value=True)
        self.sfxButton = Checkbutton(master, indicatoron=False, bg=DEFAULT_BG,
                                     relief=SUNKEN, image=sfxImage,
                                     variable=self.playSfx,
                                     command=main.sound.muteSfx)
        try:
            with open("preferences.tqp", "r") as preferencesFile:
                preferences = pickle.load(preferencesFile)
                if not preferences.musicOn:
                    self.musicButton.invoke()
                if not preferences.sfxOn:
                    self.sfxButton.invoke()
        except IOError:
            pass
        self.sfxButton.grid(row=0, padx=40, sticky=W)
        self.titleLabel = Label(master, text="Toshe's Quest II", font=font6,
                                bg=DEFAULT_BG, bd=0)
        self.titleLabel.grid(row=0, pady=6)
        self.showMap = BooleanVar()
        self.mapButton = Checkbutton(master, indicatoron=False, bg=DEFAULT_BG,
                                     relief=SUNKEN, image=mapImage,
                                     variable=self.showMap, state=DISABLED,
                                     command=self.updateMapVisibility)
        self.mapButton.bind_all("m", lambda _: self.mapButton.invoke())
        self.mapButton.bind_all("M", lambda _: self.mapButton.invoke())
        self.mapButton.grid(row=0, padx=22, sticky=E)
        self.mapButton.grid_remove()
        self.areaButton = Button(master, image=welcomeImage, bg=DEFAULT_BG,
                                 relief=RAISED, bd=6, command=self.openFile)
        self.areaButton.grid(row=1, sticky=N)
        
        MAP_PIXEL_LENGTH = 300
        MAP_LENGTH = 15
        CELL_OFFSET = 4
        self.CENTER_CELL = (MAP_LENGTH / 2, MAP_LENGTH / 2)
        self.cells = []
        
        self.map = Canvas(master, width=MAP_PIXEL_LENGTH,
                          height=MAP_PIXEL_LENGTH,
                          bg=MAP_BG,
                          highlightbackground=DEFAULT_BG,
                          relief=SUNKEN,
                          bd=CELL_OFFSET-2)
        self.map.bind("<Button-1>", self.markMap)
        self.map.grid(row=1, sticky=N, pady=3)
        self.map.grid_remove()
        
        for row in range(MAP_LENGTH):
            self.cells.append([])
            for col in range(MAP_LENGTH):
                x0 = CELL_OFFSET + col * MAP_PIXEL_LENGTH / MAP_LENGTH
                y0 = CELL_OFFSET + row * MAP_PIXEL_LENGTH / MAP_LENGTH
                x1 = CELL_OFFSET + x0 + MAP_PIXEL_LENGTH / MAP_LENGTH
                y1 = CELL_OFFSET + y0 + MAP_PIXEL_LENGTH / MAP_LENGTH
                newCell = self.map.create_rectangle(x0, y0, x1, y1)
                self.cells[-1].append(newCell)
        
        self.clearMap()
        
    def clearMap(self, baseColor=None):
        if baseColor is None:
            baseColor = MAP_BG
        for cellRow in self.cells:
            for cell in cellRow:
                self.map.itemconfig(cell,
                                    fill=baseColor, outline=BLACK, width=0,
                                    dash=(), stipple='', activedash=(),
                                    activeoutline=BLACK)
        
    def updateMapVisibility(self, event=None):
        main.character.flags['Config']['Automap On'] = self.showMap.get()
        if self.showMap.get():
            self.updateMap()
        else:
            self.areaButton.grid()
            self.map.grid_remove()
            
    def updateMap(self):
        def updateCell(row, col, y, x):
            if (x < 0 or
                y < 0 or
                y >= len(main.currentArea.spots) or
                x >= len(main.currentArea.spots[y]) or
                row < 0 or
                col < 0 or
                row >= len(self.cells) or
                col >= len(self.cells[row]) or
                "dirty" not in self.map.gettags(self.cells[row][col])):
                return False
            
            self.map.dtag(self.cells[row][col], "dirty")
            
            if (x, y) in spots and (
                0 <= x-1 < len(areaSpots[0]) and areaSpots[y][x-1] or
                0 <= y-1 < len(areaSpots) and areaSpots[y-1][x] or
                0 <= x+1 < len(areaSpots[0]) and areaSpots[y][x+1] or
                0 <= y+1 < len(areaSpots) and areaSpots[y+1][x]
                ):
                config(self.cells[row][col], fill=spotColor, width=1,
                       activedash=(2, 4), activeoutline=markColor)
            elif (((x-1, y) in spots and
                   (0 <= x-1 < len(areaSpots[0]))) or
                  ((x, y-1) in spots and
                   (0 <= y-1 < len(areaSpots))) or
                  ((x+1, y) in spots and
                   (0 <= x+1 < len(areaSpots[0]))) or
                  ((x, y+1) in spots and
                   (0 <= y+1 < len(areaSpots)))):
                if areaSpots[y][x] is None:
                    config(self.cells[row][col], fill=mapColor, width=0,
                           stipple='gray50')
                else:
                    config(self.cells[row][col], fill=spotColor, width=0,
                           stipple='gray25')

            if (x, y) in markedSpots:
                config(self.cells[row][col], fill=markColor,
                       activeoutline=spotColor)
            if x == main.x and y == main.y:
                if main.view in ("battle", "battle over"):
                    config(self.cells[row][col], fill=RED)
                else:
                    config(self.cells[row][col], fill=LIGHTRED)
                
            updateCell(row-1, col, y-1, x)
            updateCell(row+1, col, y+1, x)
            updateCell(row, col-1, y, x-1)
            updateCell(row, col+1, y, x+1)
        
        # Set up var nicknames
        areaSpots = main.currentArea.spots
        spots = main.character.flags['Discovered Areas'][main.currentArea.name]
        markedSpots = main.character.flags['Marked Areas'][main.currentArea.name]
        config = self.map.itemconfig
        # Early return if in an enclosed space
        if not (
            0 <= main.x-1 < len(areaSpots[0]) and areaSpots[main.y][main.x-1] or
            0 <= main.y-1 < len(areaSpots) and areaSpots[main.y-1][main.x] or
            0 <= main.x+1 < len(areaSpots[0]) and areaSpots[main.y][main.x+1] or
            0 <= main.y+1 < len(areaSpots) and areaSpots[main.y+1][main.x]
            ):
            self.areaButton.grid()
            self.map.grid_remove()
            return
        else:
            self.areaButton.grid_remove()
            self.map.grid()
        
        # Set up colors
        markValue = -32
        spotColor = MAP_BG
        mapColor = MAP_BG
        if main.currentArea.name in Static.AREA_COLORS:
            spotColor = Static.AREA_COLORS[main.currentArea.name]['fg']
            mapColor = Static.AREA_COLORS[main.currentArea.name]['bg']
        markColor = "#"
        for i in [1,3,5]:
            newColorValue = int(spotColor[i:i+2], 16) + markValue
            newHexColorValue = hex(max(0, min(255, (newColorValue))))[2:4]
            if len(newHexColorValue) == 1:
                newHexColorValue = "0" + newHexColorValue
            markColor += newHexColorValue
        self.map['bg'] = mapColor
        self.clearMap(mapColor)
        self.map.addtag_all("dirty")
        updateCell(self.CENTER_CELL[0], self.CENTER_CELL[1], main.y, main.x)
        for item in self.map.find_withtag("dirty"):
            self.map.dtag(item, "dirty")
            
    def markMap(self, event=None):
        if len(self.map.find_withtag(CURRENT)) != 1:
            return

        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                if (self.cells[i][j] == self.map.find_withtag(CURRENT)[0] and
                    self.map.itemcget(self.cells[i][j], 'activedash')):
                    main.markMap((main.x + j - self.CENTER_CELL[0],
                                  main.y + i - self.CENTER_CELL[1]))
                    self.updateMap()
                    requireExitConfirmation(True)
                    main.sound.playSound(main.sound.sounds['Mark Map'])
                    return

    def changeTitle(self, newTitle):
        self.titleLabel['font'] = font6 if len(newTitle) < 21 else font4
        self.titleLabel['text'] = newTitle

    def openFile(self):
        main.sound.playSound(main.sound.sounds['Open Dialog'])
        d = OpenFileDialog(root, "Start Game")
        if not hasattr(d, 'entryValue'):
            window.bottomFrame.bottomLeftFrame.insertOutput(
                "Come on. I promise not to bite.")
            return
        try:
            self.loadFile(d.entryValue)
        except IOError:
            self.createFile(d.entryValue)
        except AttributeError:
            window.bottomFrame.bottomLeftFrame.insertOutput(
                d.entryValue +
                ", some vital information is missing from your file." +
                "\nPerhaps this can be remedied with a conversion.")
        except (EOFError, ValueError, KeyError, IndexError, ImportError):
            window.bottomFrame.bottomLeftFrame.insertOutput(
                d.entryValue +
                ", your file is completely garbled! This is quite unfortunate.")
        except ImportError:
            window.bottomFrame.bottomLeftFrame.insertOutput(
                "I cannot read this file at all! What language is this?")


    def saveFile(self):
        main.sound.playSound(main.sound.sounds['Open Dialog'])
        if tkMessageBox.askokcancel("Save Game", "Do you want to save?",
                                    parent=root):
            main.saveGame()
            requireExitConfirmation(False)

    def loadFile(self, name=None):
        if not name:
            window.bottomFrame.bottomRightFrame.okButton['command'] = \
                window.bottomFrame.bottomRightFrame.clickOkButton
            window.bottomFrame.bottomRightFrame.bindChoices()
            name = main.fileName
        main.loadGame(name)
        self.startGame(name)

    def createFile(self, name):
        main.startNewGame(name)
        self.startGame(name)
        
    def startGame(self, name):
        stateChanged = False
        
        window.bottomFrame.bottomLeftFrame.insertTimestamp(True)
        
        interfaceActions = main.getLoginEvents()
        if interfaceActions is not None:
            updateInterface(interfaceActions)
            stateChanged = True
        
        interfaceActions = main.getInterfaceActions(justFought=True)
        updateInterface(interfaceActions)
        
        self.mapButton['state'] = NORMAL
        self.mapButton.grid()
        if main.character.flags['Config']['Automap On'] != self.showMap.get():
            self.mapButton.invoke()
        self.updateMapVisibility()
        
        if hasattr(main.character, 'specialization'):
            window.topFrame.topLeftFrame.spWord.grid()
            window.topFrame.topLeftFrame.spLabel.grid()
            window.topFrame.topLeftFrame.spBarLabel.grid()
        else:
            window.topFrame.topLeftFrame.spWord.grid_remove()
            window.topFrame.topLeftFrame.spLabel.grid_remove()
            window.topFrame.topLeftFrame.spBarLabel.grid_remove()
        window.bottomFrame.bottomRightFrame.centerButton['state'] = NORMAL
        self.areaButton['command'] = self.saveFile
        self.areaButton.bind_all("<Control-s>", lambda _: self.areaButton.invoke())
        self.areaButton.bind_all("<Control-S>", lambda _: self.areaButton.invoke())
        
        root.title("Toshe's Quest II | "+name)
        
        requireExitConfirmation(stateChanged)
        
class TopRightFrame:
    """Contains frames for other stats, enemy stats and store items

    Only one is displayed at a time.
    """

    def __init__(self, master):
        frameE = Frame(master, width=FRAME_C_WIDTH, height=FRAME_C_HEIGHT,
                       bg=DEFAULT_BG)
        frameE.grid(row=0, column=2)
        frameE.grid_propagate(0)
        self.makeFrameElements(frameE)

    def makeFrameElements(self, master):
        """Create labelframes for other stats, enemy stats and store items.

        Other stats displays: various character information
        Enemy stats displays: enemy name, image, HP
        Store displays: items for sale, selected item stats, buy button
        """        
        self.otherStats = LabelFrame(master, text="Other Stats", font=font3,
                                     width=FRAME_C_WIDTH, height=FRAME_C_HEIGHT,
                                     bg=DEFAULT_BG)
        self.otherStats.grid()
        self.otherStats.grid_propagate(0)
        
        self.strengthLabel = Label(self.otherStats, text="Strength", font=font2,
                                   bg=DEFAULT_BG)
        self.strengthLabel.grid(sticky=W)
        self.strengthValueButton = Button(self.otherStats, text="5", font=font1,
                                          bg=DEFAULT_BG,
                                          disabledforeground=BLACK, relief=FLAT,
                                          state=DISABLED,
                                          command=self.increaseStrength)
        self.strengthValueButton.grid(row=0, column=1, sticky=E)
        self.powerLabel = Label(self.otherStats, text="Base Damage", font=font2,
                                bg=DEFAULT_BG)
        self.powerLabel.grid(row=1, column=3, sticky=W)
        self.powerValueLabel = Label(self.otherStats, text="10", font=font1,
                                bg=DEFAULT_BG)
        self.powerValueLabel.grid(row=1, column=4, sticky=E)
        
        self.dexterityLabel = Label(self.otherStats, text="Dexterity",
                                    font=font2, bg=DEFAULT_BG)
        self.dexterityLabel.grid(row=1, column=0, sticky=W)
        self.dexterityValueButton = Button(self.otherStats, text="5",
                                           font=font1, bg=DEFAULT_BG,
                                           disabledforeground=BLACK,
                                           relief=FLAT, state=DISABLED,
                                           command=self.increaseDexterity)
        self.dexterityValueButton.grid(row=1, column=1, sticky=E)
        self.damageLabel = Label(self.otherStats, text="Avg Damage", font=font2,
                                 bg=DEFAULT_BG)
        self.damageLabel.grid(row=2, column=3, sticky=W)
        self.damageValueLabel = Label(self.otherStats, text="50", font=font1,
                                      bg=DEFAULT_BG)
        self.damageValueLabel.grid(row=2, column=4, sticky=E)
        
        self.wisdomLabel = Label(self.otherStats, text="Wisdom",
                                       font=font2, bg=DEFAULT_BG)
        self.wisdomLabel.grid(row=2, column=0, sticky=W)
        self.wisdomValueButton = Button(self.otherStats, text="5",
                                              font=font1, bg=DEFAULT_BG,
                                              disabledforeground=BLACK,
                                              relief=FLAT, state=DISABLED,
                                              command=self.increaseWisdom)
        self.wisdomValueButton.grid(row=2, column=1, sticky=E)
        self.accuracyLabel = Label(self.otherStats, text="Accuracy", font=font2,
                                   bg=DEFAULT_BG)
        self.accuracyLabel.grid(row=0, column=3, sticky=W)
        self.accuracyValueLabel = Label(self.otherStats, text="85%", font=font1,
                                        bg=DEFAULT_BG)
        self.accuracyValueLabel.grid(row=0, column=4, sticky=E)
        

        self.statPointsLabel = Label(self.otherStats,
                                     text="5\nStat Points",
                                     font=font2, bg=DEFAULT_BG, relief=FLAT)
        self.statPointsLabel.grid(rowspan=2, columnspan=2, padx=6,
                                     sticky=N+S+E+W)
        
        self.critChanceLabel = Label(self.otherStats, text="Crit Chance",
                                     font=font2, bg=DEFAULT_BG)
        self.critChanceLabel.grid(row=3, column=3, sticky=W)
        self.critChanceValueLabel = Label(self.otherStats, text="5%",
                                          font=font1, bg=DEFAULT_BG)
        self.critChanceValueLabel.grid(row=3, column=4, sticky=E)
        
        self.critDamageLabel = Label(self.otherStats, text="Crit Damage",
                                     font=font2, bg=DEFAULT_BG)
        self.critDamageLabel.grid(row=4, column=3, sticky=W)
        self.critDamageValueLabel = Label(self.otherStats, text="2000%",
                                          font=font1, bg=DEFAULT_BG)
        self.critDamageValueLabel.grid(row=4, column=4, sticky=E)

        self.earthLabel = Label(self.otherStats, text="Earth", font=font2,
                                bg=DEFAULT_BG)
        self.earthLabel.grid(row=6, sticky=W)
        self.earthValueLabel = Label(self.otherStats, text="0%", font=font1,
                                     bg=DEFAULT_BG)
        self.earthValueLabel.grid(row=6, column=1, sticky=E)
        self.defenceLabel = Label(self.otherStats, text="Defence", font=font2,
                                  bg=DEFAULT_BG)
        self.defenceLabel.grid(row=6, column=3, sticky=W)
        self.defenceValueLabel = Label(self.otherStats, text="75", font=font1,
                                       bg=DEFAULT_BG)
        self.defenceValueLabel.grid(row=6, column=4, sticky=E)

        self.waterLabel = Label(self.otherStats, text="Water", font=font2,
                                bg=DEFAULT_BG)
        self.waterLabel.grid(sticky=W)
        self.waterValueLabel = Label(self.otherStats, text="5%", font=font1,
                                     bg=DEFAULT_BG)
        self.waterValueLabel.grid(row=7, column=1, sticky=E)
        self.blockChanceLabel = Label(self.otherStats, text="Block Chance",
                                      font=font2, bg=DEFAULT_BG)
        self.blockChanceLabel.grid(row=7, column=3, sticky=W)
        self.blockChanceValueLabel = Label(self.otherStats, text="53%",
                                           font=font1, bg=DEFAULT_BG)
        self.blockChanceValueLabel.grid(row=7, column=4, sticky=E)

        self.fireLabel = Label(self.otherStats, text="Fire", font=font2,
                               bg=DEFAULT_BG)
        self.fireLabel.grid(sticky=W)
        self.fireValueLabel = Label(self.otherStats, text="0%", font=font1,
                                    bg=DEFAULT_BG)
        self.fireValueLabel.grid(row=8, column=1, sticky=E)
        self.eurosLabel = Label(self.otherStats, image=euroImage, text="5",
                                font=font2, bg=DEFAULT_BG, compound=RIGHT)
        self.eurosLabel.grid(row=8, column=3, columnspan=2, sticky=E)


        self.weaponElementLabel = Label(self.otherStats, text="Water Weapon",
                                        font=font2, bg=WATER_COLOR,
                                        relief=GROOVE)
        self.weaponElementLabel.grid(row=9, columnspan=5, sticky=E+W, ipady=3)

        self.potionButton = Button(self.otherStats, image=potionImage,
                                   text="104", font=font2,
                                   fg=WHITE, activeforeground=WHITE,
                                   bg=BUTTON_BG, command=self.usePotion,
                                   compound=CENTER, state=DISABLED)
        self.potionButton.grid(row=10, column=3, columnspan=2, sticky=E)
        self.potionButton.bind_all('p', self.usePotion)
        self.potionButton.bind_all('P', self.usePotion)

        self.vBorderLabel1 = Label(self.otherStats, image=vBorderImage1,
                                  bg=DEFAULT_BG, bd=0)
        self.vBorderLabel1.grid(row=0, column=2, rowspan=5)
        self.vBorderLabel2 = Label(self.otherStats, image=vBorderImage2,
                                  bg=DEFAULT_BG, bd=0)
        self.vBorderLabel2.grid(row=6, column=2, rowspan=3)
        self.hBorderLabel = Label(self.otherStats, image=hBorderImage,
                                 bg=DEFAULT_BG, bd=0)
        self.hBorderLabel.grid(row=5, columnspan=5, pady=8)



        self.enemyStats = LabelFrame(master, text="Enemy", font=font3,
                                     width=FRAME_C_WIDTH, height=FRAME_C_HEIGHT,
                                     bg=DEFAULT_BG)
        self.enemyStats.grid(row=0)
        self.enemyStats.grid_propagate(0)
        self.enemyNameLabel = Label(self.enemyStats, text="Richard Titball",
                                    font=italicFont4, fg=BLACK, bg=DEFAULT_BG)
        self.enemyNameLabel.grid(row=0, column=0, columnspan=2)
        self.enemyLevelLabel = Label(self.enemyStats, text="17", font=font2,
                                     width=2, bg=DEFAULT_BG, relief=RIDGE)
        self.enemyLevelLabel.grid(row=0, column=1, padx=10, pady=10, sticky=E)
        self.enemyImageLabel = Label(self.enemyStats, image=None, bg=BROWN,
                                     relief=RIDGE, bd=4)
        self.enemyImageLabel.grid(columnspan=2, pady=20)
        self.enemyHpBarLabel = Label(self.enemyStats, image=hpBars[20],
                                     bg=DEFAULT_BG, relief=SUNKEN, bd=1)
        self.enemyHpBarLabel.grid(row=3, columnspan=2)
        self.enemyHpWord = Label(self.enemyStats, text="HP",
                            bg=DEFAULT_BG, font=font1, bd=0)
        self.enemyHpWord.grid(row=2, column=0, sticky=W)
        self.enemyHpLabel = Label(self.enemyStats, text="100/100",
                                  bg=DEFAULT_BG, font=font1, bd=0)
        self.enemyHpLabel.grid(row=2, column=1, sticky=E)



        self.store = LabelFrame(master, text="Store", font=font3,
                                width=FRAME_C_WIDTH, height=FRAME_C_HEIGHT,
                                bg=DEFAULT_BG)
        self.store.grid(row=0)
        self.store.grid_propagate(0)

        # Store checkbutton variable
        self.v2 = IntVar()
        self.storeButtons = makeItemButtons(self.store, self.v2, 1)
        self.itemNameLabel = Label(self.store, text="Name", font=font2,
                                   bg=DEFAULT_BG)
        self.itemNameLabel.grid(columnspan=3, sticky=W)
        self.itemCategoryLabel = Label(self.store, text="Category", font=font2,
                                       bg=DEFAULT_BG)
        self.itemCategoryLabel.grid(columnspan=3, sticky=W)
        self.itemValueLabel = Label(self.store, text="X Euros", font=font1,
                                    bg=DEFAULT_BG)
        self.itemValueLabel.grid(columnspan=3, sticky=W)
        self.itemRequirementLabel = Label(self.store, text="Requires X Y",
                                          font=font1, bg=DEFAULT_BG)
        self.itemRequirementLabel.grid(columnspan=3, sticky=W)
        self.itemQualityLabel = Label(self.store,
                                      text="X Power/X Defence", font=font1,
                                      bg=DEFAULT_BG)
        self.itemQualityLabel.grid(columnspan=3, sticky=W)
        self.itemCBRateLabel = Label(self.store, text=
                                     "X% Critical Chance/X% Block Chance",
                                     font=font1, bg=DEFAULT_BG)
        self.itemCBRateLabel.grid(columnspan=3, sticky=W)
        self.itemElementLabel = Label(self.store,
                                      text=
                                      "Imbued with X/Reduces X Damage by Y%",
                                      font=font1, bg=DEFAULT_BG)
        self.itemElementLabel.grid(columnspan=3, sticky=W)
        self.buyButton = Button(self.store, text="Buy", font=font2,
                                fg=BUTTON_FG, bg=BUTTON_BG,
                                command=self.clickBuyButton)
        self.buyButton.grid(columnspan=3, sticky=E+W)

    def increaseStrength(self):
        main.character.strength += 1
        main.character.statPoints -= 1
        main.sound.playSound(main.sound.sounds['Increase Stat'])
        self.updateOtherStats()
        window.topFrame.topLeftFrame.updateInventory()

    def increaseDexterity(self):
        main.character.dexterity += 1
        main.character.statPoints -= 1
        main.sound.playSound(main.sound.sounds['Increase Stat'])
        self.updateOtherStats()
        window.topFrame.topLeftFrame.updateInventory()

    def increaseWisdom(self):
        main.character.wisdom += 1
        main.character.statPoints -= 1
        main.sound.playSound(main.sound.sounds['Increase Stat'])
        self.updateOtherStats()
        window.topFrame.topLeftFrame.updateInventory()

    def usePotion(self, event=None):
        if (self.potionButton['state'] == NORMAL):
            main.character.hp += 50
            main.character.potions -= 1
            message = "You consume a vial full of life fluid."
            window.bottomFrame.bottomLeftFrame.insertOutput(message)
            self.updateOtherStats()
            window.topFrame.topLeftFrame.updateVitalStats()
            main.sound.playSound(main.sound.sounds['Drink'])

    def clickBuyButton(self):
        main.buy(self.v2.get())
        window.topFrame.topLeftFrame.sellButton['state'] = DISABLED
        window.topFrame.topLeftFrame.updateInventory()
        self.buyButton['state'] = DISABLED
        self.updateStore()

    def updateOtherStats(self):
        """Change the Other Stats frame so its values reflect the character's
        current stats.
        """
        c = main.character

        self.strengthValueButton['text'] = c.strength
        self.powerValueLabel['text'] = c.damage
        self.dexterityValueButton['text'] = c.dexterity
        self.damageValueLabel['text'] = int(
            (c.accuracy if c.accuracy < 100 else 100) / 100. *
            (c.damage *
             (((c.cRate if c.cRate < 100 else 100) / 100.) *
              (c.cDamage / 100. - 1) + 1))
            )
        self.wisdomValueButton['text'] = c.wisdom
        if c.accuracy > 100:
            self.accuracyValueLabel['text'] = "100%"
        else:
            self.accuracyValueLabel['text'] = str(c.accuracy) + "%"
        
        if c.equippedWeapon.ELEMENT == "Physical":
            self.weaponElementLabel['bg'] = DEFAULT_BG
            self.weaponElementLabel['relief'] = FLAT
            self.weaponElementLabel['text'] = ""
        else:
            self.weaponElementLabel['bg'] = {
                'Earth': EARTH_COLOR,
                'Water': WATER_COLOR,
                'Fire': FIRE_COLOR
            }[c.equippedWeapon.ELEMENT] if c.equippedWeapon.ELEMENT in (
                "Earth",
                "Water",
                "Fire"
            ) else ENIGMATIC_COLOR
            self.weaponElementLabel['relief'] = GROOVE
            self.weaponElementLabel['text'] = (c.equippedWeapon.ELEMENT
                                               +" Weapon")
        self.critChanceValueLabel['text'] = str(c.cRate) + "%"
        self.critDamageValueLabel['text'] = str(c.cDamage) + "%"
        self.earthValueLabel['text'] = str(c.earthReduction) + "%"
        self.defenceValueLabel['text'] = str(c.defence)
        self.waterValueLabel['text'] = str(c.waterReduction) + "%"
        self.blockChanceValueLabel['text'] = str(c.bRate) + "%"
        self.fireValueLabel['text'] = str(c.fireReduction) + "%"
        self.eurosLabel['text'] = c.euros
        pluralOrNah = ("" if c.statPoints <= 1 else "s")
        if c.statPoints > 0:
            self.statPointsLabel['relief'] = RIDGE
            self.statPointsLabel['text'] = (str(c.statPoints) +
                                            "\nStat Point%s"
                                            % pluralOrNah)
            self.strengthValueButton.config(state=NORMAL, relief=RAISED,
                                            bg=BUTTON_BG, fg=BUTTON_FG)
            self.dexterityValueButton.config(state=NORMAL, relief=RAISED,
                                             bg=BUTTON_BG, fg=BUTTON_FG)
            self.wisdomValueButton.config(state=NORMAL, relief=RAISED,
                                          bg=BUTTON_BG, fg=BUTTON_FG)
        else:
            self.statPointsLabel['relief'] = FLAT
            self.statPointsLabel['text'] = ""
            self.strengthValueButton.config(state=DISABLED, relief=FLAT,
                                            bg=DEFAULT_BG, fg=BLACK)
            self.dexterityValueButton.config(state=DISABLED, relief=FLAT,
                                             bg=DEFAULT_BG, fg=BLACK)
            self.wisdomValueButton.config(state=DISABLED, relief=FLAT,
                                          bg=DEFAULT_BG, fg=BLACK)
        
        state = NORMAL if c.potions > 0 and (
            main.view in ("travel", "inventory")) else DISABLED
        font = font3 if c.potions < 100 else font1
        text = c.potions if c.potions > 0 else " "
        self.potionButton.config(state=state, font=font, text=text)

    def updateEnemyStats(self):
        """Show the level, name, hp bar, and hp of the current enemy in the
        enemy frame.
        """
        e = main.battle.enemy
        
        self.enemyLevelLabel['text'] = e.LEVEL
        self.enemyNameLabel['text'] = e.NAME
        self.enemyImageLabel['image'] = enemyImages[e.IDENTIFIER]
        if e.hp <= 0:
            self.enemyHpBarLabel['image'] = hpBars[0]
        elif float(e.hp) < float(e.maxHp) / (NUMBER_OF_BARS - 1):
            self.enemyHpBarLabel['image'] = hpBars[1]
        else:
            self.enemyHpBarLabel['image'] = hpBars[int(float(e.hp) / e.maxHp *
                                                       (NUMBER_OF_BARS - 1))]
        self.enemyHpBarLabel['text'] = "%d/%d" % (e.hp, e.maxHp)
        self.enemyHpLabel['text'] = "%d/%d" % (e.hp, e.maxHp)

    def updateStore(self):
        """Change images in the Store frame to match current store items."""
        clearItemStats(self, store=True)
        self.v2.set(-1)
        for i in range(0, 3):
            for j in range(0, 3):
                if not main.store[i*3+j]:
                    self.storeButtons[i*3+j].config(image=noItemImage,
                                                    state=DISABLED)
                else:
                    itemImage = itemImages[main.store[i*3+j].IMAGE_NAME]
                    self.storeButtons[i*3+j].config(image=itemImage,
                                                    state=NORMAL)


class BottomLeftFrame:
    """Contains an output box with scrollbar."""

    def __init__(self, master):
        frameF = Frame(master, bg=DEFAULT_BG)
        frameF.grid()
        self.makeFrameElements(frameF)

    def makeFrameElements(self, master):
        self.outputBox = Text(master, font=font2, width=68, height=12,
                              wrap=WORD, bg=TEXTBOX_BG, relief=GROOVE)
        self.outputBox.grid()
        self.outputBox.tag_config("italicize", font=italicFont2)
        self.outputBox.tag_config("grey", foreground=GREY)
        self.outputBox.tag_config("highlight", foreground=BLACK)
        self.outputBox.insert(END,
                              ("Welcome. Click on me to "+
                               "embark on your quest."), "italicize")
        self.outputBox['state'] = DISABLED
        
        self.outputScrollbar = Scrollbar(master, bg=DEFAULT_BG,
                                         command=self.outputBox.yview)
        self.outputScrollbar.grid(row=0, column=1, sticky=N+S)
        
        self.outputBox.config(yscrollcommand=self.outputScrollbar.set)

        self.borderButton = Button(master, image=waveBorderImage, bg=DEFAULT_BG,
                                   relief=FLAT, bd=0,
                                   command=self.clearOutputBox)
        self.borderButton.grid(row=0, column=2)
        
    def insertTimestamp(self, addSpacing=False):
        self.outputBox['state'] = NORMAL
        timestamp = "{dt:%I}:{dt.minute} {dt:%p} - {greeting}".format(
            dt = datetime.now(),
            greeting = random.choice([
                "Let the quest begin.",
                "Brace yourself.",
                "Smell those scents of adventure."
            ]))
        self.outputBox.insert(END,
                              "%s❧ %s" % ("\n\n" if addSpacing else "", timestamp),
                              ("grey", "highlight"))
        self.outputBox.yview(END)
        self.outputBox['state'] = DISABLED

    def clearOutputBox(self):
        self.outputBox['state'] = NORMAL
        self.outputBox.delete(0.0, END)
        self.outputBox['state'] = DISABLED
        self.insertTimestamp()

    def insertOutput(self, text, formatTag=None):
        """Add a string of text to the output box."""
        self.outputBox['state'] = NORMAL
        self.outputBox.insert(END, "\n"+text, (formatTag, "grey", "highlight"))
        self.outputBox.yview(END)
        self.outputBox['state'] = DISABLED

    def unhighlightOutputBox(self):
        """Change the output box contents to its original background colour."""
        self.outputBox['state'] = NORMAL
        self.outputBox.tag_remove("highlight", 1.0, END)
        self.outputBox['state'] = DISABLED


class BottomRightFrame:
    """Contains a menu box, a select/OK button, navigation arrows and a button
    to view the inventory.
    """

    def __init__(self, master):
        frameG = Frame(master, bg=DEFAULT_BG)
        frameG.grid(row=0, column=1)
        self.makeFrameElements(frameG)
        self.lastOkButtonState = None
        self.lastUpButtonState = None
        self.lastLeftButtonState = None
        self.lastRightButtonState = None
        self.lastDownButtonState = None

    def makeFrameElements(self, master):
        self.upButton = Button(master, image=upImage, relief=FLAT, bd=0,
                               bg=DEFAULT_BG, activebackground=DEFAULT_BG,
                               state=DISABLED, command=self.clickUpButton)
        self.upButton.bind_all('w', self.clickUpButton)
        self.upButton.bind_all('W', self.clickUpButton)
        self.upButton.grid(column=1)
        self.leftButton = Button(master, image=leftImage, relief=FLAT, bd=0,
                                 bg=DEFAULT_BG, activebackground=DEFAULT_BG,
                                 state=DISABLED, command=self.clickLeftButton)
        self.leftButton.bind_all('a', self.clickLeftButton)
        self.leftButton.bind_all('A', self.clickLeftButton)
        self.leftButton.grid(column=0, sticky=E)
        self.centerButton = Button(master, image=inventoryImage, relief=FLAT,
                                   bd=0, bg=DEFAULT_BG,
                                   activebackground=DEFAULT_BG, state=DISABLED,
                                   command=self.clickInventoryButton)
        self.centerButton.grid(row=1, column=1, pady=0)
        self.rightButton = Button(master, image=rightImage, relief=FLAT, bd=0,
                                  bg=DEFAULT_BG, activebackground=DEFAULT_BG,
                                  state=DISABLED, command=self.clickRightButton)
        self.rightButton.bind_all('d', self.clickRightButton)
        self.rightButton.bind_all('D', self.clickRightButton)
        self.rightButton.grid(row=1, column=2, sticky=W)
        self.downButton = Button(master, image=downImage, relief=FLAT, bd=0,
                                 bg=DEFAULT_BG, activebackground=DEFAULT_BG,
                                 state=DISABLED, command=self.clickDownButton)
        self.downButton.bind_all('s', self.clickDownButton)
        self.downButton.bind_all('S', self.clickDownButton)
        self.downButton.grid(column=1)
        self.defendButton = Button(master, image=defendImage, relief=FLAT,
                                   bd=0, bg=DEFAULT_BG,
                                   activebackground=DEFAULT_BG, state=DISABLED,
                                   command=self.clickDefendButton)
        self.defendButton.bind_all('j', self.clickDefendButton)
        self.defendButton.bind_all('J', self.clickDefendButton)
        self.defendButton.grid(row=1, column=0, sticky=E)
        self.defendButton.grid_remove()
        self.attackButton = Button(master, image=attackImage, relief=FLAT,
                                   bd=0, bg=DEFAULT_BG,
                                   activebackground=DEFAULT_BG, state=DISABLED,
                                   command=self.clickAttackButton)
        self.attackButton.bind_all('k', self.clickAttackButton)
        self.attackButton.bind_all('K', self.clickAttackButton)
        self.attackButton.grid(row=0, column=1)
        self.attackButton.grid_remove()
        self.fleeButton = Button(master, image=fleeImage, relief=FLAT,
                                 bd=0, bg=DEFAULT_BG,
                                 activebackground=DEFAULT_BG, state=DISABLED,
                                 command=self.clickFleeButton)
        self.fleeButton.bind_all('l', self.clickFleeButton)
        self.fleeButton.bind_all('L', self.clickFleeButton)
        self.fleeButton.grid(row=1, column=2, sticky=W)
        self.fleeButton.grid_remove()
        
        self.menuBox = Listbox(master, font=font2, width=40, height=4,
                               fg=BLACK, bg=TEXTBOX_BG, relief=GROOVE,
                               selectmode=SINGLE, exportselection=0)
        self.bindChoices()
        self.enableMenuBox()
        self.menuBox.grid(columnspan=3)

        self.okButton = Button(master, text="Select", font=font2,
                               fg=BUTTON_FG, bg=BUTTON_BG, state=DISABLED,
                               command=self.clickOkButton)
        self.okButton.grid(columnspan=3, sticky=E+W)
        self.skillButton = Button(master, text="Use Skill", font=font2,
                                  fg=BUTTON_FG, bg=BUTTON_BG, state=DISABLED,
                                  command=self.clickSkillButton)
        self.skillButton.grid(row=4, columnspan=3, sticky=E+W)
        self.skillButton.grid_remove()
        
    def move(self, arrowDirection, movementDirection):
        interfaceActions = main.move(arrowDirection)
        interfaceActions['map'] = True
        main.sound.playSound(main.sound.sounds['Move'])
        updateInterface(interfaceActions)

    def clickUpButton(self, event=None):
        if self.upButton['state'] == NORMAL:
            self.move("up", "forward")

    def clickLeftButton(self, event=None):
        if self.leftButton['state'] == NORMAL:
            self.move("left", "left")
            
    def clickRightButton(self, event=None):
        if self.rightButton['state'] == NORMAL:
            self.move("right", "right")

    def clickDownButton(self, event=None):
        if self.downButton['state'] == NORMAL:
            self.move("down", "backward")

    def clickInventoryButton(self, event=None):
        if self.centerButton['state'] == NORMAL:
            # Save OK Button state for when the Back Button is pressed
            self.lastOkButtonState = self.okButton['state']
            
            self.centerButton.config(image=backImage,
                                     command=self.clickBackButton)
            self.centerButton.bind_all('i', self.clickBackButton)
            self.centerButton.bind_all('I', self.clickBackButton)
            self.enableDirectionButtons([])
            self.attackButton['state'] = DISABLED
            self.defendButton['state'] = DISABLED
            self.fleeButton['state'] = DISABLED
            self.okButton['state'] = DISABLED
            self.disableMenuBox()
            enableInventoryView()
            main.sound.playSound(main.sound.sounds['Inventory'])

    def clickBackButton(self, event=None):
        if self.centerButton['state'] == NORMAL:
            self.centerButton.config(image=inventoryImage,
                                     command=self.clickInventoryButton)
            self.centerButton.bind_all('i', self.clickInventoryButton)
            self.centerButton.bind_all('I', self.clickInventoryButton)
            self.enableDirectionButtons(main.enabledDirections)
            self.enableMenuBox()
            self.okButton['state'] = self.lastOkButtonState
            views[main.view]()
            main.sound.playSound(main.sound.sounds['Return'])

    def clickCancelDropButton(self):
        self.centerButton.config(image=inventoryImage,
                                 command=self.clickInventoryButton)
        self.centerButton.bind_all('i', self.clickInventoryButton)
        self.centerButton.bind_all('I', self.clickInventoryButton)
        self.enableDirectionButtons(main.enabledDirections)
        self.upButton.grid_remove()
        self.leftButton.grid_remove()
        self.rightButton.grid_remove()
        self.downButton.grid_remove()
        self.enableMenuBox()
        views[main.view]()

    def clickCancelForgetButton(self):
        self.centerButton.config(image=inventoryImage,
                                 command=self.clickInventoryButton)  
        self.okButton['command'] = self.clickOkButton
        self.okButton['state'] = DISABLED
        self.upButton['state'] = self.lastUpButtonState
        self.leftButton['state'] = self.lastLeftButtonState
        self.rightButton['state'] = self.lastRightButtonState
        self.downButton['state'] = self.lastDownButtonState
        self.modifyMenu(self.tempMenu)
        self.bindChoices()
        views[main.view]()

    def clickAttackButton(self, event=None):
        if self.attackButton['state'] == NORMAL:
            interfaceActions = main.attack()
            updateInterface(interfaceActions)

    def clickDefendButton(self, event=None):
        if self.defendButton['state'] == NORMAL:
            interfaceActions = main.defend()
            updateInterface(interfaceActions)

    def clickFleeButton(self, event=None):
        if self.fleeButton['state'] == NORMAL:
            interfaceActions = main.flee()
            updateInterface(interfaceActions)

    def clickOkButton(self):
        if self.okButton['state'] == NORMAL:
            selection = int(self.menuBox.curselection()[0])
            interfaceActions = main.select(selection)
            interfaceActions['map'] = True
            updateInterface(interfaceActions)

    def clickSkillButton(self):
        if self.skillButton['state'] == NORMAL:
            selection = int(self.menuBox.curselection()[0])
            interfaceActions = main.useSkill(main.character.skills[selection])
            updateInterface(interfaceActions)

    def clickForgetButton(self):
        if self.okButton['state'] == NORMAL:
            selection = int(self.menuBox.curselection()[0])
            main.character.forgetSkill(main.character.skills[selection])
            main.character.learnSkill(main.tempSkill)
            window.gridnewSkillFrame(main.tempSkill.NAME)
            main.sound.playSound(main.sound.sounds['New Skill'])
            main.character.euros -= main.tempCost
            self.clickCancelForgetButton()

    def enableMenuBox(self):
        self.menuBox.bind('<<ListboxSelect>>', self.enableOkButton)
        self.menuBox.bind('<<ListboxSelect>>', self.enableSkillButton, 1)
        self.menuBox['state'] = NORMAL

    def disableMenuBox(self):
        self.menuBox.unbind('<<ListboxSelect>>')
        self.menuBox['state'] = DISABLED

    def bindSkills(self):
        self.menuBox.bind_all('1', self.selectSkill)
        self.menuBox.bind_all('2', self.selectSkill)
        self.menuBox.bind_all('3', self.selectSkill)
        self.menuBox.bind_all('4', self.selectSkill)

    def bindChoices(self):
        self.menuBox.bind_all('1', self.selectChoice)
        self.menuBox.bind_all('2', self.selectChoice)
        self.menuBox.bind_all('3', self.selectChoice)
        self.menuBox.bind_all('4', self.selectChoice)

    def selectChoice(self, event=None):
        if self.menuBox['state'] != DISABLED:
            tempSelection = self.menuBox.curselection()
            self.menuBox.selection_clear(0, 'end')
            self.menuBox.selection_set(int(event.char)-1)
            if self.menuSelectionIsValid():
                self.okButton['state'] = NORMAL
                self.clickOkButton()
            elif bool(tempSelection):
                self.menuBox.selection_set(int(tempSelection[0]))

    def selectSkill(self, event=None):
        if self.menuBox['state'] != DISABLED:
            tempSelection = self.menuBox.curselection()
            self.menuBox.selection_clear(0, 'end')
            self.menuBox.selection_set(int(event.char)-1)
            if self.menuSelectionIsValid():
                self.skillButton['state'] = NORMAL
                self.clickSkillButton()
            elif bool(tempSelection):
                self.menuBox.selection_set(int(tempSelection[0]))

    def menuSelectionIsValid(self):
        return bool(self.menuBox.curselection())

    def endBattle(self, event=None):
        if self.menuBox['state'] != DISABLED:
            bottomFrame = window.bottomFrame.bottomRightFrame
            bottomFrame.bindChoices()
            bottomFrame.okButton['command'] = bottomFrame.clickOkButton
            interfaceActions = main.getInterfaceActions(justFought=True)
            if ('text' in interfaceActions and
                interfaceActions['text'] is not None):
                interfaceActions['text'] = "\n"+interfaceActions['text'].strip()
            interfaceActions['map'] = True
            updateInterface(interfaceActions)
            main.sound.playSound(main.sound.sounds['Select Option'])

    def enableDirectionButtons(self, enabledDirections):
        """Set the state of specified direction buttons to NORMAL."""        
        if "up" in enabledDirections:
            self.upButton['state'] = NORMAL
        else:
            self.upButton['state'] = DISABLED
        if "left" in enabledDirections:
            self.leftButton['state'] = NORMAL
        else:
            self.leftButton['state'] = DISABLED
        if "right" in enabledDirections:
            self.rightButton['state'] = NORMAL
        else:
            self.rightButton['state'] = DISABLED
        if "down" in enabledDirections:
            self.downButton['state'] = NORMAL
        else:
            self.downButton['state'] = DISABLED

    def enableOkButton(self, event=None):
        if self.menuSelectionIsValid():
            self.okButton['state'] = NORMAL

    def enableSkillButton(self, event=None):
        if self.menuSelectionIsValid():
            self.skillButton['state'] = NORMAL

    def modifyMenu(self, menuItems):
        """Remove all items from the menu box, then add new ones in sequence."""
        self.menuBox.delete(0, END)
        if menuItems:
            for i in menuItems:
                self.menuBox.insert(END, i)


def makeItemButtons(master, var, inStore):
    """Create 9 buttons to represent either inventory or store items.

    inStore indicates that the buttons are being made in the store frame if its
    value is 1.
    """
    itemButtons = []
    commands = [displayItemStats, displayStoreItemStats]
    for i in range(0, 3):   # Item radiobutton values range from 0 to 8
        for j in range(0, 3):
            itemButton = Radiobutton(master, image=defaultImage,
                                     variable=var, value=i*3+j, width=64,
                                     height=64, bg=BLACK, indicatoron=0, bd=4,
                                     command=commands[inStore])
            itemButton.grid(row=i, column=j)
            itemButtons.append(itemButton)
    return itemButtons


def displayItemStats():
    """Display the stats of the selected item in the Inventory frame."""
    frame = window.topFrame.topLeftFrame
    item = main.character.items[frame.v1.get()]
    
    frame.itemNameLabel.config(text=item.NAME, font=italicFont2)
    
    frame.itemCategoryLabel['text'] = item.CATEGORY
    
    frame.itemValueLabel['text'] = "Worth "+str(item.SELL_PRICE)+" Euros"
    
    if item.CATEGORY == "Miscellaneous":
        frame.itemRequirementLabel['font'] = italicFont1
        if "*" not in item.INFORMATION:
            frame.itemRequirementLabel['text'] = item.INFORMATION
        elif "*" in item.INFORMATION:
            frame.itemRequirementLabel['text'] = item.INFORMATION.split("*")[0]
    else:
        frame.itemRequirementLabel['font'] = font1
        frame.itemRequirementLabel['text'] = ("Requires",
                                              item.REQUIREMENT_VALUE,
                                              item.REQUIREMENT_TYPE)

    frame.itemQualityLabel['font'] = font1
    if item.CATEGORY == "Armour" or item.CATEGORY == "Shield":
        frame.itemQualityLabel['text'] = item.DEFENCE, "Defence"
    elif item.CATEGORY == "Miscellaneous" and "*" not in item.INFORMATION:
        frame.itemQualityLabel['text'] = ""
    elif item.CATEGORY == "Miscellaneous" and "*" in item.INFORMATION:
        frame.itemQualityLabel['font'] = italicFont1
        frame.itemQualityLabel['text'] = item.INFORMATION.split("*")[1]
    else:
        frame.itemQualityLabel['text'] = item.POWER, "Power"
        
    if item.CATEGORY == "Shield":
        frame.itemCBRateLabel['text'] = str(item.B_RATE)+"% Block Chance"
    elif item.CATEGORY in ("Armour", "Miscellaneous"):
        frame.itemCBRateLabel['text'] = ""
    else:
        frame.itemCBRateLabel['text'] = str(item.C_RATE)+"% Critical Chance"
        
    if ((item.CATEGORY == "Shield" or item.CATEGORY == "Armour") and
        item.REDUCTION != 0):
        frame.itemElementLabel['text'] = ("Reduces", item.ELEMENT, "Damage",
                                          "by",
                                          str(item.REDUCTION)+str("%"))
    elif (item.CATEGORY != "Miscellaneous" and
          item.CATEGORY != "Shield" and
          item.CATEGORY != "Armour" and
          item.ELEMENT != "Physical"):
        frame.itemElementLabel['text'] = ("Item imbued with "+
                                          str(item.ELEMENT))
    else:
        frame.itemElementLabel['text'] = ""

    if ((item.CATEGORY == "Bow" and
         main.character.equippedShield.NAME != "Nothing") or
        (item.CATEGORY == "Shield" and
         main.character.equippedWeapon.CATEGORY == "Bow")):
        frame.itemCategoryLabel['fg'] = RED
    else:
        frame.itemCategoryLabel['fg'] = BLACK
        
    if (item.CATEGORY == "Miscellaneous" or
        (item.REQUIREMENT_TYPE == "Strength" and
         main.character.strength >= item.REQUIREMENT_VALUE) or
        (item.REQUIREMENT_TYPE == "Dexterity" and
         main.character.dexterity >= item.REQUIREMENT_VALUE) or
        (item.REQUIREMENT_TYPE == "Wisdom" and
         main.character.wisdom >= item.REQUIREMENT_VALUE)):
        frame.itemRequirementLabel['fg'] = BLACK
    else:
        frame.itemRequirementLabel['fg'] = RED

    if frame.v1.get() in main.character.equippedItemIndices.values():
        frame.equipButton['text'] = "Unequip"
        frame.sellButton['state'] = DISABLED
    else:
        frame.equipButton['text'] = "Equip"
        frame.sellButton['state'] = NORMAL

    if (item.CATEGORY == "Miscellaneous" or
        (item.REQUIREMENT_TYPE == "Strength" and
         main.character.strength < item.REQUIREMENT_VALUE) or
        (item.REQUIREMENT_TYPE == "Dexterity" and
         main.character.dexterity < item.REQUIREMENT_VALUE) or
        (item.REQUIREMENT_TYPE == "Wisdom" and
         main.character.wisdom < item.REQUIREMENT_VALUE) or
        (item.CATEGORY == "Bow" and
         main.character.equippedShield.NAME != "Nothing") or
        (item.CATEGORY == "Shield" and
         main.character.equippedWeapon.CATEGORY == "Bow")):
        frame.equipButton['state'] = DISABLED
    else:
        frame.equipButton['state'] = NORMAL

    frame.dropButton['state'] = NORMAL

    main.sound.playSound(main.sound.sounds['Select Item'])


def displayStoreItemStats():
    """Display the stats of the selected item in the Store frame."""
    frame = window.topFrame.topRightFrame
    item = main.store[frame.v2.get()]

    frame.itemNameLabel.config(text=item.NAME, font=italicFont2)
    
    frame.itemCategoryLabel['text'] = item.CATEGORY
    
    frame.itemValueLabel['text'] = "%d / %d Euros" % (item.PRICE,
                                                      main.character.euros)
    
    if item.CATEGORY == "Miscellaneous" and "*" not in item.INFORMATION:
        frame.itemRequirementLabel['text'] = item.INFORMATION
    elif item.CATEGORY == "Miscellaneous" and "*" in item.INFORMATION:
        frame.itemRequirementLabel['text'] = item.INFORMATION.split("*")[0]
    else:
        frame.itemRequirementLabel['text'] = ("Requires",
                                              item.REQUIREMENT_VALUE,
                                              item.REQUIREMENT_TYPE)
    
    if item.CATEGORY == "Armour" or item.CATEGORY == "Shield":
        frame.itemQualityLabel['text'] = item.DEFENCE, "Defence"
    elif item.CATEGORY == "Miscellaneous" and "*" not in item.INFORMATION:
        frame.itemQualityLabel['text'] = ""
    elif item.CATEGORY == "Miscellaneous" and "*" in item.INFORMATION:        
        frame.itemQualityLabel['text'] = item.INFORMATION.split("*")[1]
    else:
        frame.itemQualityLabel['text'] = item.POWER, "Power"
        
    if item.CATEGORY == "Shield":
        frame.itemCBRateLabel['text'] = str(item.B_RATE)+"% Block Chance"
    elif item.CATEGORY in ("Armour", "Miscellaneous"):
        frame.itemCBRateLabel['text'] = ""
    else:
        frame.itemCBRateLabel['text'] = str(item.C_RATE)+"% Critical Chance"
        
    if ((item.CATEGORY == "Shield" or item.CATEGORY == "Armour") and
        item.REDUCTION != 0):
        frame.itemElementLabel['text'] = ("Reduces", item.ELEMENT, "Damage",
                                          "by",
                                          str(item.REDUCTION)+str("%"))
    elif (item.CATEGORY != "Miscellaneous" and
          item.CATEGORY != "Shield" and
          item.CATEGORY != "Armour" and
          item.ELEMENT != "Physical"):
        frame.itemElementLabel['text'] = ("Item imbued with "+
                                          str(item.ELEMENT))
    else:
        frame.itemElementLabel['text'] = ""

    if ((item.CATEGORY == "Bow" and
         main.character.equippedShield.NAME != "Nothing") or
        (item.CATEGORY == "Shield" and
         main.character.equippedWeapon.CATEGORY == "Bow")):
        frame.itemCategoryLabel['fg'] = RED
    else:
        frame.itemCategoryLabel['fg'] = BLACK

    if main.character.euros < item.PRICE:
        frame.itemValueLabel['fg'] = RED
    else:
        frame.itemValueLabel['fg'] = BLACK
            
    if (item.CATEGORY == "Miscellaneous" or
        (item.REQUIREMENT_TYPE == "Strength" and
         main.character.strength >= item.REQUIREMENT_VALUE) or
        (item.REQUIREMENT_TYPE == "Dexterity" and
         main.character.dexterity >= item.REQUIREMENT_VALUE) or
        (item.REQUIREMENT_TYPE == "Wisdom" and
         main.character.wisdom >= item.REQUIREMENT_VALUE)):
        frame.itemRequirementLabel['fg'] = BLACK
    else:
        frame.itemRequirementLabel['fg'] = RED

    if main.character.euros < item.PRICE or not main.character.hasRoom():
        frame.buyButton['state'] = DISABLED
    else:
        frame.buyButton['state'] = NORMAL

    main.sound.playSound(main.sound.sounds['Select Item'])


def clearItemStats(frame, store):
    frame.itemNameLabel.config(text="Select an item.", font=italicFont2)
    if main.character.hasNoItems() and not store:
        frame.itemNameLabel.config(text="Your inventory is empty.",
                                   font=italicFont2)
    frame.itemCategoryLabel['text'] = ""
    frame.itemValueLabel['text'] = ""
    frame.itemRequirementLabel['text'] = ""
    frame.itemQualityLabel['text'] = ""
    frame.itemCBRateLabel['text'] = ""
    frame.itemElementLabel['text'] = ""


def flash():
    frame = window.topFrame.topCenterFrame
    if frame.showMap.get():
        frame.map.grid_remove()
        frame.areaButton.grid()
        root.update()
    for i in range(0, 5):
        frame.areaButton.flash()
    if frame.showMap.get():
        frame.areaButton.grid_remove()
        frame.map.grid()


def updateInterface(updates):
    """Update the interface to reflect current game events.

    actions is a dictionary that may contain updates to the textbox, menu,
    center image, or current view.
    """
        
    bottomRightFrame = window.bottomFrame.bottomRightFrame
    topRightFrame = window.topFrame.topRightFrame
    topCenterFrame = window.topFrame.topCenterFrame
    bottomLeftFrame = window.bottomFrame.bottomLeftFrame

    # Flash must occur before battle view is shown and area button is disabled
    if ('flash' in updates):
        flash()
        
    if ('image index' in updates) and (updates['image index'] is not None):
        areaName = main.currentArea.name
        if len(areaImages[areaName]) == 0:
            def incrementProgress(complete=False):
                global loadProgress
                if complete:
                    loadProgress = FULL_PROGRESS
                else:
                    loadProgress += float(FULL_PROGRESS) / worstCaseAssetCount
                root.update()
            enableLoadingView()
            updateLoadingScreen(displayLoadingScreen())
            worstCaseAssetCount = 99
            for i in range(0, worstCaseAssetCount):
                try:
                    areaImages[areaName].append(PhotoImage(
                        file="images\\areas\\"+areaName+"\\"+str(i)+".gif"
                    ))
                    incrementProgress()
                except TclError:
                    incrementProgress(True)
                    break
            window.bottomFrame.bottomRightFrame.bindChoices()
            window.gameFrame.grid()
        topCenterFrame.areaButton['image'] =\
            areaImages[areaName][updates['image index']]

    bottomLeftFrame.unhighlightOutputBox()
    topCenterFrame.changeTitle(main.currentArea.name)
    views[updates['view']]()
            
    while main.character.hasLeveledUp():
        if not updates['text']:
            updates['text'] = ""
        updates['text'] += "\nToshe has reached level "+str(
            main.character.level)+"!"
        window.gridLevelUpFrame()
        window.levelUpLabel['text'] = "LEVEL %d!" % main.character.level
        main.sound.playSound(main.sound.sounds['Level Up'])

    if hasattr(main.character, 'specialization'):
        while main.character.hasSpecializedUp():
            if not updates['text']:
                updates['text'] = ""
            updates['text'] += "\nToshe is now a %s rank %s!" % (
                main.character.specialization, main.character.ub205e2nmzfwi)
            window.gridPowerUpFrame()

    for mercenary in main.character.mercenaries:
        while mercenary.hasLeveledUp():
            if not updates['text']:
                updates['text'] = ""
            updates['text'] += "\n%s has reached level %s!" % (mercenary.NAME,
                                                               mercenary.level)
            window.gridMercenaryUpFrame(mercenary.NAME)
            main.sound.playSound(main.sound.sounds['Mercenary Up'])
            
    if ('game over' == updates['view']):
        if not updates['text']:
            updates['text'] = ""
        updates['enabled directions'] = []
        updates['text'] += ("\nToshe has died.\nToshe's quest ends here.")
        updates['menu'] = ["Exit."]
        updates['italic text'] = None
        updates['image index'] = None
    if ('enabled directions' in updates) and (updates['enabled directions']
                                              is not None):
        bottomRightFrame.enableDirectionButtons(
            updates['enabled directions'])
    if ('menu' in updates) and (updates['menu'] is not None):
        if len(updates['menu']) > 0:
            main.sound.playSound(main.sound.sounds['Menu'])
        bottomRightFrame.modifyMenu(updates['menu'])
        bottomRightFrame.okButton['state'] = DISABLED
    if ('overloaded' in updates) and (updates['overloaded'] == "items"):
        enableDropItemView()
    elif ('overloaded' in updates) and (updates['overloaded'] == "skills"):
        enableForgetSkillView()
    if 'new skill' in updates:
        window.gridnewSkillFrame(updates['skill'])
    if ('item' in updates) and (updates['item'] is not None):
        window.gridLootFrame()
        main.sound.playSound(main.sound.sounds['Get Item'])
    if 'save' in updates and updates['save'] is not None:
        main.saveGame()
        if not updates['text']:
            updates['text'] = ""
        updates['text'] += ("\nGame saved.")
    if ('text' in updates) and (updates['text'] is not None):
        if 'format text' in updates:
            bottomLeftFrame.insertOutput(updates['text'],
                                         updates['format text'])
        else:
            bottomLeftFrame.insertOutput(updates['text'])
    if ('italic text' in updates) and (updates['italic text'] is not None):
        bottomLeftFrame.insertOutput(updates['italic text'], "italicize")
    if ('map' in updates) and topCenterFrame.showMap.get():
        topCenterFrame.updateMap()
    topRightFrame.updateOtherStats()
    requireExitConfirmation(True)
        

def enableTravelView():
    window.topFrame.topCenterFrame.areaButton['state'] = NORMAL
    leftFrame = window.topFrame.topLeftFrame
    rightFrame = window.topFrame.topRightFrame
    leftFrame.vitalStats.grid()
    leftFrame.inventory.grid_remove()
    rightFrame.otherStats.grid()
    rightFrame.enemyStats.grid_remove()
    rightFrame.store.grid_remove()
    leftFrame.updateVitalStats()

    bottomFrame = window.bottomFrame.bottomRightFrame
    bottomFrame.centerButton['state'] = NORMAL
    bottomFrame.upButton.grid()
    bottomFrame.leftButton.grid()
    bottomFrame.rightButton.grid()
    bottomFrame.downButton.grid()
    bottomFrame.centerButton.grid(pady=0)
    bottomFrame.centerButton.bind_all('i', bottomFrame.clickInventoryButton)
    bottomFrame.centerButton.bind_all('I', bottomFrame.clickInventoryButton)
    bottomFrame.okButton.grid()
    bottomFrame.attackButton.grid_remove()
    bottomFrame.defendButton.grid_remove()
    bottomFrame.fleeButton.grid_remove()
    bottomFrame.skillButton.grid_remove()


def enableBattleView():
    window.topFrame.topCenterFrame.areaButton['state'] = DISABLED
    leftFrame = window.topFrame.topLeftFrame
    rightFrame = window.topFrame.topRightFrame
    leftFrame.vitalStats.grid()
    leftFrame.inventory.grid_remove()
    rightFrame.otherStats.grid_remove()
    rightFrame.enemyStats.grid()
    rightFrame.store.grid_remove()
    leftFrame.updateVitalStats()
    rightFrame.updateEnemyStats()

    bottomFrame = window.bottomFrame.bottomRightFrame
    bottomFrame.upButton['state'] = DISABLED
    bottomFrame.leftButton['state'] = DISABLED
    bottomFrame.rightButton['state'] = DISABLED
    bottomFrame.downButton['state'] = DISABLED
    bottomFrame.okButton['state'] = DISABLED
    bottomFrame.upButton.grid_remove()
    bottomFrame.leftButton.grid_remove()
    bottomFrame.rightButton.grid_remove()
    bottomFrame.downButton.grid_remove()
    bottomFrame.okButton.grid_remove()
    bottomFrame.centerButton['state'] = NORMAL
    bottomFrame.attackButton['state'] = NORMAL
    bottomFrame.defendButton['state'] = NORMAL
    bottomFrame.fleeButton['state'] = NORMAL
    bottomFrame.centerButton.grid(pady=(0, 34))
    bottomFrame.attackButton.grid()
    bottomFrame.defendButton.grid()
    bottomFrame.fleeButton.grid()
    bottomFrame.skillButton.grid()
    
    bottomFrame.bindSkills()
    
    skills = []
    bottomFrame.skillButton['state'] = DISABLED
    for skill in main.character.skills:
        skills.append(skill.NAME)
    bottomFrame.modifyMenu(skills)


def enableBattleOverView():
    enableBattleView()
    frame = window.bottomFrame.bottomRightFrame
    frame.centerButton['state'] = DISABLED
    frame.attackButton['state'] = DISABLED
    frame.defendButton['state'] = DISABLED
    frame.fleeButton['state'] = DISABLED
    frame.skillButton['state'] = DISABLED
    frame.skillButton.grid_remove()
    frame.menuBox.bind_all('1', frame.endBattle)
    frame.modifyMenu(["Proceed."])
    frame.okButton.grid()
    frame.okButton['state'] = DISABLED
    frame.okButton['command'] = frame.endBattle


def enableGameOverView():
    topFrame = window.topFrame.topCenterFrame
    topFrame.areaButton.config(state=NORMAL, image=gameOverImage,
                               command=topFrame.loadFile)
    bottomFrame = window.bottomFrame.bottomRightFrame
    bottomFrame.centerButton['state'] = DISABLED
    bottomFrame.attackButton['state'] = DISABLED
    bottomFrame.defendButton['state'] = DISABLED
    bottomFrame.fleeButton['state'] = DISABLED
    bottomFrame.skillButton['state'] = DISABLED
    bottomFrame.skillButton.grid_remove()
    bottomFrame.menuBox.unbind_all('1')
    bottomFrame.okButton.grid()
    bottomFrame.okButton['state'] = DISABLED
    bottomFrame.okButton['command'] = root.destroy
    bottomFrame.centerButton['state'] = DISABLED
    window.topFrame.topRightFrame.potionButton['state'] = DISABLED
    window.topFrame.topCenterFrame.areaButton.grid()
    window.topFrame.topCenterFrame.map.grid_remove()
    window.topFrame.topCenterFrame.mapButton['state'] = DISABLED
    window.topFrame.topCenterFrame.mapButton.grid_remove()
    
    window.topFrame.topLeftFrame.updateVitalStats()
    window.topFrame.topRightFrame.updateEnemyStats()


def enableLoadingView():
    window.gameFrame.grid_remove()
    window.topFrame.topCenterFrame.areaButton['state'] = DISABLED
    bottomFrame = window.bottomFrame.bottomRightFrame
    bottomFrame.upButton['state'] = DISABLED
    bottomFrame.leftButton['state'] = DISABLED
    bottomFrame.rightButton['state'] = DISABLED
    bottomFrame.downButton['state'] = DISABLED
    bottomFrame.centerButton['state'] = DISABLED
    bottomFrame.attackButton['state'] = DISABLED
    bottomFrame.defendButton['state'] = DISABLED
    bottomFrame.fleeButton['state'] = DISABLED
    bottomFrame.skillButton['state'] = DISABLED
    bottomFrame.okButton['state'] = DISABLED
    bottomFrame.centerButton['state'] = DISABLED
    bottomFrame.menuBox.unbind_all('1')
    bottomFrame.menuBox.unbind_all('2')
    bottomFrame.menuBox.unbind_all('3')
    bottomFrame.menuBox.unbind_all('4')


def enableInventoryView():
    window.topFrame.topCenterFrame.areaButton['state'] = DISABLED
    leftFrame = window.topFrame.topLeftFrame
    rightFrame = window.topFrame.topRightFrame
    bottomFrame = window.bottomFrame.bottomRightFrame
    leftFrame.vitalStats.grid_remove()
    leftFrame.inventory.grid()
    rightFrame.otherStats.grid()
    rightFrame.enemyStats.grid_remove()
    rightFrame.store.grid_remove()
    leftFrame.updateInventory()

    leftFrame.sellButton.grid_remove()
    leftFrame.dropButton.grid_remove()
    leftFrame.equipButton.grid()
    leftFrame.equipButton['state'] = DISABLED


def enableStoreView():
    window.topFrame.topCenterFrame.areaButton['state'] = NORMAL
    leftFrame = window.topFrame.topLeftFrame
    rightFrame = window.topFrame.topRightFrame
    leftFrame.vitalStats.grid_remove()
    leftFrame.inventory.grid()
    leftFrame.updateInventory()
    rightFrame.otherStats.grid_remove()
    rightFrame.enemyStats.grid_remove()
    rightFrame.store.grid()
    leftFrame.updateInventory()
    rightFrame.updateStore()

    leftFrame.equipButton.grid_remove()
    leftFrame.dropButton.grid_remove()
    leftFrame.sellButton.grid()
    leftFrame.sellButton['state'] = DISABLED
    rightFrame.buyButton['state'] = DISABLED

    bottomFrame = window.bottomFrame.bottomRightFrame
    bottomFrame.upButton.grid()
    bottomFrame.leftButton.grid()
    bottomFrame.rightButton.grid()
    bottomFrame.downButton.grid()
    bottomFrame.centerButton.grid(pady=0)
    bottomFrame.okButton.grid()
    bottomFrame.attackButton.grid_remove()
    bottomFrame.defendButton.grid_remove()
    bottomFrame.fleeButton.grid_remove()
    bottomFrame.skillButton.grid_remove()
    bottomFrame.centerButton['state'] = NORMAL


def enableDropItemView():
    enableInventoryView()
    window.topFrame.topCenterFrame.areaButton['state'] = DISABLED
    leftFrame = window.topFrame.topLeftFrame
    leftFrame.equipButton.grid_remove()
    leftFrame.sellButton.grid_remove()
    leftFrame.dropButton.grid()
    leftFrame.dropButton['state'] = DISABLED

    bottomFrame = window.bottomFrame.bottomRightFrame
    bottomFrame.okButton['state'] = DISABLED
    bottomFrame.attackButton.grid_remove()
    bottomFrame.defendButton.grid_remove()
    bottomFrame.fleeButton.grid_remove()
    bottomFrame.centerButton.config(state=NORMAL, image=backImage,
                                    command=bottomFrame.clickCancelDropButton)
    bottomFrame.centerButton.unbind_all('i')
    bottomFrame.centerButton.unbind_all('I')
    bottomFrame.centerButton.grid(pady=34)
    bottomFrame.upButton['state'] = DISABLED
    bottomFrame.leftButton['state'] = DISABLED
    bottomFrame.rightButton['state'] = DISABLED
    bottomFrame.downButton['state'] = DISABLED
    bottomFrame.upButton.grid_remove()
    bottomFrame.leftButton.grid_remove()
    bottomFrame.rightButton.grid_remove()
    bottomFrame.downButton.grid_remove()
    bottomFrame.disableMenuBox()


def enableForgetSkillView():
    enableTravelView()
    bottomFrame = window.bottomFrame.bottomRightFrame
    bottomFrame.okButton.config(state=DISABLED,
                                command=bottomFrame.clickForgetButton)
    bottomFrame.enableMenuBox()
    bottomFrame.lastUpButtonState = bottomFrame.upButton['state']
    bottomFrame.lastLeftButtonState = bottomFrame.leftButton['state']
    bottomFrame.lastRightButtonState = bottomFrame.rightButton['state']
    bottomFrame.lastDownButtonState = bottomFrame.downButton['state']
    bottomFrame.upButton['state'] = DISABLED
    bottomFrame.leftButton['state'] = DISABLED
    bottomFrame.centerButton.config(state=NORMAL, image=backImage,
                                    command=bottomFrame.clickCancelForgetButton)
    bottomFrame.rightButton['state'] = DISABLED
    bottomFrame.downButton['state'] = DISABLED
    bottomFrame.tempMenu = list(bottomFrame.menuBox.get(0, END))
    skills = []
    for skill in main.character.skills:
        skills.append(skill.NAME)
    bottomFrame.modifyMenu(skills)
    bottomFrame.menuBox.unbind_all('1')
    bottomFrame.menuBox.unbind_all('2')
    bottomFrame.menuBox.unbind_all('3')
    bottomFrame.menuBox.unbind_all('4')


def hideSideFrames():
    leftFrame = window.topFrame.topLeftFrame
    rightFrame = window.topFrame.topRightFrame
    leftFrame.vitalStats.grid_remove()
    leftFrame.inventory.grid_remove()
    rightFrame.otherStats.grid_remove()
    rightFrame.enemyStats.grid_remove()
    rightFrame.store.grid_remove()


def close(event=None):
    if requireExitConfirmation():
        canSave = (window.topFrame.topCenterFrame.areaButton['state'] == NORMAL
                   and main.view != "game over")
        main.sound.playSound(main.sound.sounds['Open Dialog'])
        if canSave:
            answer = tkMessageBox.askyesnocancel(
                "Save and Exit",
                "Do you want to save the game?",
                parent=root)
            if answer is None:
                return
            elif answer:
                main.saveGame()
        elif main.view != "game over":
            if not tkMessageBox.askokcancel(
                 "Warning",
                 "You can't save right now. Are you sure you want to quit?",
                 parent=root):
                return

    root.destroy()


def displayLoadingScreen():
    global loadProgress
    loadProgress = 0
    loadingText = random.choice([
        "Blub blub.",
        "Yaouw!",
        "Let the adventure begin...",
        "I have been waiting for you.",
        "Please be patient. I am a little slow.",
        "Let me get everything ready for you.",
        "Greetings! Please dry your feet on the mat.",
        "It seems as though my loading bar has become uncalibrated.",
        "You caught me by surprise! Where did I leave my shell?",
        "Brace yourself."])
    loadingBar = Label(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT,
                       bg=DEFAULT_BG, compound=BOTTOM, font=font1,
                       text=loadingText)
    loadingBar.grid(sticky=E)
    loadingBar.grid_propagate(0)
    return loadingBar


def updateLoadingScreen(loadingBar):
    loadingBar['image'] = xpBars[
        int(loadProgress / FULL_PROGRESS * (NUMBER_OF_BARS - 1))]
    if loadProgress == FULL_PROGRESS:
        loadingBar.destroy()
    else:
        root.after(30, updateLoadingScreen, loadingBar)
        
        
def loadAssets():
    def incrementProgress(complete=False):
        global loadProgress
        if complete:
            loadProgress = FULL_PROGRESS
        else:
            loadProgress += float(FULL_PROGRESS) / assetsToLoad
        root.update()
    
    assetsToLoad = NUMBER_OF_BARS
    assetsToLoad += len(main.weapons)
    assetsToLoad += len(main.armour)
    assetsToLoad += len(main.shields)
    assetsToLoad += len(main.miscellaneousItems)
    assetsToLoad += len(main.enemies)
    # assetsToLoad += len(main.areas)
    
    for i in range(1, NUMBER_OF_BARS):
        xpBars.append(PhotoImage(file="images\\bars\\xpbar"+
                                 str(i)+".gif"))
        hpBars.append(PhotoImage(file="images\\bars\\hpbar"+
                                 str(NUMBER_OF_BARS - i - 1)+".gif"))
        epBars.append(PhotoImage(file="images\\bars\\epbar"+
                                 str(NUMBER_OF_BARS - i - 1)+".gif"))
        spBars.append(PhotoImage(file="images\\bars\\spbar"+
                                 str(i)+".gif"))
        incrementProgress()
    
    for area in main.areas.itervalues():
        areaImages[area.name] = []

    for enemyId in main.enemies:
        enemyImages[enemyId] = (PhotoImage(file="images\\enemies\\"+
                                           main.enemies[enemyId].IMAGE+".gif"))
        incrementProgress()

    for weaponName in main.weapons:
        itemImages[main.weapons[weaponName].IMAGE_NAME] = (
            PhotoImage(file="images\\weapons\\"+weaponName+".gif"))
        incrementProgress()
    for armourName in main.armour:
        itemImages[main.armour[armourName].IMAGE_NAME] = (
            PhotoImage(file="images\\armour\\"+armourName+".gif"))
        incrementProgress()
    for shieldName in main.shields:
        itemImages[main.shields[shieldName].IMAGE_NAME] = (
            PhotoImage(file="images\\shields\\"+shieldName+".gif"))
        incrementProgress()
    for itemName in main.miscellaneousItems:
        itemImages[main.miscellaneousItems[itemName].IMAGE_NAME] = (
            PhotoImage(file="images\\miscellaneous\\"+itemName+".gif"))
        incrementProgress()
        
    incrementProgress(True)
    
    
def loadGame(event=None):
    updateLoadingScreen(displayLoadingScreen())
    loadAssets()
    
    global window
    window = Window(root)
    hideSideFrames()
    main.sound.playMusic(main.sound.songs['Intro Theme'])
    
    
def requireExitConfirmation(yes=None):
    global askToSave
    if yes is None:
        return askToSave
    else:
        askToSave = yes


main = Main()

WINDOW_WIDTH = 822
WINDOW_HEIGHT = 642
FRAME_C_WIDTH = 233
FRAME_C_HEIGHT = 426

NUMBER_OF_BARS = 46

BEIGE = "#ebdec0"
DARKBEIGE = "#d1c29d"
BROWN = "#704F16"
LIGHTBEIGE = "#f4ead2"
RED = "#90000d"
LIGHTRED = "#d31524"
CYAN = "#24828b"
BLACK = "#000000"
BLUE = "#0093DC"
GREY = "#888888"
LIGHTCYAN = "#7bb4b9"
YELLOW = "#eec000"
WHITE = "#f4f4f4"
NAVY = "#000050"
PURPLE = "#26065c"
MAGENTA = "#de6ef1"
LIGHTPURPLE = "#4f3c70"
ORANGE = "#f8b681"
DARKORANGE = "#a33c00"
EARTH_COLOR = "#b0ca90"
WATER_COLOR = "#b0cbc7"
FIRE_COLOR = "#e6ba90"
ENIGMATIC_COLOR = "#e2afc9"

DEFAULT_BG = BEIGE
BUTTON_BG = DARKBEIGE
BUTTON_FG = BROWN
TEXTBOX_BG = LIGHTBEIGE
MAP_BG = TEXTBOX_BG
LEVEL_UP_BG = CYAN
LEVEL_UP_FG = LIGHTCYAN
MERCENARY_UP_BG = YELLOW
MERCENARY_UP_FG = BROWN
LOOT_BG = DARKBEIGE
LOOT_FG = BROWN
MYSTIC_BG = PURPLE
MYSTIC_FG = MAGENTA
MYSTIC_FG2 = LIGHTPURPLE
SKILL_BG = ORANGE
SKILL_FG = DARKORANGE

root = Tk()

# Initialize variables
font1 = tkFont.Font(family="Garamond", size=10)
italicFont1 = tkFont.Font(family="Garamond", size=10, slant="italic")
font2 = tkFont.Font(family="Garamond", size=11)
italicFont2 = tkFont.Font(family="Garamond", size=11, slant="italic", weight="bold")
font3 = tkFont.Font(family="Garamond", size=12, weight="bold")
font4 = tkFont.Font(family="Garamond", size=14)
italicFont4 = tkFont.Font(family="Garamond", size=14, slant="italic")
font5 = tkFont.Font(family="Garamond", size=80, weight="bold")
font6 = tkFont.Font(family="Garamond", size=18)
font7 = tkFont.Font(family="Garamond", size=66, weight="bold")
font8 = tkFont.Font(family="Garamond", size=16, weight="bold")

welcomeImage = PhotoImage(file="images\\other\\turtle.gif")
tosheImage = PhotoImage(file="images\\other\\toshe.gif")
gameOverImage = PhotoImage(file="images\\other\\gameover.gif")

euroImage = PhotoImage(file="images\\icons\\euro.gif")
potionImage = PhotoImage(file="images\\icons\\potion.gif")
sfxImage = PhotoImage(file="images\\icons\\sfx.gif")
musicImage = PhotoImage(file="images\\icons\\music.gif")
mapImage = PhotoImage(file="images\\icons\\map.gif")
vBorderImage1 = PhotoImage(file="images\\other\\border21.gif")
vBorderImage2 = PhotoImage(file="images\\other\\border22.gif")
hBorderImage = PhotoImage(file="images\\other\\border3.gif")
waveBorderImage = PhotoImage(file="images\\other\\border1.gif")

upImage = PhotoImage(file="images\\icons\\up.gif")
leftImage = PhotoImage(file="images\\icons\\left.gif")
rightImage = PhotoImage(file="images\\icons\\right.gif")
downImage = PhotoImage(file="images\\icons\\down.gif")
inventoryImage = PhotoImage(file="images\\icons\\inventory.gif")
backImage = PhotoImage(file="images\\icons\\back.gif")
attackImage = PhotoImage(file="images\\icons\\attack.gif")
defendImage = PhotoImage(file="images\\icons\\defend.gif")
fleeImage = PhotoImage(file="images\\icons\\flee.gif")

noItemImage = PhotoImage(file="images\\other\\empty.gif")
defaultImage = PhotoImage(file="images\\other\\default.gif")

xpBars = []
hpBars = []
epBars = []
spBars = []
areaImages = {}
itemImages = {}
enemyImages = {}
FULL_PROGRESS = 100

xpBars.append(PhotoImage(file="images\\bars\\xpbar"+
                         str(0)+".gif"))
hpBars.append(PhotoImage(file="images\\bars\\hpbar"+
                         str(NUMBER_OF_BARS - 1)+".gif"))
epBars.append(PhotoImage(file="images\\bars\\epbar"+
                         str(NUMBER_OF_BARS - 1)+".gif"))
spBars.append(PhotoImage(file="images\\bars\\spbar"+
                         str(0)+".gif"))
        
views = {'travel': enableTravelView,
         'battle': enableBattleView,
         'inventory': enableInventoryView,
         'store': enableStoreView,
         'battle over': enableBattleOverView,
         'game over': enableGameOverView}

askToSave = False
root.protocol('WM_DELETE_WINDOW', close)
root.iconbitmap("images\\icons\\tq.ico")
root.title("Toshe's Quest II")
root.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))
root.resizable(0, 0)
root.after(0, loadGame)
root.update()
root.mainloop()
