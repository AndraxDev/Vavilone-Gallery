r'''
Vavilone Gallery
Version: 1.0
Create date: 24.06.2020
Developer: xXDima212DimaXx
Description: This gallery contains all avaliabe and unavaliable images. Program based
on autogeneration
'''
from PIL import Image
from PIL import ExifTags
from os import system
import numpy as np

r''' PREPARE IMAGE TO CONVERTIONG '''
def white_black(source_name, result_name, brightness):
    source = Image.open(source_name)
    result = Image.new('RGB', source.size)
    separator = 15 / brightness / 2 * 3
    for x in range(source.size[0]):
        for y in range(source.size[1]):
            r, g, b = source.getpixel((x, y))
            total = r + g + b
            if total > (separator*15+14) < (separator*16+15):
                result.putpixel((x, y), (255, 255, 255))
            elif total > (separator*14+13) < (separator*15+14):
                result.putpixel((x, y), (238, 238, 238))
            elif total > (separator*13+12) < (separator*14+13):
                result.putpixel((x, y), (221, 221, 221))
            elif total > (separator*12+11) < (separator*13+12):
                result.putpixel((x, y), (204, 204, 204))
            elif total > (separator*11+10) < (separator*12+11):
                result.putpixel((x, y), (187, 187, 187))
            elif total > (separator*10+9) < (separator*11+10):
                result.putpixel((x, y), (170, 170, 170))
            elif total > (separator*9+8) < (separator*10+9):
                result.putpixel((x, y), (153, 153, 153))
            elif total > (separator*8+7) < (separator*9+8):
                result.putpixel((x, y), (136, 136, 136))
            elif total > (separator*7+6) < (separator*8+7):
                result.putpixel((x, y), (119, 119, 119))
            elif total > (separator*6+5) < (separator*7+6):
                result.putpixel((x, y), (102, 102, 102))
            elif total > (separator*5+4) < (separator*6+5):
                result.putpixel((x, y), (85, 85, 85))
            elif total > (separator*4+3) < (separator*5+4):
                result.putpixel((x, y), (68, 68, 68))
            elif total > (separator*3+2) < (separator*4+3):
                result.putpixel((x, y), (51, 51, 51))
            elif total > (separator*2+1) < (separator*3+2):
                result.putpixel((x, y), (34, 34, 34))
            elif total > (separator) < (separator*2+1):
                result.putpixel((x, y), (17, 17, 17))
            else:
                result.putpixel((x, y), (0, 0, 0))
    
    result.save(result_name)
    #result.show() - DEBUG

r''' RESIZE IMAGE '''
def resize(inp, outp, sz):
    img = Image.open(inp)
    img = img.resize((sz, sz))
    img.save(outp)

r''' CROP IMAGE '''
def crop(inp, outp):
    im = Image.open(inp)
    width, height = im.size
    
    if width > height:
        left = (width - height)/2
        top = (height - height)/2
        right = (width + height)/2
        bottom = (height + height)/2
        im = im.crop((left, top, right, bottom))
        #im=im.rotate(180, expand=True) - DEBUG
        
        im.convert('RGB').save(outp)
    
    elif width < height:
        left = (width - width)/2
        top = (height - width)/2
        right = (width + width)/2
        bottom = (height + width)/2
        im = im.crop((left, top, right, bottom))
        #im=im.rotate(180, expand=True) - DEBUG
        
        im.convert('RGB').save(outp)
    else:
        left = (width - width)/2
        top = (height - width)/2
        right = (width + width)/2
        bottom = (height + width)/2
        im = im.crop((left, top, right, bottom))
        #im=im.rotate(180, expand=True) - DEBUG
        
        im.convert('RGB').save(outp)

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
    
    r''' FINAL EXPORT IMAGE WITH RGB CHANNEL'''
    source = Image.open(r"output.png")
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
    
    r''' SAVE TO DISK '''
    result.save(r"images.png")



''' PROGRAMM START POINT '''
print("Processing ...")

# Image size
basesize = 200

# Cropping
input_image_crop = r"input.png"
output_image_crop = r"cropped.png"
crop(input_image_crop, output_image_crop)

# Resizing
input_image_resize = output_image_crop
output_image_resize = r"resized.png"
resize(input_image_resize, output_image_resize, basesize)

# Converting to gray
input_image_wb = output_image_resize
output_image_wb = r"output.png"
bright = 0.5
white_black(input_image_wb, output_image_wb, bright);

# Converting to array
imgid = np.array(Image.open(output_image_wb))
rlist = np.array([[0 for i in range(basesize)] for j in range(basesize)])

#print() - DEBUG

r''' - DEBUG
for g in range(100):
    for t in range(100):
        #print(imgids[g][t], end="")
        for s in range(3):
            if s == 1:
                rlist[g][t] = imgids[g][t]
'''

