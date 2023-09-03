from enums import Weapons, AmmoType, Rarity
from items import Sword, Axe, Shield, Bow, Mace, Dagger, Staff, Wand, Crossbow, Halberd, Hammer


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
        "image_path": './images/items/weapons/sword.png',
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
        "image_path": './images/items/weapons/axe.png',
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
        "image_path": './images/items/weapons/shield.jpg',
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
        "image_path": './images/items/weapons/bow.png',
        "slot": 'main_hand',
        "attack_power": 8,
        "defense_power": 2,
        "weapon_range": 10,
        "ammo_type": AmmoType.ARROW  # Assuming you have an ARROW in your AmmoType Enum
    },
    Weapons.MACE: {
        "class": Mace,
        "value": 40,
        "image_path": './images/items/weapons/mace.png',
        "slot": 'main_hand',
        "attack_power": 12,
        "defense_power": 2,
        "weapon_range": 1,
        "spike_length": 5
    },

    Weapons.DAGGER: {
        "class": Dagger,
        "value": 25,
        "image_path": './images/items/weapons/dagger.png',
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
        "image_path": './images/items/weapons/staff.jpg',
        "slot": 'main_hand',
        "attack_power": 5,
        "defense_power": 3,
        "weapon_range": 2
    },

    Weapons.WAND: {
        "class": Wand,
        "value": 30,
        "image_path": './images/items/weapons/wand.png',
        "slot": 'main_hand',
        "attack_power": 8,
        "defense_power": 1,
        "weapon_range": 3
    },

    Weapons.CROSSBOW: {
        "class": Crossbow,
        "value": 50,
        "image_path": './images/items/weapons/crossbow.png',
        "slot": 'main_hand',
        "attack_power": 14,
        "defense_power": 3,
        "weapon_range": 12,
        "ammo_type": AmmoType.BOLT  # Assuming you have a BOLT in your AmmoType Enum
    },

    Weapons.HALBERD: {
        "class": Halberd,
        "value": 50,
        "image_path": './images/items/weapons/halberd.jpg',
        "slot": 'main_hand',
        "attack_power": 16,
        "defense_power": 4,
        "blade_length": 15,
        "weapon_range": 2,
        "sharpness": 10
    },

    Weapons.HAMMER: {
        "class": Hammer,
        "value": 45,
        "image_path": './images/items/weapons/hammer.png',
        "slot": 'main_hand',
        "attack_power": 14,
        "defense_power": 5,
        "weapon_range": 1
    }
}
