# -*- coding: utf-8 -*-
#Toshe's Underwater Adventures 1.1

"""
File: Toshe's Quest II.py
Author: Ben Gardner
Created: December 25, 2012
Revised: May 19, 2023
"""


from Tkinter import *
import tkFont
import tkMessageBox
from TUAMain import Main
from TUADialog import OpenFileDialog
from TUAStatics import Static
import converter
import random
from datetime import datetime
import pickle


class Window:
    """Contains the game window."""

    def __init__(self, master):
        self.gameFrame = Frame(master, bg=DEFAULT_BG, relief=SUNKEN, bd=4)
        self.gameFrame.grid(row=0, column=0)
        
        self.sideFrame = Frame(master, bg=DEFAULT_BG)
        self.sideFrame.grid(row=0, column=1)
        
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
        
        self.questFrame = Frame(master, bg=QUEST_BG, relief=RIDGE, bd=10)
        self.questFrame.grid(row=0)
        self.questFrame.grid_remove()
        
        self.powerUpFrame = Frame(master, bg=MYSTIC_BG, relief=RIDGE, bd=10)
        self.powerUpFrame.grid(row=0)
        self.powerUpFrame.grid_remove()
        
        self.newSkillFrame = Frame(master, bg=SKILL_BG, relief=RIDGE, bd=10)
        self.newSkillFrame.grid(row=0)
        self.newSkillFrame.grid_remove()
        
        self.upgradeFrame = Frame(master, bg=UPGRADE_BG, relief=RIDGE, bd=10)
        self.upgradeFrame.grid(row=0)
        self.upgradeFrame.grid_remove()
        
        self.levelUpLabel = Label(self.levelUpFrame, text="LEVEL UP!",
                                  font=font5, bg=LEVEL_UP_BG, fg=LEVEL_UP_FG)
        self.levelUpLabel.grid()
        self.levelUpLabel.bind("<Button-1>", self.removeLevelUpFrame)
        self.levelUpCallback = None
        
        self.mercenaryUpLabel = Label(self.mercenaryUpFrame,
                                 text="MERC. UP!",
                                 font=font7,
                                 bg=MERCENARY_UP_BG, fg=MERCENARY_UP_FG)
        self.mercenaryUpLabel.grid()
        self.mercenaryUpLabel.bind("<Button-1>", self.removeMercenaryUpFrame)
        self.mercenaryCallback = None
        
        lootLabel = Label(self.lootFrame, text="LOOT!", font=font5,
                          bg=LOOT_BG, fg=LOOT_FG)
        lootLabel.grid()
        lootLabel.bind("<Button-1>", self.removeLootFrame)
        self.lootCallback = None
        
        self.questLabel = Label(self.questFrame, text="QUEST!", font=font7,
                           bg=QUEST_BG, fg=QUEST_FG)
        self.questLabel.grid()
        self.questLabel.bind("<Button-1>", self.removeQuestFrame)
        self.questCallback = None
        
        powerUpLabel = Label(self.powerUpFrame, text="RANK UP!",
                                  font=font5, bg=MYSTIC_BG, fg=MYSTIC_FG2)
        powerUpLabel.grid()
        powerUpLabel.bind("<Button-1>", self.removePowerUpFrame)
        self.powerUpCallback = None
        
        self.newSkillLabelBottom = Label(self.newSkillFrame,
                                         text="PUMMELER'S PRECISION!",
                                         wraplength=WINDOW_WIDTH-20,
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
        self.newSkillCallback = None
        
        self.upgradeLabel = Label(self.upgradeFrame, font=font5,
                             text="UPGRADE!", bg=UPGRADE_BG, fg=UPGRADE_FG)
        self.upgradeLabel.grid()
        self.upgradeLabel.bind("<Button-1>", self.removeUpgradeFrame)
        self.upgradeCallback = None
        
        self.makeChildren(self.gameFrame, self.sideFrame)

    def makeChildren(self, leftMaster, rightMaster):
        self.topFrame = TopFrame(leftMaster)
        self.bottomFrame = BottomFrame(leftMaster)
        self.rightFrame = RightFrame(rightMaster)
        
    def gridLevelUpFrame(self):
        if self.levelUpCallback:
            root.after_cancel(self.levelUpCallback)
        self.levelUpFrame.grid()
        self.levelUpCallback = root.after(4000, window.removeLevelUpFrame)

    def removeLevelUpFrame(self, event=None):
        self.levelUpFrame.grid_remove()

    def gridMercenaryUpFrame(self, name):
        if self.mercenaryCallback:
            root.after_cancel(self.mercenaryCallback)
        self.mercenaryUpLabel.config(text="%s UP!" % name.upper())
        self.mercenaryUpFrame.grid()
        self.mercenaryCallback = root.after(3000, window.removeMercenaryUpFrame)

    def removeMercenaryUpFrame(self, event=None):
        self.mercenaryUpFrame.grid_remove()
        
    def gridLootFrame(self):
        if self.lootCallback:
            root.after_cancel(self.lootCallback)
        self.lootFrame.grid()
        self.lootCallback = root.after(2500, window.removeLootFrame)

    def removeLootFrame(self, event=None):
        self.lootFrame.grid_remove()
        
    def gridQuestFrame(self, phrase):
        if self.questCallback:
            root.after_cancel(self.questCallback)
        self.questLabel.config(text=phrase)
        self.questFrame.grid()
        self.questCallback = root.after(2500, window.removeQuestFrame)

    def removeQuestFrame(self, event=None):
        self.questFrame.grid_remove()
        
    def gridPowerUpFrame(self):
        if self.powerUpCallback:
            root.after_cancel(self.powerUpCallback)
        self.powerUpFrame.grid()
        self.powerUpCallback = root.after(3500, window.removePowerUpFrame)

    def removePowerUpFrame(self, event=None):
        self.powerUpFrame.grid_remove()
        
    def gridnewSkillFrame(self, skillName):
        if self.newSkillCallback:
            root.after_cancel(self.newSkillCallback)
        self.newSkillLabelBottom.config(text="%s!" % skillName.upper())
        self.newSkillFrame.grid()
        self.newSkillCallback = root.after(3000, window.removeNewSkillFrame)
        
    def removeNewSkillFrame(self, event=None):
        self.newSkillFrame.grid_remove()
        
    def gridUpgradeFrame(self, success):
        if self.upgradeCallback:
            root.after_cancel(self.upgradeCallback)
        if success:
            self.upgradeLabel.config(text="UPGRADE!",
                                     bg=UPGRADE_BG, fg=UPGRADE_FG)
            self.upgradeFrame.config(bg=UPGRADE_BG)
        else:
            self.upgradeLabel.config(text="FAILURE!",
                                     bg=FAILURE_BG, fg=FAILURE_FG)
            self.upgradeFrame.config(bg=FAILURE_BG)
        self.upgradeFrame.grid()
        self.upgradeCallback = root.after(3000, window.removeUpgradeFrame)
        
    def removeUpgradeFrame(self, event=None):
        self.upgradeFrame.grid_remove()


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


class RightFrame:
    def __init__(self, master):
        self.missions = LabelFrame(master,
            bg=MEDIUMBEIGE,
            font=font3,
            text="Missions",
            width=FRAME_C_WIDTH,
            height=WINDOW_HEIGHT)
        self.missions.grid()
        self.missions.grid_propagate(0)
        self.missions.columnconfigure(0, weight=1)
        
        self.noMissions = Label(self.missions,
            bg=MEDIUMBEIGE,
            font=font2,
            text="No current missions.",
            wraplength=FRAME_C_WIDTH-20,
            pady=2,
            justify=LEFT,
            anchor=W,)
        self.noMissions.grid(sticky=EW)
        
        self.missionLog = {}

    def updateMissions(self):
        for quest, mission in self.missionLog.iteritems():
            mission.missionDetails['text'] = quest.getDetailsFor(main.character)
            if quest.getDetailsFor(main.character):
                mission.missionDetails.grid(sticky=W)
                
            
    def pushDownMissions(self):
        for mission in self.missionLog:
            element = self.missionLog[mission]
            element.grid(row=int(element.grid_info()['row']) + 1)

    def addMission(self, quest, pushToTop=True):
        self.noMissions.grid_remove()
        
        missionFrame = Frame(self.missions,
            bg=MEDIUMBEIGE,
            pady=2,
            bd=2,)
        missionFrame.grid(sticky=EW, padx=2, pady=2)
        if pushToTop:
            self.pushDownMissions()
            missionFrame.grid(row=0)
        missionFrame.columnconfigure(0, weight=1)
        
        missionTitle = Label(missionFrame,
            bg=MEDIUMBEIGE,
            text=quest.TITLE + (" (Repeatable)" if quest.REPEATABLE else ""),
            font=italicFont2,
            wraplength=FRAME_C_WIDTH-20,
            justify=LEFT,)
        if quest.OPTIONAL:
            missionTitle['fg'] = BROWN
        missionTitle.grid(sticky=W)
        missionDescription = Label(missionFrame,
            bg=MEDIUMBEIGE,
            text=quest.DESCRIPTION,
            font=italicFont1,
            wraplength=FRAME_C_WIDTH-20,
            justify=LEFT,)
        missionDescription.grid(sticky=W)
        missionFrame.missionDetails = Label(missionFrame,
            bg=MEDIUMBEIGE,
            text=quest.getDetailsFor(main.character),
            font=font1,
            wraplength=FRAME_C_WIDTH-20,
            justify=LEFT,)
        if quest.getDetailsFor(main.character):
            missionFrame.missionDetails.grid(sticky=W)
        
        self.missionLog[quest] = missionFrame

    def clearMissions(self):
        for mission in self.missionLog.itervalues():
            mission.grid_forget()
            mission.destroy()
        self.missionLog = {}
        self.noMissions.grid()

    def markMission(self, quest):
        self.pushDownMissions()
        self.missionLog[quest].grid(row=0)
        self.missionLog[quest].config(
            relief=GROOVE,
        )

    def unmarkMission(self, quest):
        self.pushDownMissions()
        self.missionLog[quest].grid(row=0)
        self.missionLog[quest].config(
            relief=FLAT,
        )

    def removeMission(self, quest):
        self.missionLog[quest].grid_forget()
        self.missionLog[quest].destroy()
        del self.missionLog[quest]
        if len(self.missionLog) == 0:
            self.noMissions.grid()


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
        self.makeIntroFrameElements(frameC)

    def makeIntroFrameElements(self, master):
        self.makeRecentGamesFrame(master)

    def makeRecentGamesFrame(self, master):
        self.recentGames = LabelFrame(master, text="Recent Games", font=font3,
                                 width=FRAME_C_WIDTH, height=FRAME_C_HEIGHT,
                                 bg=DEFAULT_BG)
        self.recentGames.grid()
        self.recentGames.grid_propagate(0)
        self.recentGames.columnconfigure(0, weight=1)

        noRecentGames = Label(self.recentGames,
            bg=DEFAULT_BG,
            font=font2,
            justify=LEFT,
            anchor=W,
            text=("No recent games."+
                "\nClick the turtle to start one."))

        try:
            with open("prefs\\recent_games.tqp", "r") as preferencesFile:
                recentCharacters = pickle.load(preferencesFile).recentCharacters

            if len(recentCharacters) == 0:
                noRecentGames.grid(sticky=EW)
                return

            MAX_FILES_TO_SHOW = 5
            for i in range(0, min(len(recentCharacters), MAX_FILES_TO_SHOW)):
                name, character = recentCharacters.popitem()
                gameDetailFrame = Frame(self.recentGames,
                    bg=DEFAULT_BG,
                    pady=6,)
                gameDetailFrame.columnconfigure(1, weight=1)
                portrait = Label(gameDetailFrame,
                    bg=DEFAULT_BG,
                    image=itemImages[character.equippedWeapon.IMAGE_NAME],)
                portrait.grid(row=0, column=0)
                gameInfo = Button(gameDetailFrame,
                    bg=BUTTON_BG,
                    fg=BUTTON_FG,
                    font=font2,
                    justify=LEFT,
                    anchor=W,
                    command=lambda n=name: window.topFrame.topCenterFrame.tryToLoadFile(n),)
                gameInfo.grid(row=0, column=1, padx=(0, 4), sticky=EW)

                def getTitle(character):
                    str = character.strength
                    dex = character.dexterity
                    wis = character.wisdom
                    if character.specialization is not None:
                        return character.specialization
                    elif str >= 50:
                        if dex >= 50:
                            if wis >= 50:
                                return "Omnibus"
                            return "Ranger"
                        elif wis >= 50:
                            return "Monk"
                        return "Warrior"
                    elif dex >= 50:
                        if wis >= 50:
                            return "Druid"
                        return "Archer"
                    elif wis >= 50:
                        return "Mage"
                    elif (str >= 25 and dex >= 25 and wis >= 25 and
                          max(str, dex, wis) / min(str, dex, wis) < 1.25):
                        return "Adventurer"
                    elif str >= 25:
                        if 0.8 < str / dex < 1.25:
                            return "Trainee Ranger"
                        elif 0.8 < str / wis < 1.25:
                            return "Trainee Monk"
                        return "Trainee Warrior"
                    elif wis >= 25:
                        if 0.8 < wis / dex < 1.25:
                            return "Trainee Druid"
                        return "Trainee Mage"
                    elif dex >= 25:
                        return "Trainee Archer"
                    elif character.level > 1:
                        return "Trainee"
                    else:
                        return "Castaway"

                MAX_LINE_LENGTH = 26
                lines = [
                    name,
                    "%s ❦ %s" % (character.level, getTitle(character)),
                    character.area.name,
                ]
                try:
                    for i, line in enumerate(lines):
                        if len(line) > MAX_LINE_LENGTH:
                            lines[i] = "%s..." % line[:MAX_LINE_LENGTH-1]
                    gameInfo['text'] = "\n".join(lines)
                    gameDetailFrame.grid(sticky=EW)
                except UnicodeDecodeError:
                    continue
        except IOError:
            noRecentGames.grid(sticky=EW)

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

        levelFrame = Frame(self.vitalStats, bd=2, relief=RIDGE, bg=LEVEL_BG)
        levelFrame.grid(column=1, padx=10, pady=10, sticky=E)
        self.levelLabel = Label(levelFrame, text="1", font=font2,
                                width=2, bg=DEFAULT_BG, bd=0)
        self.levelLabel.grid()
        self.nameLabel = Label(self.vitalStats, text="Toshe", font=italicFont4,
                               fg=BLACK, bg=DEFAULT_BG)
        self.nameLabel.grid(row=0, column=0, columnspan=2)
        self.xpBarLabel = Label(self.vitalStats, image=xpBars[6], bg=DEFAULT_BG,
                                relief=SUNKEN, bd=1, compound=CENTER,
                                font=font8, fg=WHITE)
        self.xpBarLabel.grid(row=1, columnspan=2)
        self.spBarLabel = Label(self.vitalStats, image=spBars[34],
                                bg=DEFAULT_BG, relief=SUNKEN, bd=2)
        self.spBarLabel.grid(row=3, columnspan=2)
        self.spWord = Label(self.vitalStats, text="Mystic 2", fg=MYSTIC_FG,
                            bg=MYSTIC_BG, font=font1, relief=RIDGE)
        self.spWord.grid(row=4, padx=1, ipadx=4, ipady=1, sticky=W)
        self.spLabel = Label(self.vitalStats, text="80",
                             bg=DEFAULT_BG, font=font1, bd=0)
        self.spLabel.grid(row=4, column=1, sticky=E+N, padx=(0, 1))
        self.tosheLabel = Label(self.vitalStats, image=tosheImage, bg=COMMON_BD,
                                relief=RIDGE, bd=4)
        self.tosheLabel.grid(columnspan=2, pady=20)
        self.tosheLabel.queuedImages = []
        self.hpWord = Label(self.vitalStats, text="HP",
                            bg=DEFAULT_BG, font=font1, bd=0)
        self.hpWord.grid(column=0, sticky=W)
        self.hpLabel = Label(self.vitalStats, text="100/100",
                                  bg=DEFAULT_BG, font=font1, bd=0)
        self.hpLabel.grid(row=6, column=1, sticky=E, padx=(0, 1))
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
        self.epLabel.grid(row=9, column=1, sticky=E, padx=(0, 1))


        self.inventory = LabelFrame(master, text="Inventory", font=font3,
                                    width=FRAME_C_WIDTH, height=FRAME_C_HEIGHT,
                                    bg=DEFAULT_BG)
        self.inventory.grid(row=0)
        self.inventory.grid_propagate(0)

        # Inventory checkbutton variable
        self.v1 = IntVar()
        self.itemButtonFrame = Frame(self.inventory, bg=DEFAULT_BG)
        self.itemButtonFrame.grid()
        self.itemButtons = makeItemButtons(self.itemButtonFrame, self.v1, 0)
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
        self.placeButton = Button(self.inventory, text="Place", font=font2,
                                   fg=BUTTON_FG, bg=BUTTON_BG,
                                   command=self.clickPlaceButton)
        self.placeButton.grid(row=10, columnspan=3, sticky=E+W)
        self.placeButton.grid_remove()

    def animateToshe(self):
        interval = 125
        for event in self.tosheLabel.queuedImages:
            root.after_cancel(event)
        self.tosheLabel.queuedImages = []
        def updateImageDelayed(delay, image):
            self.tosheLabel.queuedImages.append(
                root.after(delay, lambda: self.tosheLabel.config(image=image)))
        for i, image in enumerate(bloodSlashImages):
            updateImageDelayed(i * interval, image)
        self.tosheLabel.queuedImages.append(
            root.after((i+1) * interval, lambda: self.tosheLabel.config(image=tosheImage)))

    def expandInventory(self, expand=True):
        for button in self.itemButtons:
            button.destroy()
        self.itemButtons = makeItemButtons(self.itemButtonFrame, self.v1, 0,
            4 if expand else 3)
        self.itemNameLabel.grid(columnspan=4 if expand else 3)
        self.itemCategoryLabel.grid(columnspan=4 if expand else 3)
        self.itemValueLabel.grid(columnspan=4 if expand else 3)
        self.itemRequirementLabel.grid(columnspan=4 if expand else 3)
        self.itemQualityLabel.grid(columnspan=4 if expand else 3)
        self.itemCBRateLabel.grid(columnspan=4 if expand else 3)
        self.itemElementLabel.grid(columnspan=4 if expand else 3)
        self.equipButton.grid(row=10, columnspan=4 if expand else 3)
        self.equipButton.grid_remove()
        self.dropButton.grid(row=10, columnspan=4 if expand else 3)
        self.dropButton.grid_remove()
        self.sellButton.grid(row=10, columnspan=4 if expand else 3)

    def clickEquipButton(self):
        if main.view == "battle":
            interfaceActions = main.equipItem(self.v1.get())
            updateInterface(interfaceActions)
        else:
            main.character.equip(self.v1.get())
            main.sound.playSound(main.sound.sounds['Equip'])
        window.topFrame.topRightFrame.updateOtherStats()
        self.equipButton['state'] = DISABLED
        self.updateInventory()
        
    def clickSellButton(self):
        main.sell(self.v1.get())
        self.sellButton['state'] = DISABLED
        self.updateInventory()
        window.topFrame.topRightFrame.buyButton['state'] = DISABLED
        window.topFrame.topRightFrame.updateStore()
        window.topFrame.topRightFrame.updateOtherStats()

    def clickDropButton(self):
        if self.v1.get() in main.character.equippedItemIndices.values():
            main.character.equip(self.v1.get())
        main.character.removeItem(self.v1.get())
        main.character.addItem(main.tempItem)
        window.bottomFrame.bottomRightFrame.clickCancelDropButton()

    def clickPlaceButton(self):
        def updateWidgets():
            if main.forge.hasAllSacrifices():
                if forgeFrame.crucible['state'] == DISABLED:
                    main.sound.playSound(main.sound.sounds['Burning'])
                forgeFrame.crucible['state'] = NORMAL
            else:
                forgeFrame.crucible['state'] = DISABLED
            if main.forge.isReady():
                if forgeFrame.anvilButton['state'] == DISABLED:
                    main.sound.playSound(main.sound.sounds['Hammer'])
                forgeFrame.forgeSuccess['text'] = "Success chance: %s%%" % (
                    main.forge.getSuccessChance())
                forgeFrame.forgeSuccess.grid()
                forgeFrame.anvilButton['state'] = NORMAL
                forgeFrame.anvilButton['relief'] = RAISED
                forgeFrame.anvilButton['cursor'] = "@hammer.cur"
            else:
                forgeFrame.forgeSuccess.grid_remove()
                forgeFrame.anvilButton['state'] = DISABLED
                forgeFrame.anvilButton['relief'] = FLAT
                forgeFrame.anvilButton['cursor'] = ""
            
        forgeFrame = window.topFrame.topRightFrame
        if forgeFrame.v3.get() == 0:
            replacementIndex = main.setForgeItem(self.v1.get())
            main.sound.playSound(main.sound.sounds['Place on Anvil'])
            main.sound.playSound(main.sound.sounds['Crucible'])
        else:
            replacementIndex = main.setSacrificeItem(forgeFrame.v3.get(), self.v1.get())
            main.sound.playSound(main.sound.sounds['Crucible'])
        if replacementIndex is not None:
            button = forgeFrame.forgeButtons[replacementIndex]
            button['image'] = noItemImage
            button['text'] = "Select an item to %s" % (
                "upgrade" if replacementIndex == 0 else "sacrifice")
        button = forgeFrame.forgeButtons[forgeFrame.v3.get()]
        button['image'] = self.itemButtons[self.v1.get()]['image']
        button['text'] = " "
        updateWidgets()

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
        if "Newly Specialized" in main.character.flags:
            del main.character.flags['Newly Specialized']
            self.spWord.grid()
            self.spLabel.grid()
            self.spBarLabel.grid()
            self.tosheLabel['bg'] = LEGENDARY_BD
        if c.specialization is not None:
            self.spWord['text'] = "%s %s" % (c.specialization, c.mastery)
            if c.sp > c.spTnl:
                self.spBarLabel['image'] = spBars[-1]
            else:
                self.spBarLabel['image'] = spBars[int(float(c.sp) / c.spTnl *
                                                      (NUMBER_OF_BARS - 1))]
            self.spLabel['text'] = "%d/%d" % (c.sp, c.spTnl)
        self.tosheLabel['state'] = NORMAL
        if c.hp <= 0:
            self.hpBarLabel['image'] = hpBars[0]
            self.tosheLabel['state'] = DISABLED
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
        if len(self.itemButtons) < 16 and "Chasmic Rucksack" in main.character.flags:
            self.expandInventory()
            window.bottomFrame.bottomLeftFrame.insertOutput(
                "Your inventory can now hold 16 items.",
                "italicize")
        clearItemStats(self, store=False)
        self.v1.set(-1)
        rows = 4 if "Chasmic Rucksack" in main.character.flags else 3
        for i in range(0, rows):
            for j in range(0, rows):
                if not main.character.items[i*rows+j]:
                    self.itemButtons[i*rows+j].config(image=noItemImage,
                                                   state=DISABLED,
                                                   bg=BLACK)
                elif i*rows+j in main.character.equippedItemIndices.values():
                    try:
                        itemImage = itemImages[
                            main.character.items[i*rows+j].IMAGE_NAME]
                    except KeyError as e:
                        print "Missing image: %s" % e
                        itemImage = defaultImage
                    self.itemButtons[i*rows+j].config(image=itemImage,
                                                      state=NORMAL,
                                                      bg=LIGHTCYAN)
                elif i*rows+j not in main.character.equippedItemIndices.values():
                    try:
                        itemImage = itemImages[
                            main.character.items[i*rows+j].IMAGE_NAME]
                    except KeyError as e:
                        print "Missing image: %s" % e
                        itemImage = defaultImage
                    self.itemButtons[i*rows+j].config(image=itemImage,
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
        self.musicButton = Checkbutton(master, indicatoron=False, bg=BUTTON_BG,
                                     relief=SUNKEN, image=musicImage,
                                     variable=self.playMusic,
                                     command=main.sound.muteMusic)
        self.musicButton.grid(row=0, padx=16, sticky=W)
        self.musicButton.bind_all("<Control-m>", lambda _: self.musicButton.invoke())
        self.musicButton.bind_all("<Control-M>", lambda _: self.musicButton.invoke())
        self.playSfx = BooleanVar(value=True)
        self.sfxButton = Checkbutton(master, indicatoron=False, bg=BUTTON_BG,
                                     relief=SUNKEN, image=sfxImage,
                                     variable=self.playSfx,
                                     command=main.sound.muteSfx)
        try:
            with open("prefs\\preferences.tqp", "r") as preferencesFile:
                preferences = pickle.load(preferencesFile)
                if not preferences.musicOn:
                    self.musicButton.invoke()
                if not preferences.sfxOn:
                    self.sfxButton.invoke()
        except IOError:
            pass
        self.sfxButton.grid(row=0, padx=40, sticky=W)
        self.sfxButton.bind_all("<Alt-m>", lambda _: self.sfxButton.invoke())
        self.sfxButton.bind_all("<Alt-M>", lambda _: self.sfxButton.invoke())
        self.titleLabel = Label(master, text="Toshe's Quest II", font=font6,
                                bg=DEFAULT_BG, bd=0)
        self.titleLabel.grid(row=0, pady=6)
        self.showMap = BooleanVar()
        self.mapButton = Checkbutton(master, indicatoron=False, bg=BUTTON_BG,
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

    def saveFile(self):
        main.sound.playSound(main.sound.sounds['Open Dialog'])
        if tkMessageBox.askokcancel("Save Game", "Do you want to save?",
                                    parent=root):
            main.saveGame()
            requireExitConfirmation(False)

    def openFile(self):
        main.sound.playSound(main.sound.sounds['Open Dialog'])
        d = OpenFileDialog(root, "Start Game")
        if not hasattr(d, 'entryValue'):
            window.bottomFrame.bottomLeftFrame.insertOutput(
                "Come on. I promise not to bite.")
            return
        self.tryToLoadFile(d.entryValue)

    def tryToLoadFile(self, name):
        try:
            self.loadFile(name)
        except IOError:
            self.createFile(name)
        except AttributeError as e:
            window.bottomFrame.bottomLeftFrame.insertOutput(
                name +
                ", some vital information is missing from your file." +
                " Perhaps this can be remedied with a conversion.")
            path = "saves\\"+name+".tq"
            with open(path, "r") as gameFile:
                changed = converter.update(gameFile, path)
            if changed:
                window.bottomFrame.bottomLeftFrame.insertOutput(
                    name +
                    ", your file has been successfully converted!")
                self.tryToLoadFile(name)
            else:
                raise e
        # except (EOFError, ValueError, KeyError, IndexError):
            # window.bottomFrame.bottomLeftFrame.insertOutput(
                # name +
                # ", your file is completely garbled! This is quite unfortunate.")
        # except ImportError:
            # window.bottomFrame.bottomLeftFrame.insertOutput(
                # "I cannot read this file at all! What language is this?")

    def loadFile(self, name=None):
        if not name:
            window.bottomFrame.bottomRightFrame.okButton['command'] = \
                window.bottomFrame.bottomRightFrame.clickOkButton
            window.bottomFrame.bottomRightFrame.bindChoices()
            name = main.fileName
        main.loadGame(name)
        self.startGame(name)
        window.topFrame.topCenterFrame.areaButton.bind_all("<Control-r>", lambda _: self.loadFile())
        window.topFrame.topCenterFrame.areaButton.bind_all("<Control-R>", lambda _: self.loadFile())

    def restoreFile(self):
        window.bottomFrame.bottomRightFrame.okButton['command'] = \
            window.bottomFrame.bottomRightFrame.clickOkButton
        window.bottomFrame.bottomRightFrame.bindChoices()
        name = main.fileName
        main.loadFromCheckpoint()
        self.startGame(name)

    def createFile(self, name):
        main.startNewGame(name)
        self.startGame(name)
        
    def startGame(self, name):
        stateChanged = False
        
        hideSideIntroFrames()

        window.bottomFrame.bottomLeftFrame.insertTimestamp(True)
        window.topFrame.topRightFrame.logButton['state'] = NORMAL
        if main.character.flags['Config']['Mission Log Open'] != window.topFrame.topRightFrame.showMissionLog.get():
            window.topFrame.topRightFrame.logButton.invoke()

        window.topFrame.topLeftFrame.expandInventory(
            True if "Chasmic Rucksack" in main.character.flags else False)

        interfaceActions = main.getInterfaceActions(justFought=True)
        eventActions = main.getLoginEvents()
        if eventActions is not None:
            interfaceActions.update(eventActions)
            stateChanged = True
        # We must clear missions when reloading
        window.rightFrame.clearMissions()
        updateInterface(interfaceActions)

        # We must clear again so that new missions from updateInterface() are not shown twice
        window.rightFrame.clearMissions()
        for quest in main.character.quests:
            window.rightFrame.addMission(quest, pushToTop=False)
            if quest.isCompletedBy(main.character):
                window.rightFrame.markMission(quest)
        
        self.mapButton['state'] = NORMAL
        self.mapButton.grid()
        if main.character.flags['Config']['Automap On'] != self.showMap.get():
            self.mapButton.invoke()
        self.updateMapVisibility()
        
        if main.character.specialization is not None:
            window.topFrame.topLeftFrame.spWord.grid()
            window.topFrame.topLeftFrame.spLabel.grid()
            window.topFrame.topLeftFrame.spBarLabel.grid()
            window.topFrame.topLeftFrame.tosheLabel['bg'] = LEGENDARY_BD
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
        self.makeIntroFrameElements(frameE)

    def makeIntroFrameElements(self, master):
        self.makeNewsFrame(master)

    def makeNewsFrame(self, master):
        news = LabelFrame(master, text="News", font=font3,
                          width=FRAME_C_WIDTH, height=FRAME_C_HEIGHT,
                          bg=DEFAULT_BG)
        news.grid()
        news.grid_propagate(0)
        news.columnconfigure(0, weight=1)

        newsContent = Text(news,
            bg=DEFAULT_BG,
            height=28,
            font=font1,
            wrap=WORD,
            bd=0,)
        newsContent.tag_config("title", font=font3)
        newsContent.tag_config("section", font=italicFont2, spacing3=2)
        newsContent.tag_config("emphasis", font=boldFont1)

        newsContent.insert(END, "Content Updates", ("section"))
        newsContent.insert(END,
"""
The remaining """)
        newsContent.insert(END, "Guardian Beasts", ("emphasis"))
        newsContent.insert(END,
""" have been unleashed! Find all three—Earth, Water and Fire—and navigate their labyrithine abodes to challenge them. Prepare yourself for some tough battles!

The lair of the dark commander """)
        newsContent.insert(END, "Niplin", ("emphasis"))
        newsContent.insert(END,
""" has been spotted. Scope him out to score some sweet loot, if you can take him on. However, you may have to solve a little puzzle first.

The """)
        newsContent.insert(END, "endgame", ("emphasis"))
        newsContent.insert(END,
""" is nigh! Completing the main game will unlock a new town with new challenges.

""")
        newsContent.insert(END, "Feature Updates", ("section"))
        newsContent.insert(END,
"""
Select a character with the """)
        newsContent.insert(END, "Recent Games", ("emphasis"))
        newsContent.insert(END,
""" list. Hit the ground running with a single click: no more typing your name in!

Find your way around with the new """)
        newsContent.insert(END, "Map", ("emphasis"))
        newsContent.insert(END,
""". Leave it open for a top-down view of the current area. Click to mark important tiles to remember them later.

Are you thirsty? Quench that craving with a """)
        newsContent.insert(END, "potion", ("emphasis"))
        newsContent.insert(END,
""", and heal some HP! All blood-bearing enemies now drop life fluid potions. Suck on that, Vampire Bat!

It's 2023 and people's screens are getting wider...that means it's time for a """)
        newsContent.insert(END, "Mission Log", ("emphasis"))
        newsContent.insert(END,
"""! That's right, you can now view your current missions in your very own log, at your leisure.

Zounds, we have """)
        newsContent.insert(END, "sounds", ("emphasis"))
        newsContent.insert(END,
"""! You can now toggle sound effects, as well as music.

Check your hits and heals at a glance with """)
        newsContent.insert(END, "damage numbers", ("emphasis"))
        newsContent.insert(END,
""". They're animated!

Game over? Don't fret. You can now """)
        newsContent.insert(END, "resume from town", ("emphasis"))
        newsContent.insert(END,
""".""")
        newsContent['state'] = DISABLED
        newsContent.grid(sticky=EW)

        scrollbar = Scrollbar(news, bg=DEFAULT_BG, command=newsContent.yview)
        scrollbar.grid(row=0, column=1, sticky=N+S)
        newsContent.config(yscrollcommand=scrollbar.set)

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
        self.weaponElementLabel.grid(row=9, columnspan=5, sticky=E+W,
            ipady=3, padx=6, pady=14)

        self.showMissionLog = BooleanVar()
        self.logButton = Checkbutton(self.otherStats,
            image=logImage,
            text="Mission Log ",
            font=font2,
            fg=BUTTON_FG,
            bg=BUTTON_BG,
            variable=self.showMissionLog,
            command=self.clickMissionLog,
            compound=RIGHT,
            indicatoron=0,
            state=DISABLED)
        self.logButton.grid(row=10, columnspan=5)
        self.logButton.bind_all("q", lambda _: self.logButton.invoke())
        self.logButton.bind_all("Q", lambda _: self.logButton.invoke())

        self.potionButton = Button(self.otherStats, image=potionImage,
                                   text="104", font=font2,
                                   fg=WHITE, activeforeground=WHITE,
                                   bg=BUTTON_BG, command=self.clickPotionButton,
                                   compound=CENTER, state=DISABLED)
        self.potionButton.grid(row=10, column=3, columnspan=2, sticky=E,
            padx=6)
        self.potionButton.bind_all('p', self.clickPotionButton)
        self.potionButton.bind_all('P', self.clickPotionButton)

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
        nameFrame = Frame(self.enemyStats, bg=DEFAULT_BG)
        nameFrame.grid(columnspan=2)
        self.enemyNameLabel = Label(nameFrame, text="Richard Titball",
                                    font=italicFont4, fg=BLACK, bg=DEFAULT_BG)
        self.enemyNameLabel.grid(pady=(0, 6))
        self.enemySubNameLabel = Label(nameFrame, text="Secret Agent",
                                       font=italicFont1, fg=GREY, bg=DEFAULT_BG,
                                       pady=0)
        self.enemySubNameLabel.grid(row=0, ipady=0, pady=(32, 0), sticky=S)
        levelFrame = Frame(self.enemyStats, bd=2, relief=RIDGE, bg=LEVEL_BG)
        levelFrame.grid(row=0, column=1, padx=10, pady=10, sticky=N+E)
        self.enemyLevelLabel = Label(levelFrame, text="17", font=font2,
                                     width=2, bg=DEFAULT_BG, bd=0)
        self.enemyLevelLabel.grid()
        self.enemyImageLabel = Label(self.enemyStats, image=None, bg=COMMON_BD,
                                     relief=RIDGE, bd=4)
        self.enemyImageLabel.grid(columnspan=2, pady=(10, 20))
        self.enemyImageLabel.queuedImages = []
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



        self.forge = LabelFrame(master, text="Forge of Olympus", font=font3,
                                width=FRAME_C_WIDTH, height=FRAME_C_HEIGHT,
                                bg=DEFAULT_BG)
        self.forge.grid(row=0)
        self.forge.grid_propagate(0)

        self.v3 = IntVar()
        self.forgeButtons = []
        self.anvilButton = Button(self.forge, image=anvilImage, bg=DEFAULT_BG,
                                  bd=8, relief=FLAT, state=DISABLED,
                                  command=self.strikeAnvil)
        self.strikeAnvilCallback = None
        self.anvilButton.grid(columnspan=2, pady=(64, 0))
        
        def enablePlaceButton():
            frame = window.topFrame.topLeftFrame
            itemIndex = frame.v1.get()
            if ( itemIndex != -1 and
                 main.character.items[itemIndex].CATEGORY != "Miscellaneous"):
                frame.placeButton['state'] = NORMAL
            main.sound.playSound(main.sound.sounds['Select Item'])

        anvilItemButton = Radiobutton(self.forge, image=noItemImage,
                                      variable=self.v3, value=0, width=64,
                                      height=64, bg=BLACK, indicatoron=0,
                                      bd=4, compound=CENTER,
                                      text="Select an item to upgrade",
                                      activeforeground=WHITE,
                                      font=font2, fg=WHITE, wrap=64,
                                      command=enablePlaceButton)
        self.forgeButtons.append(anvilItemButton)
        anvilItemButton.grid(columnspan=2, row=0, pady=(6, 140))
        self.forgeSuccess = Label(self.forge, text="Success chance: 1%", pady=3,
                                  font=font2, bg=DEFAULT_BG, relief=GROOVE)
        topPad = 8
        self.forgeSuccess.grid(row=1, columnspan=2, ipadx=6, pady=(topPad, 0))
        self.forge.rowconfigure(1,
            minsize=self.forgeSuccess.winfo_reqheight()+topPad)
        self.crucible = Label(self.forge, image=crucibleImage,
                              bg=DEFAULT_BG, state=DISABLED)
        self.crucible.grid(columnspan=2, pady=(32, 0))
        sacrificeButton1 = Radiobutton(self.forge, image=noItemImage,
                                       variable=self.v3, value=1, width=64,
                                       height=64, bg=BLACK, indicatoron=0,
                                       bd=4, compound=CENTER,
                                       text="Select an item to sacrifice",
                                       activeforeground=WHITE,
                                       font=font2, fg=WHITE, wrap=64,
                                       command=enablePlaceButton)
        self.forgeButtons.append(sacrificeButton1)
        sacrificeButton1.grid(row=2, pady=(0, 32))
        sacrificeButton2 = Radiobutton(self.forge, image=noItemImage,
                                       variable=self.v3, value=2, width=64,
                                       height=64, bg=BLACK, indicatoron=0,
                                       bd=4, compound=CENTER,
                                       text="Select an item to sacrifice",
                                       activeforeground=WHITE,
                                       font=font2, fg=WHITE, wrap=64,
                                       command=enablePlaceButton)
        self.forgeButtons.append(sacrificeButton2)
        sacrificeButton2.grid(row=2, column=1, pady=(0, 32))
        self.resetForge()

    def animateEnemy(self):
        interval = 250
        enemyImage = self.enemyImageLabel['image']
        for event in self.enemyImageLabel.queuedImages:
            root.after_cancel(event)
        self.enemyImageLabel.queuedImages = []
        def updateImageDelayed(delay, image):
            self.enemyImageLabel.queuedImages.append(
                root.after(delay, lambda: self.enemyImageLabel.config(image=image)))
        for i, image in enumerate(bloodDropImages):
            updateImageDelayed(i * interval, image)
        self.enemyImageLabel.queuedImages.append(
            root.after((i+1) * interval, lambda: self.enemyImageLabel.config(image=enemyImage)))

    def increaseStrength(self):
        main.character.strength += 1
        self.useStatPoint()

    def increaseDexterity(self):
        main.character.dexterity += 1
        self.useStatPoint()

    def increaseWisdom(self):
        main.character.wisdom += 1
        self.useStatPoint()

    def useStatPoint(self):
        main.character.statPoints -= 1
        main.sound.playSound(main.sound.sounds['Increase Stat'])
        self.updateOtherStats()
        window.topFrame.topLeftFrame.updateInventory()
        requireExitConfirmation(True)

    def clickPotionButton(self, event=None):
        if (self.potionButton['state'] == NORMAL):
            if main.view == "battle":
                interfaceActions = main.drinkPotion()
                updateInterface(interfaceActions)
            else:
                message = main.usePotion()
                self.updateOtherStats()
                window.topFrame.topLeftFrame.updateVitalStats()
                window.bottomFrame.bottomLeftFrame.insertOutput(message)

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
        if c.accuracy > 100 and c.specialization != "Swift Sharpshooter":
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
            main.view in ("travel", "inventory", "battle")) else DISABLED
        font = font2 if c.potions < 100 else font1
        text = c.potions if c.potions > 0 else " "
        self.potionButton.config(state=state, font=font, text=text)

    def updateEnemyStats(self):
        """Show the level, name, hp bar, and hp of the current enemy in the
        enemy frame.
        """
        e = main.battle.enemy
        
        self.enemyLevelLabel['text'] = e.LEVEL
        self.enemyNameLabel['text'] = e.NAME
        if hasattr(e, "SUBNAME"):
            self.enemySubNameLabel['text'] = e.SUBNAME
            self.enemySubNameLabel.grid()
            self.enemyNameLabel.grid(pady=(0, 6))
        else:
            self.enemySubNameLabel.grid_remove()
            self.enemyNameLabel.grid(pady=0)
        self.enemyImageLabel['image'] = enemyImages[e.IDENTIFIER]
        borderColours = {
            "COMMON": COMMON_BD,
            "RARE": RARE_BD,
            "LEGENDARY": LEGENDARY_BD,
        }
        self.enemyImageLabel['bg'] = borderColours[e.RARITY]
        self.enemyImageLabel['state'] = NORMAL
        if e.hp <= 0:
            self.enemyHpBarLabel['image'] = hpBars[0]
            self.enemyImageLabel['state'] = DISABLED
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

    def resetForge(self):
        main.resetForge()
        self.v3.set(-1)
        self.anvilButton.config(state=DISABLED, relief=FLAT, cursor="")
        self.crucible.config(state=DISABLED)
        for i, button in enumerate(self.forgeButtons):
            button.config(image=noItemImage, text="Select an item to %s" % (
                "upgrade" if i == 0 else "sacrifice"), state=NORMAL)
        self.forgeSuccess.grid_remove()

    def strikeAnvil(self):
        insertText = window.bottomFrame.bottomLeftFrame.insertOutput
        fiddle = 0
        if self.strikeAnvilCallback is not None:
            root.after_cancel(self.strikeAnvilCallback)
            self.strikeAnvilCallback = None
            insertText("You strike the anvil with the Hammer of Hephaestus.")
            fiddle = main.forge.fiddleWithSuccess()
            self.forgeSuccess['text'] = "Success chance: %s%%" % (
                    main.forge.getSuccessChance())
        else:
            insertText("You stoke the flames of the crucible with your equipment and strike the anvil with the Hammer of Hephaestus.")
        main.sound.playSound(main.sound.sounds['Strike Anvil'][fiddle+5], interruptible=True)
        self.strikeAnvilCallback = root.after(875 + 125 * fiddle, self.upgradeForgeEquip)

    def upgradeForgeEquip(self):
        self.strikeAnvilCallback = None
        insertText = window.bottomFrame.bottomLeftFrame.insertOutput
        upgradedSuccessfully, interfaceActions = main.smith()
        window.gridUpgradeFrame(upgradedSuccessfully)
        updateInterface(interfaceActions)

    def cleanUpForge(self):
        self.v3.set(-1)
        self.anvilButton.config(state=DISABLED, relief=FLAT, cursor="")
        self.crucible.config(state=DISABLED)
        for button in self.forgeButtons:
            button.config(state=DISABLED)
        for button in self.forgeButtons[1:]:
            button.config(image=noItemImage)
        self.forgeSuccess.grid_remove()
        window.topFrame.topLeftFrame.placeButton['state'] = DISABLED

    def clickMissionLog(self):
        main.sound.playSound(main.sound.sounds['Open Log'])
        self.updateMissionLog()
        main.character.flags['Config']['Mission Log Open'] = self.showMissionLog.get()
        requireExitConfirmation(True)

    def updateMissionLog(self, on=None):
        if on is not False and self.showMissionLog.get() or on:
            window.sideFrame.grid()
            root.geometry(str(WINDOW_WIDTH+FRAME_C_WIDTH)+"x"+str(WINDOW_HEIGHT))
        else:
            window.sideFrame.grid_remove()
            root.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))


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
        self.outputBox.tag_config("dialogue", foreground=BROWN)
        self.outputBox.tag_config("gan", foreground=CYAN)
        self.outputBox.tag_config("toshe", foreground=RED)
        self.outputBox.tag_config("qendresa", foreground=DARKORANGE)
        self.outputBox.tag_config("barrie", foreground=BLUE)
        self.outputBox.tag_config("tomas tam", foreground=LIGHTRED)
        self.outputBox.tag_config("silvio", foreground=JADE)
        self.outputBox.tag_config("niplin", foreground=GREEN)
        self.outputBox.tag_config("riplin", foreground=MAGENTA)
        self.outputBox.insert(END,
            "Welcome. Click on me to embark on a quest.",
            ("grey", "highlight"))
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
        timestamp = "{dt:%I}:{dt.minute:02d} {dt:%p} on {dt:%B} {dt.day}, {dt.year}".format(dt = datetime.now())
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
        self.outputBox.tag_remove("dialogue", 1.0, END)
        self.outputBox.tag_remove("gan", 1.0, END)
        self.outputBox.tag_remove("toshe", 1.0, END)
        self.outputBox.tag_remove("qendresa", 1.0, END)
        self.outputBox.tag_remove("barrie", 1.0, END)
        self.outputBox.tag_remove("tomas tam", 1.0, END)
        self.outputBox.tag_remove("silvio", 1.0, END)
        self.outputBox.tag_remove("niplin", 1.0, END)
        self.outputBox.tag_remove("riplin", 1.0, END)
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

    def clickCancelDropButton(self, event=None):
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
        main.sound.playSound(main.sound.sounds['Cancel'])

    def clickCancelForgetButton(self, event=None):
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
        main.sound.playSound(main.sound.sounds['Cancel'])

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
            window.topFrame.topRightFrame.updateOtherStats()
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
                self.okButton.invoke()
            elif bool(tempSelection):
                self.menuBox.selection_set(int(tempSelection[0]))

    def selectSkill(self, event=None):
        if self.menuBox['state'] != DISABLED:
            tempSelection = self.menuBox.curselection()
            self.menuBox.selection_clear(0, 'end')
            self.menuBox.selection_set(int(event.char)-1)
            if self.menuSelectionIsValid():
                self.skillButton['state'] = NORMAL
                self.skillButton.invoke()
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


