import pyautogui, time
f = open("beemovie.txt", 'r')
time.sleep(8)
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

