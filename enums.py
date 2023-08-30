from enum import Enum, auto


class Weapons(Enum):
    AXE = auto()
    SWORD = auto()
    SHIELD = auto()
    MACE = auto()
    DAGGER = auto()
    STAFF = auto()
    WAND = auto()
    BOW = auto()
    CROSSBOW = auto()
    HALBERD = auto()
    HAMMER = auto()


class Consumables(Enum):
    POTION = auto()
    BANDAGE = auto()
    FOOD = auto()
    WATER = auto()
    BEER = auto()
    WINE = auto()


class Armor(Enum):
    HELMET = auto()
    CHEST_ARMOR = auto()
    LEGGINGS = auto()
    BOOTS = auto()
    GLOVES = auto()
    SHOULDER_PADS = auto()


class Accessories(Enum):
    RING = auto()
    NECKLACE = auto()
    BELT = auto()
    CAPE = auto()
    CLOAK = auto()
    BRACERS = auto()
    EARRINGS = auto()


class Items(Enum):
    WEAPONS = (Weapons, "Weapons")
    #ARMOR = (Armor, "Armor")
    #CONSUMABLES = (Consumables, "Consumables")
    #ACCESSORIES = (Accessories, "Accessories")

    # Add more items as needed

    def __init__(self, item_enum, name):
        self._enum_ = item_enum
        self._name_ = name


class Rarity(Enum):
    COMMON = ("Common", "#FFFFFF")  # White color for common items
    UNCOMMON = ("Uncommon", "#1EFF00")  # Green for uncommon items
    RARE = ("Rare", "#0070DD")  # Blue for rare items
    EPIC = ("Epic", "#A335EE")  # Purple for epic items
    LEGENDARY = ("Legendary", "#FF8000")  # Orange for legendary items
    MYTHIC = ("Mythic", "#FF0000")  # Red for mythic items

    def __init__(self, name, color):
        self._name_ = name
        self.color = color


class Effects(Enum):
    POISON = auto()
    BURN = auto()
    BLEED = auto()
    STUN = auto()
    SLOW = auto()
    CONFUSE = auto()
    FEAR = auto()
    SLEEP = auto()
    CHARM = auto()
    BLIND = auto()
    SILENCE = auto()
    ROOT = auto()
    KNOCKBACK = auto()
    KNOCKDOWN = auto()
    DISARM = auto()
    FREEZE = auto()
    PETRIFY = auto()
    CURSE = auto()
    HEX = auto()
    BANISH = auto()
    BLESS = auto()
    HEAL = auto()
    REGENERATE = auto()


class AmmoType(Enum):
    ARROW = auto()
    BOLT = auto()
