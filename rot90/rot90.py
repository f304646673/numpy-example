import numpy as np
import PIL.Image as Image

data = np.array(Image.open('the_starry_night.jpg'))

# left 90
rot90LeftWithOne = np.rot90(data, 1)

rot90LeftWithOneImg = Image.fromarray(rot90LeftWithOne)
rot90LeftWithOneImg.save('rot90leftone.png')

# right 90
rot90RightWithMinusOne = np.rot90(data, -1)

rot90RightWithMinusOneImg = Image.fromarray(rot90RightWithMinusOne)
rot90RightWithMinusOneImg.save('rot90rightminusone.png')

rot90RightWithThree = np.rot90(data, 3)

rot90RightWithThreeImg = Image.fromarray(rot90RightWithThree)
rot90RightWithThreeImg.save('rot90rightthree.png')

rot90RightWithAOnexes = np.rot90(data, 1, axes=(1,0))

rot90RightWithAOnexesImg = Image.fromarray(rot90RightWithAOnexes)
rot90RightWithAOnexesImg.save('rot90rightaonexes.png')

# rot 180
rot180WithLeftTwice = np.rot90(data, 2)

rot180WithLeftTwiceImg = Image.fromarray(rot180WithLeftTwice)
rot180WithLeftTwiceImg.save('rot180lefttwice.png')

rot180WithRightMinusTwo = np.rot90(data, -2)

rot180WithRightMinusTwoImg = Image.fromarray(rot180WithRightMinusTwo)
rot180WithRightMinusTwoImg.save('rot180rightminustwo.png')