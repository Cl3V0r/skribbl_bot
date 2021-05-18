import pyautogui
from time import sleep
from PIL import Image
import numpy as np

size = (80,80)

im = Image.open('gnome.png')
#im = Image.open('rickroll.png')
im.thumbnail(size,Image.ANTIALIAS)
im = im.convert('1') # convert image to black and white
im.save('result.png')

im = np.array(im)


WIDTH, HEIGHT = im.shape

x_start, y_start = 300, 300
sleep(3)
scale = 3
pyautogui.PAUSE = 0
for i in range(0,WIDTH):
    for j in range(0, HEIGHT):
        if not im[i,j]: #use inverted pixels
            pyautogui.click(y_start+scale*j,x_start+scale*i)