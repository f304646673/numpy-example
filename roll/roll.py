import numpy as np
from PIL import Image

img = Image.open('the_starry_night.jpg')
data = np.array(img)

rollData = np.roll(data, (100,300,0), axis=(0,1,2))
Image.fromarray(rollData).save('roll.png')