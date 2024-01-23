在[《使用numpy处理图片——滤镜》](https://blog.csdn.net/breaksoftware/article/details/135510077)一文中，我们尝试了去掉一原色来产生滤镜效果。本文将使用更复杂的算法，来做图像模糊处理。
基本思路还是和前文类似：先切分出各个原色的数组，然后对每个数组用算法进行重新计算，最后把它们堆叠到一起。
区别在于，我们需要把各个原色的数组从3维变成2维。对2维数组进行计算，然后把3个2维数组堆叠出一个3维数组。
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/a1eb77e577d841d0aa36c99729f433d3.png)

```python
import numpy as np
from PIL import Image
import scipy.ndimage as ndimage

img = Image.open('the_starry_night.jpg')
data = np.array(img)

colorDim3List = np.dsplit(data, 3)
red = colorDim3List[0].reshape((data.shape[0], data.shape[1]))
green = colorDim3List[1].reshape((data.shape[0], data.shape[1]))
blue = colorDim3List[2].reshape((data.shape[0], data.shape[1]))
```
data就是原始图片的3维数组。
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/1fc672f31842489e966637482a4d0e48.png)
colorDim3List是一个数组，每个元素是一个3维数组。比如colorDim3List[0]就是红色（R）值构成的3维数组。
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/e32e41889d5e4a86ab3ff1441d12feb1.png)
colorDim3List[0].reshape((data.shape[0], data.shape[1]))是通过reshape方法，将3维数组重构成2维数组。
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/57d1eb2cb8274fbbb19b6d679bf9c3cf.png)
至此，我们准备工作做完了。下面我们将展现各种模糊处理。算法是由scipy库提供。

```python
import scipy.ndimage as ndimage
```
最后我们看一眼原图。
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/6acaadddf26349fbb7f1f8d27c094711.jpeg#pic_center)

# 高斯模糊

```python
redGaussian = ndimage.gaussian_filter(red, sigma=1.5)
greenGaussian = ndimage.gaussian_filter(green, sigma=1.5)
blueGaussian = ndimage.gaussian_filter(blue, sigma=1.5)

gaussian = np.dstack((redGaussian, greenGaussian, blueGaussian))
gaussianImg = Image.fromarray(gaussian)
gaussianImg.save('gaussian.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/929f1743a4d04de0af351e0f302dd9b5.png#pic_center)
# 方框模糊

```python
redBox = ndimage.uniform_filter(red, size=15)
greenBox = ndimage.uniform_filter(green, size=15)
blueBox = ndimage.uniform_filter(blue, size=15)

