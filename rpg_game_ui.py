import tkinter as tk
from tkinter import messagebox
from typing import List, Union

from PIL import Image, ImageTk

from characters import Hero, TILE_SIZE, MAP_SIZE
from environment import TreasureChest, Tree, Wall
from inventory_service import InventoryService
from item_service import ItemService


class RPGGame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # Define the instance attributes
        self.down_button = None
        self.right_button = None
        self.canvas = None
        self.up_button = None
        self.left_button = None
        self.exit_button = None
        self.inventory_button = None
        self.wall = None
        self.tree = None
        self.explore_button = None
        self.treasure_chest = None
        self.battle_button = None
        self.hero = None
        self.map = None
        self.elements = None

        assert isinstance(self.master, tk.Tk)
        self.master.title("Fantasy RPG Game")
        self.pack()

        # Initialize attributes
        self.initialize_attributes()
        self.create_widgets()
        self.initialize_map()
        self.draw_map()

    def initialize_attributes(self):
        """ Initialize class attributes """
        self.hero = Hero(name="Sir Lancelot")
        self.map: List[List[Union[str, Hero]]] = [['.' for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]
        self.elements = {
            "hero": self.hero,
            "tree": Tree(),
            "wall": Wall(),
            "treasure_chest": TreasureChest()
        }

    def initialize_map(self):
        """ Set the initial configuration of the map """
        # Place the hero at the center
        self.map[self.hero.position[1]][self.hero.position[0]] = self.hero

        # Set obstacles and items
        self.map[3][4] = self.elements["tree"]
        self.map[6][1] = self.elements["treasure_chest"]
        for i in range(MAP_SIZE):  # Vertical wall on the left side
            self.map[i][0] = self.elements["wall"]

    def draw_map(self):
        """ Draw the entire map on canvas """
        self.canvas.delete("all")

        images = self.get_element_images()
        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                if tile in self.elements.values():
                    self.canvas.create_image(x * TILE_SIZE, y * TILE_SIZE, anchor=tk.NW, image=images[tile])
                else:
                    self.canvas.create_rectangle(x * TILE_SIZE, y * TILE_SIZE,
                                                 (x + 1) * TILE_SIZE, (y + 1) * TILE_SIZE, fill='white')

    def get_element_images(self):
        """ Load and return images for all map elements """
        images = {}
        for key, element in self.elements.items():
            pil_image = Image.open(element.image_path).resize((TILE_SIZE, TILE_SIZE), 3)
            images[element] = ImageTk.PhotoImage(pil_image)
            setattr(self.canvas, f"{key}_image", images[element])
        return images

    def move_hero(self, dx, dy):
        x, y = self.hero.position
        new_x, new_y = x + dx, y + dy
        self.check_item_pick_up(new_x, new_y)
        self.check_map_collision(new_x, new_y, x, y)

    def draw_map_elements(self):
        hero_image = self.draw_hero()
        tree_image = self.draw_tree()
        wall_image = self.draw_wall()
        treasure_chest_image = self.draw_treasure_chest()
        return hero_image, tree_image, wall_image, treasure_chest_image

    def draw_wall(self):
        wall_pil_image = Image.open(self.wall.image_path)
        wall_pil_image = wall_pil_image.resize((TILE_SIZE, TILE_SIZE), 3)
        wall_image = ImageTk.PhotoImage(wall_pil_image)
        self.canvas.wall_image = wall_image
        return wall_image

    def draw_tree(self):
        tree_pil_image = Image.open(self.tree.image_path)  # Using PIL to open the image
        tree_pil_image = tree_pil_image.resize((TILE_SIZE, TILE_SIZE), 3)  # Resize the image to fit the tile size
        tree_image = ImageTk.PhotoImage(tree_pil_image)  # Convert PIL image to Tkinter PhotoImage
        self.canvas.tree_image = tree_image  # Store a reference to avoid garbage collection
        return tree_image

    def draw_treasure_chest(self):
        treasure_chest_pil_image = Image.open(self.treasure_chest.image_path)
        treasure_chest_pil_image = treasure_chest_pil_image.resize((TILE_SIZE, TILE_SIZE), 3)
        treasure_chest_image = ImageTk.PhotoImage(treasure_chest_pil_image)
        self.canvas.treasure_chest_image = treasure_chest_image
        return treasure_chest_image

    def draw_hero(self):
        hero_pil_image = Image.open(self.hero.image_path)
        hero_pil_image = hero_pil_image.resize((TILE_SIZE, TILE_SIZE), 3)
        hero_image = ImageTk.PhotoImage(hero_pil_image)
        self.canvas.hero_image = hero_image
        return hero_image

    def check_item_pick_up(self, new_x, new_y):
        if isinstance(self.map[new_y][new_x], TreasureChest):
            # Convert the enum items from the treasure chest to a real items object
            chest: TreasureChest = self.map[new_y][new_x]
            actual_item = ItemService.create_item_from_enum(chest.item)
            self.hero.inventory.append(actual_item)

            # Clear the treasure chest tile (replace with '.')
            self.map[new_y][new_x] = '.'

            # (Optional) Display a message to the player
            messagebox.showinfo("Item Collected", f"You've collected a {actual_item.name}!")

    def check_map_collision(self, new_x, new_y, x, y):
        if 0 <= new_x < len(self.map[0]) and 0 <= new_y < len(self.map) and self.is_passable(new_x, new_y):
            # Clear the old position of the hero on the map.
            self.map[y][x] = '.'
            # Set the new position of the hero on the map.
            self.hero.position = (new_x, new_y)
            self.map[new_y][new_x] = self.hero
            self.draw_map()  # Redraw the map to reflect the new hero position.

    def is_passable(self, x, y):
        return not isinstance(self.map[y][x], (Wall, Tree))

    def move_up(self):
        print("Up button pressed")
        self.move_hero(0, -1)

    def move_down(self):
        print("Down button pressed")
        self.move_hero(0, 1)

    def move_left(self):
        print("Left button pressed")
        self.move_hero(-1, 0)

    def move_right(self):
        print("Right button pressed")
        self.move_hero(1, 0)

    def create_widgets(self):
        # Directional buttons styling
        style_args = {
            'relief': 'ridge',
            'borderwidth': 2,
            'width': 10,
            'bg': '#D3D3D3',  # light gray
            'activebackground': '#A9A9A9'  # dark gray
        }

        # Menu Block
        menu_frame = tk.Frame(self)
        menu_frame.grid(row=0, column=0, padx=10, pady=10)

        self.explore_button = tk.Button(menu_frame, text="Explore", command=self.explore)
        self.explore_button.pack(pady=5)

        self.battle_button = tk.Button(menu_frame, text="Battle", command=self.battle)
        self.battle_button.pack(pady=5)

        self.inventory_button = tk.Button(menu_frame, text="Inventory", command=self.inventory)
        self.inventory_button.pack(pady=5)

        self.exit_button = tk.Button(menu_frame, text="Exit", command=self.master.quit)
        self.exit_button.pack(pady=5)

        # Map Block
        self.canvas = tk.Canvas(self, width=TILE_SIZE * MAP_SIZE, height=TILE_SIZE * MAP_SIZE, bg='white')
        self.canvas.grid(row=0, column=1, padx=20, pady=20)  # Adjusted placement of canvas

        # Directional Block
        directional_frame = tk.Frame(self)
        directional_frame.grid(row=0, column=2, padx=10, pady=10)

        self.up_button = tk.Button(directional_frame, text="UP", command=self.move_up, **style_args)
        self.up_button.grid(row=0, column=1, pady=5)

        self.left_button = tk.Button(directional_frame, text="LEFT", command=self.move_left, **style_args)
        self.left_button.grid(row=1, column=0, padx=5, pady=5)

        self.right_button = tk.Button(directional_frame, text="RIGHT", command=self.move_right, **style_args)
        self.right_button.grid(row=1, column=2, padx=5, pady=5)

        self.down_button = tk.Button(directional_frame, text="DOWN", command=self.move_down, **style_args)
        self.down_button.grid(row=2, column=1, pady=5)

    @staticmethod
    def explore():
        messagebox.showinfo("Explore", "You explore the world...")

    @staticmethod
    def battle():
        messagebox.showinfo("Battle", "A wild enemy appears!")

    def inventory(self):
        # Create a new window for the inventory
        inventory_window = tk.Toplevel(self)
        inventory_window.title("Inventory")

        # Retrieve detailed descriptions for each items
        item_descriptions = InventoryService.list_items(self.hero.inventory)

        self.iterate_inventory(inventory_window, item_descriptions)

        # If the inventory is empty
        self.display_empty_inventory_message(inventory_window)

    def display_empty_inventory_message(self, inventory_window):
        if not self.hero.inventory:
            empty_label = tk.Label(inventory_window, text="Your inventory is empty.")
            empty_label.pack(pady=10)

    def iterate_inventory(self, inventory_window, item_descriptions):
        for item, desc in zip(self.hero.inventory, item_descriptions):
            item_frame = tk.Frame(inventory_window, pady=10)
            item_frame.pack(fill=tk.X)

            # Handle image rendering and resize the image using Pillow
            image_path = item.get_image_path()

            # Open the image using Pillow
            pil_image = Image.open(image_path)

            # Resize the image to desired dimensions
            pil_image = self.resize_item_img(pil_image)

            # Convert the PIL image to a format Tkinter understands
            tk_image = ImageTk.PhotoImage(pil_image)

            # Use the resized image in your label
            self.resize_inventory_item_img(item_frame, tk_image)

            # Display items attributes using descriptions from InventoryService
            self.display_item_attributes(desc, item_frame)

    @staticmethod
    def display_item_attributes(desc, item_frame):
        attributes_label = tk.Label(item_frame, text=desc, justify=tk.LEFT, anchor=tk.W)
        attributes_label.pack(side=tk.RIGHT, padx=10)

    @staticmethod
    def resize_item_img(pil_image):
        desired_width = 100
        desired_height = 100
        pil_image = pil_image.resize((desired_width, desired_height), Image.BILINEAR)
        return pil_image

    @staticmethod
    def resize_inventory_item_img(item_frame, tk_image):
        image_label = tk.Label(item_frame, image=tk_image)
        image_label.image = tk_image  # Keep a reference to prevent garbage collection
        image_label.pack(side=tk.LEFT, padx=10)

    def use_item(self, item):
        if item.use_function:
            item.use_function(self.hero)  # Assuming the function expects a hero as an argument
            self.hero.inventory.remove(item)  # Remove the used items from inventory
            self.inventory()
