import pyautogui
import time
import pyperclip

pyautogui.moveTo(1600, 165, 0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울 날씨")
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)

pyautogui.write(['enter'])
time.sleep(1)

start_x = 1558
start_y = 566
end_x = 2083
end_y = 800

pyautogui.screenshot(r'P10_Webpage_auto\서울날씨.png', region = (start_x, start_y, end_x-start_x, end_y-start_y))