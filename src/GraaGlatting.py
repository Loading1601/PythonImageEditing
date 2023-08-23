import matplotlib.pyplot as plt

import Funksjoner

def GGlatting():
    """
    funksjon: Glatter bilde
    image: numpy array
    mirrorimage: kopi av image variabel
    stages: hvor mange steg det glattes på
    lambda Hvor mye det glattes
    :return:
    """
    image = Funksjoner.Grey(Funksjoner.importImg()) #Henter bilde som er klar til å bli grå
    mirrorImage = image
    alpha = 0.25
    lamBda = 0.001
    stages = 25

    for x in range(stages):
        plt.axis('off')
        image[1:-1, 1:-1] += alpha * Funksjoner.eksplisitt(image)
        Funksjoner.neumann(image)
        image = image - (lamBda * (image - mirrorImage))
        plt.imshow(image, plt.cm.gray).set_array(image) #gjør bilde grått
        plt.draw()
        plt.pause(2)