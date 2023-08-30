import tkinter as tk
from tkinter import messagebox
from typing import List, Union
from PIL import Image, ImageTk

from characters import Hero, MAP_SIZE, TILE_SIZE
from environment import TreasureChest, Tree, Wall


class RPGGame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master
        self.master.title("Fantasy RPG Game")
        self.pack()

        # Initialize attributes
        self.intro_label = None
        self.canvas = None
        self.explore_button = None
        self.battle_button = None
        self.inventory_button = None
        self.exit_button = None
        self.up_button = None
        self.down_button = None
        self.right_button = None
        self.left_button = None
        self.hero_pos = None
        self.map = None

        # Create Objects instance
        self.hero = Hero(name="Sir Lancelot")
        self.tree = Tree()
        self.wall = Wall()
        self.treasure_chest = TreasureChest()

        # Initialize and draw the map
        self.create_widgets()
        self.initialize_map()
        self.draw_map()

        self.map[self.hero.position[1]][self.hero.position[0]] = self.hero

    def initialize_map(self):
        # Create a 10x10 map with '.' as empty tiles
        self.map: List[List[Union[str, Hero]]] = [['.' for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]

        # Place the hero at the center
        self.map[self.hero.position[1]][self.hero.position[0]] = self.hero

        # Example obstacle: Place a tree 'T' at a specific position
        tree = Tree()
        self.map[3][4] = tree

        treasure_chest = TreasureChest()
        self.map[6][1] = treasure_chest
        print(treasure_chest.item)

        wall = Wall()
        for i in range(0, 10):  # This creates a vertical wall from (2,2) to (2,7)
            self.map[i][0] = wall

    def draw_map(self):
        self.canvas.delete("all")  # Clear the canvas before redrawing

        hero_image, tree_image, wall_image, treasure_chest_image = self.draw_map_elements()

        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                if isinstance(tile, Hero):
                    self.canvas.create_image(x * TILE_SIZE, y * TILE_SIZE, anchor=tk.NW, image=hero_image)
                elif isinstance(tile, Tree):
                    self.canvas.create_image(x * TILE_SIZE, y * TILE_SIZE, anchor=tk.NW, image=tree_image)
                elif isinstance(tile, Wall):
                    self.canvas.create_image(x * TILE_SIZE, y * TILE_SIZE, anchor=tk.NW, image=wall_image)
                elif isinstance(tile, TreasureChest):
                    self.canvas.create_image(x * TILE_SIZE, y * TILE_SIZE, anchor=tk.NW, image=treasure_chest_image)
                else:
                    color = 'white'
                    self.canvas.create_rectangle(x * TILE_SIZE, y * TILE_SIZE,
                                                 (x + 1) * TILE_SIZE, (y + 1) * TILE_SIZE,
                                                 fill=color)

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

    def move_hero(self, dx, dy):
        # Get the hero's current position.
        x, y = self.hero.position

        # Calculate the hero's intended new position.
        new_x, new_y = x + dx, y + dy

        # Check if the hero is moving onto a treasure chest tile
        self.check_item_pick_up(new_x, new_y)

        # Check if the new position is within the map boundaries and is passable
        self.check_map_collision(new_x, new_y, x, y)

    def check_item_pick_up(self, new_x, new_y):
        if isinstance(self.map[new_y][new_x], TreasureChest):
            # Add the item from the treasure chest to the hero's inventory
            chest: TreasureChest = self.map[new_y][new_x]
            self.hero.inventory.append(chest.item)

            # Clear the treasure chest tile (replace with '.')
            self.map[new_y][new_x] = '.'

            # (Optional) Display a message to the player
            messagebox.showinfo("Item Collected", f"You've collected a {chest.item.name}!")

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

        # Loop through the hero's inventory and display each item
        for idx, item in enumerate(self.hero.inventory, start=1):
            item_label = tk.Label(inventory_window, text=f"{idx}. {item}")
            item_label.pack(pady=2)

        # If the inventory is empty
        if not self.hero.inventory:
            empty_label = tk.Label(inventory_window, text="Your inventory is empty.")
            empty_label.pack(pady=10)
