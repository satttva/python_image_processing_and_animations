import numpy as np
import matplotlib.pyplot as plt
from cs1graphics import*
from cs1media import*
from time import sleep

# This code converts an image into a black & white poster.
w, h = (512, 304)
x, y = (1, 1)
t = 500
i = 0
up = True
right = True
img = Image('./dvd_logo.png')
w_img, h_img = (img.getWidth(), img.getHeight())
time_delay = 0.007
paper = Canvas(w, h, 'skyBlue', 'My World')
x_step = w_img//2
y_step = h_img//2
x = x + x_step
y = y + y_step
img.moveTo(x,y)
paper.add(img)

if (w>=2 and h>=2 and w<=10000 and h<=10000 and x<w and y<h and x>0 and y>0 and t>=1 and t<= 10000000):

    while (True):

        if (x == w - x_step and y == h - y_step and up == True) or (x == x_step and y==y_step and up == False) or (x == x_step and y== h - y_step and up == True) or (x == w - x_step and y==y_step and up == False):
            break

        if (x >= w - x_step):
            right = False

        elif (x <= x_step):
            right = True

        elif (y >= h - y_step):
            up = False
        
        elif (y <= y_step):
            up = True
            
        if (right == True):
            x+=1

        else:
            x-=1

        if  (up == True):
            y+=1

        else:
            y-=1

        img.moveTo(x,y)
        sleep(time_delay)
        #i = i + 1
