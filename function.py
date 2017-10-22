import numpy as np

def grey_scale(I):

	#get height, width, channel of image
	[height, width, channel] = np.shape(I)

	# initial intensity array Y using zeros()
	Y = np.zeros([height, width])

	# weight of rgb channel
	matrix = np.array([0.299, 0.587, 0.114])

	Y = np.sum(I * matrix, axis = 2)

	# save intensity Y to output image
	I_grey = np.zeros([height, width, channel])
	I_grey[:,:,0] = Y
	I_grey[:,:,1] = Y
	I_grey[:,:,2] = Y
	
	return I_grey

def flip(I, type):

	#get height, width, channel of image
	[height, width, channel] = np.shape(I)

	R_flip = np.zeros([height, width])
	G_flip = np.zeros([height, width])
	B_flip = np.zeros([height, width])
	I_flip = np.zeros([height, width, channel])

	if (type == 0):
		for i in range(I.shape[0]):
			I_flip[i, :, 0] = I[i, ::-1, 0]
			I_flip[i, :, 1] = I[i, ::-1, 1]
			I_flip[i, :, 2] = I[i, ::-1, 2]

	elif (type == 1):
		for i in range(I.shape[1]):
			I_flip[:, i, 0] = I[::-1, i, 0]
			I_flip[:, i, 1] = I[::-1, i, 1]
			I_flip[:, i, 2] = I[::-1, i, 2]

	elif (type == 2):
		for i in range(I.shape[0]):
			I_flip[i, :, 0] = I[i, ::-1, 0]
			I_flip[i, :, 1] = I[i, ::-1, 1]
			I_flip[i, :, 2] = I[i, ::-1, 2]
		for i in range(I.shape[1]):
			I_flip[:, i, 0] = I_flip[::-1, i, 0]
			I_flip[:, i, 1] = I_flip[::-1, i, 1]
			I_flip[:, i, 2] = I_flip[::-1, i, 2]		

	return I_flip

def rotation(I, radius):

	#get height, width, channel of image
	[height, width, channel] = np.shape(I)

	## create new image
	# step1. record image vertex, and use rotation matrix to get new vertex.
	matrix = np.array([[np.cos(radius), -np.sin(radius)], [np.sin(radius), np.cos(radius)]])
	vertex = np.array([[0, 0], [width, 0], [0, height], [width, height]])
	vertex_new = np.zeros([4,2])
	for i in range(vertex_new.shape[0]):
		vertex_new[i, :] = np.dot(matrix, vertex[i, :])
	
	# step2. find min x, min y, max x, max y, use "min()" & "max()" function is ok
	min_x = vertex_new[:, 0].min()
	max_x = vertex_new[:, 0].max()
	min_y = vertex_new[:, 1].min()
	max_y = vertex_new[:, 1].max()

	# step3. consider how much to shift the image to the positive axis
	x_shift = min_x - 0
	y_shift = min_y - 0

	# step4. calculate new width and height, if they are not integer, use
	# "ceil()" & "floor()" to help get the largest width and height.
	width_new = int(np.ceil(max_x) - np.floor(min_x))
	height_new = int(np.ceil(max_y) - np.floor(min_y))

	# step5. initial r,g,b array for the new image
	I_rot = np.ones([height_new,  width_new, channel])
	
	## back-warping using bilinear interpolation
	# for each pixel on the rotation image, find the correspond r,g,b value 
	# from the source image, and save to R_rot, G_rot, B_rot.
	for y_new in range(height_new):
		for x_new in range(width_new):

			# step5. shift the new pixel (x_new, y_new) back, and rotate -radius
			# degree to get (x_old, y_old)
			x_new_shift = x_new + x_shift
			y_new_shift = y_new + y_shift
			inverse_matrix = np.array([[np.cos(-radius), -np.sin(-radius)], [np.sin(-radius), np.cos(-radius)]])
			original_location = np.zeros([1,2])
			original_location = np.dot(inverse_matrix, np.array([x_new_shift, y_new_shift]))
			
			# step6. using "ceil()" & "floor()" to get interpolation coordinates
			# x1, x2, y1, y2
			ceil_x = int(np.ceil(original_location[0]))
			floor_x = int(np.floor(original_location[0]))
			ceil_y = int(np.ceil(original_location[1]))
			floor_y = int(np.floor(original_location[1]))
			
       		# step7. if (x_old, y_old) is inside of the source image, 
        	# calculate r,g,b by interpolation.
        	# else if (x_old, y_old) is outside of the source image, set
        	# r,g,b = 0(black).
			if (original_location[0].is_integer() == True):
				ceil_x = ceil_x + 1
			if (original_location[1].is_integer() == True):
				ceil_y = ceil_y + 1

			if ((ceil_x >= 0) and (ceil_x <= width - 1) and (floor_x >= 0) and (floor_x <= width - 1) and (ceil_y >= 0) and (ceil_y <= height - 1) and (floor_y >= 0) and (floor_y <= height - 1)):
        		
				area_1 = (original_location[0] - floor_x) * (original_location[1] - floor_y)
				area_2 = (ceil_x - original_location[0]) * (original_location[1] - floor_y)
				area_3 = (original_location[0] - floor_x) * (ceil_y - original_location[1])
				area_4 = (ceil_x - original_location[0]) * (ceil_y - original_location[1])

				I_rot[y_new, x_new, 0] = I[floor_y, floor_x, 0] * area_4 + I[ceil_y, ceil_x, 0] * area_1 + I[ceil_y, floor_x, 0] * area_2 + I[floor_y, ceil_x, 0] * area_3
				I_rot[y_new, x_new, 1] = I[floor_y, floor_x, 1] * area_4 + I[ceil_y, ceil_x, 1] * area_1 + I[ceil_y, floor_x, 1] * area_2 + I[floor_y, ceil_x, 1] * area_3
				I_rot[y_new, x_new, 2] = I[floor_y, floor_x, 2] * area_4 + I[ceil_y, ceil_x, 2] * area_1 + I[ceil_y, floor_x, 2] * area_2 + I[floor_y, ceil_x, 2] * area_3
				
			else:

				I_rot[y_new, x_new, 0] = 0
				I_rot[y_new, x_new, 1] = 0
				I_rot[y_new, x_new, 2] = 0
	
	return I_rot


