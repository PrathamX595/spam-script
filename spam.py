import time
import pyautogui
print('welcome to the spammer')
time.sleep(1)
s = input('what message would you like to spam ? \n')
n = int(input('how many times shall I spam ? \n'))
print("I'll spam in 5 secs")
time.sleep(0.5)
print("Place your cursors")
time.sleep(5)
i = 0
while i < n:
    i = i + 1
    for word in s:
        pyautogui.write(word)
    pyautogui.press('enter')