from abc import ABC
from dataclasses import dataclass

from enums import Rarity, Effects, AmmoType


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
    blade_length: int

    def __post_init__(self):
        if not self.thumbnail_path:
            self.thumbnail_path = './images/thumbnails/blade.jpg'

    def sharpen(self):
        pass


@dataclass
class Blunt(Weapon, ABC):
    spike_length: int = 0

    def __post_init__(self):
        if not self.thumbnail_path:
            self.thumbnail_path = './images/thumbnails/blunt.png'


@dataclass
class Ranged(Weapon, ABC):
    ammo_type: AmmoType

    def __post_init__(self):
        if not self.thumbnail_path:
            self.thumbnail_path = './images/thumbnails/ranged.png'

    def shoot(self):
        pass


@dataclass
class Shield(Weapon, ABC):
    block_power: int
    block_chance: int

    def block(self):
        pass


@dataclass
class Sword(Blade, ABC):
    pass


@dataclass
class Axe(Blade, ABC):
    pass


@dataclass
class Mace(Blunt, ABC):
    pass


@dataclass
class Bow(Ranged, ABC):
    pass


@dataclass
class Crossbow(Ranged, ABC):
    pass


@dataclass
class Dagger(Blade, ABC):
    pass


@dataclass
class Halberd(Weapon, ABC):
    pass


@dataclass
class Hammer(Blunt, ABC):
    pass


@dataclass
class Staff(Blunt, ABC):
    pass


@dataclass
class Wand(Blunt, ABC):
    pass


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
