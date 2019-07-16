from PIL import Image
# import os, sys

for i in range(360, 361, 10):
    inf = Image.open("omg"+str(i)+".eps")
    outf = "omg"+str(i)+".jpg"
    inf.save(outf)
