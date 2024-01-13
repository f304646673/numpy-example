import numpy as np
import PIL.Image as Image

img = Image.open('the_starry_night.jpg')
data = np.array(img)

colorDim3List = np.dsplit(data, 3)
red = colorDim3List[0].reshape(data.shape[0], data.shape[1])
green = colorDim3List[1].reshape(data.shape[0], data.shape[1])
blue = colorDim3List[2].reshape(data.shape[0], data.shape[1])

zeros = np.zeros_like(blue)
red = np.dstack((red, zeros, zeros))
green = np.dstack((zeros, green, zeros))
blue = np.dstack((zeros, zeros, blue))

red, green, blue = data.copy(), data.copy(), data.copy()
red[:, :, (1,2)] = 0
green[:, :, (0,2)] = 0
blue[:, :, (0,1)] = 0

redImg = Image.fromarray(np.hstack((red, green, blue)))
redImg.save('rgb.png')

