import pyautogui as pg
import time

data = "" # Initiate the data variable

def fill():                 # Fill the data
    global data
    time.sleep(0.35)
    pg.write(data)

def prompt():               # Asks to change the data
    data = pg.prompt(text="Please enter the data you want to make a shortcut of.", title="Shortcut maker")
    if data:
        return data


def update_data():          # Update the data
    global data
    data = prompt()