def makeItemButtons(master, var, inStore, rows=3):
    """Create 9 buttons to represent either inventory or store items.

    inStore indicates that the buttons are being made in the store frame if its
    value is 1.
    """
    itemButtons = []
    commands = [displayItemStats, displayStoreItemStats]
    sidePx = 64 if rows == 3 else 45
    for i in range(0, rows):
        for j in range(0, rows):
            itemButton = Radiobutton(master, image=defaultImage,
                                     variable=var, value=i*rows+j, width=sidePx,
                                     height=sidePx, bg=BLACK, indicatoron=0,
                                     bd=4, command=commands[inStore])
            itemButton.grid(row=i, column=j)
            itemButtons.append(itemButton)
    return itemButtons


def displayItemStats():
    """Display the stats of the selected item in the Inventory frame."""
    frame = window.topFrame.topLeftFrame
    item = main.character.items[frame.v1.get()]
    
    remainingWords = item.displayName.split(" ")
    abbreviatedPortion = ""
    truncatedName = abbreviatedPortion + " ".join(remainingWords)
    while len(truncatedName) > 30 and len(remainingWords) > 1:
        abbreviatedWord = "%s. " % remainingWords[0][0]
        abbreviatedPortion += abbreviatedWord
        remainingWords = remainingWords[1:]
        truncatedName = abbreviatedPortion + " ".join(remainingWords)
    frame.itemNameLabel.config(text=truncatedName, font=italicFont2)
    
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

    if main.character.specialization != "Scallywag" and (
        (item.CATEGORY == "Bow" and
         main.character.equippedWeapon is not item and 
         main.character.equippedShield.NAME != "Nothing") or
        (item.CATEGORY == "Shield" and
         main.character.equippedShield is not item and
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
        main.character.specialization != "Scallywag" and
        (item.CATEGORY == "Bow" and
         main.character.equippedWeapon is not item and 
         main.character.equippedShield.NAME != "Nothing" or
         item.CATEGORY == "Shield" and
         main.character.equippedShield is not item and
         main.character.equippedWeapon.CATEGORY == "Bow")):
        frame.equipButton['state'] = DISABLED
    else:
        frame.equipButton['state'] = NORMAL

    frame.dropButton['state'] = NORMAL

    if ( item.CATEGORY != "Miscellaneous" and
         window.topFrame.topRightFrame.v3.get() != -1):
        frame.placeButton['state'] = NORMAL
    else:
        frame.placeButton['state'] = DISABLED

    main.sound.playSound(main.sound.sounds['Select Item'])


def displayStoreItemStats():
    """Display the stats of the selected item in the Store frame."""
    frame = window.topFrame.topRightFrame
    item = main.store[frame.v2.get()]

    remainingWords = item.displayName.split(" ")
    abbreviatedPortion = ""
    truncatedName = abbreviatedPortion + " ".join(remainingWords)
    while len(truncatedName) > 30 and len(remainingWords) > 1:
        abbreviatedWord = "%s. " % remainingWords[0][0]
        abbreviatedPortion += abbreviatedWord
        remainingWords = remainingWords[1:]
        truncatedName = abbreviatedPortion + " ".join(remainingWords)
    frame.itemNameLabel.config(text=truncatedName, font=italicFont2)
    
    frame.itemCategoryLabel['text'] = item.CATEGORY
    
    frame.itemValueLabel['text'] = "%d / %d Euros" % (item.PRICE,
                                                      main.character.euros)
    
    if item.CATEGORY == "Miscellaneous":
        frame.itemRequirementLabel['font'] = italicFont1
        if "*" not in item.INFORMATION:
            frame.itemRequirementLabel['text'] = item.INFORMATION
        elif "*" in item.INFORMATION:
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

    if main.character.euros < item.PRICE or not main.character.hasRoom() and item.NAME != "Chasmic Rucksack":
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

    global hitBoxes
    global hitBoxTriggers

    bottomRightFrame = window.bottomFrame.bottomRightFrame
    topRightFrame = window.topFrame.topRightFrame
    topCenterFrame = window.topFrame.topCenterFrame
    bottomLeftFrame = window.bottomFrame.bottomLeftFrame
        
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
            updateLoadingScreen(*displayLoadingScreen())
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
            bottomRightFrame.bindChoices()
            window.gameFrame.grid()
            topRightFrame.updateMissionLog()
        topCenterFrame.areaButton['image'] =\
            areaImages[areaName][updates['image index']]

    bottomLeftFrame.unhighlightOutputBox()
    topCenterFrame.changeTitle(main.currentArea.name)
    views[updates['view']]()

    hasLeveledUp = False
    while main.character.hasLeveledUp():
        hasLeveledUp = True
        if not updates['text']:
            updates['text'] = ""
        updates['text'] += "\nToshe has reached level "+str(
            main.character.level)+"!"
        window.gridLevelUpFrame()
        window.levelUpLabel['text'] = "LEVEL %d!" % main.character.level
    if hasLeveledUp:
        main.sound.playSound(main.sound.sounds['Level Up'])

    if main.character.specialization is not None:
        hasSpecializedUp = False
        while main.character.hasSpecializedUp():
            hasSpecializedUp = True
            if not updates['text']:
                updates['text'] = ""
            updates['text'] += "\nToshe is now %s %s rank %s!" % (
                "an" if main.character.specialization[0]
                    in ("A", "E", "I", "O", "U") else "a",
                main.character.specialization,
                main.character.mastery)
            window.gridPowerUpFrame()
        if hasSpecializedUp:
            main.sound.playSound(main.sound.sounds['Power Up'])

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
        updates['menu'] = ["Restart from last save."]
        if main.character.checkpoint:
            updates['menu'].append("Restart in town.")
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
        def eachWordIsCapitalized(string):
            for word in string.split(" "):
                if not word[0].isupper():
                    return False
            return True
        def getTag(speaker):
            if speaker.lower() in [
                "gan",
                "toshe",
                "qendresa",
                "barrie",
                "tomas tam",
                "silvio",
                "niplin",
                "riplin",
            ]:
                return speaker.lower()
            else:
                return "dialogue"
        for line in updates['text'].split("\n"):
            if len(line.split(":")) > 1:
                possibleName = line.split(":")[0]
                if ( not any([punc in possibleName for punc in ".!?"]) and
                     eachWordIsCapitalized(possibleName)):
                    bottomLeftFrame.insertOutput(line, getTag(possibleName))
                    continue
            bottomLeftFrame.insertOutput(line)
        if 'format text' in updates:
            bottomLeftFrame.insertOutput(updates['format text'])
    if ('italic text' in updates) and (updates['italic text'] is not None):
        bottomLeftFrame.insertOutput(updates['italic text'], "italicize")
    if ('map' in updates and
         topCenterFrame.showMap.get() and
         'game over' != updates['view']):
        topCenterFrame.updateMap()
    if ('hits' in updates):
        def createDelayedHitBox(delay, hit):
            if hit['Target'] == "Toshe":
                parent = window.topFrame.topLeftFrame.vitalStats
                boundaryWidget = window.topFrame.topLeftFrame.tosheLabel
            elif hit['Target'] == "Enemy":
                parent = window.topFrame.topRightFrame.enemyStats
                boundaryWidget = window.topFrame.topRightFrame.enemyImageLabel
            number = hit['Number'] if "Number" in hit else None
            skill = hit['Skill'] if "Skill" in hit else False
            critical = hit['Critical'] if "Critical" in hit else False
            hitBoxTriggers.append(
                root.after(
                    delay,
                    lambda: hitBoxes.append(
                        createHitBox(parent,
                            boundaryWidget,
                            hit['Kind'],
                            number,
                            skill,
                            critical,
                            hit['Aux']))))
        tosheHits = filter(lambda hit: hit['Target'] == "Toshe", updates['hits'])
        enemyHits = filter(lambda hit: hit['Target'] == "Enemy", updates['hits'])
        for hits in [tosheHits, enemyHits]:
            for i, hit in enumerate(hits):
                createDelayedHitBox(int(i * 150 / len(hits)**0.5), hit)
        if any(filter(lambda hit: hit['Kind'] == "Bloody Attack", updates['hits'])):
            window.topFrame.topLeftFrame.animateToshe()
        if any(filter(lambda hit: hit['Kind'] == "Bloody Up", updates['hits'])):
            window.topFrame.topRightFrame.animateEnemy()
    elif updates['view'] != "battle":
        for box in hitBoxes:
            if box.next:
                root.after_cancel(box.next)
            box.destroy()
        hitBoxes = []
        for trigger in hitBoxTriggers:
            root.after_cancel(trigger)
        hitBoxTriggers = []
    if updates['view'] == "forge":
        topRightFrame.resetForge()
    if ('new quest' in updates):
        window.rightFrame.addMission(updates['new quest'])
        window.gridQuestFrame("MISSION!")
        if not topRightFrame.showMissionLog.get():
            topRightFrame.logButton.invoke()
    if ('completed quest' in updates):
        window.rightFrame.markMission(updates['completed quest'])
    if ('uncompleted quests' in updates):
        for quest in updates['uncompleted quests']:
            window.rightFrame.unmarkMission(quest)
    if ('remove quest' in updates):
        window.rightFrame.removeMission(updates['remove quest'])
        window.gridQuestFrame("MISSION\nCOMPLETE!")
    window.rightFrame.updateMissions()
    topRightFrame.updateOtherStats()
    requireExitConfirmation(True)
    if ('flash' in updates):
        lastState = topCenterFrame.areaButton['state']
        topCenterFrame.areaButton['state'] = NORMAL
        flash()
        topCenterFrame.areaButton['state'] = lastState
        

def enableTravelView():
    window.topFrame.topCenterFrame.areaButton['state'] = NORMAL
    leftFrame = window.topFrame.topLeftFrame
    rightFrame = window.topFrame.topRightFrame
    leftFrame.vitalStats.grid()
    leftFrame.inventory.grid_remove()
    rightFrame.otherStats.grid()
    rightFrame.enemyStats.grid_remove()
    rightFrame.store.grid_remove()
    rightFrame.forge.grid_remove()
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
    bottomFrame.centerButton.unbind_all('x')
    bottomFrame.centerButton.unbind_all('X')
    bottomFrame.centerButton.unbind_all('<BackSpace>')
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
    bottomFrame.centerButton.config(image=inventoryImage,
                                    command=bottomFrame.clickInventoryButton)
    bottomFrame.centerButton.grid(pady=(0, 34))
    bottomFrame.centerButton.bind_all('i', bottomFrame.clickInventoryButton)
    bottomFrame.centerButton.bind_all('I', bottomFrame.clickInventoryButton)
    bottomFrame.centerButton.unbind_all('x')
    bottomFrame.centerButton.unbind_all('X')
    bottomFrame.centerButton.unbind_all('<BackSpace>')
    bottomFrame.attackButton.grid()
    bottomFrame.defendButton.grid()
    bottomFrame.fleeButton.grid()
    bottomFrame.skillButton.grid()
    
    bottomFrame.enableMenuBox()
    bottomFrame.bindSkills()
    
    skills = []
    for skill in main.character.skills:
        skills.append(skill.NAME)
    if len(skills) != bottomFrame.menuBox.size() or len(filter(lambda skill:
        skill in bottomFrame.menuBox.get(0, bottomFrame.menuBox.size()-1),
        skills)) < len(skills):
        bottomFrame.modifyMenu(skills)
    if not bottomFrame.menuSelectionIsValid():
        bottomFrame.skillButton['state'] = DISABLED


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
    def selectGameOverOption(event=None):
        [
            topFrame.loadFile,
            topFrame.restoreFile,
        ][int(bottomFrame.menuBox.curselection()[0])]()

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
    bottomFrame.okButton.grid()
    bottomFrame.okButton['state'] = DISABLED
    bottomFrame.okButton['command'] = selectGameOverOption
    bottomFrame.centerButton['state'] = DISABLED
    bottomFrame.menuBox.unbind_all('1')
    bottomFrame.menuBox.unbind_all('2')
    bottomFrame.menuBox.unbind_all('3')
    bottomFrame.menuBox.unbind_all('4')
    window.topFrame.topRightFrame.potionButton['state'] = DISABLED
    window.topFrame.topCenterFrame.areaButton.grid()
    window.topFrame.topCenterFrame.map.grid_remove()
    window.topFrame.topCenterFrame.mapButton['state'] = DISABLED
    window.topFrame.topCenterFrame.mapButton.grid_remove()
    
    window.topFrame.topLeftFrame.updateVitalStats()
    window.topFrame.topRightFrame.updateEnemyStats()


def enableLoadingView():
    window.topFrame.topRightFrame.updateMissionLog(False)
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
    rightFrame.forge.grid_remove()
    rightFrame.store.grid_remove()
    leftFrame.updateInventory()

    leftFrame.sellButton.grid_remove()
    leftFrame.dropButton.grid_remove()
    leftFrame.placeButton.grid_remove()
    leftFrame.equipButton.grid()
    leftFrame.equipButton['state'] = DISABLED
    bottomFrame.skillButton['state'] = DISABLED


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
    rightFrame.updateStore()

    leftFrame.equipButton.grid_remove()
    leftFrame.dropButton.grid_remove()
    leftFrame.placeButton.grid_remove()
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
    bottomFrame.centerButton.unbind_all('x')
    bottomFrame.centerButton.unbind_all('X')
    bottomFrame.centerButton.unbind_all('<BackSpace>')
    bottomFrame.centerButton.bind_all('i', bottomFrame.clickInventoryButton)
    bottomFrame.centerButton.bind_all('I', bottomFrame.clickInventoryButton)


def enableDropItemView():
    enableInventoryView()
    window.topFrame.topCenterFrame.areaButton['state'] = DISABLED
    leftFrame = window.topFrame.topLeftFrame
    leftFrame.equipButton.grid_remove()
    leftFrame.sellButton.grid_remove()
    leftFrame.placeButton.grid_remove()
    leftFrame.dropButton.grid()
    leftFrame.dropButton['state'] = DISABLED

    bottomFrame = window.bottomFrame.bottomRightFrame
    bottomFrame.okButton['state'] = DISABLED
    bottomFrame.attackButton.grid_remove()
    bottomFrame.defendButton.grid_remove()
    bottomFrame.fleeButton.grid_remove()
    bottomFrame.centerButton.config(state=NORMAL, image=cancelImage,
                                    command=bottomFrame.clickCancelDropButton)
    bottomFrame.centerButton.unbind_all('i')
    bottomFrame.centerButton.unbind_all('I')
    bottomFrame.centerButton.bind_all('x', bottomFrame.clickCancelDropButton)
    bottomFrame.centerButton.bind_all('X', bottomFrame.clickCancelDropButton)
    bottomFrame.centerButton.bind_all('<BackSpace>', bottomFrame.clickCancelDropButton)
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
    bottomFrame.centerButton.config(state=NORMAL, image=cancelImage,
                                    command=bottomFrame.clickCancelForgetButton)
    bottomFrame.centerButton.unbind_all('i')
    bottomFrame.centerButton.unbind_all('I')
    bottomFrame.centerButton.bind_all('x', bottomFrame.clickCancelForgetButton)
    bottomFrame.centerButton.bind_all('X', bottomFrame.clickCancelForgetButton)
    bottomFrame.centerButton.bind_all('<BackSpace>', bottomFrame.clickCancelForgetButton)
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


def enableForgeView():
    window.topFrame.topCenterFrame.areaButton['state'] = NORMAL

    leftFrame = window.topFrame.topLeftFrame
    leftFrame.vitalStats.grid_remove()
    leftFrame.equipButton.grid_remove()
    leftFrame.sellButton.grid_remove()
    leftFrame.dropButton.grid_remove()
    leftFrame.inventory.grid()
    leftFrame.updateInventory()
    leftFrame.placeButton.grid()
    leftFrame.placeButton['state'] = DISABLED

    rightFrame = window.topFrame.topRightFrame
    rightFrame.forge.grid()


def enableForgeDoneView():
    enableForgeView()
    window.topFrame.topRightFrame.cleanUpForge()


def hideSideGameFrames():
    leftFrame = window.topFrame.topLeftFrame
    rightFrame = window.topFrame.topRightFrame
    leftFrame.vitalStats.grid_remove()
    leftFrame.inventory.grid_remove()
    rightFrame.otherStats.grid_remove()
    rightFrame.enemyStats.grid_remove()
    rightFrame.store.grid_remove()
    rightFrame.forge.grid_remove()


def hideSideIntroFrames():
    leftFrame = window.topFrame.topLeftFrame
    rightFrame = window.topFrame.topRightFrame
    leftFrame.recentGames.grid_remove()


def close(event=None):
    if requireExitConfirmation():
        canSave = (window.topFrame.topCenterFrame.areaButton['state'] == NORMAL
                   and main.view != "game over")
        main.sound.playSound(main.sound.sounds['Open Dialog'])
        if canSave:
            answer = tkMessageBox.askyesnocancel(
                "Save and exit",
                "Do you want to save the game?",
                parent=root)
            if answer is None:
                return
            elif answer:
                main.saveGame(True)
        elif main.view != "game over":
            if "no" == tkMessageBox.askquestion(
                 "Exit without saving?",
                 "You can't save right now. Are you sure you want to quit?",
                 icon="warning",
                 parent=root):
                return

    root.destroy()


def displayLoadingScreen():
    global loadProgress
    loadProgress = 0
    frame = Frame(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=DEFAULT_BG,
        bd=4, relief=SUNKEN)
    frame.grid(row=0)
    frame.grid_propagate(0)
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)
    loadingText = random.choice([
        "Blub blub.",
        "Yaouw!",
        "Let the adventure begin...",
        "I have been waiting for you.",
        "Please be patient. I am a little slow.",
        "Let me get everything ready for you.",
        "Dry your feet on the mat, please.",
        "It seems as though my loading bar has become uncalibrated.",
        "You caught me by surprise! Where did I leave my shell?",
        "Brace yourself.",
        "I can smell your scents of adventure.",])
    loadingBar = Label(frame, bg=DEFAULT_BG, relief=SUNKEN, bd=1)
    loadingBar.grid(row=0)
    loadingLabel = Label(frame, bg=DEFAULT_BG, font=font1, text=loadingText)
    loadingLabel.grid(row=0, pady=(0, 50))
    return (frame, loadingBar)


