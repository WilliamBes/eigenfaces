import random
import tkinter as tk

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from eigenfaces.app.DisplayDatasetView import DisplayDatasetView


class DisplayDatasetController():
    """
        Classe controller faisant référence à la page qui affiche des images du dataset

    """

    def __init__(self, maincontroller):
        """Constructeur de la classe DisplayDatasetController"""
        self.window = tk.Tk()
        self.maincontroller = maincontroller
        self.view = DisplayDatasetView(self.window)
        self.fig, self.axs = plt.subplots(3, 3)

        self.configure_action_buttons()

    def configure_action_buttons(self):
        """fonction qui configure les actions des boutons de la page DisplayDatasetController"""
        pass

    def plot_images(self):
        """Méthode affichant sur la page différente images aléatoirement tirées dans le dataset

        Parameters:
            faces: faces du dataset
            m: taille x des images
            n: taille y des images
        """

        faces = self.maincontroller.faces
        m = self.maincontroller.m
        n = self.maincontroller.n
        random_numbers = random.sample(range(0, faces.shape[1]), 9)


        self.fig.set_dpi(200)
        canvas = FigureCanvasTkAgg(self.fig, self.view.frame)
        canvas.get_tk_widget().pack()

        img_1 = self.axs[0,0].imshow(np.reshape(faces[:, random_numbers[0]], (m, n)).T)
        img_1.set_cmap('gray')
        self.axs[0,0].axis('off')

        img_2 = self.axs[1,0].imshow(np.reshape(faces[:, random_numbers[1]], (m, n)).T)
        img_2.set_cmap('gray')
        self.axs[1,0].axis('off')

        img_4 = self.axs[1, 1].imshow(np.reshape(faces[:, random_numbers[2]], (m, n)).T)
        img_4.set_cmap('gray')
        self.axs[1, 1].axis('off')

        img_3 = self.axs[0, 1].imshow(np.reshape(faces[:, random_numbers[3]], (m, n)).T)
        img_3.set_cmap('gray')
        self.axs[0, 1].axis('off')

        img_5 = self.axs[2, 0].imshow(np.reshape(faces[:, random_numbers[4]], (m, n)).T)
        img_5.set_cmap('gray')
        self.axs[2, 0].axis('off')

        img_6 = self.axs[2, 1].imshow(np.reshape(faces[:, random_numbers[5]], (m, n)).T)
        img_6.set_cmap('gray')
        self.axs[2, 1].axis('off')

        img_7 = self.axs[2, 2].imshow(np.reshape(faces[:, random_numbers[6]], (m, n)).T)
        img_7.set_cmap('gray')
        self.axs[2, 2].axis('off')

        img_8 = self.axs[0, 2].imshow(np.reshape(faces[:, random_numbers[7]], (m, n)).T)
        img_8.set_cmap('gray')
        self.axs[0, 2].axis('off')

        img_9 = self.axs[1, 2].imshow(np.reshape(faces[:, random_numbers[8]], (m, n)).T)
        img_9.set_cmap('gray')
        self.axs[1, 2].axis('off')

        plt.show()
