import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

img = Image.open('the_starry_night.jpg')
data = np.array(img)

colorDim3List = np.dsplit(data, 3)
red = colorDim3List[0].reshape((data.shape[0], data.shape[1]))
green = colorDim3List[1].reshape((data.shape[0], data.shape[1]))
blue = colorDim3List[2].reshape((data.shape[0], data.shape[1]))

redGaussian = ndimage.gaussian_filter(red, sigma=1.5)
greenGaussian = ndimage.gaussian_filter(green, sigma=1.5)
blueGaussian = ndimage.gaussian_filter(blue, sigma=1.5)

gaussian = np.dstack((redGaussian, greenGaussian, blueGaussian))
gaussianImg = Image.fromarray(gaussian)
gaussianImg.save('gaussian.png')

redBox = ndimage.uniform_filter(red, size=15)
greenBox = ndimage.uniform_filter(green, size=15)
blueBox = ndimage.uniform_filter(blue, size=15)

box = np.dstack((redBox, greenBox, blueBox))
boxImg = Image.fromarray(box)
boxImg.save('box.png')

redMedian = ndimage.median_filter(red, size=15)
greenMedian = ndimage.median_filter(green, size=15)
blueMedian = ndimage.median_filter(blue, size=15)

median = np.dstack((redMedian, greenMedian, blueMedian))
medianImg = Image.fromarray(median)
medianImg.save('median.png')

redMaximum = ndimage.maximum_filter(red, size=15)
greenMaximum = ndimage.maximum_filter(green, size=15)
blueMaximum = ndimage.maximum_filter(blue, size=15)

maximum = np.dstack((redMaximum, greenMaximum, blueMaximum))
maximumImg = Image.fromarray(maximum)
maximumImg.save('maximum.png')

redMinimum = ndimage.minimum_filter(red, size=15)
greenMinimum = ndimage.minimum_filter(green, size=15)
blueMinimum = ndimage.minimum_filter(blue, size=15)

minimum = np.dstack((redMinimum, greenMinimum, blueMinimum))
minimumImg = Image.fromarray(minimum)
minimumImg.save('minimum.png')

redPercentile = ndimage.percentile_filter(red, percentile=50, size=15)
greenPercentile = ndimage.percentile_filter(green, percentile=50, size=15)
bluePercentile = ndimage.percentile_filter(blue, percentile=50, size=15)

percentile = np.dstack((redPercentile, greenPercentile, bluePercentile))
percentileImg = Image.fromarray(percentile)
percentileImg.save('percentile.png')

redRank = ndimage.rank_filter(red, rank=15, size=15)
greenRank = ndimage.rank_filter(green, rank=15, size=15)
blueRank = ndimage.rank_filter(blue, rank=15, size=15)

rank = np.dstack((redRank, greenRank, blueRank))
rankImg = Image.fromarray(rank)
rankImg.save('rank.png')

redGaussianLaplace = ndimage.gaussian_laplace(red, sigma=1.5)
greenGaussianLaplace = ndimage.gaussian_laplace(green, sigma=1.5)
blueGaussianLaplace = ndimage.gaussian_laplace(blue, sigma=1.5)

gaussianLaplace = np.dstack((redGaussianLaplace, greenGaussianLaplace, blueGaussianLaplace))
gaussianLaplaceImg = Image.fromarray(gaussianLaplace)
gaussianLaplaceImg.save('gaussianlaplace.png')

redCorrelate = ndimage.correlate(red, weights=np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
greenCorrelate = ndimage.correlate(green, weights=np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
blueCorrelate = ndimage.correlate(blue, weights=np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))

correlate = np.dstack((redCorrelate, greenCorrelate, blueCorrelate))
correlateImg = Image.fromarray(correlate)
correlateImg.save('correlate.png')

redMorphologicalLaplace = ndimage.morphological_laplace(red, size=15)
greenMorphologicalLaplace = ndimage.morphological_laplace(green, size=15)
blueMorphologicalLaplace = ndimage.morphological_laplace(blue, size=15)

morphologicalLaplace = np.dstack((redMorphologicalLaplace, greenMorphologicalLaplace, blueMorphologicalLaplace))
morphologicalLaplaceImg = Image.fromarray(morphologicalLaplace)
morphologicalLaplaceImg.save('morphologicallaplace.png')

redWhiteTophat = ndimage.white_tophat(red, size=15)
greenWhiteTophat = ndimage.white_tophat(green, size=15)
blueWhiteTophat = ndimage.white_tophat(blue, size=15)

whiteTophat = np.dstack((redWhiteTophat, greenWhiteTophat, blueWhiteTophat))
whiteTophatImg = Image.fromarray(whiteTophat)
whiteTophatImg.save('whitetophat.png')

redMorphologicalGradient = ndimage.morphological_gradient(red, size=15)
greenMorphologicalGradient = ndimage.morphological_gradient(green, size=15)
blueMorphologicalGradient = ndimage.morphological_gradient(blue, size=15)

morphologicalGradient = np.dstack((redMorphologicalGradient, greenMorphologicalGradient, blueMorphologicalGradient))
morphologicalGradientImg = Image.fromarray(morphologicalGradient)
morphologicalGradientImg.save('morphologicalgradient.png')

redBlackTophat = ndimage.black_tophat(red, size=15)
greenBlackTophat = ndimage.black_tophat(green, size=15)
blueBlackTophat = ndimage.black_tophat(blue, size=15)

blackTophat = np.dstack((redBlackTophat, greenBlackTophat, blueBlackTophat))
blackTophatImg = Image.fromarray(blackTophat)
blackTophatImg.save('blacktophat.png')
