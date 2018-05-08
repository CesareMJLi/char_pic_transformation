
from PIL import Image
import argparse

# parse the input parameters
parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-o','--output')
parser.add_argument('--width',type = int)
parser.add_argument('--height',type = int)

args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char=''' 01'''
ascii_length=len(ascii_char)

def char_for_pixel(r,g,b,alpha = 256):
    # RGBA files, rgb are 3 channels and alpha is a paramter about the transparency
    if alpha == 0:
        return ' '
    gray = int(r* 0.299+g* 0.587+b* 0.114)
    # unit = (256.0+1)/ascii_length
    # return ascii_char[int(gray/unit)]
    return ascii_char[int(gray%ascii_length)]

if __name__ == '__main__':
    img = Image.open(IMG)
    # img = img.convert("L")
    if not HEIGHT:
        height=80
        width=int(img.size[1]*0.5/(img.size[0]/80))
        img = img.resize((height,width))
    else:
        img = img.resize((HEIGHT,WIDTH))
    txt = ""
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            # r,g,b,a = img.getpixel((j,i))
            txt += char_for_pixel(*img.getpixel((j,i)))
        txt += '\n'
    print txt

    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