def updateLoadingScreen(frame, loadingBar):
    loadingBar['image'] = xpBars[
        int(loadProgress / FULL_PROGRESS * (NUMBER_OF_BARS - 1))]
    if loadProgress == FULL_PROGRESS:
        frame.grid_forget()
        frame.destroy()
    else:
        root.after(30, updateLoadingScreen, frame, loadingBar)
        
        
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
    updateLoadingScreen(*displayLoadingScreen())
    loadAssets()
    
    global window
    window = Window(root)
    hideSideGameFrames()
    main.sound.playMusic(main.sound.songs['Intro Theme'])
    
    
def requireExitConfirmation(yes=None):
    global askToSave
    if yes is None:
        return askToSave
    else:
        askToSave = yes


def createHitBox(parent,
                 boundaryWidget,
                 kind,
                 number=0,
                 skill=False,
                 critical=False,
                 aux=False):
    def raiseHitBox(hitBox, height, motion):
        hitBoxMaxHeight = 32
        hitBox.grid(pady=(height if motion[0] == "D" else 0,
                          height if motion[0] == "U" else 0))
        if height > boundaryWidget.winfo_height() - hitBoxMaxHeight:
            hitBox.next = None
            hitBox.destroy()
        else:
            frameCount = 50.
            frameDuration = 20
            if "Linear" in motion:
                delta = boundaryWidget.winfo_height() / frameCount
                if delta >= 1:
                    # Smooth motion
                    delta = int(delta)
            elif "Ease" in motion:
                delta = (boundaryWidget.winfo_height() - height) / frameCount * 2
            hitBox.next = root.after(frameDuration,
                lambda: raiseHitBox(hitBox, height + delta, motion))
    fgs = {
        "Physical": DAMAGE_BOX_FG,
        "Heal": DAMAGE_BOX_FG,
        "Earth": EARTH_COLOR,
        "Water": WATER_COLOR,
        "Fire": FIRE_COLOR,
        "Frostfire": ENIGMATIC_COLOR,
        "Miss": BLACK,
        "Block": DAMAGE_BOX_FG,
        "Parry": DAMAGE_BOX_FG,
        "Boost": DAMAGE_BOX_FG,

        "Grounded": BLACK,
        "Poisoned": BLACK,
        "Paralyzed": BLACK,
        "Drowned": BLACK,
        "Frozen": BLACK,
        "Petrified": BLACK,
        "Sundered": BLACK,
        "Burning": BLACK,
    }
    bgs = {
        "Physical": DAMAGE_BOX_BG,
        "Heal": HEAL_BOX_BG,
        "Earth": DAMAGE_BOX_BG,
        "Water": DAMAGE_BOX_BG,
        "Fire": DAMAGE_BOX_BG,
        "Frostfire": DAMAGE_BOX_BG,
        "Miss": WHITE,
        "Block": GREY,
        "Parry": GREY,
        "Boost": GREY,

        "Grounded": EARTH_COLOR,
        "Poisoned": POISON_COLOR,
        "Paralyzed": LIGHTNING_COLOR,
        "Drowned": WATER_COLOR,
        "Frozen": ICE_COLOR,
        "Petrified": PETRIFICATION_COLOR,
        "Sundered": SUNDERED_BG,
        "Burning": FIRE_COLOR,
    }
    misses = set([
        "Miss",
        "Block",
        "Parry",
        "Boost",
    ])
    ailments = set([
        "Grounded",
        "Poisoned",
        "Paralyzed",
        "Drowned",
        "Frozen",
        "Petrified",
        "Sundered",
        "Burning",
    ])
    healing = set([
        "Heal"
    ])
    font = lightFont8
    if critical:
        if aux:
            font = boldFont2
        else:
            font = font8
    elif kind == "Miss":
        if aux:
            font = font1
        else:
            font = font4
    elif aux:
        font = font2
    hitBox = Frame(parent,
                   bg=SKILL_BG if skill else bgs[kind]
                      if number or kind in misses | ailments | healing
                      else GREY,
                   relief=RIDGE,
                   bd=2)
    hitLabel = Label(hitBox,
                     text=("%s!" % kind) if kind in
                          misses | ailments else number,
                     font=font,
                     fg=fgs[kind],
                     bg=bgs[kind]
                        if number or kind in misses | ailments | healing
                        else GREY,
                     bd=0,
                     padx=2).grid()
    hitBoxMaxWidth = 64
    pad = random.randint(0, min(boundaryWidget.winfo_width(), 190) - hitBoxMaxWidth)
    if random.randrange(100) < 50:
        padx = (pad, 0)
    else:
        padx = (0, pad)
    hitBox.grid(row=boundaryWidget.grid_info()['row'], columnspan=2, padx=padx)
    motion = "Up/Ease"
    if kind in misses:
        motion = "Down/Linear"
    elif kind in ailments:
        motion = "Up/Linear"
    raiseHitBox(hitBox, 0, motion)
    return hitBox

