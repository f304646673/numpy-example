在[《使用numpy处理图片——滤镜》](https://fangliang.blog.csdn.net/article/details/135510077)中，我们剥离了RGB中的一个颜色，达到一种滤镜的效果。
如果我们只保留一种元素，就可以做到PS中分离通道的效果。
# 读入图片

```python
import numpy as np
import PIL.Image as Image

img = Image.open('the_starry_night.jpg')
data = np.array(img)
```

# 分离通道
## 堆叠法
堆叠法是先把各个通道分离出来，然后重构成二维数组。最后和其他值为0的同大小二维数组进行堆叠，构造成三维数组。
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/bab7ec591dd5492eb529ffd80e10e601.png)

```python
colorDim3List = np.dsplit(data, 3)
red = colorDim3List[0].reshape(data.shape[0], data.shape[1])
green = colorDim3List[1].reshape(data.shape[0], data.shape[1])
blue = colorDim3List[2].reshape(data.shape[0], data.shape[1])

zeros = np.zeros_like(blue)
red = np.dstack((red, zeros, zeros))
green = np.dstack((zeros, green, zeros))
blue = np.dstack((zeros, zeros, blue))
```
## 复制修改法
复制修改法就是将原来的三维数组进行复制，然后针对性的修改第三维度上相应字段的值。
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/c12d45cad9a948e780fd397e81efee33.png)

```python
red, green, blue = data.copy(), data.copy(), data.copy()
red[:, :, (1,2)] = 0
green[:, :, (0,2)] = 0
blue[:, :, (0,1)] = 0
```

# 生成图片
原图
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/27abd028af384174a610670d1f1b2fe3.jpeg#pic_center)

我们在一张图中展现各个通道。
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/78aa842066b141069023d37278cb6962.png#pic_center)
# 代码地址
[https://github.com/f304646673/numpy-example/tree/main/rgb](https://github.com/f304646673/numpy-example/tree/main/rgb)
