import pyautogui
import time

print("Welcome to like_tool\n You will be offered 15 seconds to position your mouse properly!\n")
amount = input("Now, how many likes you wanna send(leave blank for INFINITE; example: 2000:\n--->")

def countdown(sec):
	while sec > 0:
		counter=0
		if counter == 0:
			print("\nStart liking in :")
			counter+=1
		print(sec)
		sec-=1
		time.sleep(1)
countdown(15)

if amount == "":
	print("<<<Deploying {0} likes>>>\n".format(amount))
	while True:
		pyautogui.click()

else:
	counter = 0
	print("<<<Deploying INFINTE likes>>>\n")
	while counter<int(amount)	:
		pyautogui.click()
		counter+=1
		print("Clicks remaining : {0}".format(int(amount) - counter))


