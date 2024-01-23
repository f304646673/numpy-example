在[《使用numpy处理图片——图片切割》](https://blog.csdn.net/breaksoftware/article/details/135514849)一文中，我们介绍了如何使用numpy将一张图片切割成4部分。本文我们将反其道而行之，将4张图片拼接成1张图片。
基本的思路就是先用两张图以左右结构拼接成上部，另外两张图也以左右拼接成为下部。然后上下两部再拼接。当然也可以先上下拼接成左部和右部，然后再左右拼接。
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/8e6186ccf5ba4dff9079d60c53fcd0f9.png)
# 左右拼接
左右拼接也就是第二维度拼接。使用的是hstack方法，给它传递的是需要拼接的数组所组成的元组。这样我们就拼接出上下两部。
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/69529b6604d7493db63ccb6341ca1067.png)

```python
import numpy as np
from PIL import Image

correlateImg = Image.open('correlate.png')
correlateData = np.array(correlateImg)

gaussianLaplaceImg = Image.open('gaussianlaplace.png')
gaussianLaplaceData = np.array(gaussianLaplaceImg)

morphoLogicalLaplaceImg = Image.open('morphologicallaplace.png')
morphoLogicalLaplaceData = np.array(morphoLogicalLaplaceImg)

whiteTophatImg = Image.open('whitetophat.png')
whiteTophatData = np.array(whiteTophatImg)

top = np.hstack((correlateData, gaussianLaplaceData))
bottom = np.hstack((morphoLogicalLaplaceData, whiteTophatData))
```
# 上下拼接
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/c6a0129ea7cd44a29ec6cf053adac8fc.png)
上下拼接使用的是vstack方法。给它传递的是上下两部数组组成的元组。
```python
full = np.vstack((top, bottom))

fullImg = Image.fromarray(full)
fullImg.save('full.png')
```

我们以[《使用numpy处理图片——模糊处理》](https://blog.csdn.net/breaksoftware/article/details/135512428)中生成的图片为例，用4个模糊处理的图片拼接出1张图片。
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/75673b26b2964190a4af4eb4f8f4cec7.png#pic_center)
# 代码地址
[https://github.com/f304646673/numpy-example/tree/main/stack](https://github.com/f304646673/numpy-example/tree/main/stack)
