import math
import tkinter as tk
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from eigenfaces.app.DisplayEigenfacesView import DisplayEigenfacesView


class DisplayEigenfacesController():
    """
        Classe controller faisant référence à la page qui affiche des Eigenfaces du dataset

    """

    def __init__(self, maincontroller):
        """Constructeur de la classe DisplayDatasetController"""

        self.window = tk.Tk()
        self.maincontroller = maincontroller
        self.computed = False
        self.fig, self.axs = None, None

        self.view = DisplayEigenfacesView(self.window)

        self.configure_action_buttons()

    def configure_action_buttons(self):
        """fonction qui configure les actions des boutons de la page DisplayEigenfacesController"""
        pass

    def plot_eigenfaces(self):
        """Méthode affichant sur la page les eigenfaces du dataset
        """

        m = self.maincontroller.m
        n = self.maincontroller.n
        eigenvectors = self.maincontroller.eigenvectors
        singular_values = self.maincontroller.singular_values

        nb_subplot = eigenvectors.shape[1] if eigenvectors.shape[1] <= 16 else 16

        # On divise le graph en sous graph contenant nb_subplot
        self.fig, self.axs = plt.subplots(int(math.sqrt(nb_subplot)), int(math.sqrt(nb_subplot)))
        self.fig.set_dpi(200)
        canvas = FigureCanvasTkAgg(self.fig, self.view.frame)
        canvas.get_tk_widget().pack()

        # Affichage
        for i in range(0, nb_subplot):
            img_1 = self.axs[int(i/int(math.sqrt(nb_subplot))), i % int(math.sqrt(nb_subplot))]\
                         .imshow(np.reshape(eigenvectors[:, i], (m, n)).T)
            img_1.set_cmap('gray')
            self.axs[int(i / int(math.sqrt(nb_subplot))), i % int(math.sqrt(nb_subplot))]\
                .set_title("n°{} | Singular value:{}".format(i+1, round(singular_values[i], 1)), fontsize=5)
            self.axs[int(i/int(math.sqrt(nb_subplot))), i % int(math.sqrt(nb_subplot))]\
                .axis('off')

        nb_faces_str = "(Soit {} personnes sur {})".format(self.maincontroller.nb_train_faces, len(self.maincontroller.nfaces))
        plt.suptitle(nb_faces_str, fontsize=10)
        plt.show()

