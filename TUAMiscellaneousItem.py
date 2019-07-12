"""
File: TUAMiscellaneousItem.py
Author: Ben Gardner
Created: June 14, 2015
Revised: June 14, 2015
"""


class MiscellaneousItem:

    def __init__(self, name, price, info):
        self.NAME = str(name)
        self.IMAGE_NAME = self.NAME
        self.PRICE = int(price)
        self.SELL_PRICE = int(price)/4
        self.INFORMATION = str(info)
        self.CATEGORY = "Miscellaneous"
