from abc import ABC, abstractmethod

from enums import Rarity


class Item(ABC):
    def __init__(self, item_id: int, name: str, rarity: Rarity, value: float, image_path: str):
        self.item_id = item_id
        self.name = name
        self.rarity = rarity
        self.value = value
        self.image_path = image_path

    @abstractmethod
    def use(self):
        pass  # Define a general use action or just raise an exception to be implemented in child classes


class Equipment(Item, ABC):
    def __init__(self, item_id, name, rarity, value, image_path, durability: int, slot):
        super().__init__(item_id, name, rarity, value, image_path)
        self.durability = durability
        self.slot = slot

    def equip(self):
        pass

    def unequip(self):
        pass


class Weapon(Equipment, ABC):
    def __init__(self, item_id, name, rarity, value, image_path, durability, slot, attack_power: int, range_: int):
        super().__init__(item_id, name, rarity, value, image_path, durability, slot)
        self.attack_power = attack_power
        self.range = range_

    def swing(self):
        pass

    def repair(self):
        pass


class Sword(Weapon, ABC):
    def __init__(self, item_id, name, rarity, value, image_path, durability, slot, attack_power, range_,
                 blade_length: int, sharpness: int):
        super().__init__(item_id, name, rarity, value, image_path, durability, slot, attack_power, range_)
        self.blade_length = blade_length
        self.sharpness = sharpness
        self.thumbnail_path = './images/sword.png'

    def sharpen(self):
        pass


class Axe(Weapon, ABC):
    def __init__(self, item_id, name, rarity, value, image_path, durability, slot, attack_power, range_,
                 blade_length: int, sharpness: int):
        super().__init__(item_id, name, rarity, value, image_path, durability, slot, attack_power, range_)
        self.blade_length = blade_length
        self.sharpness = sharpness
        self.thumbnail_path = './images/axe.png'

    def sharpen(self):
        pass


class Shield(Weapon, ABC):
    def __init__(self, item_id, name, rarity, value, image_path, durability, slot, defense: int):
        super().__init__(item_id, name, rarity, value, image_path, durability, slot)
        self.defense = defense

    def block(self):
        pass

    def repair(self):
        pass


class Consumable(Item, ABC):
    def __init__(self, item_id, name, rarity, value, image_path, duration: int, effect):
        super().__init__(item_id, name, rarity, value, image_path)
        self.duration = duration
        self.effect = effect

    def consume(self):
        pass


class Key(Item, ABC):
    def __init__(self, item_id, name, rarity, value, image_path, key_type, door_id: int):
        super().__init__(item_id, name, rarity, value, image_path)
        self.key_type = key_type
        self.door_id = door_id

    def unlock(self):
        pass
