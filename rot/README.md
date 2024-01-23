在[《使用numpy处理图片——90度旋转》](https://blog.csdn.net/breaksoftware/article/details/135534921)中，我们使用numpy提供的方法，可以将矩阵旋转90度。而如果我们需要旋转任意角度，则需要自己撸很多代码。如果我们使用scipy库提供的方法，则会容易很多。
需要注意的是，旋转导致原始的图片会“撑开”修改后的图片大小。当然我们也可以通过参数设置，让图片大小不变，但是会让部分图片显示不出来。

# 载入图片

```python
import numpy as np
import PIL.Image as Image
import scipy.ndimage as ndimage

data = np.array(Image.open('the_starry_night.jpg'))
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/cb204335469245058b578ff2c0c8a771.jpeg#pic_center)

# 左旋转30度，且重新调整图片大小

```python
left30 = ndimage.rotate(data, 30)

Image.fromarray(left30).save('left30.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/f9069738c900413da7bd1640cbf251ce.png#pic_center)


# 右旋转30度，且重新调整图片大小

```python
right30 = ndimage.rotate(data, -30)

Image.fromarray(right30).save('right30.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/41c5b64be48f467c9f35460cd6518933.png#pic_center)
# 左旋转135度，保持图片大小不变
注意我们给reshape参数传递了False，即不调整图片大小
```python
left135 = ndimage.rotate(data, 135, reshape=False)

Image.fromarray(left135).save('left135.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/e309c52629f9425ab3be1277ef670d44.png#pic_center)

# 右旋转135度，保持图片大小不变

```python
right135 = ndimage.rotate(data, -135, reshape=False)

Image.fromarray(right135).save('right135.png')
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/04f04798e5d54f9ab4f5c852306779f6.png#pic_center)
# 代码地址
[https://github.com/f304646673/scipy-ndimage-example/tree/main/rot](https://github.com/f304646673/scipy-ndimage-example/tree/main/rot)
