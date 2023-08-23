import numpy as np
from matplotlib import pyplot as plt

import Funksjoner

def mosaicFunksjon(image):

        """

        :param image: numpy array av bilde
        :return:mossaic gray image
        """
        mosaic = np.zeros(image.shape[:2])
        mosaic[ ::2, ::2] = image[ ::2, ::2, 0]    #->R
        mosaic[1::2, ::2] = image[1::2, ::2, 1]     #->G
        mosaic[ ::2, 1::2] = image[ ::2, 1::2, 1]   #->G
        mosaic[1::2, 1::2] = image[1::2, 1::2, 2]   #->B
        return mosaic


def demosaicing(image):
    image = image.astype(float) / 255
    alpha = 0.25
    mosaicdemo = mosaicFunksjon(image)

    def inpainting(image, mask):
        for i in range(1):
            image[1:-1, 1:-1] += alpha * Funksjoner.eksplisitt(image)
            image[:, 0] = mosaicdemo[:, 0]
            image[:, -1] = mosaicdemo[:, -1]
            image[0, :] = mosaicdemo[0, :]
            image[-1, :] = mosaicdemo[-1, :]
            image[~mask] = mosaicdemo[~mask]

        return image

    def demosaicing():
        demo = np.zeros((mosaicdemo.shape[0], mosaicdemo.shape[1], 3))
        demo[::2, ::2, 0] = mosaicdemo[::2, ::2]  # --> R-kanal
        demo[1::2, ::2, 1] = mosaicdemo[1::2, ::2]  # --> G-kanal
        demo[::2, 1::2, 1] = mosaicdemo[::2, 1::2]  # --> G-kanal
        demo[1::2, 1::2, 2] = mosaicdemo[1::2, 1::2]  # --> B-kanal

        mask = np.ones(demo.shape)
        mask[::2, ::2, 0] = 0  #R-Kanal -> false
        mask[1::2, ::2, 1] = 0  #G-Kanal -> false
        mask[::2, 1::2, 1] = 0  #G-Kanal -> false
        mask[1::2, 1::2, 2] = 0  #B-Kanal -> false
        mask = mask.astype(bool)

        data = plt.imshow(demo)

        for i in range(50):
            inpainting(demo[:, :, 0], mask[:, :, 0])  #R-kanal inpainting
            inpainting(demo[:, :, 1], mask[:, :, 1])  #G-kanal inpainting
            inpainting(demo[:, :, 2], mask[:, :, 2])  #B-kanal inpainting
            data.set_array(demo)
            plt.draw()
            plt.pause(1)

        return demo

    demosaicing()  # kaller på inner funksjonen demo()