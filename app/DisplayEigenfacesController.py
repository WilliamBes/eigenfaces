import math
import random
import tkinter as tk

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from eigenfaces.app.DisplayDatasetView import DisplayDatasetView
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
        self.train_purcentage = 0.9
        self.test_purcentage = 1 - self.train_purcentage
        self.nb_train_faces = None

        if not self.computed:
            self.eigenvectors, self.singulars_values = self.compute_eigenvectors()
        else:
            self.eigenvectors = self.maincontroller.eigenvectors
            self.singulars_values = self.maincontroller.singular_values

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

        nb_subplot = self.eigenvectors.shape[1] if self.eigenvectors.shape[1] <= 16 else 16

        # On divise le graph en sous graph contenant nb_subplot
        self.fig, self.axs = plt.subplots(int(math.sqrt(nb_subplot)), int(math.sqrt(nb_subplot)))
        self.fig.set_dpi(200)
        canvas = FigureCanvasTkAgg(self.fig, self.view.frame)
        canvas.get_tk_widget().pack()

        # Affichage
        for i in range(0, nb_subplot):
            img_1 = self.axs[int(i/int(math.sqrt(nb_subplot))), i % int(math.sqrt(nb_subplot))]\
                         .imshow(np.reshape(self.eigenvectors[:, i], (m, n)).T)
            img_1.set_cmap('gray')
            self.axs[int(i / int(math.sqrt(nb_subplot))), i % int(math.sqrt(nb_subplot))]\
                .set_title("n°{} | Singular value:{}".format(i+1, round(self.singulars_values[i], 1)), fontsize=5)
            self.axs[int(i/int(math.sqrt(nb_subplot))), i % int(math.sqrt(nb_subplot))]\
                .axis('off')

        nb_faces_str = "(Soit {} personnes sur {})".format(self.nb_train_faces, len(self.maincontroller.nfaces))
        plt.suptitle(nb_faces_str, fontsize=10)
        plt.show()

    def compute_eigenvectors(self):
        """
        Fonction calculant les eigenvectors ainsi que le visage moyen du dataset.

        Returns:
            U: eigenvectors
        """

        self.nb_train_faces = int(self.train_purcentage * len(self.maincontroller.nfaces))
        training_faces = self.maincontroller.faces[:, :np.sum(self.maincontroller.nfaces[:self.nb_train_faces])]
        mean_training_face = np.mean(training_faces, axis=1)  # size n*m by 1

        self.maincontroller.mean_training_face = mean_training_face

        # utilisation du svd pour la détermination des eigenvectors
        X = training_faces - np.tile(mean_training_face, (training_faces.shape[1], 1)).T
        U, S, VT = np.linalg.svd(X, full_matrices=False)

        self.maincontroller.eigenvectors = U
        self.maincontroller.singular_values = S

        return U, S
