"""
File: TUASkill.py
Author: Ben Gardner
Created: March 14, 2013
Revised: November 23, 2022
"""


class Skill:
    """Skill that can be used in battle.

    name: The name of the skill.
    category: The category the skill falls under in battle (e.g. damage,
    healing).
    permittedWeapons: Weapons that can be used in conjunction with the skill.
    epUsed: Amount of EP deducted when using this skill.
    multiplier: Amount by which to multiply the stat (in %).
    element: The type of elemental damage the skill deals, if any.
    userEffects: Any additional effects bestowed upon the user.
    targetEffects: Any additional effects the target will be afflicted by.
    text: Message to display in battle when the skill is used.
    flag: Name of a trigger that is set after this skill is used, if one exists.
    """

    def __init__(self, name, category, permittedWeapons, epUsed, multiplier,
                 element, userEffects, targetEffects, text, flag):
        self.NAME = str(name)
        self.CATEGORY = str(category)
        permittedWeapons = set(permittedWeapons)
        if "Melee" in permittedWeapons:
            permittedWeapons.remove("Melee")
            self.PERMITTED_WEAPONS = permittedWeapons |\
                                     set(["Sword", "Club", "Axe", "Spear"])
        elif "All" in permittedWeapons:
            permittedWeapons.remove("All")
            self.PERMITTED_WEAPONS = permittedWeapons |\
                                     set(["Sword", "Club", "Axe", "Spear",
                                          "Bow", "Wand", "Gun"])
        else:
            self.PERMITTED_WEAPONS = permittedWeapons
        self.EP_USED = int(epUsed)
        self.MULTIPLIER = int(multiplier)
        self.ELEMENT = str(element)
        self.USER_EFFECTS = dict(userEffects)
        self.TARGET_EFFECTS = dict(targetEffects)
        self.TEXT = str(text)
        self.FLAG = str(flag)
