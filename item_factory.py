import random

from enums import Items, Rarity
from item_attributes import ITEM_ATTRIBUTES


class ItemFactory:

    @staticmethod
    def build_item(item_enum, durability, rarity):
        item_data = ITEM_ATTRIBUTES.get(item_enum)

        if not item_data:
            return None

        return item_data["class"](
            item_id=item_enum.value,
            name=item_enum.name,
            durability=durability,
            rarity=rarity,
            value=item_data["value"],
            image_path=item_data["image_path"],
            slot=item_data.get("slot", None),
            # These .get() methods provide a default value of None if the key doesn't exist
            attack_power=item_data.get("attack_power", None),
            range_=item_data.get("range_", None),
            blade_length=item_data.get("blade_length", None),
            sharpness=item_data.get("sharpness", None),
            block_chance=item_data.get("block_chance", None),
            block_amount=item_data.get("block_amount", None)

        )

    @staticmethod
    def create_random_item():
        # Select a random item category
        random_item_category = random.choice(list(Items))

        # Select a random item from that category
        specific_item_enum = random.choice(list(random_item_category.enum))

        # Generate random attributes (for example, durability)
        durability = random.randint(1, 100)
        rarity = random.choice(list(Rarity))

        # Use the builder method
        return ItemFactory.build_item(specific_item_enum, durability, rarity)