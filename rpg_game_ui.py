import tkinter as tk
from tkinter import messagebox
from typing import List, Union
from PIL import Image, ImageTk
from models import Hero, Wall, TILE_SIZE, MAP_SIZE, Tree


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

        # Create hero instance
        self.hero = Hero(name="Sir Lancelot")

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

        wall = Wall()
        for i in range(2, 8):  # This creates a vertical wall from (2,2) to (2,7)
            self.map[i][2] = wall

    def draw_map(self):
        self.canvas.delete("all")  # Clear the canvas before redrawing

        pil_image = Image.open(self.hero.image_path)  # Using PIL to open the image
        pil_image = pil_image.resize((TILE_SIZE, TILE_SIZE), 3)  # Resize the image to fit the tile size
        hero_image = ImageTk.PhotoImage(pil_image)  # Convert PIL image to Tkinter PhotoImage
        self.canvas.hero_image = hero_image  # Store a reference to avoid garbage collection

        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                if isinstance(tile, Hero):
                    self.canvas.create_image(x * TILE_SIZE, y * TILE_SIZE, anchor=tk.NW, image=hero_image)
                elif isinstance(tile, Tree):
                    color = 'green'
                    self.canvas.create_rectangle(x * TILE_SIZE, y * TILE_SIZE,
                                                 (x + 1) * TILE_SIZE, (y + 1) * TILE_SIZE,
                                                 fill=color)
                elif isinstance(tile, Wall):
                    color = 'gray'
                    self.canvas.create_rectangle(x * TILE_SIZE, y * TILE_SIZE,
                                                 (x + 1) * TILE_SIZE, (y + 1) * TILE_SIZE,
                                                 fill=color)
                else:
                    color = 'white'
                    self.canvas.create_rectangle(x * TILE_SIZE, y * TILE_SIZE,
                                                 (x + 1) * TILE_SIZE, (y + 1) * TILE_SIZE,
                                                 fill=color)

    def move_hero(self, dx, dy):
        # Get the hero's current position.
        x, y = self.hero.position

        # Calculate the hero's intended new position.
        new_x, new_y = x + dx, y + dy

        # Check if the new position is within the map boundaries.
        if 0 <= new_x < len(self.map[0]) and 0 <= new_y < len(self.map):
            # Check if the destination tile is passable.
            if self.is_passable(new_x, new_y):
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

    @staticmethod
    def inventory():
        messagebox.showinfo("Inventory", "You check your items...")
