import pyautogui
import time

f = open("spam.txt", "r")
time.sleep(5)
for words in f:
    print(words)
    pyautogui.typewrite(words)
    pyautogui.press("enter")
    time.sleep(6)
