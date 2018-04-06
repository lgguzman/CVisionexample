from pylab import *


def plot_images(ims, titles, axis = 'off'):
    n = len(ims)
    for i, v in enumerate(range(n)):
        v +=1
        ax1 = subplot(n,1,v)
        ax1.axis(axis)
        ax1.imshow(ims[v-1])
        ax1.set_title(titles[v-1])
    show()