import random

from enums import Items


class Wall:
    def __init__(self):
        self.image_path = './images/wall.jpg'


class Tree:
    def __init__(self):
        self.image_path = './images/tree.png'


class TreasureChest:
    def __init__(self):
        self.image_path = './images/treasure-chest.jpg'

        # Choose a random category (e.g., Weapons, Armor)
        random_category = random.choice(list(Items)).value[0]

        # Choose a random item from that category
        self.item = random.choice(list(random_category))