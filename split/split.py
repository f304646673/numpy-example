import numpy as np
from PIL import Image

img = Image.open('the_starry_night.jpg')
data = np.array(img)

topBottom = np.vsplit(data, 2)
top = topBottom[0]
bottom = topBottom[1]

leftRight = np.hsplit(top, 2)
topLeft = leftRight[0]
topRight = leftRight[1]

leftRight = np.hsplit(bottom, 2)
bottomLeft = leftRight[0]
bottomRight = leftRight[1]

topLeftImg = Image.fromarray(topLeft)
topLeftImg.save('top_left.png')

topRightImg = Image.fromarray(topRight)
topRightImg.save('top_right.png')

bottomLeftImg = Image.fromarray(bottomLeft)
bottomLeftImg.save('bottom_left.png')

bottomRightImg = Image.fromarray(bottomRight)
bottomRightImg.save('bottom_right.png')