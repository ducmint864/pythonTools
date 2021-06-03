from os import system
import pyautogui as pg
import time

while True:
    system("clear")
    str = input("what to type:\n")
    list = str.split(" ")

    time.sleep(2)

    for i in list:
        pg.typewrite(i + " ")
        time.sleep(0.05)
