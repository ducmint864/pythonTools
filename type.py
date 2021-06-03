from os import system
import pyautogui as pg
import time

while True:
    system("clear")
    str = input("what to type:\n")
    list = str.split(" ")
    first69 = round(len(list) * 69/100)

    time.sleep(2)

    count=0
    while count <= first69:
        pg.typewrite(list[count] + " ")
        count+=1
        time.sleep(0.4)
    while count < len(list):
        pg.typewrite(list[count] + " ")
        count+=1
        #time.sleep(0.8571428571)
        time.sleep(0.7)
