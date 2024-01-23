缩放图片是让图片丢失部分像素，从而导致图片失真。一种比较简单的方法就是抽取法。比如如果我们要将照片在宽度上缩小50%，则可以在第二维度上每隔2个像素取一个像素来保存；类似的，如果我们希望在高度上缩小50%，则可以在第一维度上每隔2个像素取一个像素保存。

```python
import numpy as np
import PIL.Image as Image

img = Image.open('the_starry_night.jpg')
data = np.array(img)

compressX = data[:,::2]
compressY = data[::2,:]

compressXImg = Image.fromarray(compressX)
compressXImg.save('compressx.png')

compressYImg = Image.fromarray(compressY)
compressYImg.save('compressy.png')
```
以compressX = data[:,::2]为例。第一个“:”表示对所有第一维度（高度）上的数组都遍历到，“::2”是指对第二个维度上每隔2个像素取一个。
我们看下效果：
原图
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/fd5cb8c4727646feb518f64fcb0fc236.jpeg#pic_center)

宽度缩放（第二维度）
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/93cd71d5467d4313938d0872ac488e93.png#pic_center)

高度缩放（第一维度）

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/0180031ea16c4b2787edf14c30babbb6.png#pic_center)
# 代码地址
[https://github.com/f304646673/numpy-example/tree/main/compress](https://github.com/f304646673/numpy-example/tree/main/compress)
