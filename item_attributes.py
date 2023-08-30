from enums import Weapons
from characters import Sword, Axe, Shield

ITEM_ATTRIBUTES = {
    Weapons.SWORD: {
        "class": Sword,
        "value": 35,
        "image_path": './images/sword.png',
        "slot": 'main_hand',
        "attack_power": 10,
        "range_": 1,
        "blade_length": 10,
        "sharpness": 10
    },
    Weapons.AXE: {
        "class": Axe,
        "value": 35,
        "image_path": './images/axe.png',
        "slot": 'main_hand',
        "attack_power": 10,
        "range_": 1,
        "blade_length": 10,
        "sharpness": 10
    },
    Weapons.SHIELD: {
        "class": Shield,
        "value": 35,
        "image_path": './images/shield.png',
        "slot": 'off_hand',
        "attack_power": 0,
        "range_": 0,
        "block_chance": 10,
        "block_amount": 10
        # ... Add similar entries for other weapons and items
    }
}
