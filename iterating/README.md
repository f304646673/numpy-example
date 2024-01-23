在[《使用numpy处理图片——基础操作》](https://fangliang.blog.csdn.net/article/details/135484022)一文中，我们通过对所有像素的alpha值做修改，让图片变成半透明。
![原图](https://img-blog.csdnimg.cn/direct/1bdfcadd204d4a8f825f8644bd80a56d.png#pic_center)
![统一进行alpha修改后的图](https://img-blog.csdnimg.cn/direct/aaf7570c2086415984f4551f3e8e8689.png#pic_center)
我们看到本来是黑色的字体也因为半透明的原因变得颜色比较淡。
本文我们将判断每个像素的RGB值。如果是纯白底色，则将该像素的alpha值调整到0，以达到全透明的程度，否则不做调整。
我们基本的思路就是遍历这个三维数组。这次使用的是nditer方法，它可以辅助我们进行遍历操作，而不是写三层for循环。
由于我们的逻辑需要将RGBA当做一个像素点去看待，而遍历操作会将它们当成4个独立的迭代器去看，失去了关联性。于是我们需要引入每个迭代器所代表元素的坐标来建立它们之间的关系。这样nditer的flags参数我们就传递了multi_index，以让迭代器返回坐标。比如第一个迭代器的multi_index值就是[0,0,0]。第三个维度就是RGBA的信息：坐标0表示红色（R），坐标1表示绿色（G），坐标2表示蓝色（B），坐标3表示Alpha值。如果RGB的值都是255，则说明其是白色，那就直接修改其alpha的值为0，以让这个像素点全透明。为了在遍历过程中可以修改被遍历的对象，需要给op_flags传递和“写入”相关的选项，比如writeonly和readwrite。否则nditer的迭代器就是只读的，写入将失败。
在进行修改操作时，nditer迭代器并不会马上修改原来的数据，而是将修改后的值放在一个缓冲区数组中。我们需要在适当的时机告诉它可以将换冲区数组复制到原数组中。于是可以通过with关键字来管理其上下文，以在迭代结束后通知nditer去回写；或者主动调用close方法，来触发回写。

```python
import numpy as np
from PIL import Image

img = Image.open('example.png')
data = np.array(img)

with np.nditer(data, flags=['multi_index'], op_flags=['writeonly']) as it:
    while not it.finished:
        if it.multi_index[2] == 3:
            if r == g == b == 255:
                it[0] = 0
        elif it.multi_index[2] == 0:
            r = it[0]
        elif it.multi_index[2] == 1:
            g = it[0]
        elif it.multi_index[2] == 2:
            b = it[0]
        is_not_finished = it.iternext()
        
horizontalImg = Image.fromarray(data)
horizontalImg.save('alpha0.png')
```
我们看到生成的图片比之前粗暴的将所有像素的alpha改成32的图上的字要清楚。
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/d50aeee24d834aceae7257371d34f2b5.png#pic_center)
# 代码地址
[https://github.com/f304646673/numpy-example/tree/main/alpha](https://github.com/f304646673/numpy-example/tree/main/alpha)
