灰阶（Gray scale）影像是每个像素只有一个采样颜色的图像。
# 载入图像
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/b0c9fdee543744229b05ca8b0a36775e.png#pic_center)

```python
import numpy as np
import PIL.Image as Image

img = Image.open('lena.png')
data = np.array(img)
```

# 灰阶处理
我们有三种方法来生成这种图像。

## lightness
基本算法就是对每个像素点的RGB值取最大和最小值的均值，即（Max(RGB)+Min(RGB))/2。
```python
lightnessGrey = ((np.max(data, axis=-1).astype(np.uint16) + np.min(data, axis=-1).astype(np.uint16)) / 2).astype(np.uint8)

lightnessGreyImg = Image.fromarray(lightnessGrey)
lightnessGreyImg.save('lightness_grey.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/a0342283e44c4809bdfe2d8b96194cbc.png#pic_center)
## average
基本算法就是对每个像素点的RGB取均值，即（R+G+B）/3。
```python
averageGrey = np.zeros_like(data)
averageGrey[:] = (np.sum(data, axis=-1, keepdims=1) / 3).astype(np.uint8)
# averageGrey = np.mean(data, axis=2).astype(np.uint8)

averageGreyImg = Image.fromarray(averageGrey)
averageGreyImg.save('average_grey.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/951db6006fe14345952598c25f9065f9.png#pic_center)

## luminosity
这种方法是一种加权算法。它会对每个像素的RGB的值配以不同的权重来计算出一个新的值，即0.2989R+0.587G+ 0.114B。
```python
# luminosity 
            
luminosityGrey = np.dot(data[...,:3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)

luminosityGreyImg = Image.fromarray(luminosityGrey)
luminosityGreyImg.save('luminosity_grey.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/506f2fada0a84304b25d6898f2604fde.png#pic_center)
还有一种写法就是用PIL库

```python
lGreyImg = Image.fromarray(data).convert('L')
lGreyImg.save('lgrey.png')
```
# 代码地址
[https://github.com/f304646673/numpy-example/tree/main/grey](https://github.com/f304646673/numpy-example/tree/main/grey)
