TILE_SIZE = 60
MAP_SIZE = 10


class Hero:
    def __init__(self, name, hp=100, atk=10, defense=5):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.inventory = []
        self.xp = 0
        self.level = 1

        self.position = (MAP_SIZE // 2, MAP_SIZE // 2)  # Starting position: center of the map
        self.image_path = './images/hero.png'  # Path to the hero's image
