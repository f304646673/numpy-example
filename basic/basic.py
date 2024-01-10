from PIL import Image
import numpy as np
img = Image.open('example.png')
data = np.array(img)
print(data.shape)