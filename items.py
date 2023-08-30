from abc import ABC
from dataclasses import dataclass

from enums import Rarity, Effects


@dataclass
class Item(ABC):
    item_id: int
    name: str
    rarity: Rarity
    value: float
    image_path: str
    weight: int


@dataclass
class Equipment(Item, ABC):
    durability: int
    slot: str
    thumbnail_path: str

    def equip(self):
        pass

    def unequip(self):
        pass

    def repair(self):
        pass


@dataclass
class Weapon(Equipment, ABC):
    attack_power: int
    defense_power: int
    weapon_range: int

    def swing(self):
        pass


@dataclass
class Blade(Weapon, ABC):
    sharpness: int
    length: int
    thumbnail_path: str = './images/thumbnails/blade.jpg'

    def sharpen(self):
        pass


@dataclass
class Blunt(Weapon, ABC):
    thumbnail_path: str = './images/thumbnails/blunt.png'


@dataclass
class Shield(Weapon, ABC):
    block_power: int
    block_chance: int
    image_path: str = './images/shield.png'

    def block(self):
        pass


@dataclass
class Sword(Blade, ABC):
    image_path: str = './images/sword.png'


@dataclass
class Axe(Blade, ABC):
    image_path: str = './images/axe.png'


@dataclass
class Mace(Blunt, ABC):
    image_path: str = './images/item/mace.png'


@dataclass
class Consumable(Item, ABC):
    duration: int
    effect: Effects

    def consume(self):
        pass


@dataclass
class Key(Item, ABC):
    key_type: str
    door_id: int

    def unlock(self):
        pass
