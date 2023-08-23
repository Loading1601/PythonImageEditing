import numpy as np
import matplotlib.pyplot as plt

import Funksjoner

def FGlatting():
    """
    funksjon: Glatter bilde

    image: numpy array bilde
    mirrorimage: kopi av image variabel
    stages: hvor mange steg det glattes på
    lambda Hvor mye det glattes
    :return:
    """

    alpha = 0.1
    lamBda = 0.0001
    stages = 100
    image = Funksjoner.importImg()
    image = image.astype(float) / 255
    mirrorImage = np.copy(image)

    plt.imshow(image)
    plt.show(block=False)
    plt.close()

    BufferData = plt.imshow(image)
    for x in range(stages):
        plt.axis('off')
        image[1:-1, 1:-1] += alpha * Funksjoner.eksplisitt(image)
        Funksjoner.neumann(image)
        image = image - (lamBda * (image - mirrorImage))
        BufferData.set_array(image)
        plt.draw()
        plt.pause(1e-2)




