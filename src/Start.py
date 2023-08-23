from tkinter import *
import cv2
#import av program funksjoner:
import numpy as np
from matplotlib import pyplot as plt

from tkinter import filedialog

#import av lokale funksjoner
import FargetGlatting
import GraaGlatting

import FargetInpainting
import GraaInpainting

import Graakontrast
import FargetKontrast

import somlos

import Demosaicing

import Anonimiser

import Funksjoner

def DamageImage(image, x):
    image = image.astype(float) / (255 * x)
    image[300:310, 300:310] = 1
    return(image)


def FargetImageInpainting():
    image = Funksjoner.importImg()
    Damaged = DamageImage(image, 1)
    FargetInpainting.inpainting(image, Damaged)
    plt.imshow(Damaged)
    plt.pause(3)
    plt.close()

def GraaImageInpainting():
    image = Funksjoner.importImg()
    Damaged = DamageImage(image, 3)
    GraaInpainting.GreyInpainting(image, Damaged)
    plt.imshow(Damaged)
    plt.pause(3)
    plt.close()

def graaKontrast():
    image = Funksjoner.importImg()
    Graakontrast.kontrast(image)


def demosaicing():
    image = Funksjoner.importImg()
    Demosaicing.demosaicing(image)

def fargetKontrast():
    image = Funksjoner.importImg()
    FargetKontrast.ContrastColor(image)

def somlosRedirect():
    image1 = Funksjoner.importImg()
    image2 = Funksjoner.importImg()
    somlos.somlos(image1, image2)

def anonymiser():
    image = filedialog.askopenfilename()
    imageCV2 = cv2.imread(image)
    Anonimiser.anonymiser(imageCV2)




def makeButton(window, message, commando, row, columnr, x, y):
    add_Button=Button(window, width=20, text=message, command=commando)
    add_Button.grid(row=row, column=columnr, padx=x, pady=y, sticky=W)



def start():
    root = Tk()
    root.title('Image Editing')

    makeButton(root, "FargeBilde Glatting", FargetGlatting.FGlatting, 0, 0, 5, 5)
    makeButton(root, "Grå Glatting", GraaGlatting.GGlatting, 0, 1, 5, 5)
    makeButton(root, "Farget Impainting", FargetImageInpainting,   1, 0, 5, 5)
    makeButton(root, "Grå Impainting", GraaImageInpainting, 1, 1, 5, 5)
    makeButton(root, "Farget Kontrast", fargetKontrast, 2, 0, 5, 5)
    makeButton(root, "Grå Kontrast", graaKontrast, 2, 1, 5, 5)
    makeButton(root, "Somlos",somlosRedirect, 3, 0, 5, 5)
    makeButton(root, "Demosaicing", demosaicing, 3, 1, 5, 5)
    makeButton(root, "Anonymiser", anonymiser, 4, 0, 5, 5)


    root.mainloop()



start()
