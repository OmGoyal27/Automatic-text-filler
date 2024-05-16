import keyboard
from filler import fill, update_data

# Register the hotkey
keyboard.add_hotkey('right shift', fill)
keyboard.add_hotkey('right shift+shift', update_data)

# Block until ESC is pressed
input("Hit enter to exit.")
