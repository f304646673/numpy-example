import numpy as np
import PIL.Image as Image

img = Image.open('the_starry_night.jpg')
data = np.array(img)

compressX = data[:,::2]
compressY = data[::2,:]

compressXImg = Image.fromarray(compressX)
compressXImg.save('compressx.png')

compressYImg = Image.fromarray(compressY)
compressYImg.save('compressy.png')