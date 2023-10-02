import tkinter as tk
from PIL import Image, ImageTk

from model.characters import TILE_SIZE


def draw_element(element, image_cache):
    """
    Draws an element on the canvas and returns the Tkinter-compatible image.

    Parameters:
    - canvas: The canvas on which the element is drawn.
    - element: The element (like Hero, Tree, TreasureChest, etc.) to be drawn.
    - image_cache: A dictionary that caches already loaded images to avoid reloading.

    Returns:
    - The Tkinter-compatible image of the element.
    """

    # Use the element'foods id or its string representation as a fallback
    element_id = getattr(element, "element_id", str(element))

    # Check if the image for the current element is already cached
    if element_id in image_cache:
        return image_cache[element_id]

    # If it'foods not cached, then load the image, resize it, and add it to the cache
    pil_image = Image.open(element.image_path).resize((TILE_SIZE, TILE_SIZE), 3)
    tk_image = ImageTk.PhotoImage(pil_image)

    # Cache the image
    image_cache[element_id] = tk_image

    return tk_image


def draw_map(canvas, map_data, elements, images_cache):
    canvas.delete("all")

    # Ensure all elements have their images cached
    for element in elements.values():
        # Use the element'foods id, or its string representation as a fallback
        element_id = getattr(element, "element_id", str(element))
        if element_id not in images_cache:
            images_cache[element_id] = draw_element(element, images_cache)

    # Draw the map based on map_data
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            tile_id = getattr(tile, "element_id", str(tile))
            if tile_id in images_cache:
                canvas.create_image(x * TILE_SIZE, y * TILE_SIZE, anchor=tk.NW, image=images_cache[tile_id])
            else:
                canvas.create_rectangle(x * TILE_SIZE, y * TILE_SIZE, (x + 1) * TILE_SIZE, (y + 1) * TILE_SIZE,
                                        fill='white')
