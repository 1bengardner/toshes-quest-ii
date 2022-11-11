# Toshe Save File Converter
# Updates 0.0-1.0 characters to 2.0

import pickle

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
         "Automap On" not in character.flags['Config']):
        character.flags['Config'] = dict()
        character.flags['Config']['Automap On'] = 1
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
            
    with open(path, "w") as gameFile:
        pickle.dump(character, gameFile)
        
    return changed

if __name__ == "__main__":
    try:
        print ("This program will update your character file from" +
               " version 0.0 or later to 2.0.")
        fileName = raw_input("What's the name of the character to update? ")

        try:
            path = "saves\\"+fileName+".tq"
            with open(path, "r") as gameFile:
                update(gameFile, path)
        except:
            path = "saves\\"+fileName+".toshe"
            with open(path, "r") as gameFile:
                update(gameFile, fileName)
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
