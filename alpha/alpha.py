from PIL import Image
import numpy as np
img = Image.open('example.png')
data = np.array(img)
data[:,:,3]= 32
newImg = Image.fromarray(data)
newImg.save('alpha32.png')