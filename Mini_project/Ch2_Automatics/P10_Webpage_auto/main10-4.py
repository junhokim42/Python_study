import pyautogui
import time
import pyperclip

weather = ['서울 날씨','시흥 날씨','청주 날씨','부산 날씨','강원도 날씨']

addr_x = 1869
addr_y = 316
start_x = 1558
start_y = 566
end_x = 2083
end_y = 800

for loc in weather:
    pyautogui.moveTo(addr_x,addr_y,1)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.write('www.naver.com', interval=0.1)
    pyautogui.write(['enter'])
    time.sleep(1)

    pyperclip.copy(loc)
    pyautogui.hotkey('ctrl','v')
    time.sleep(0.5)
    pyautogui.write(['enter'])
    time.sleep(1)
    save_loc = 'P10_Webpage_auto\\' + loc + '.png'
    pyautogui.screenshot(save_loc, region=(start_x, start_y, end_x-start_x, end_y-start_y))