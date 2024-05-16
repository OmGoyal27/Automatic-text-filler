import keyboard
from filler import fill, update_data                        # Imports the actual functions

# Register the hotkey
keyboard.add_hotkey('right shift', fill)                    # Hooks the right shift key(Which is one of the most useless keys) to have a function of paste
keyboard.add_hotkey('right shift+shift', update_data)       # Asks to update data when both "shifts" are pressed 

# Block until ESC is pressed
input("Hit enter to exit.")
