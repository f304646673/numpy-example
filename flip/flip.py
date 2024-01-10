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