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