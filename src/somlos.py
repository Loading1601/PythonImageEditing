import matplotlib.pyplot as plt


import Funksjoner

def somlos(image1, image2):
    """

    :param image1:
    :param image2:

    xlengde: lengde i x retning
    ylengde: lengde i y retning
    x0:start av x
    y0:start av y
    xn:stop av x
    yn:stop av y

    omega: delen som skal settes inn


    :return:
    """
    xlengde = 100
    ylengde = 100
    x0 = 100
    y0 = 100
    xn = 100
    yn = 100
    alpha = 0.25

    image1 = image1.astype(float) / 255
    image2 = image2.astype(float) / 255
    omega = image2[xn:xn + xlengde, yn:yn + ylengde]

    image3 = omega.view()
    lap_image3 = Funksjoner.eksplisitt(image3)
    for i in range(100):
        lap_omega = Funksjoner.eksplisitt(omega)
        omega[1:-1, 1:-1] += alpha * (lap_omega - lap_image3)
        omega[:, 0] = image1[x0:x0 + xlengde, y0]
        omega[:, -1] = image1[x0:x0 + xlengde, y0 + ylengde]
        omega[0, :] = image1[x0, y0:y0 + ylengde]
        omega[-1, :] = image1[x0 + xlengde, y0:y0 + ylengde]
        omega[omega < 0] = 0
        omega[omega > 1] = 1

    image1[x0:x0 + xlengde, y0:y0 + ylengde] = omega
    plt.imshow(image1)
    plt.show()

