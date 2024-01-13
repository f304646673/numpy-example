import numpy as np
import PIL.Image as Image
import scipy.ndimage as ndimage

data = np.array(Image.open('the_starry_night.jpg'))

left30 = ndimage.rotate(data, 30)

Image.fromarray(left30).save('left30.png')

right30 = ndimage.rotate(data, -30)

Image.fromarray(right30).save('right30.png')

left135 = ndimage.rotate(data, 135, reshape=False)

Image.fromarray(left135).save('left135.png')

right135 = ndimage.rotate(data, -135, reshape=False)

Image.fromarray(right135).save('right135.png')