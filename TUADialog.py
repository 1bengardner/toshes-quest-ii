"""
File: TUADialog.py
Author: Ben Gardner
Created: February 3, 2013
Revised: June 6, 2020
"""

from Tkinter import *
import tkMessageBox
import tkSimpleDialog


class OpenFileDialog(tkSimpleDialog.Dialog):
    """A dialog window asking the user the name of the file they want to create
    or open.
    """

    def body(self, master):
        self.iconbitmap("images\\icons\\tq.ico")
        Label(master, text=("Enter the name of the savefile you want to "+
                            "load/create.\n"+
                            "A new file will be created if it does not exist.")
              ).grid()
        validateInput = self.parent.register(self.isValid), '%d', '%s', '%S'
        self.entry = Entry(master,
                           validate="key", validatecommand=validateInput)
        self.entry.grid()
        self.entry.focus_set()

    def validate(self):
        if self.entry.get() == "":
            tkMessageBox.showerror(self.title(), "Please enter a name.")
            return 0
        try:
            open("saves\\"+self.entry.get()+".tq")
            return 1
        except IOError:
            if tkMessageBox.askokcancel("Create New | "+self.entry.get(), "Start a new game?",
                                        parent=self):
                return 1
            return 0
        
    def apply(self):
        self.entryValue = self.entry.get()

    def isValid(self, insertOrDelete, currentInput, newInput):
        invalidCharacters = set('\\/:*?"<>|.')
        if int(insertOrDelete) == 1 and len(currentInput) > 50:
            return False
        for c in newInput:
            if c in invalidCharacters:
                return False
        return True
