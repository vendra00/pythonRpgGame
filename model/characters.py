from dataclasses import dataclass, field
from typing import List, Dict, Optional

from model.base_attributes import BaseAttributes
from model.items import Item
from utils.enums import ItemSlot, MonsterType

TILE_SIZE = 60
MAP_SIZE = 10


@dataclass(frozen=False)
class Character:
    name: str
    base_attributes: BaseAttributes
    hp: int
    mana: int
    xp: int
    level: int
    attack: int
    defense: int
    position: Optional[tuple]
    image_path: str


@dataclass(frozen=False)
class Hero(Character):
    element_id: str = 'hero'
    inventory: List[Item] = field(default_factory=list)
    equipment: Dict[ItemSlot, Item] = field(default_factory=dict)
    image_path: str = './images/characters/heroes/hero.png'


@dataclass(frozen=False)
class Monster(Character):
    monster_type: MonsterType
    element_id: str
    loot: List[Item] = field(default_factory=list)

    def __post_init__(self):
        self.image_path = self.monster_type.image_path
