import pyautogui
import time
from PIL.Image import *
import os


def get_origin():
    x, y, _, _ = pyautogui.locateOnScreen('assets/corner.png')
    return x + 5, y + 5


def image_position(x, y):
    xprime, yprime = get_origin()
    return x + xprime, y + yprime


def get_color_palette_origin():
    x, y, color_width, color_height = pyautogui.locateOnScreen('assets/colorPalette.png')
    return x, y, color_width, color_height


def get_color_position(color):
    x, y, color_w, color_h = palette_location

    if color >= 10:
        y = y + color_h / 2
        color = color-10
    x = x + (color * color_w / 10)
    return x + 10, y + 10


def get_dist(a, b):
    R = pow(a[0]-b[0], 2)
    G = pow(a[1]-b[1], 2)
    B = pow(a[2]-b[2], 2)
    return 1*R+2*G+1*B
    #color1_rgb = sRGBColor(a[0], a[1], a[2]);
    #color2_rgb = sRGBColor(b[0], b[1], b[2]);
    #color1_lab = convert_color(color1_rgb, LabColor);
    #color2_lab = convert_color(color2_rgb, LabColor);
    #delta_e = delta_e_cie2000(color1_lab, color2_lab);
    #return delta_e



def get_closest_color(color):
    min_dist = get_dist(color, colors[0])
    min_index = 0
    for i in range(1, len(colors)):
        distance = get_dist(color, colors[i])
        if distance < min_dist:
            min_dist = distance
            min_index = i
    return min_index


def sort_colors(image):
    pixels = []
    for color in range(0, len(colors)):
        pixels.append([])
    for x in range(0, width):
        print(repr(x/width*100)+'% done \n')
        for y in range(0, height):
            color = get_closest_color(Image.getpixel(image, (x, y)))
            pixels[color].append((x, y))
    return pixels


def start_paint():
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('mspaint\n')
    time.sleep(0.5)
    pyautogui.hotkey('win', 'up')


def resize_to_image():
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(0.01)
    pyautogui.hotkey('right')
    time.sleep(0.01)
    pyautogui.hotkey('tab')
    time.sleep(0.01)

    pyautogui.typewrite(repr(width))
    time.sleep(0.01)
    pyautogui.hotkey('tab')
    time.sleep(0.01)
    pyautogui.hotkey('tab')
    time.sleep(0.01)
    pyautogui.hotkey('-')
    time.sleep(0.01)
    pyautogui.hotkey('up')
    time.sleep(0.01)
    pyautogui.typewrite(repr(height))
    time.sleep(0.01)
    pyautogui.hotkey('enter')
    time.sleep(0.2)



def select_color(c):
    color_position = get_color_position(c)
    pyautogui.click(color_position)
    time.sleep(0.1)
    pyautogui.click(color_position)


def print_color(pixels):
    pyautogui.PAUSE = 0.00001
    xprime, yprime = origin
    for i in range(0, len(pixels)):
        x, y = pixels[i]
        x, y = x + xprime, y + yprime
        pyautogui.click(x, y)
    pyautogui.PAUSE = 0.1


def set_size():
    x, y, _, _ = pyautogui.locateOnScreen('assets/size.png')
    pyautogui.click(x, y)
    x, y, _, _ = pyautogui.locateOnScreen('assets/size2.png')
    pyautogui.click(x, y)


colors = [[0, 0, 0],
          [127, 127, 127],
          [136, 0, 21],
          [237, 28, 36],
          [255, 127, 39],
          [255, 242, 0],
          [34, 177, 76],
          [0, 162, 232],
          [63, 72, 204],
          [163, 73, 164],
          [255, 255, 255],
          [195, 195, 195],
          [185, 122, 87],
          [255, 174, 201],
          [255, 201, 14],
          [239, 228, 176],
          [181, 230, 29],
          [153, 217, 234],
          [112, 146, 190],
          [200, 191, 231]]

im = open("assets/image.png")

width, height = im.size

start_paint()
time.sleep(0.01)
resize_to_image()
time.sleep(0.01)

time.sleep(0.01)
palette_location = get_color_palette_origin()
origin = get_origin()
pyautogui.moveTo(origin)
image_pixels = sort_colors(im)



for c in range(0, 20):
    select_color(c)
    print_color(image_pixels[c])
