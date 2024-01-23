滚动图片是指：图片尺寸不变的情况下，把图片内容做某个方向的移动。这样就会出现一种情况：被移走的区域显示为空白，或者被超出尺寸的区域填充。
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/40b50f1820eb4d6c973b93ffdf955039.png#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/76987f517afc453ca2dfbc0be33db823.png#pic_center)
numpy的滚动数组的方法能够做到下图效果，即空白区域用超出尺寸的元素填充。
下面代码中（100,300,0）和（0,1,2）表示0轴方向（向下）移动100个元素，1轴方向（向右）移动300个元素，2轴方向不变。
```python
import numpy as np
from PIL import Image

img = Image.open('the_starry_night.jpg')
data = np.array(img)

rollData = np.roll(data, (100,300,0), axis=(0,1,2))
Image.fromarray(rollData).save('roll.png')
```
![请添加图片描述](https://img-blog.csdnimg.cn/direct/5a7a8669aa234e268bab9e35c5bb909a.png)
# 代码地址
[https://github.com/f304646673/numpy-example/tree/main/roll](https://github.com/f304646673/numpy-example/tree/main/roll)