box = np.dstack((redBox, greenBox, blueBox))
boxImg = Image.fromarray(box)
boxImg.save('box.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/3c2ae3c61c094231861092425e5b392b.png#pic_center)
# 其他算法
## median_filter

```python
redMedian = ndimage.median_filter(red, size=15)
greenMedian = ndimage.median_filter(green, size=15)
blueMedian = ndimage.median_filter(blue, size=15)

median = np.dstack((redMedian, greenMedian, blueMedian))
medianImg = Image.fromarray(median)
medianImg.save('median.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/09ac2428c56a47d893da63ea2d3a8815.png#pic_center)
## maximum_filter

```python
redMaximum = ndimage.maximum_filter(red, size=15)
greenMaximum = ndimage.maximum_filter(green, size=15)
blueMaximum = ndimage.maximum_filter(blue, size=15)

maximum = np.dstack((redMaximum, greenMaximum, blueMaximum))
maximumImg = Image.fromarray(maximum)
maximumImg.save('maximum.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/7dd14eacb8f84b7e84c588f4dbdb0599.png#pic_center)
## minimum_filter

```python
redMinimum = ndimage.minimum_filter(red, size=15)
greenMinimum = ndimage.minimum_filter(green, size=15)
blueMinimum = ndimage.minimum_filter(blue, size=15)

minimum = np.dstack((redMinimum, greenMinimum, blueMinimum))
minimumImg = Image.fromarray(minimum)
minimumImg.save('minimum.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/47e71bda1ba4477da32a87fec755f9bb.png#pic_center)
## percentile_filter

```python
redPercentile = ndimage.percentile_filter(red, percentile=50, size=15)
greenPercentile = ndimage.percentile_filter(green, percentile=50, size=15)
bluePercentile = ndimage.percentile_filter(blue, percentile=50, size=15)

percentile = np.dstack((redPercentile, greenPercentile, bluePercentile))
percentileImg = Image.fromarray(percentile)
percentileImg.save('percentile.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/51cf73b459624b0a9e976e9e370281f8.png#pic_center)
## rank_filter

```python
redRank = ndimage.rank_filter(red, rank=15, size=15)
greenRank = ndimage.rank_filter(green, rank=15, size=15)
blueRank = ndimage.rank_filter(blue, rank=15, size=15)

rank = np.dstack((redRank, greenRank, blueRank))
rankImg = Image.fromarray(rank)
rankImg.save('rank.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/983acf990fb848c4bfc88481cb8676e6.png#pic_center)
## gaussian_laplace

```python
redGaussianLaplace = ndimage.gaussian_laplace(red, sigma=1.5)
greenGaussianLaplace = ndimage.gaussian_laplace(green, sigma=1.5)
blueGaussianLaplace = ndimage.gaussian_laplace(blue, sigma=1.5)

gaussianLaplace = np.dstack((redGaussianLaplace, greenGaussianLaplace, blueGaussianLaplace))
gaussianLaplaceImg = Image.fromarray(gaussianLaplace)
gaussianLaplaceImg.save('gaussianlaplace.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/23599bf6998a4de5a2522146a9f8dc10.png#pic_center)
## correlate

```python
redCorrelate = ndimage.correlate(red, weights=np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
greenCorrelate = ndimage.correlate(green, weights=np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
blueCorrelate = ndimage.correlate(blue, weights=np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))

correlate = np.dstack((redCorrelate, greenCorrelate, blueCorrelate))
correlateImg = Image.fromarray(correlate)
correlateImg.save('correlate.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/e54b1c1e8eef4070b42ce3df87924fcd.png#pic_center)
## morphological_laplace

```python
redMorphologicalLaplace = ndimage.morphological_laplace(red, size=15)
greenMorphologicalLaplace = ndimage.morphological_laplace(green, size=15)
blueMorphologicalLaplace = ndimage.morphological_laplace(blue, size=15)

morphologicalLaplace = np.dstack((redMorphologicalLaplace, greenMorphologicalLaplace, blueMorphologicalLaplace))
morphologicalLaplaceImg = Image.fromarray(morphologicalLaplace)
morphologicalLaplaceImg.save('morphologicallaplace.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/97eaab106640484b84a6dd7ab79c5b35.png#pic_center)
## white_tophat

```python
redWhiteTophat = ndimage.white_tophat(red, size=15)
greenWhiteTophat = ndimage.white_tophat(green, size=15)
blueWhiteTophat = ndimage.white_tophat(blue, size=15)

whiteTophat = np.dstack((redWhiteTophat, greenWhiteTophat, blueWhiteTophat))
whiteTophatImg = Image.fromarray(whiteTophat)
whiteTophatImg.save('whitetophat.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/0c3f8f6cacd2448cb41068e1eb59f567.png#pic_center)
## morphological_gradient

```python
redMorphologicalGradient = ndimage.morphological_gradient(red, size=15)
greenMorphologicalGradient = ndimage.morphological_gradient(green, size=15)
blueMorphologicalGradient = ndimage.morphological_gradient(blue, size=15)

morphologicalGradient = np.dstack((redMorphologicalGradient, greenMorphologicalGradient, blueMorphologicalGradient))
morphologicalGradientImg = Image.fromarray(morphologicalGradient)
morphologicalGradientImg.save('morphologicalgradient.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/268042d1caf54d19b7cd4c073229b6bc.png#pic_center)
## black_tophat

```python
redBlackTophat = ndimage.black_tophat(red, size=15)
greenBlackTophat = ndimage.black_tophat(green, size=15)
blueBlackTophat = ndimage.black_tophat(blue, size=15)

blackTophat = np.dstack((redBlackTophat, greenBlackTophat, blueBlackTophat))
blackTophatImg = Image.fromarray(blackTophat)
blackTophatImg.save('blacktophat.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/0b6b3f611db647a9b39e4d1bcc251814.png#pic_center)
# 代码地址
[https://github.com/f304646673/numpy-example/tree/main/blur](https://github.com/f304646673/numpy-example/tree/main/blur)
