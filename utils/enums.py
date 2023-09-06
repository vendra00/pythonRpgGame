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

    # ARMOR = (Armor, "Armor")
    # CONSUMABLES = (Consumables, "Consumables")
    # ACCESSORIES = (Accessories, "Accessories")

    # Add more items as needed

    def __init__(self, item_enum, name):
        self._enum_ = item_enum
        self._name_ = name


class Rarity(Enum):
    COMMON = ("Common", "a4a4a4")  # White color for common items
    UNCOMMON = ("Uncommon", "#1EFF00")  # Green for uncommon items
    RARE = ("Rare", "#0070DD")  # Blue for rare items
    EPIC = ("Epic", "#A335EE")  # Purple for epic items
    LEGENDARY = ("Legendary", "#FF8000")  # Orange for legendary items
    MYTHIC = ("Mythic", "#FF0000")  # Red for mythic items

    def __init__(self, name, color):
        self._name_ = name
        self.color = color


class ItemTier(Enum):
    TIER_1 = ("Tier 1", 1),
    TIER_2 = ("Tier 2", 2),
    TIER_3 = ("Tier 3", 3),
    TIER_4 = ("Tier 4", 4),
    TIER_5 = ("Tier 5", 5),


class ItemSlot(Enum):
    HEAD = auto()
    CHEST = auto()
    LEGS = auto()
    FEET = auto()
    HANDS = auto()
    SHOULDERS = auto()
    RING = auto()
    NECK = auto()
    BELT = auto()
    CAPE = auto()
    CLOAK = auto()
    BRACERS = auto()
    EARRINGS = auto()
    MAIN_HAND = auto()
    OFF_HAND = auto()
    TWO_HAND = auto()

    def __init__(self, slot):
        self.slot = slot


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


class DamageType(Enum):
    PHYSICAL = auto()
    FIRE = auto()
    ICE = auto()
    LIGHTNING = auto()
    POISON = auto()
    HOLY = auto()
    UNHOLY = auto()
    ARCANE = auto()


class AmmoType(Enum):
    ARROW = auto()
    BOLT = auto()


class ItemActions(Enum):
    EQUIP = "Equip"
    UNEQUIP = "Unequip"
    USE = "Use"
    DROP = "Drop"
    REPAIR = "Repair"
    SELL = "Sell"
    BUY = "Buy"
    TRADE = "Trade"

    def __init__(self, action):
        self.action = action


class GameActions(Enum):
    BATTLE = "Battle"
    MOVE = "Move"
    INVENTORY = "Inventory"
    EXPLORE = "Explore"
    EXIT = "Exit"
    UP = "Up"
    DOWN = "Down"
    LEFT = "Left"
    RIGHT = "Right"

    def __init__(self, action):
        self.action = action


class MapElements(Enum):
    HERO = "hero"
    WALL = "wall"
    TREE = "tree"
    TREASURE_CHEST = "treasure_chest"

    def __init__(self, element):
        self.element = element


class KeyBindings(Enum):
    CLOSE = "<Escape>"
    ENTER = "<Return>"
    UP = "<Up>"
    DOWN = "<Down>"
    LEFT = "<Left>"
    RIGHT = "<Right>"
    INVENTORY = "i"

    def __init__(self, key):
        self.key = key


class BaseMovementCoordinates(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    def __init__(self, dx, dy):
        self.coordinate = (dx, dy)


class Sfx(Enum):
    WALK = "walk.mp3"
    PICK_UP = "pick_up_item.mp3"
    DROP = "drop_item.mp3"
    SELECTOR = "selector.mp3"

    def __init__(self, sfx):
        self.sfx_file = sfx


class MusicTrack(Enum):
    FORREST = "forrest.mp3"

    def __init__(self, track):
        self.track_file = track


class SoundPaths(Enum):
    SFX = (Sfx, "audio/sfx/")
    MUSIC = (MusicTrack, "audio/track/")

    def __init__(self, sound_enum, path):
        self.sound_enum = sound_enum
        self.path = path


class MonsterType(Enum):
    GOBLIN = ("Goblin", "./images/characters/enemy/goblin.png")
    ORC = ("Orc", "./images/characters/enemy/orc.png")
    DRAGON = ("Dragon", "./images/characters/enemy/dragon.png")
    TROLL = ("Troll", "./images/characters/enemy/troll.png")
    WITCH = ("Witch", "./images/characters/enemy/witch.png")

    def __new__(cls, monster_name, image_path):
        member = object.__new__(cls)
        member._value_ = monster_name
        member.image_path = image_path
        return member

    @property
    def name(self):
        return self._name_

    @property
    def value(self):
        return self._value_


class HeroesType(Enum):
    MALE = ("Sir lancelot", "./images/characters/heroes/default.png")
    FEMALE = ("Lady Joan", "./images/characters/heroes/hero.png")

    def __new__(cls, monster_name, image_path):
        member = object.__new__(cls)
        member._value_ = monster_name
        member.image_path = image_path
        return member

    @property
    def name(self):
        return self._name_

    @property
    def value(self):
        return self._value_