# Preprocessing image
for a in range(basesize):
    for b in range(basesize):
        #print(imgid[a][b], end="") - DEBUG
        if imgid[a][b][0] == 255:
            rlist[a][b] = 15
            #print("f", end = "") - DEBUG
        if imgid[a][b][0] == 238:
            rlist[a][b] = 14
            #print("e", end = "") - DEBUG
        if imgid[a][b][0] == 221:
            rlist[a][b] = 13
            #print("d", end = "") - DEBUG
        if imgid[a][b][0] == 204:
            rlist[a][b] = 12
            #print("c", end = "") - DEBUG
        if imgid[a][b][0] == 187:
            rlist[a][b] = 11
            #print("b", end = "") - DEBUG
        if imgid[a][b][0] == 170:
            rlist[a][b] = 10
            #print("a", end = "") - DEBUG
        if imgid[a][b][0] == 153:
            rlist[a][b] = 9
            #print("9", end = "") - DEBUG
        if imgid[a][b][0] == 136:
            rlist[a][b] = 8
            #print("8", end = "") - DEBUG
        if imgid[a][b][0] == 119:
            rlist[a][b] = 7
            #print("7", end = "") - DEBUG
        if imgid[a][b][0] == 102:
            rlist[a][b] = 6
            #print("6", end = "") - DEBUG
        if imgid[a][b][0] == 85:
            rlist[a][b] = 5
            #print("5", end = "") - DEBUG
        if imgid[a][b][0] == 68:
            rlist[a][b] = 4
            #print("4", end = "") - DEBUG
        if imgid[a][b][0] == 51:
            rlist[a][b] = 3
            #print("3", end = "") - DEBUG
        if imgid[a][b][0] == 34:
            rlist[a][b] = 2
            #print("2", end = "") - DEBUG
        if imgid[a][b][0] == 17:
            rlist[a][b] = 1
            #print("1", end = "") - DEBUG
        if imgid[a][b][0] == 0:
            rlist[a][b] = 0
            #print("0", end = "") - DEBUG
#    print() - DEBUG

r''' - DEBUG
for x1 in range(len(rlist)):
    for y1 in range(len(rlist[0])):
        print(rlist[x1][y1], end="")
    print()
'''

r''' SHOW IMAGE ''' r'''
for x in range(len(rlist)):
    for y in range(len(rlist[0])):
        if rlist[x][y] == 0:
            print(" ", end = "")
        if rlist[x][y] == 1:
            print(".", end = "")
        if rlist[x][y] == 2:
            print("-", end = "")
        if rlist[x][y] == 3:
            print("+", end = "")
        if rlist[x][y] == 4:
            print("=", end = "")
        if rlist[x][y] == 5:
            print(":", end = "")
        if rlist[x][y] == 6:
            print("░", end = "")
        if rlist[x][y] == 7:
            print("*", end = "")
        if rlist[x][y] == 8:
            print("▒", end = "")
        if rlist[x][y] == 9:
            print("%", end = "")
        if rlist[x][y] == 10:
            print("0", end = "")
        if rlist[x][y] == 11:
            print("$", end = "")
        if rlist[x][y] == 12:
            print("#", end = "")
        if rlist[x][y] == 13:
            print("@", end = "")
        if rlist[x][y] == 14:
            print("▓", end = "")
        if rlist[x][y] == 15:
            print("█", end = "")
    print()
'''

data = np.array(rlist.ravel())
value = 0
datastr = ""

for i in range(len(data)):
    #print(data[i]) - DEBUG
    if data[i] == 0:
        datastr = datastr + "0"
    if data[i] == 1:
        datastr = datastr + "1"
    if data[i] == 2:
        datastr = datastr + "2"
    if data[i] == 3:
        datastr = datastr + "3"
    if data[i] == 4:
        datastr = datastr + "4"
    if data[i] == 5:
        datastr = datastr + "5"
    if data[i] == 6:
        datastr = datastr + "6"
    if data[i] == 7:
        datastr = datastr + "7"
    if data[i] == 8:
        datastr = datastr + "8"
    if data[i] == 9:
        datastr = datastr + "9"
    if data[i] == 10:
        datastr = datastr + "a"
    if data[i] == 11:
        datastr = datastr + "b"
    if data[i] == 12:
        datastr = datastr + "c"
    if data[i] == 13:
        datastr = datastr + "d"
    if data[i] == 14:
        datastr = datastr + "e"
    if data[i] == 15:
        datastr = datastr + "f"

#print("Image decoded string: " + datastr) - DEBUG
value = int(datastr, 16)

# Show image ID
print()
print("Image ID: " + str(value))

# Convert id to image
toImage(value, basesize, basesize)
