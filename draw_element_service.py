import tkinter as tk
from PIL import Image, ImageTk

from characters import TILE_SIZE


def draw_element(canvas, element, image_cache):
    """
    Draws an element on the canvas and returns the Tkinter-compatible image.

    Parameters:
    - canvas: The canvas on which the element is drawn.
    - element: The element (like Hero, Tree, TreasureChest, etc.) to be drawn.
    - image_cache: A dictionary that caches already loaded images to avoid reloading.

    Returns:
    - The Tkinter-compatible image of the element.
    """

    # Check if the image for the current element is already cached
    if element in image_cache:
        return image_cache[element]

    # If it's not cached, then load the image, resize it, and add it to the cache
    pil_image = Image.open(element.image_path).resize((TILE_SIZE, TILE_SIZE), 3)
    tk_image = ImageTk.PhotoImage(pil_image)

    # Cache the image
    image_cache[element] = tk_image

    return tk_image


def draw_map(canvas, map_data, elements, images_cache):
    canvas.delete("all")

    # Ensure all elements have their images cached
    for element in elements.values():
        if element not in images_cache:
            images_cache[element] = draw_element(canvas, element, images_cache)

    # Draw the map based on map_data
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile in images_cache:
                canvas.create_image(x * TILE_SIZE, y * TILE_SIZE, anchor=tk.NW, image=images_cache[tile])
            else:
                canvas.create_rectangle(x * TILE_SIZE, y * TILE_SIZE,
                                        (x + 1) * TILE_SIZE, (y + 1) * TILE_SIZE, fill='white')

