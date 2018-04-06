from PIL import Image
from imtools import get_imlist
from imtools import histeq
from imtools import sobel_filter_magnitud
from imtools import gaussian_filter_magnitud
from scipy.ndimage import measurements, morphology
from pylab import *
from implot import plot_images

data = get_imlist('photos')
im_il = Image.open( data[0])
# box = (50,50,100,100)
# region = im_il.crop(box)
# region = region.transpose(Image.ROTATE_180)
# region = region.rotate(180)
# im_il.paste(region,box)
# im_il.save("photos/output2.jpg")

im_plot = array(im_il.convert('L'))
gray()

# histogram
# axis('equal')
# axis('off')
# hist(im_plot.flatten(), 256)
# figure()
# img = histeq(im_plot)[0]
# imshow(img)


# filters
# f, ((ax1, ax2), (ax3, ax4)) = subplots(2,2)
# ax1.imshow(im_plot)
# ax1.set_title('Original image')
# ax1.axis('off')
# new_image = sobel_filter_magnitud(im_plot)
# ax2.imshow(new_image)
# ax2.set_title('Sobel magnitud filter')
# ax2.axis('off')
# new_image = gaussian_filter_magnitud(im_plot)
# ax3.imshow(new_image)
# ax3.set_title('Gaussian magnitud filter sigma 5')
# ax3.axis('off')
# new_image = gaussian_filter_magnitud(im_plot,1)
# ax4.imshow(new_image)
# ax4.set_title('Gaussian magnitud filter sigma 1')
# ax4.axis('off')
# show()


# counting objetcs
im_plot = 1*(im_plot < 128)
labels, nbr_objetcs = measurements.label(im_plot)
print("Number of objets with measurements:", nbr_objetcs)
im_open = morphology.binary_opening(im_plot, ones((2, 2)), iterations=2)
labels2, nbr_objetcs_open = measurements.label(im_open)
print("Number of objets with measurements on open :", nbr_objetcs_open)
plot_images([im_plot, labels, im_open, labels2], ['', '', '', ''])