main = Main()

WINDOW_WIDTH = 822
WINDOW_HEIGHT = 642
FRAME_C_WIDTH = 233
FRAME_C_HEIGHT = 426

NUMBER_OF_BARS = 46

BEIGE = "#ebdec0"
MEDIUMBEIGE = "#E5D7B7"
DARKBEIGE = "#d1c29d"
BROWN = "#704F16"
LIGHTBEIGE = "#f4ead2"
RED = "#90000d"
LIGHTRED = "#d31524"
GREEN = "#009037"
CYAN = "#24828b"
LIGHTCYAN = "#7bb4b9"
BLACK = "#000000"
BLUE = "#1250ac"
GREY = "#888888"
YELLOW = "#daa520"
WHITE = "#f4f4f4"
NAVY = "#000050"
PURPLE = "#26065c"
LIGHTPURPLE = "#9c76c7"
MAGENTA = "#de6ef1"
ORANGE = "#f8b681"
DARKORANGE = "#a33c00"
JADE = "#426e5b"
LIGHTJADE = "#83ccab"
EARTH_COLOR = "#b5e080"
WATER_COLOR = "#a7d3e8"
FIRE_COLOR = "#e6ba90"
ENIGMATIC_COLOR = "#e2afc9"
POISON_COLOR = "#befa46"
LIGHTNING_COLOR = "#f2f2aa"
ICE_COLOR = "#c0f0f0"
PETRIFICATION_COLOR = "#ded4ca"

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
QUEST_BG = BROWN
QUEST_FG = DARKBEIGE
MYSTIC_BG = PURPLE
MYSTIC_FG = MAGENTA
MYSTIC_FG2 = LIGHTPURPLE
SKILL_BG = ORANGE
SKILL_FG = DARKORANGE
UPGRADE_BG = JADE
UPGRADE_FG = LIGHTJADE
FAILURE_BG = BLACK
FAILURE_FG = GREY
COMMON_BD = BROWN
RARE_BD = YELLOW
LEGENDARY_BD = ORANGE
DAMAGE_BOX_FG = WHITE
DAMAGE_BOX_BG = RED
HEAL_BOX_BG = GREEN
SUNDERED_BG = DARKBEIGE
LEVEL_BG = LIGHTCYAN

