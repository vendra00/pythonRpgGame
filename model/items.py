from abc import ABC
from dataclasses import dataclass

from utils.enums import Rarity, Effects, AmmoType, BladeImgPaths, BluntImgPaths, RangedImgPaths, PolearmsImgPaths


@dataclass
class Item(ABC):
    item_id: int
    name: str
    rarity: Rarity
    value: float
    image_path: str
    weight: int

    def detailed_description(self):
        details = [
            f"Name: {self.name}",
            f"Rarity: {self.rarity.name}",
            f"Value: {self.value} gold",
            f"Weight: {self.weight} kg",
        ]
        return "\n".join(details)

    def get_image_path(self):
        return self.image_path


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

    def parry(self):
        pass


@dataclass
class Blade(Weapon, ABC):
    sharpness: int
    blade_length: int

    def __post_init__(self):
        if not self.thumbnail_path:
            self.thumbnail_path = BladeImgPaths.THUMBNAIL.value.path

    def sharpen(self):
        pass

    def slash(self):
        pass


@dataclass
class Blunt(Weapon, ABC):
    spike_length: int = 0

    def __post_init__(self):
        if not self.thumbnail_path:
            self.thumbnail_path = self.thumbnail_path = BluntImgPaths.THUMBNAIL.value.path

    def bludgeon(self):
        pass


@dataclass
class Ranged(Weapon, ABC):
    ammo_type: AmmoType

    def __post_init__(self):
        if not self.thumbnail_path:
            self.thumbnail_path = self.thumbnail_path = RangedImgPaths.THUMBNAIL.value.path

    def shoot(self):
        pass

    def reload(self):
        pass

    def aim(self):
        pass


@dataclass
class Polearm(Weapon, ABC):
    pole_length: int

    def __post_init__(self):
        if not self.thumbnail_path:
            self.thumbnail_path = self.thumbnail_path = PolearmsImgPaths.THUMBNAIL.value.path

    def thrust(self):
        pass

    def sweep(self):
        pass


@dataclass
class Shield(Weapon, ABC):
    block_power: int
    block_chance: int

    def block(self):
        pass

    def bash(self):
        pass

    def riposte(self):
        pass

    def deflect(self):
        pass

    def counter(self):
        pass


@dataclass
class Sword(Blade, ABC):
    pass


@dataclass
class Axe(Blade, ABC):

    def cleave(self):
        pass


@dataclass
class Mace(Blunt, ABC):

    def crush(self):
        pass


@dataclass
class Bow(Ranged, ABC):
    def arrow(self):
        pass


@dataclass
class Crossbow(Ranged, ABC):
    def bolt(self):
        pass


@dataclass
class Dagger(Blade, ABC):

    def stab(self):
        pass


@dataclass
class Halberd(Weapon, ABC):

    def pierce(self):
        pass


@dataclass
class Hammer(Blunt, ABC):

    def smash(self):
        pass


@dataclass
class Staff(Blunt, ABC):

    def jab(self):
        pass


@dataclass
class Wand(Blunt, ABC):

    def cast(self):
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
