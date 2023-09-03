from typing import List
from items import Item


class InventoryService:
    @staticmethod
    def list_items(inventory: List[Item]):
        if not inventory:
            return ["Your inventory is empty."]

        item_descriptions = [item.detailed_description() for item in inventory]
        return item_descriptions

    # Future methods related to inventory (like use_item, remove_item, etc.) can go here.