root = Tk()

# Initialize variables
font1 = tkFont.Font(family="Garamond", size=10)
italicFont1 = tkFont.Font(family="Garamond", size=10, slant="italic")
boldFont1 = tkFont.Font(family="Garamond", size=10, weight="bold")
font2 = tkFont.Font(family="Garamond", size=11)
italicFont2 = tkFont.Font(family="Garamond", size=11, slant="italic", weight="bold")
boldFont2 = tkFont.Font(family="Garamond", size=11, weight="bold")
font3 = tkFont.Font(family="Garamond", size=12, weight="bold")
font4 = tkFont.Font(family="Garamond", size=14)
italicFont4 = tkFont.Font(family="Garamond", size=14, slant="italic")
font5 = tkFont.Font(family="Garamond", size=80, weight="bold")
font6 = tkFont.Font(family="Garamond", size=18)
font7 = tkFont.Font(family="Garamond", size=66, weight="bold")
font8 = tkFont.Font(family="Garamond", size=16, weight="bold")
lightFont8 = tkFont.Font(family="Garamond", size=16)

welcomeImage = PhotoImage(file="images\\other\\turtle.gif")
tosheImage = PhotoImage(file="images\\other\\toshe.gif")
bloodDropImages = [PhotoImage(file="images\\other\\blood_drop%s.gif" % (i+1))
    for i in range(3)]
