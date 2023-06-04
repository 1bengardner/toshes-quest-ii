# Toshe Save File Converter
# Updates 0.0-2.0 characters to 2.1

import pickle

def updateChangedAreaNames(character):
    changed = False
    changedAreas = [
        ("Herceg Fields",
         "Frolicking Fields"),
        ("Herceg Bluffs",
         "Billowing Bluffs"),
        ("Mojkovac Summit",
         "Summit of Presage"),
    ]
    for area in changedAreas:
        if area[0] in character.flags['Discovered Areas']:
            if area[1] not in character.flags['Discovered Areas']:
                character.flags['Discovered Areas'][area[1]] = character.flags['Discovered Areas'][area[0]]
                character.flags['Marked Areas'][area[1]] = character.flags['Marked Areas'][area[0]]
            del character.flags['Discovered Areas'][area[0]]
            del character.flags['Marked Areas'][area[0]]
            changed = True
    return changed

def update(gameFile, path):
    changed = False
    character = pickle.load(gameFile)
    if "Discovered Areas" not in character.flags:
        character.flags['Discovered Areas'] = {}
        changed = True
    if "Marked Areas" not in character.flags:
        character.flags['Marked Areas'] = {}
        changed = True
    if ( "Config" not in character.flags or
         "Automap On" not in character.flags['Config'] or
         "Mission Log Open" not in character.flags['Config']):
        character.flags['Config'] = dict()
        character.flags['Config']['Automap On'] = 1
        character.flags['Config']['Mission Log Open'] = 0
        changed = True
    for area in character.flags['Discovered Areas']:
        if area not in character.flags['Marked Areas']:
            character.flags['Marked Areas'][area] = set()
            changed = True
    if not hasattr(character, "LIVING"):
        setattr(character, "LIVING", 1)
        changed = True
    if not hasattr(character, "mercenaries"):
        changed = "error"
    else:
        for mercenary in character.mercenaries:
            setattr(mercenary, "LIVING", 1)
    if not hasattr(character, "potions"):
        setattr(character, "potions", 0)
        for mercenary in character.mercenaries:
            setattr(mercenary, "potions", 0)
        changed = True
    if not hasattr(character, "checkpoint"):
        setattr(character, "checkpoint", None)
        changed = True
    if not hasattr(character, "quests"):
        setattr(character, "quests", [])
        changed = True
    if not hasattr(character, "_specialization"):
        setattr(character, "_specialization", None)
        setattr(character, "mastery", 1)
        setattr(character, "sp", 0)
        setattr(character, "_maxHp", max(character.level * 20 + 80, character.hp))
        setattr(character, "_maxEp", max(character.level * 20 + 80, character.ep))
        for mercenary in character.mercenaries:
            setattr(mercenary, "_specialization", None)
            setattr(mercenary, "_maxHp", max(mercenary.level * 20 + 80, mercenary.hp))
            setattr(mercenary, "_maxEp", max(mercenary.level * 20 + 80, mercenary.ep))
        changed = True
    itemsToCheck = character.items
    if "Buyback Items" in character.flags:
        itemsToCheck += character.flags['Buyback Items']
    for item in filter(lambda item: item is not None, itemsToCheck):
        if item is not None and item.CATEGORY != "Miscellaneous" and not hasattr(item, "upgradeCount"):
            item.upgradeCount = 0
            changed = True
        if item.CATEGORY == "Club":
            item.CATEGORY = "Bludgeon"
            changed = True
    for skill in filter(lambda skill: skill is not None, character.skills):
        if skill.ELEMENT == "Electricity":
            skill.ELEMENT = "Lightning"
            changed = True
        if "Club" in skill.PERMITTED_WEAPONS:
            skill.PERMITTED_WEAPONS.add("Bludgeon")
            skill.PERMITTED_WEAPONS.remove("Club")
            changed = True
    changed = updateChangedAreaNames(character) or changed
    if changed:
        with open(path, "w") as gameFile:
            pickle.dump(character, gameFile)
        
    return changed

if __name__ == "__main__":
    try:
        print ("This program will update your character file from" +
               " version 0.0 or later to 2.0.")
        fileName = raw_input("What's the name of the character to update? ")

        try:
            path = "saves/"+fileName+".tq"
            with open(path, "r") as gameFile:
                changed = update(gameFile, path)
        except (IOError):
            try:
                path = "saves/"+fileName+".toshe"
                with open(path, "r") as gameFile:
                    changed = update(gameFile, fileName)
            except (IOError):
                raw_input("No .tq or .toshe file named %s was found." % fileName)
                exit()
        print
        if changed == "error":
            raw_input(fileName+" could not be updated. The file format is probably too old.")
        elif changed:
            raw_input(fileName+" got updated!")
        else:
            raw_input(fileName+" is already up to date.")

    except (IndexError, EOFError, KeyError):
        raw_input("\nThere was an error processing the character data." +
                  "\nYour savefile is probably corrupt.")
        raise
