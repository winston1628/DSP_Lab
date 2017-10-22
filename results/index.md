# 陳永慶 <span style="color:red">(103061122)</span>

# Project 0 / Pixel Array Manipulation

## Overview
1. The project is related to 
	* Image file input/output <br />
	* pixel array manipulation, ex: grey scale, image flip, rotation

## Implementation
## grey scale
### Goals
> converting a colored image to grey scaled image.

### Procedure
	matrix = np.array([0.299, 0.587, 0.114])
	Y = np.sum(I * matrix, axis = 2)
	I_grey[:,:,0] = Y
	I_grey[:,:,1] = Y
	I_grey[:,:,2] = Y

First, create a intensity matrix. Then each pixel of RGB and intensity matrix do the inner product. The value of RGB is the third dimension, so I sum the third dimension of the inner product.

### Results

<div style="text-align: center">
<img src="/Users/winston/Desktop/DSP_Lab_HW0/image.jpg" width="300"/>

<img src="/Users/winston/Desktop/DSP_Lab_HW0/example.jpg" width="300"/>

original image

<img src="/Users/winston/Desktop/DSP_Lab_HW0/results/image/grey_image.jpg" width="300"/>

<img src="/Users/winston/Desktop/DSP_Lab_HW0/results/image/grey_example.jpg" width="300"/>

grey-scale image

<div style="text-align: left">
## Image Flipping
### Goals 
> flip the image in three ways: <br />
> horizontal flipping (type 0) <br />
> vertical flipping (type 1) <br />
> horizontal & vertical flipping (type 2)

### Procedure
	if (type == 0):
	for i in range(I.shape[0]):
		I_flip[i, :, 0] = I[i, ::-1, 0]
		I_flip[i, :, 1] = I[i, ::-1, 1]
		I_flip[i, :, 2] = I[i, ::-1, 2]

Using if statement to choose the type and then reverse each row or each column of pixel.

### Results

<div style="text-align: center">
<img src="/Users/winston/Desktop/DSP_Lab_HW0/image.jpg" width="300"/>

<img src="/Users/winston/Desktop/DSP_Lab_HW0/example.jpg" width="300"/>

original image

<img src="/Users/winston/Desktop/DSP_Lab_HW0/results/image/H_flip_image.jpg" width="300"/>

<img src="/Users/winston/Desktop/DSP_Lab_HW0/results/image/H_flip_example.jpg" width="300"/>

horizontal flipping image

<img src="/Users/winston/Desktop/DSP_Lab_HW0/results/image/V_flip_image.jpg" width="300"/>

<img src="/Users/winston/Desktop/DSP_Lab_HW0/results/image/V_flip_example.jpg" width="300"/>

vertical flipping image

<img src="/Users/winston/Desktop/DSP_Lab_HW0/results/image/H&V_flip_image.jpg" width="300"/>

<img src="/Users/winston/Desktop/DSP_Lab_HW0/results/image/H&V_flip_example.jpg" width="300"/>

horizontal % vertical flipping image

<div style="text-align: left">
## Image Rotation
### Goals 
> rotate the image from original image. I try three different angles <br />
> 45 degree <br />
> 90 degree

### Procedure

	matrix = np.array([[np.cos(radius), -np.sin(radius)], 
							[np.sin(radius), np.cos(radius)]])
	vertex = np.array([[0, 0], [width, 0], [0, height], [width, height]])
	vertex_new = np.zeros([4,2])
	for i in range(vertex_new.shape[0]):
		vertex_new[i, :] = np.dot(matrix, vertex[i, :])

1.Creat the rotation matrix, and record the original vertex and new vertex

	min_x = vertex_new[:, 0].min()
	max_x = vertex_new[:, 0].max()
	min_y = vertex_new[:, 1].min()
	max_y = vertex_new[:, 1].max()
	
	x_shift = min_x - 0
	y_shift = min_y - 0
	
	width_new = int(np.ceil(max_x) - np.floor(min_x))
	height_new = int(np.ceil(max_y) - np.floor(min_y))
	
2.Find the minimun (x,y) and maximun (x,y). And then calculate how much we move the rotated image to positive axus. Measure the new width and height of rotated image.

	x_new_shift = x_new + x_shift
	y_new_shift = y_new + y_shift
	inverse_matrix = np.array([[np.cos(-radius), -np.sin(-radius)], 
									[np.sin(-radius), np.cos(-radius)]])
	original_location = np.zeros([1,2])
	original_location = np.dot(inverse_matrix, np.array([x_new_shift, 									 y_new_shift]))

3.Back-warping each pixel on the rotated image to the original image.

	area_1 = (original_location[0] - floor_x) * (original_location[1] - floor_y)
	area_2 = (ceil_x - original_location[0]) * (original_location[1] - floor_y)
	area_3 = (original_location[0] - floor_x) * (ceil_y - original_location[1])
	area_4 = (ceil_x - original_location[0]) * (ceil_y - original_location[1])

	I_rot[y_new, x_new, 0] = I[floor_y, floor_x, 0] * area_4 + 
								 I[ceil_y, ceil_x, 0] * area_1 + 
								 I[ceil_y, floor_x, 0] * area_2 + 
								 I[floor_y, ceil_x, 0] * area_3
								 
4.Use bilinear interpolation to find the corresponding RGB value from the original image. 

### Results

<div style="text-align: center">
<img src="/Users/winston/Desktop/DSP_Lab_HW0/image.jpg" width="300"/>

<img src="/Users/winston/Desktop/DSP_Lab_HW0/example.jpg" width="300"/>

original image

<img src="/Users/winston/Desktop/DSP_Lab_HW0/results/image/rotation45_image.jpg" width="300"/>

<img src="/Users/winston/Desktop/DSP_Lab_HW0/results/image/rotation45_example.jpg" width="300"/>

45 degree rotation image

<img src="/Users/winston/Desktop/DSP_Lab_HW0/results/image/rotation90_image.jpg" width="250"/>

<img src="/Users/winston/Desktop/DSP_Lab_HW0/results/image/rotation90_example.jpg" width="250"/>

90 degree rotation image

<div style="text-align: left">
## Discussion

In this lab, I realized the data types are important. The original image data type is uint8, whose range is from 0 to 255. I convert uint8 to float for simple calculation. And I knew the principle of rotation image from this lab.


