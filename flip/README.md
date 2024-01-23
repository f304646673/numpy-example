在[《使用numpy处理图片——基础操作》](https://blog.csdn.net/breaksoftware/article/details/135484022)一文中，我们介绍了如何使用numpy修改图片的透明度。本文我们将介绍镜像翻转和旋转。
# 镜像翻转
## 上下翻转
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/8e23115f677e44d58d394fdbc88ce323.png)

```python
from PIL import Image
import numpy as np
img = Image.open('example.png')
data = np.array(img)

# axis=0 is vertical, axis=1 is horizontal
verticalData = np.flip(data, axis=0)
verticalImg = Image.fromarray(verticalData)
verticalImg.save('vertical.png')
```
![请添加图片描述](https://img-blog.csdnimg.cn/direct/4eda35ac9eec4d75b7925d1a6f322829.png)

## 左右翻转
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/2fe5dac1f4be412f9bfca841f6ac4706.png)


```python
from PIL import Image
import numpy as np
img = Image.open('example.png')
data = np.array(img)

# axis=0 is vertical, axis=1 is horizontal
horizontalData = np.flip(data, axis=1)
horizontalImg = Image.fromarray(horizontalData)
horizontalImg.save('horizontal.png')
```
![请添加图片描述](https://img-blog.csdnimg.cn/direct/daa036faf2ac45aa8720668d6f0e7252.png)

# 旋转
上面的翻转，又可以称之为镜像翻转。因为得到的图片，只有通过镜子去查看，才是正常的字。

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/df5d58e8cf2645e6a04a4c3266d076d5.png)
而一般情况下，我们需要的是旋转，即得到的文字还是可以正确识别的。
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/38f1f7accdd941bbba3ea8c443ef9b24.png)
## 向左旋转90度
向左旋转90需要通过两个步骤完成：

 1. 转置
 2. 上下镜像翻转
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/5d6db1581bc0446cbb05b2d672e7e01f.png)
```python
def flip_left_90(arr):
    return np.flip(arr.transpose((1,0,2)), axis=0)
```
需要解释下transpose传递元组的意思

> If specified, it must be a tuple or list which contains a permutation of [0,1,…,N-1] where N is the number of axes of a. The i’th axis of the returned array will correspond to the axis numbered axes[i] of the input. If not specified, defaults to range(a.ndim)[::-1], which reverses the order of the axes.

这句话的意思是，传递的元组要包含该数组所有的维度的值。转换的方法就是对应项相互转置。比如数组最开始时的维度表示是（0，1，2），如果给transpose传递了（1，0，2）。就意味着0维度和1维度转置，2维度保持不变。这个对我们处理图片特别重要，因为2维度保存的是RGBA信息。这个信息不能转置，否则就会导致颜色错乱。
![请添加图片描述](https://img-blog.csdnimg.cn/direct/5631871f402e4c398f18f02eea2ae33b.png)
## 旋转180度
旋转180度有两种方法：

 1. 两次90度左转。
 2. 上下镜像翻转后左右镜像翻转。（顺序无所谓）

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/a456743fda76416390c7c2078e409277.png)

```python
def flip_180_with_flip_left_90(arr):
    return flip_left_90(flip_left_90(arr))
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/df1cdbb12cb84c17b89aa74ae8a1b9ca.png)

```python
def flip_180_with_axis(arr):
    return np.flip(np.flip(arr, axis=1), axis=0)
```
![请添加图片描述](https://img-blog.csdnimg.cn/direct/ee208d80b0ad4e239218fb8b4e02271e.png)
## 向右旋转90度
向右旋转90度，也是向左旋转270度。可以拆解为：

 - 3次向左旋转
 - 1次180度旋转外加1次90度向左旋转
 - 1次90度向左旋转外加1次180度旋转

```python
def flip_right_90_with_left_90(arr):
    return flip_left_90(flip_left_90(flip_left_90(arr)))

def flip_right_90_with_axis_left_90(arr):
    return flip_left_90(flip_180_with_axis(arr))

def flip_right_90_with_left_90_axis(arr):
    return flip_180_with_axis(flip_left_90(arr))
```
![请添加图片描述](https://img-blog.csdnimg.cn/direct/3cfb45b648994d0a8edd6a39bc2c0564.png)
# 代码

```python
from PIL import Image
import numpy as np
img = Image.open('example.png')
data = np.array(img)

# axis=0 is vertical, axis=1 is horizontal
verticalData = np.flip(data, axis=0)
verticalImg = Image.fromarray(verticalData)
verticalImg.save('vertical.png')

horizontalData = np.flip(data, axis=1)
horizontalImg = Image.fromarray(horizontalData)
horizontalImg.save('horizontal.png')

def flip_180_with_flip_left_90(arr):
    return flip_left_90(flip_left_90(arr))

def flip_180_with_axis(arr):
    return np.flip(np.flip(arr, axis=1), axis=0)

def flip_left_90(arr):
    return np.flip(arr.transpose((1,0,2)), axis=0)

def flip_right_90_with_left_90(arr):
    return flip_left_90(flip_left_90(flip_left_90(arr)))

def flip_right_90_with_axis_left_90(arr):
    return flip_left_90(flip_180_with_axis(arr))

def flip_right_90_with_left_90_axis(arr):
    return flip_180_with_axis(flip_left_90(arr))

left90Data = flip_left_90(data)
left90Img = Image.fromarray(left90Data)
left90Img.save('flipleft90.png')

right90DataFromLeft90 = flip_right_90_with_left_90(data)
right90ImgFromLeft90 = Image.fromarray(right90DataFromLeft90)
right90ImgFromLeft90.save('flipright90fromleft90.png')

right90DataFromAxisLeft90 = flip_right_90_with_axis_left_90(data)
right90ImgFromAxisLeft90 = Image.fromarray(right90DataFromAxisLeft90)
right90ImgFromAxisLeft90.save('flipright90fromamxisleft90.png')

right90DataFromLeft90Axis = flip_right_90_with_left_90_axis(data)
right90ImgFromLeft90Axis = Image.fromarray(right90DataFromLeft90Axis)
right90ImgFromLeft90Axis.save('flipright90fromleft90amxis.png')

left180DataFromLeft90 = flip_180_with_flip_left_90(data)
left180ImgFromLeft90 = Image.fromarray(left180DataFromLeft90)
left180ImgFromLeft90.save('flip180fromleft90.png')

left180DataFromAxis = flip_180_with_axis(data)
left180ImgFromAxis = Image.fromarray(left180DataFromAxis)
left180ImgFromAxis.save('flip180fromaxis.png')
```
# 代码地址
[https://github.com/f304646673/numpy-example/tree/main/flip](https://github.com/f304646673/numpy-example/tree/main/flip)

# 参考资料

 - [https://flat2010.github.io/2017/05/31/Numpy%E6%95%B0%E7%BB%84%E8%A7%A3%E6%83%91/](https://flat2010.github.io/2017/05/31/Numpy%E6%95%B0%E7%BB%84%E8%A7%A3%E6%83%91/)
 - [https://numpy.org/doc/stable/reference/generated/numpy.transpose.html](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html)
