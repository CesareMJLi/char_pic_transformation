

import os
import argparse

# parse the input parameters
parser = argparse.ArgumentParser()

parser.add_argument('gif')

args = parser.parse_args()

GIF = args.gif

counter = 0

# try:
#     while True:
#         cmd = "python transform.py "+GIF+"-"+str(counter)+".png --width 30 --height 30"
#         os.system(cmd)
#         counter+=1
# except EOFError:
#     quit()

cd = "cd "+GIF
os.system(cd)

# while True:
#     try:
#         cmd = "python transform.py "+GIF+"-"+str(counter)+".png --width 30 --height 30"
#         os.system(cmd)
#         counter+=1
#     except Exception:
#         print("#"*30)
#         break

while counter<=10:
    cmd = "python transform.py "+GIF+"-"+str(counter)+".png --width 30 --height 30"
    os.system(cmd)
    counter+=1