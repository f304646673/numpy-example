在[《使用numpy处理图片——滤镜》](https://blog.csdn.net/breaksoftware/article/details/135510077)和[《用numpy处理图片——模糊处理》](https://blog.csdn.net/breaksoftware/article/details/135512428)中，我们认识到对三维数组使用dsplit方法按第3维度（深度）方向切分的方法。
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/54d1ee65a9bf4dbc8339926d5b39f64c.png)
本文我们将介绍如何进行第一和第二维度切分，来达到图片切割的效果。
# 上下切分
上下切分也是按第一维度切分，使用的是vsplit方法。

```python
import numpy as np
from PIL import Image

img = Image.open('the_starry_night.jpg')
data = np.array(img)

topBottom = np.vsplit(data, 2)
top = topBottom[0]
bottom = topBottom[1]
```
上面我们给vsplit第二个参数传递的是2，即将数组按第一维度切分为上下2部分。
# 左右切分
我们分别对之前切分的上下两部分，进行第二维度切分，使用的是hsplit方法。我们给hsplit第二个参数传递的是2，也就是说我们要将其切分成左右两部分。
```python
leftRight = np.hsplit(top, 2)
topLeft = leftRight[0]
topRight = leftRight[1]

leftRight = np.hsplit(bottom, 2)
bottomLeft = leftRight[0]
bottomRight = leftRight[1]
```
于是构成上左、上右、下左和下右四部分。
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/bde69b75c1d94438b0db8f3a1fbeb50e.png)

以梵高的《星空》为例。
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/74e16484ce844beaaa959f7c885e9ebc.jpeg#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/765ac208edd64495b3e7ce00bb07614d.png#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/2f90cb485a7b499c8d092c48fc110b32.png#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/830fe0528e2b42818c0e43a03fc0e643.png#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/8fd25fa587864d5495afb8ead72fa57c.png#pic_center)
# 代码地址
[https://github.com/f304646673/numpy-example/tree/main/split](https://github.com/f304646673/numpy-example/tree/main/split)
