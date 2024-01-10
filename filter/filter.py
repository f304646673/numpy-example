import numpy as np
from PIL import Image

img = Image.open('the_starry_night.jpg')
data = np.array(img)

# colorDim3List = np.dsplit(data, 3)
# red = colorDim3List[0]
# green = colorDim3List[1]
# blue = colorDim3List[2]

dataOneDim = data.reshape(data.size)
red = dataOneDim[0::3].reshape((data.shape[0], data.shape[1], 1))
green = dataOneDim[1::3].reshape((data.shape[0], data.shape[1], 1))
blue = dataOneDim[2::3].reshape((data.shape[0], data.shape[1], 1))

zeros = np.zeros_like(blue)

redgreen = np.dstack((red, green, zeros))
redgreenImg = Image.fromarray(redgreen)
redgreenImg.save('redgreen.png')

redblue = np.dstack((red, zeros, blue))
redblueImg = Image.fromarray(redblue)
redblueImg.save('redblue.png')

greenblue = np.dstack((zeros, green, blue))
greenblueImg = Image.fromarray(greenblue)
greenblueImg.save('greenblue.png')


