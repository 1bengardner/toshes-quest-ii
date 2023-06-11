"""
File: TUADialog.py
Author: Ben Gardner
Created: February 3, 2013
Revised: June 11, 2023
"""

import pickle
from Tkinter import *
import tkMessageBox
import tkSimpleDialog
from TUAPreferences import Preferences


class OpenFileDialog(tkSimpleDialog.Dialog):
    """A dialog window asking the user the name of the file they want to create
    or open.
    """

    def body(self, master):
        self.iconbitmap("images/icons/tq.ico")
        Label(master, text=("Enter the name of the character you want to load/create."+
                            "\nA new character will be created if it does not exist.")
              ).grid()
        validateInput = self.parent.register(self.isValid), '%d', '%s', '%S'
        self.entry = Entry(master,
                           validate="key", validatecommand=validateInput)
        self.entry.grid()
        return self.entry

    def validate(self):
        if self.entry.get() == "":
            tkMessageBox.showerror(self.title(), "Please enter a name.")
            return 0
        return 1
        
    def apply(self):
        self.fileName = self.entry.get().strip()

    def isValid(self, insertOrDelete, currentInput, newInput):
        validCharacters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 ,')
        if int(insertOrDelete) == 1 and len(currentInput) > 50:
            return False
        for c in newInput:
            if c not in validCharacters:
                return False
        return True

class NewGameDialog(tkSimpleDialog.Dialog):

    def body(self, master):
        self.iconbitmap("images/icons/tq.ico")
        import tkFont

        for fontFamily in ["Garamond", "Times"]:
            if fontFamily in tkFont.families():
                break
        titleFont = tkFont.Font(family=fontFamily, size=18)
        blurbFont = tkFont.Font(family=fontFamily, size=14, slant="italic")
        boldBlurb = tkFont.Font(family=fontFamily, size=14, slant="italic", weight="bold")
        modeFont = tkFont.Font(family=fontFamily, size=14)

        def updateBlurb():
            def getBlurb(character):
                return {
"Toshe":
    ", the eponymous warrior, uses his brawn to strike powerful blows.",
"Toshette":
    " has a high chance to land hits using quick and precise maneuvers.",
"Nome":
    " is smart. It doesn't look like it, but he's got wisdom beyond his ears.",
"Pyroshe":
    " hails from the depths of Yaouw. He can withstand fire damage.",
"Reese":
    " had a rough childhood and as a result he can take more hits.",
"Chris":
    " is always trying to show off, so he can use skills more often.",
"Toady":
    " has a natural defence against earth and water from his swampy upbringing.",
"Foxy":
    ", the Maine Coon, evades physical damage with her unpredictable movements.",
"Lily":
    " is protected by a thick layer of soil.",
"Gumball Machine":
    " can do anything.",
"M. Wizzard":
    " is resilient against magic of all kinds.",
"Apoc":
    " can mitigate attacks with his suit of armour.",
                }[character]
            blurb['state'] = NORMAL
            blurb.delete(1.0, END)
            blurb.insert(1.0, self.portraitVar.get(), ("bold"))
            blurb.insert(END, getBlurb(self.portraitVar.get()))
            blurb['state'] = DISABLED

        Label(master, text=("Choose Your Character"), font=titleFont
              ).grid(pady=6)
        portraitsFrame = Frame(master)
        portraitsFrame.grid()
        characters = [
            "Apoc",
            "Toshe",
            "Toshette",
            "Pyroshe",
            "Toady",
            "M. Wizzard",
            "Gumball Machine",
            "Nome",
            "Reese",
            "Chris",
            "Foxy",
            "Lily",
            "Hidden",
            "Unlocked",
        ]
        if not hasattr(NewGameDialog, "images"):
            NewGameDialog.images = {}
            for character in characters:
                NewGameDialog.images[character] = PhotoImage(file=("images/other/%s.gif" % character.replace(".", "")))
        width = 126
        height = 158
        rows = 2
        cols = 6
        self.portraitVar = StringVar()
        characterButtons = {}
        for i in range(0, rows):
            for j in range(0, cols):
                portraitName = characters[i*cols+j]
                characterButtons[portraitName] = Radiobutton(
                    portraitsFrame,
                    image=NewGameDialog.images[portraitName],
                    variable=self.portraitVar,
                    value=portraitName,
                    width=width,
                    height=height,
                    indicatoron=0,
                    bd=4,
                    bg="#0d0706",
                    command=updateBlurb,
                )
                characterButtons[portraitName].grid(row=i, column=j)
        def readUnlocks():
            try:
                with open("settings/unlocks.tqp", "r") as unlocksFile:
                    return pickle.load(unlocksFile).unlocks
            except IOError:
                return {}
        def writeUnlocks():
            preferences = Preferences()
            preferences.unlocks = unlocks
            with open("settings/unlocks.tqp", "w") as preferencesFile:
                pickle.dump(preferences, preferencesFile)
        def revealCharacter():
            character = self.portraitVar.get()
            self.portraitVar.set(None)
            characterButtons[character].flash()
            characterButtons[character].flash()
            self.portraitVar.set(character)
            characterButtons[character]['image'] = NewGameDialog.images[character]
            characterButtons[character]['command'] = updateBlurb
            characterButtons[character].invoke()
            unlocks[character] = False
            writeUnlocks()
        unlocks = readUnlocks()
        for character in ["Apoc", "M. Wizzard", "Gumball Machine", "Lily"]:
            if character in unlocks and unlocks[character]:
                characterButtons[character]['image'] = NewGameDialog.images["Unlocked"]
                characterButtons[character]['state'] = NORMAL
                characterButtons[character]['command'] = revealCharacter
            elif character not in unlocks:
                characterButtons[character]['image'] = NewGameDialog.images["Hidden"]
                characterButtons[character]['state'] = DISABLED

        blurb = Text(
            master,
            fg="#efece2",
            bg="#694138",
            height=1,
            font=blurbFont,
            wrap=WORD,
            bd=4,
            relief=RIDGE,
            state=DISABLED,
        )
        blurb.grid(sticky=EW)
        blurb.tag_config("bold", font=boldBlurb, justify='center')
        self.portraitVar.set("Toshe")
        updateBlurb()

        modeFrame = Frame(master)
        modeFrame.grid()
        self.modeVar = StringVar()
        Radiobutton(
            modeFrame,
            text="Easy Mode",
            font=modeFont,
            variable=self.modeVar,
            value="Easy",
            indicatoron=0,
            fg="#704F16",
            bg="#d1c29d",
            padx=8,
            pady=4,
            bd=4,
            width=12,
        ).grid(padx=6, pady=24)
        Radiobutton(
            modeFrame,
            text="Hard Mode",
            font=modeFont,
            variable=self.modeVar,
            value="Hard",
            indicatoron=0,
            fg="#704F16",
            bg="#daa520",
            padx=8,
            pady=4,
            bd=4,
            width=12,
        ).grid(padx=6, pady=24, row=0, column=1)
        if "Ultimate Mode" in unlocks:
            Radiobutton(
                modeFrame,
                text="Ultimate Mode",
                font=modeFont,
                variable=self.modeVar,
                value="Ultimate",
                indicatoron=0,
                fg="#704F16",
                bg="#e2afc9",
                padx=8,
                pady=4,
                bd=4,
                width=12,
            ).grid(padx=6, pady=24, row=0, column=2)
        self.modeVar.set("Easy")

    def apply(self):
        self.portrait = self.portraitVar.get()
        self.mode = self.modeVar.get()
        self.complete = True