import cv2
import Funksjoner

def anonymiser(image):
    """
    :param image(array): Bilde array
    :variables:
    alpha (float): mengde glatting
    top (float): øverste venstre hjørne
    down (float): nederste venstre hjørne
    height høyde av firkanten på ansiktet
    omega (array) der fjeset skal bli glattet
    :return:
    """
    alpha = 0.2
    recolor = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = image.astype(float) / 255
    cv2.imshow('Original', image)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

    face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml').detectMultiScale(recolor, 1.3, 6)

    for (top, down, height, width) in face:
        image = cv2.rectangle(image, (top, down), (top + width, down + height), (0, 0, 0), 0)
        omega = image[down:down + height, top:top + width]

    buffer = image.view()

    for x in range(100):
        omega[1:-1, 1:-1] += alpha * Funksjoner.eksplisitt(omega)
        omega[:, 0] = buffer[top:(top + width), down]
        omega[:, -1] = buffer[top:(top + width), down + height]
        omega[0, :] = buffer[top, down:(down + height)]
        omega[-1, :] = buffer[(top + width), down:(down + height)]

    cv2.imshow('Anon', image) #viser bilde
    cv2.waitKey(10000)
    cv2.destroyAllWindows()