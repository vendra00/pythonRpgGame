from utils.enums import Weapons, AmmoType, Rarity, SwordsImgPaths, AxesImgPaths, ShieldImgPaths, BowsImgPaths, \
    MacesImgPaths, DaggersImgPaths, StavesImgPaths, WandImgPaths, CrossBowsImgPaths, HalberdsImgPaths, WarHammerImgPaths
from model.items import Sword, Axe, Shield, Bow, Mace, Dagger, Staff, Wand, Crossbow, Halberd, Hammer


BASE_ITEM_ATTRIBUTES = {
    'name': 'Default Name',  # same here, you'd probably want a more dynamic approach
    'rarity': Rarity.COMMON,  # assuming you have a COMMON value in your Rarity enum
    'weight': 1,
    'thumbnail_path': './default/path.jpg',
    'durability': 100
}

ITEM_ATTRIBUTES = {
    Weapons.SWORD: {
        "class": Sword,
        "value": 35,
        "image_path": lambda: SwordsImgPaths.DEFAULT.value.path,
        "slot": 'main_hand',
        "attack_power": 10,
        "defense_power": 5,
        "weapon_range": 1,
        "blade_length": 10,
        "sharpness": 10
    },
    Weapons.AXE: {
        "class": Axe,
        "value": 40,
        "image_path": lambda: AxesImgPaths.DEFAULT.value.path,
        "slot": 'main_hand',
        "attack_power": 12,
        "defense_power": 4,
        "weapon_range": 1,
        "blade_length": 10,
        "sharpness": 8
    },
    Weapons.SHIELD: {
        "class": Shield,
        "value": 30,
        "image_path": lambda: ShieldImgPaths.DEFAULT.value,
        "slot": 'off_hand',
        "attack_power": 0,
        "defense_power": 10,
        "weapon_range": 0,
        "block_chance": 20,
        "block_power": 10
    },
    Weapons.BOW: {
        "class": Bow,
        "value": 45,
        "image_path": lambda: BowsImgPaths.DEFAULT.value,
        "slot": 'main_hand',
        "attack_power": 8,
        "defense_power": 2,
        "weapon_range": 10,
        "ammo_type": AmmoType.ARROW  # Assuming you have an ARROW in your AmmoType Enum
    },
    Weapons.MACE: {
        "class": Mace,
        "value": 40,
        "image_path": lambda: MacesImgPaths.DEFAULT.value.path,
        "slot": 'main_hand',
        "attack_power": 12,
        "defense_power": 2,
        "weapon_range": 1,
        "spike_length": 5
    },

    Weapons.DAGGER: {
        "class": Dagger,
        "value": 25,
        "image_path": lambda: DaggersImgPaths.DEFAULT.value.path,
        "slot": 'main_hand',
        "attack_power": 7,
        "defense_power": 3,
        "weapon_range": 1,
        "blade_length": 5,
        "sharpness": 12
    },
    Weapons.STAFF: {
        "class": Staff,
        "value": 25,
        "image_path": lambda: StavesImgPaths.DEFAULT.value.path,
        "slot": 'main_hand',
        "attack_power": 5,
        "defense_power": 3,
        "weapon_range": 2
    },

    Weapons.WAND: {
        "class": Wand,
        "value": 30,
        "image_path": lambda: WandImgPaths.DEFAULT.value.path,
        "slot": 'main_hand',
        "attack_power": 8,
        "defense_power": 1,
        "weapon_range": 3
    },

    Weapons.CROSSBOW: {
        "class": Crossbow,
        "value": 50,
        "image_path": lambda: CrossBowsImgPaths.DEFAULT.value.path,
        "slot": 'main_hand',
        "attack_power": 14,
        "defense_power": 3,
        "weapon_range": 12,
        "ammo_type": AmmoType.BOLT  # Assuming you have a BOLT in your AmmoType Enum
    },

    Weapons.HALBERD: {
        "class": Halberd,
        "value": 50,
        "image_path": lambda: HalberdsImgPaths.DEFAULT.value.path,
        "slot": 'main_hand',
        "attack_power": 16,
        "defense_power": 4,
        "weapon_range": 2
    },

    Weapons.HAMMER: {
        "class": Hammer,
        "value": 45,
        "image_path": lambda: WarHammerImgPaths.DEFAULT.value.path,
        "slot": 'main_hand',
        "attack_power": 14,
        "defense_power": 5,
        "weapon_range": 1
    }
}
