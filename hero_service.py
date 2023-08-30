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


def move_hero(hero, dx, dy):
    """Update hero's position by (dx, dy)"""
    new_x = hero.position[0] + dx
    new_y = hero.position[1] + dy
    hero.position = (new_x, new_y)
