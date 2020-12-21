import numpy as np
import matplotlib.pyplot as plt
from cs1graphics import*
from cs1media import*
from time import sleep
from PIL import Image, ImageDraw, ImageFont


img2 = load_picture('./ang.png')
w_img, h_img = (img2.size())
img = Image.new('RGB', (8000,6000), color = (255,255,255))
d = ImageDraw.Draw(img)
# This code converts an image into a black & white poster.
fnt = ImageFont.truetype('./courier.ttf', 8)
# print(w_img, h_img)
word = "ABCDEFG"
limit=len(word)
count=0
fw = open("anginn.txt", 'w')
a = []
b = []
for y in range(h_img):
    for x in range(w_img):
        if img2.get(x,y) == (0,0,0):
            if count != limit:
                a.append(word[count])
                count=count+1
            else:
                count = 0
        else:
            a.append(' ')
    b.append(' '.join(a))
    a = []
y = 0
print(len(b))
for i in range(len(b)):
    d.text((0,y), b[i], fill=(0,0,0))
    y = y+9
    fw.write(b[i])
img.save('pil_anginn.png')