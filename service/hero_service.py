def hero_attack(hero, enemy):
    damage = hero.atk - enemy.defense
    if damage > 0:
        enemy.hp -= damage
        return f"{hero.name} dealt {damage} damage to {enemy.name}!"
    return f"{hero.name}'s attack was ineffective against {enemy.name}!"


def hero_defend(hero, enemy_atk):
    damage = enemy_atk - hero.defense
    if damage > 0:
        hero.hp -= damage
        return f"{hero.name} took {damage} damage!"
    return f"The attack was ineffective against {hero.name}!"


def use_item(hero, item):
    # For simplicity, let's just have health potions
    if item == "health_potion":
        hero.hp += 20
        hero.inventory.remove("health_potion")
        return f"{hero.name} used a health potion and recovered 20 HP!"


def gain_experience(hero, amount):
    hero.xp += amount
    if hero.xp >= hero.level * 100:  # Level up every 100 XP for simplicity
        level_up(hero)


def level_up(hero):
    hero.level += 1
    hero.hp += 10
    hero.atk += 2
    hero.defense += 1
    hero.xp = 0  # Reset XP after leveling up
    return f"{hero.name} leveled up to Level {hero.level}!"


def move_hero(hero, current_map, dx, dy, check_item_pick_up, check_map_collision, play_sfx):
    new_x, new_y = hero.position[0] + dx, hero.position[1] + dy
    updated_map = check_map_collision(hero, new_x, new_y, current_map)  # Pass the current_map here
    check_item_pick_up(new_x, new_y)
    play_sfx('audio/sfx/walk.mp3', 1000)


def check_map_collision(hero, new_x, new_y, current_map):
    x, y = hero.position
    if 0 <= new_x < len(current_map[0]) and 0 <= new_y < len(current_map) and is_passable(current_map, new_x, new_y):
        # Clear the old position of the hero on the map.
        current_map[y][x] = '.'
        # Set the new position of the hero on the map.
        hero.position = (new_x, new_y)
        current_map[new_y][new_x] = hero
    return current_map  # Return the updated map


def is_passable(current_map, x, y):
    # Your logic to determine if the tile is passable
    return current_map[y][x] in ['.', 'path', 'etc']  # Modify this as per your game rules.


def equip(self, item):
    """
        Equip an item to the appropriate slot.
        For simplicity, let's assume the item has an 'slot' attribute indicating where it fits.
        """
    slot = item.slot  # assuming the item has a 'slot' attribute
    if slot in self.equipment:
        # If there's already an item in that slot, unequip it first
        if self.equipment[slot]:
            self.unequip(slot)
        self.equipment[slot] = item

        # Modify hero's stats based on the item's properties
        # For this example, we'll assume items have 'atk_bonus', 'defense_bonus', etc.
        self.atk += item.atk_bonus
        self.defense += item.defense_bonus
