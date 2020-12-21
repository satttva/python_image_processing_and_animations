import numpy as np
import matplotlib.pyplot as plt
from cs1graphics import*
from cs1media import*
from time import sleep
import random

# This code converts an image into a black & white poster.
w, h = (1440, 1440)
t = 500
i = 0
up = True
right = True

left, right, left_fall, right_fall = (Image('./r_100.png'), Image('./l_100.png'), Image('./lf_100.png'), Image('./rf_100.png'))
time_delay = 0.01
paper = Canvas(w, h, 'skyBlue', 'My World')
lx = 0
rx = w
ly, ry = (200, 300)
left.moveTo(lx, ly)
right.moveTo(rx+500, ry)
paper.add(left)
paper.add(right)

while(True):
    lx += random.randint(1,3)
    rx -= random.randint(1,3)
    ly += random.randint(-3,3)
    ry -= random.randint(-3,3)
    left.moveTo(lx,ly)
    right.moveTo(rx, ry)
    sleep(time_delay)

    