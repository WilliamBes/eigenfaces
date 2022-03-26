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
        self.view = DisplayEigenfacesView(self.window)
        self.train_purcentage = 0.9
        self.test_purcentage = 1 - self.train_purcentage
        self.nb_train_faces = None

        self.configure_action_buttons()

    def configure_action_buttons(self):
        """fonction qui configure les actions des boutons de la page DisplayEigenfacesController"""
        pass

    def plot_eigenfaces(self, computed=False):
        """Méthode affichant sur la page les eigenfaces du dataset
        """

        if not computed:
            eigenvectors = self.compute_eigenvectors()
        else:
            eigenvectors = self.maincontroller.eigenvectors

        m = self.maincontroller.m
        n = self.maincontroller.n

        nb_subplot = len(eigenvectors) if len(eigenvectors) <= 16 else 16
        self.fig, self.axs = plt.subplots(nb_subplot)
        self.fig.set_dpi(200)
        canvas = FigureCanvasTkAgg(self.fig, self.view.frame)
        canvas.get_tk_widget().pack()

        for i in range(0, nb_subplot):
            img_1 = self.axs[i].imshow(np.reshape(eigenvectors[:, i], (m, n)).T)
            img_1.set_cmap('gray')
            self.axs[i].axis('off')

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

        return U
