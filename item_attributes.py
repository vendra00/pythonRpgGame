from enums import Weapons, AmmoType
from items import Sword, Axe, Shield, Bow, Mace, Dagger, Staff, Wand, Crossbow, Halberd, Hammer

ITEM_ATTRIBUTES = {
    Weapons.SWORD: {
        "class": Sword,
        "value": 35,
        "image_path": './images/item/weapons/sword.png',
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
        "image_path": './images/item/weapons/axe.png',
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
        "image_path": './images/item/weapons/shield.png',
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
        "image_path": './images/item/weapons/bow.png',
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
        "range_": 1,
        "spike_length": 5
    },

    Weapons.DAGGER: {
        "class": Dagger,
        "value": 25,
        "image_path": './images/item/weapons/dagger.png',
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
        "image_path": './images/items/weapons/staff.png',
        "slot": 'main_hand',
        "attack_power": 5,
        "range_": 2
    },

    Weapons.WAND: {
        "class": Wand,
        "value": 30,
        "image_path": './images/items/weapons/wand.png',
        "slot": 'main_hand',
        "attack_power": 8,
        "range_": 3
    },

    Weapons.CROSSBOW: {
        "class": Crossbow,
        "value": 50,
        "image_path": './images/item/weapons/crossbow.png',
        "slot": 'main_hand',
        "attack_power": 14,
        "defense_power": 3,
        "weapon_range": 12,
        "ammo_type": AmmoType.BOLT  # Assuming you have a BOLT in your AmmoType Enum
    },

    Weapons.HALBERD: {
        "class": Halberd,
        "value": 50,
        "image_path": './images/items/weapons/halberd.png',
        "slot": 'main_hand',
        "attack_power": 16,
        "range_": 2,
        "blade_length": 15,
        "sharpness": 10
    },

    Weapons.HAMMER: {
        "class": Hammer,
        "value": 45,
        "image_path": './images/items/weapons/hammer.png',
        "slot": 'main_hand',
        "attack_power": 14,
        "range_": 1
    }
}
