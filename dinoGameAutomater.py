import pyautogui as PyAutoGui
import time

PyAutoGui.moveTo(317,637 ) 
while(True):   
    x , y = PyAutoGui.position ()
    print(x,y) 
    if(PyAutoGui.pixel(x,y)!=(255,255,255)):
        PyAutoGui.press("space")
    if(PyAutoGui.pixel(298,589)!=(255,255,255)):
        PyAutoGui.press("down") 
     
                                                                               