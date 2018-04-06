import os
from numpy import *
from scipy.ndimage import filters


def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg') or f.endswith('.jpeg')]


def histeq(im, nbr_bins =256):
    imhist, bins = histogram(im.flatten(), nbr_bins, normed=True)
    cdf = imhist.cumsum()
    cdf = 255 * cdf / cdf[-1]
    im2 = interp(im.flatten(), bins[:-1], cdf)
    return im2.reshape(im.shape), cdf


def sobel_filter_ix(im):
    imx = zeros(im.shape)
    filters.sobel(im, 1, imx)
    return imx


def sobel_filter_iy(im):
    imy = zeros(im.shape)
    filters.sobel(im, 0, imy)
    return imy


def sobel_filter_magnitud(im):
    return sqrt(sobel_filter_ix(im)**2+sobel_filter_iy(im)**2)


def gaussian_filter_ix(im, sigma = 5):
    imx = zeros(im.shape)
    filters.gaussian_filter(im,(sigma, sigma), (0, 1), imx)
    return imx


def gaussian_filter_iy(im, sigma = 5):
    imy = zeros(im.shape)
    filters.gaussian_filter(im, (sigma, sigma), (1, 0), imy)
    return imy


def gaussian_filter_magnitud(im , sigma = 5):
    return sqrt(gaussian_filter_ix(im, sigma)**2,
                gaussian_filter_iy(im, sigma)**2)

