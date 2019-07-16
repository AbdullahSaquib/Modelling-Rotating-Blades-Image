from PIL import Image
# import os, sys

for i in range(0, 201, 5):
    inf = Image.open("ts"+str(i)+".eps")
    outf = "ts"+str(i)+".jpg"
    inf.save(outf)
