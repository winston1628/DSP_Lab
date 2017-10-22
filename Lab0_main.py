import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import function
import scipy.misc


## read image
filename = 'example.jpg'
I = mpimg.imread("/Users/winston/Desktop/DSP_Lab_HW0-master/" + filename)
I = (I - I.min()) / (I.max() - I.min()) # normalized to 0~1
plt.figure(1)
plt.imshow(I)
plt.show(block = False)

## ----- pre-lab ----- ##
# output = function(input1, input2, ...)
# grey_scale function
I2 = function.grey_scale(I)

plt.figure(2)
plt.imshow(I2)
plt.show(block = False)
##  ----- homework lab ----- ##
# flip function
I3 = function.flip(I, 0)
I4 = function.flip(I, 1)
I5 = function.flip(I, 2)

plt.figure(3)
plt.imshow(I3)
plt.show(block = False)
plt.figure(4)
plt.imshow(I4)
plt.show(block = False)
plt.figure(5)
plt.imshow(I5)
plt.show(block = False)
# rotation function
radius = np.pi/2
I6 = function.rotation(I, radius)
I7 = function.rotation(I, radius/2)

plt.figure(6)
plt.imshow(I6)
plt.show(block = False)
plt.figure(7)
plt.imshow(I7)
plt.show()

## write image
# save image for your report
filename2 = 'grey_example.jpg'
filename3 = 'H_flip_example.jpg'
filename4 = 'V_flip_example.jpg'
filename5 = 'H&V_flip_example.jpg'
filename6 = 'rotation90_example.jpg'
filename7 = 'rotation45_example.jpg'

scipy.misc.imsave(filename2, I2)
scipy.misc.imsave(filename3, I3)
scipy.misc.imsave(filename4, I4)
scipy.misc.imsave(filename5, I5)
scipy.misc.imsave(filename6, I6)
scipy.misc.imsave(filename7, I7)





