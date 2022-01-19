import pyautogui as pg
import time


def run():
    # try:
    #     location = pg.locateCenterOnScreen(r'C:\Users\PHOO\Desktop\img\chrome.png')
    #     pg.moveTo(location)
    # except Exception:
    #     location = pg.locateCenterOnScreen(r'C:\Users\PHOO\Desktop\img\chrome1.png')
    #     pg.moveTo(location)
    # pg.click(location)

    chat3 = pg.locateCenterOnScreen(r'C:\Users\PHOO\Desktop\img\chat2.png')
    pg.moveTo(chat3)
    pg.click(chat3)
    # chat1 = pg.locateCenterOnScreen(r'C:\Users\PHOO\Desktop\img\chat1.png')
    # pg.moveTo(chat1,duration=0)
    # pg.click(chat1,duration=1)
    
    time.sleep(1)
    pg.write('Chakrit 48868 30 check')
    pg.press('enter')