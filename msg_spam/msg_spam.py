import pyautogui, time

#SPAM_FUNCTION , THE PROGRAM DOESN'T START HERE, LOOK DOWN THERE
def spam(x):
	print("You've got {0} seconds to open chat app, choose conversation to spam, use mouse click to get your keyboard cursor into the msg typing box, now enjoy mass destruction".format(x))
	time.sleep(int(x))
	for whatever in text:
		if mode == 1:
			pyautogui.typewrite(whatever)
			time.sleep(gap) 
			pyautogui.press("enter")
		elif mode == 2:
			pyautogui.write(whatever, interval=gap)
			pyautogui.press("Enter")
		else:
			print("Unknown spam mode!!!")
			print(type(mode))


#THE PROGRAM STARTS HERE, NOT UP THERE : DEFINE VALUES, AND RUN spam() based on those values
	#OPTION
print("option 1: Paste in whatever text ya wanna spam \n option 2; paste in the directory on yur computer in which the text file containing whataver ya wanna spam is stored in")
option = input("Option(1/2): ")
if option == str(1):
	text = str(input("What to spam?:"))
elif option == str(2):
	path = str(input("Paste in the link to the text file(must be exact): "))
	with open(path) as file:	
		text = file.read()
else:
	print("Please do type nothing but 1 or 2")

	#MODE
mode = int(input("Choose mode : (1 for spamming letters by letters, 2 for spamming sentences after sentences; Leave blank for default mode : 2)"))
if mode == "":
	mode = 2

	#GAP BETWEEN MESSAGES
gap = input("Decide the gap between each msg being sent(in seconds, example, 3), leave bank for default gap = 0.75 secs:")
if gap == "":
	gap = 0.75

	#RECAP
print("\n RECAP:\n -Option {0} selected\n -Mode {1} selected\n -Gap between messages is {2} seconds\n".format(option, mode, gap))

	#IN CASE OF RESTARTING
counter=0
if counter>0:
	spam(5)
else:
	counter+=1
	spam(5)

