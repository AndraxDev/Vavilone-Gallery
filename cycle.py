from PIL import Image
from PIL import ExifTags
from os import system
import numpy as np

r''' CONVERT TO HEXDECIMAL '''
def decimalToHex(n):
    return hex(n).replace("0x","")


r''' CONVERT DECOMAL NUMBER TO 16-bit GRAY IMAGE '''
def toImage(b, w, h):
    if int(b) < 0:
        print("Entered value is too small")
        exit(1)
    
    b = decimalToHex(b)
    #print(b) - DEBUG

    bin = list(b)
    bin = np.flipud(bin)
    #print() - DEBUG
    #for s in range(len(bin)): - DEBUG
    #    print(bin[s], end="") - DEBUG
    #print() - DEBUG
    
    replacer = np.array(['0' for i in range(w*h)])
    for d in range(len(bin)):
        replacer[d] = bin[d]
    
    immgs = np.flipud(replacer)
    
    #for dd in range(w*h): - DEBUG
    #    print(immgs[dd], end="") - DEBUG

    image = np.reshape(immgs, (-1, w))
    
    r''' SHOW IMAGE '''
    for r in image:
        for c in r:
            if c == "0":
                print(" ", end = "")
            if c == "1":
                print(".", end = "")
            if c == "2":
                print("-", end = "")
            if c == "3":
                print("+", end = "")
            if c == "4":
                print("=", end = "")
            if c == "5":
                print(":", end = "")
            if c == "6":
                print("░", end = "")
            if c == "7":
                print("*", end = "")
            if c == "8":
                print("▒", end = "")
            if c == "9":
                print("%", end = "")
            if c == "a":
                print("0", end = "")
            if c == "b":
                print("$", end = "")
            if c == "c":
                print("#", end = "")
            if c == "d":
                print("@", end = "")
            if c == "e":
                print("▓", end = "")
            if c == "f":
                print("█", end = "")
        print()
    
    r''' FINAL EXPORT IMAGE WITH RGB CHANNEL
    source = Image.open(r"C:\Users\conta\Desktop\output.png")
    result = Image.new('RGB', source.size)
    
    for x in range(w):
        for y in range(h):
            if image[x][y] == "0":
                result.putpixel((x, y), (0, 0, 0))
            if image[x][y] == "1":
                result.putpixel((x, y), (17, 17, 17))
            if image[x][y] == "2":
                result.putpixel((x, y), (34, 34, 34))
            if image[x][y] == "3":
                result.putpixel((x, y), (51, 51, 51))
            if image[x][y] == "4":
                result.putpixel((x, y), (68, 68, 68))
            if image[x][y] == "5":
                result.putpixel((x, y), (85, 85, 85))
            if image[x][y] == "6":
                result.putpixel((x, y), (102, 102, 102))
            if image[x][y] == "7":
                result.putpixel((x, y), (119, 119, 119))
            if image[x][y] == "8":
                result.putpixel((x, y), (136, 136, 136))
            if image[x][y] == "9":
                result.putpixel((x, y), (153, 153, 153))
            if image[x][y] == "a":
                result.putpixel((x, y), (170, 170, 170))
            if image[x][y] == "b":
                result.putpixel((x, y), (187, 187, 187))
            if image[x][y] == "c":
                result.putpixel((x, y), (204, 204, 204))
            if image[x][y] == "d":
                result.putpixel((x, y), (221, 221, 221))
            if image[x][y] == "e":
                result.putpixel((x, y), (238, 238, 238))
            if image[x][y] == "f":
                result.putpixel((x, y), (255, 255, 255))
    
    result = result.transpose(Image.ROTATE_270) # - BUGFIX WITH ROTATION
    result = result.transpose(Image.FLIP_LEFT_RIGHT) # - BUGFIX WITH FLIP
    result.save(r"C:\Users\conta\Desktop\images.png")'''
    system('cls')

system('cls')

# Size of image
width = 200
height = 200

# Image id (you can get it by starting processor.py)
someid = 0

# If value mor than 1, programm will skip some ids
speed = 1
starts = someid
ends = pow(16, (width*height))

if starts < ends:
    if 0 < speed < ends:
        for u in range(starts, ends):
            toImage(speed*u, width, height)
    else:
        print("Speed is too large")
        exit(1)
else:
    print("Reverse not allowed: starts must be more than ends")
    exit(1)
    
input()