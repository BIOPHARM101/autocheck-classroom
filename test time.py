from cProfile import run
from cgi import test
from pickle import NONE
import time 
import datetime
from test import hee
import pyautogui as pg

a=1

point = datetime.datetime(2022,1,19,8,10)
point2 = datetime.datetime(2022,1,19,9,00)
pointmin = int(point.hour *1000 + point.minute) 
pointmin2 = int(point2.hour *1000 + point2.minute) 
print(pointmin)



while a==1:

  now = datetime.datetime.now()
  nowmin =  int(now.hour *1000 + now.minute) 

  
  locate = pg.locateCenterOnScreen(r'C:\Users\PHOO\Desktop\img\call.png')
  print(locate)

  if locate==None:
    chat1 = pg.locateCenterOnScreen(r'C:\Users\PHOO\Desktop\img\chat1.png')
    pg.moveTo(chat1,duration=0)
    pg.click(chat1,duration=0)
    print('exceptcall')

  
  ABC = pg.locateCenterOnScreen(r'C:\Users\PHOO\Desktop\img\16.png')
  if ABC==None:
    print('NNNNNNNNNNNN')
  else:
    print('run')
    run()
    a=0

  print(nowmin)
  
  if nowmin<=pointmin2 and nowmin>=pointmin :
    time.sleep(0.01)

  else :
    print('time')
    time.sleep(1200)
    
# while True:
    
#     if (nowmin == pointmin):
#         hee()
        
#     else:
#         print('k')

#     time.sleep(1)
        