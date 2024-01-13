import numpy as np
import PIL.Image as Image

img = Image.open('lena.png')
data = np.array(img)

blackWhiteImg = Image.fromarray(data).convert('1')
blackWhiteImg.save('blackWhite.png')

lGreyImg = Image.fromarray(data).convert('L')
lGreyImg.save('lgrey.png')
###############################################################################################################
# lightness 
lightnessGrey = ((np.max(data, axis=-1).astype(np.uint16) + np.min(data, axis=-1).astype(np.uint16)) / 2).astype(np.uint8)

lightnessGreyImg = Image.fromarray(lightnessGrey)
lightnessGreyImg.save('lightness_grey.png')
###############################################################################################################
# average 
averageGrey = np.zeros_like(data)
averageGrey[:] = (np.sum(data, axis=-1, keepdims=1) / 3).astype(np.uint8)
# averageGrey = np.mean(data, axis=2).astype(np.uint8)

averageGreyImg = Image.fromarray(averageGrey)
averageGreyImg.save('average_grey.png')
###############################################################################################################
# luminosity 
            
luminosityGrey = np.dot(data[...,:3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)

luminosityGreyImg = Image.fromarray(luminosityGrey)
luminosityGreyImg.save('luminosity_grey.png')
###############################################################################################################
sorted=np.sort(luminosityGrey.reshape(-1))
mid = sorted[sorted.shape[0] // 2]
binary = luminosityGrey > mid
binaryImg = Image.fromarray(binary.astype(np.uint8) * 255)
binaryImg.save('binary.png')