import random

from utils.enums import Items


class Wall:
    def __init__(self):
        self.image_path = './images/map_elements/wall.jpg'


class Tree:
    def __init__(self):
        self.image_path = './images/map_elements/tree.png'


class TreasureChest:
    def __init__(self):
        self.image_path = './images/map_elements/treasure-chest.jpg'

        # Choose a random category (e.g., Weapons, Armor)
        random_category = random.choice(list(Items)).value[0]

        # Choose a random items from that category
        self.item = random.choice(list(random_category))
