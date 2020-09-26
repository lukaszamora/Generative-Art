import os
import numpy as np
from PIL import Image

def create_complex_plane(X, Y, x0, x1, y0, y1, endpoint=False):
    I = np.indices((Y,X)).astype(np.float64)
    fy = (y1 - y0) / (Y - 1) if endpoint else (y1 - y0) / Y
    fx = (x1 - x0) / (X - 1) if endpoint else (x1 - x0) / X
    return (x0 + fx*I[1]) + 1j*(y0 + fy*I[0])

def colorize(R, bins, rgb0, rgb1 = None):
    D = np.digitize(R, bins) - 1
    C0 = np.take(rgb0, D, axis=0)
    if rgb1 is None:
        return C0
    # create gradients between rgb0 and rgb1
    bin_widths = bins[1:] - bins[:-1]
    C1 = np.take(rgb1, D, axis=0)
    F = (R - np.take(bins, D))/np.take(bin_widths, D)
    F = np.repeat(F, 3)
    F.shape = C0.shape
    C = (1-F)*C0 + F*C1
    return C

def normalize(x, floor = -1e+300, ceil = +1e+300, nan_replace = 0.0):
    x = np.where(np.isnan(x), nan_replace, x)
    x = np.maximum(x, floor)
    x = np.minimum(x, ceil)
    xmin, xmax = np.min(x), np.max(x)
    return (x - xmin) / (xmax - xmin)

def save_rgb(R, path):
    R = np.round(R).astype(np.uint8)
    image = Image.fromarray(R, mode='RGB')
    image.save(path)


#-------------------------------------------------------------------
color_stops = np.array([-0.0000001, 0.059782608695652176, 0.07065217391304349, 0.1141304347826087, 0.125, 0.17391304347826086, 0.18478260869565216, 0.25, 0.2608695652173913, 0.30978260869565216, 0.32065217391304346, 0.3804347826086956, 0.3913043478260869, 0.4347826086956521, 0.4456521739130434, 0.49456521739130427, 0.5054347826086956, 0.5489130434782608, 0.5597826086956521, 0.6249999999999999, 0.6358695652173912, 0.6684782608695652, 0.6793478260869565, 0.7228260869565217, 0.7336956521739131, 0.7989130434782609, 0.8097826086956522, 0.8586956521739131, 0.8695652173913044, 0.923913043478261, 0.9347826086956523, 0.9891304347826089, 1.0000001])
rgb = [(239, 6, 109), (0, 0, 0), (157, 67, 137), (0, 0, 0), (31, 163, 223), (0, 0, 0), (163, 147, 242), (0, 0, 0), (239, 6, 109), (0, 0, 0), (157, 67, 137), (0, 0, 0), (31, 163, 223), (0, 0, 0), (163, 147, 242), (0, 0, 0), (239, 6, 109), (0, 0, 0), (157, 67, 137), (0, 0, 0), (31, 163, 223), (0, 0, 0), (163, 147, 242), (0, 0, 0), (239, 6, 109), (0, 0, 0), (157, 67, 137), (0, 0, 0), (31, 163, 223), (0, 0, 0), (163, 147, 242), (0, 0, 0)]
#-------------------------------------------------------------------
W, H = 800, 800
s = 33.68
r0 = create_complex_plane(W, H, s, -s, s, -s, endpoint=False)
r1 = (-12.38-15.73j) * (np.cos(np.real(r0)) + (1j * np.sin(np.imag(r0))))
r2 = ((-3.35+2.57j) + np.exp(np.real(r0)))
r2c = np.log(r0 + r1/r2)
r3 = np.square(np.real(r2c)) + np.square(np.imag(r2c))
r4 = normalize(r3)
r5 = colorize(r4, color_stops, rgb)
#-------------------------------------------------------------------
save_rgb(r5, 'snippet2.jpg')
