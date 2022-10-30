"""
File: TUAStatics.py
Author: Ben Gardner
Created: May 25, 2020
Created: October 30, 2022
"""


class Static:
    ICAS = [
        "Ica 1",
        "Ica 2",
        "Ica 3",
        "Ica 4",
        "Ica 5",
        "Ica 6",
        "Ica 7"
    ]
    ICA_DATA = {
        "Ica 1": {'area': "Herceg Fields",
                  'coordinates': (6, 1)},
        "Ica 2": {'area': "Mojkovac Summit",
                  'coordinates': (3, 3)},
        "Ica 3": {'area': "Eastern Kosovo",
                  'coordinates': (1, 1)},
        "Ica 4": {'area': "Greece",
                  'coordinates': (1, 1)},
        "Ica 5": {'area': "Dune Hots Peak",
                  'coordinates': (1, 10)},
        "Ica 6": {'area': "Fartooq Hold",
                  'coordinates': (1, 7)},
        "Ica 7": {'area': "Simellierm Pit",
                  'coordinates': (1, 4)}
    }
    
    class HexColors:
        SEA_FLOOR = "#3aadd4"
        DEEP_WATER = "#185294"
        WOOD = "#ca7c37"
        WATER = "#b6dfff"
        SAND_PATH = "#f7f38d"
        SKY = "#dcedee"
        TOWN_PATH = "#e2c86b"
        HERCEG_WALL = "#f8ebbe"
        DIRT_PATH = "#7d501f"
        IGALO_WALL = "#c5bfe1"
        PLAINS = "#9bec88"
        FOREST = "#4cba32"
        LIT_PATH = "#fceb5a"
        DARKNESS = "#3c3c3c"
        STONE_MOUNTAIN = "#d1d8d6"
        FIRE_PATH = "#ff6826"
        BURNT_WALL = "#5f392d"
        LAB_WALL = "#baa4b6"
        ROCK_WALL = "#d7c9a8"
        PEC_WALL = ROCK_WALL
        PRISTINA_WALL = "#f2dbf2"
        TRAF_CAFE_PATH = "#e5198e"
        TRAF_CAFE_WALL = "#f5cfe2"
        STONE_PATH = "#626258"
        RUINS_PATH = "#fde68e"
        ALBANIAN_PATH = "#e98a1a"
        ALBANIAN_DUNES = "#e8d0b4"
        CASTLE_PATH = "#db6e3f"
        CASTLE_WALL = "#f6cc84"
        MEADOW = "#59ea37"
        ATHENS_WALL = "#f3d3b9"
        MACEDONIA = "#a5aae6"
        ICE = "#ffffff"
        THIN_ICE = "#f0f8ff"
        LAIR = "#747799"
        
    
    AREA_COLORS = {
        "Adriatic Sea": {
            "fg": HexColors.SEA_FLOOR,
            "bg": HexColors.DEEP_WATER},
        "Boat at Sea": {
            "fg": HexColors.WOOD,
            "bg": HexColors.WATER},
        "Kismet II": {
            "fg": HexColors.WOOD,
            "bg": HexColors.DEEP_WATER},
        "Bay of Kotor": {
            "fg": HexColors.SAND_PATH,
            "bg": HexColors.WATER},
        "Herceg Novi": {
            "fg": HexColors.TOWN_PATH,
            "bg": HexColors.HERCEG_WALL},
        "Herceg Bluffs": {
            "fg": HexColors.DIRT_PATH,
            "bg": HexColors.SKY},
        "Igalo": {
            "fg": HexColors.TOWN_PATH,
            "bg": HexColors.IGALO_WALL},
        "Herceg Fields": {
            "fg": HexColors.PLAINS,
            "bg": HexColors.FOREST},
        "Black Mountain": {
            "fg": HexColors.LIT_PATH,
            "bg": HexColors.DARKNESS},
        "Mojkovac Summit": {
            "fg": HexColors.FOREST,
            "bg": HexColors.SKY},
        "Mojkovac Valley": {
            "fg": HexColors.TOWN_PATH,
            "bg": HexColors.FOREST},
        "The Watchmaking Facility": {
            "fg": HexColors.WOOD,
            "bg": HexColors.BURNT_WALL},
        "Cemetery": {
            "fg": HexColors.STONE_MOUNTAIN,
            "bg": HexColors.FOREST},
        "Scutari Peninsula": {
            "fg": HexColors.WATER,
            "bg": HexColors.ROCK_WALL},
        "Western Kosovo": {
            "fg": HexColors.DIRT_PATH,
            "bg": HexColors.ROCK_WALL},
        "The Secret Laboratory": {
            "fg": HexColors.LIT_PATH,
            "bg": HexColors.LAB_WALL},
        "Pec": {
            "fg": HexColors.TOWN_PATH,
            "bg": HexColors.PEC_WALL},
        "Albanian Desert": {
            "fg": HexColors.ALBANIAN_PATH,
            "bg": HexColors.ALBANIAN_DUNES},
        "Eastern Kosovo": {
            "fg": HexColors.FOREST,
            "bg": HexColors.ROCK_WALL},
        "Pristina": {
            "fg": HexColors.TOWN_PATH,
            "bg": HexColors.PRISTINA_WALL},
        "Traf Cafe": {
            "fg": HexColors.TRAF_CAFE_PATH,
            "bg": HexColors.TRAF_CAFE_WALL},
        "Presidential Path": {
            "fg": HexColors.STONE_PATH,
            "bg": HexColors.STONE_MOUNTAIN},
        "Old Ruins": {
            "fg": HexColors.RUINS_PATH,
            "bg": HexColors.DARKNESS},
        "Rumadan Village": {
            "fg": HexColors.TOWN_PATH,
            "bg": HexColors.ALBANIAN_DUNES},
        "Rumadan Hideout": {
            "fg": HexColors.TOWN_PATH,
            "bg": HexColors.DARKNESS},
        "Berlusconi Castle": {
            "fg": HexColors.CASTLE_PATH,
            "bg": HexColors.CASTLE_WALL},
        "Hidden Passage": {
            "fg": HexColors.STONE_PATH,
            "bg": HexColors.DARKNESS},
        "Greek Plains": {
            "fg": HexColors.MEADOW,
            "bg": HexColors.FOREST},
        "Athens": {
            "fg": HexColors.TOWN_PATH,
            "bg": HexColors.ATHENS_WALL},
        "Coliseum": {
            "fg": HexColors.RUINS_PATH,
            "bg": HexColors.ATHENS_WALL},
        "Thessalonian Highlands": {
            "fg": HexColors.MEADOW,
            "bg": HexColors.STONE_MOUNTAIN},
        "Greek Fortress": {
            "fg": HexColors.CASTLE_PATH,
            "bg": HexColors.STONE_MOUNTAIN},
        "Macedonia": {
            "fg": HexColors.MACEDONIA,
            "bg": HexColors.SKY},
        "Golem Cavern": {
            "fg": HexColors.DIRT_PATH,
            "bg": HexColors.DARKNESS},
        "Simellierm Pit": {
            "fg": HexColors.FOREST,
            "bg": HexColors.DARKNESS},
        "Galijula": {
            "fg": HexColors.ICE,
            "bg": HexColors.WATER},
        "Fartooq Hold": {
            "fg": HexColors.THIN_ICE,
            "bg": HexColors.ICE},
        "Yaouw Volcano": {
            "fg": HexColors.FIRE_PATH,
            "bg": HexColors.DARKNESS},
        "Dune Hot's Peak": {
            "fg": HexColors.ALBANIAN_DUNES,
            "bg": HexColors.STONE_MOUNTAIN},
        "Lair of the Magi": {
            "fg": HexColors.LAIR,
            "bg": HexColors.DARKNESS},
    }
