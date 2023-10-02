# main.py

import tkinter as tk
from rpg_game_ui import RPGGame


def main():
    root = tk.Tk()
    app = RPGGame(master=root)
    app.mainloop()


# This is the standard boilerplate that calls the main() function.
if __name__ == "__main__":
    main()