bloodSlashImages = [PhotoImage(file="images\\other\\blood_slash%s.gif" % (i+1))
    for i in range(4)]
gameOverImage = PhotoImage(file="images\\other\\gameover.gif")

euroImage = PhotoImage(file="images\\icons\\euro.gif")
potionImage = PhotoImage(file="images\\icons\\potion.gif")
logImage = PhotoImage(file="images\\icons\\mission log.gif")
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
cancelImage = PhotoImage(file="images\\icons\\cancel.gif")
attackImage = PhotoImage(file="images\\icons\\attack.gif")
defendImage = PhotoImage(file="images\\icons\\defend.gif")
fleeImage = PhotoImage(file="images\\icons\\flee.gif")

noItemImage = PhotoImage(file="images\\other\\empty.gif")
defaultImage = PhotoImage(file="images\\other\\default.gif")

anvilImage = PhotoImage(file="images\\other\\anvil.gif")
crucibleImage = PhotoImage(file="images\\other\\crucible.gif")

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
         'forge': enableForgeView,
         'forge done': enableForgeDoneView,
         'battle over': enableBattleOverView,
         'game over': enableGameOverView}

askToSave = False

hitBoxes = []
hitBoxTriggers = []

root.protocol('WM_DELETE_WINDOW', close)
root.iconbitmap("images\\icons\\tq.ico")
root.title("Toshe's Quest II")
root.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT)+"+"+str(root.winfo_screenwidth()/2-WINDOW_WIDTH/2)+"+"+str(root.winfo_screenheight()/2-WINDOW_HEIGHT/2))
root.resizable(0, 0)
root.after(0, loadGame)
root.update()
root.mainloop()
