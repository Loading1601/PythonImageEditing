import imageio
from tkinter import filedialog

import numpy as np
from matplotlib import pyplot as plt



def Grey(image):
    return(np.sum(image.astype(float), 2) / 765)

def importImg():
    image_path = filedialog.askopenfilename()
    image = imageio.imread(image_path)
    return image

def neumann(image):
    image[:, 0] = image[:, 1]
    image[:, -1] = image[:, -2]
    image[0, :] = image[1, :]
    image[-1, :] = image[-2, :]
    return image

def eksplisitt(image):
    return (image[:-2, 1:-1] + image[2:, 1:-1] + image[1:-1, :-2] + image[1:-1, 2:] - 4 * image[1:-1, 1:-1])



