# models.py
import random

from enums import Items

TILE_SIZE = 50
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

    def attack(self, enemy):
        damage = self.atk - enemy.defense
        if damage > 0:
            enemy.hp -= damage
            return f"{self.name} dealt {damage} damage to {enemy.name}!"
        return f"{self.name}'s attack was ineffective against {enemy.name}!"

    def defend(self, enemy_atk):
        damage = enemy_atk - self.defense
        if damage > 0:
            self.hp -= damage
            return f"{self.name} took {damage} damage!"
        return f"The attack was ineffective against {self.name}!"

    def use_item(self, item):
        # For simplicity, let's just have health potions
        if item == "health_potion":
            self.hp += 20
            self.inventory.remove("health_potion")
            return f"{self.name} used a health potion and recovered 20 HP!"

    def gain_experience(self, amount):
        self.xp += amount
        if self.xp >= self.level * 100:  # Level up every 100 XP for simplicity
            self.level_up()

    def level_up(self):
        self.level += 1
        self.hp += 10
        self.atk += 2
        self.defense += 1
        self.xp = 0  # Reset XP after leveling up
        return f"{self.name} leveled up to Level {self.level}!"

    def move(self, dx, dy):
        """Update hero's position by (dx, dy)"""
        new_x = self.position[0] + dx
        new_y = self.position[1] + dy
        self.position = (new_x, new_y)


class Wall:
    def __init__(self):
        self.image_path = './images/wall.jpg'


class Tree:
    def __init__(self):
        self.image_path = './images/tree.png'


class TreasureChest:
    def __init__(self):
        self.image_path = './images/treasure-chest.jpg'
        self.item = random.choice(list(Items))
