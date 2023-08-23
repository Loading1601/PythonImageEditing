import numpy as np
from matplotlib import pyplot as plt, pyplot

import Funksjoner


def GreyInpainting(image, DmgImage):
    """
    Funksjon: Fyller opp skadet bilde

    :param image: numpy array bilde
    :param DmgImage: numpy array bilde


    x:kordinater
    y:kordinater
    omega: numpy array av område som skal inpaintes
    overlay: områade som er skadet satt til 1

    """
    x = 300
    y = 310
    alpha = 0.25

    OverLay = np.zeros(image.shape)
    OverLay[np.where(image == 1)] = 1
    OverLay = OverLay.astype(bool)
    Omega = DmgImage[x:y, x:y]

    MirrorImage = np.copy(DmgImage)
    for i in range(100):
        MirrorImage[1:-1, 1:-1] += alpha * Funksjoner.eksplisitt(MirrorImage)
        Omega[:, :0] = MirrorImage[x, :0]
        Omega[:, :-1] = MirrorImage[x:y, x:y - 1]
        Omega[0:, :] = MirrorImage[x:y, x:y]
        Omega[-1:, :0] = MirrorImage[-1, :0]
        MirrorImage[~OverLay] = DmgImage[~OverLay]

        plt.imshow(DmgImage).set_array(DmgImage)

        plt.draw()
        plt.pause(1e-4)


