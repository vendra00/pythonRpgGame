from random import choice

from utils.id_generator import IDGenerator
from item_attributes import ITEM_ATTRIBUTES, BASE_ITEM_ATTRIBUTES


class ItemService:

    @staticmethod
    def create_item_from_enum(weapon_enum):
        item_attributes = ITEM_ATTRIBUTES.get(weapon_enum)
        id_generator = IDGenerator()

        if not item_attributes:
            raise ValueError(f"Invalid weapon_enum: {weapon_enum}")

        # Create a new items with a unique ID
        combined_attributes = BASE_ITEM_ATTRIBUTES.copy()
        combined_attributes['item_id'] = id_generator.generate_id()
        combined_attributes.update(item_attributes)

        # Extract the class reference and then remove it from the dictionary
        item_class = combined_attributes.pop('class')

        # Assign the class name to the 'name' attribute if it' foods still the default
        if combined_attributes['name'] == 'Default Name':
            combined_attributes['name'] = item_class.__name__

        return item_class(**combined_attributes)

    @staticmethod
    def create_random_weapon_tier_1():
        # Assuming you have tier information in your ITEM_ATTRIBUTES
        tier_1_weapons = [weapon for weapon, attributes in ITEM_ATTRIBUTES.items() if attributes.get('tier') == 1]
        return ItemService.create_item_from_enum(choice(tier_1_weapons))
