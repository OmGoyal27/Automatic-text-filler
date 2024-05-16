import pyautogui as pg
import time

data = ""

def fill():
    global data
    time.sleep(0.35)
    pg.write(data)

def prompt():
    data = pg.prompt(text="Please enter the data you want to make a shortcut of.", title="Shortcut maker")
    if data:
        return data


def update_data():
    global data
    data = prompt()
