import numpy as np
from matplotlib import pyplot as plt

import Funksjoner

def kontrast(image):
    """
    Funksjon: Endrer på kontrasten på bilde

    :param image: numpy array av bilde
    k: konstanten som bestemmer konstanten

    derivx: første derivert med hensyn på x
    derivx2: andre derivert med hensyn på x
    derivy: første derivert med hensyn på y
    derivy2: andre derivert med hensyn på y

    gradient:linjær funksjon
    gradient2:linjær funksjon

    :return:
    """
    alpha = 0.25
    k = 3
    image = Funksjoner.Grey(image)

    derivx = np.zeros(image.shape)
    derivx[1:-1, 1:-1] = image[2:, 1:-1] - image[1:-1, 1:-1]
    derivy = np.zeros(image.shape)
    derivy[1:-1, 1:-1] = image[1:-1, 2:] - image[1:-1, 1:-1]
    gradient = np.exp(derivx**2) + np.exp(derivy**2)

    derivx2 = np.zeros(derivx.shape)
    derivx2[1:-1, 1:-1] = derivx[2:, 1:-1] - derivx[1:-1, 1:-1]
    derivy2 = np.zeros(derivy.shape)
    derivy2[1:-1, 1:-1] = derivy[1:-1, 2:] - derivy[1:-1, 1:-1]
    gradient2 = derivx2 + derivy2

    BufferData = plt.imshow(image, plt.cm.gray)

    for i in range(50):
        image[1:-1, 1:-1] += alpha * Funksjoner.eksplisitt(image) - k * gradient2[1:-1, 1:-1] * gradient[1:-1, 1:-1]
        Funksjoner.neumann(image)
        image[image>1]=1
        image[image<0]=0
        BufferData.set_array(image)
        plt.draw()
        plt.pause(1e-2)
    plt.close()