import os
import tkinter as tk
from tkinter.messagebox import showerror

import numpy as np
import scipy.io


from MenuView import MenuView
from eigenfaces.app.DisplayDatasetController import DisplayDatasetController
from eigenfaces.app.DisplayEigenfacesController import DisplayEigenfacesController


class MainController():
    """

    Classe correspondant au controller principal

    """

    def __init__(self):
        self.faces = None
        self.m = None
        self.n = None
        self.nfaces = None
        self.window = tk.Tk()
        self.dataset = None
        self.eigenvectors = None
        self.mean_training_face = None


        # liste des interfaces
        self.menu_view = MenuView(self.window)

        # configuration des boutons
        self.configure_action_buttons_menu_view()

        # afficher fenetre
        self.window.mainloop()

    def configure_action_buttons_menu_view(self):
        """fonction qui configure les actions des boutons de la page d'acceuil"""

        self.menu_view.butt_import.config(command=self.change_dataset)
        self.menu_view.butt_visualisation_dataset.config(command=self.display_dataset_images)
        self.menu_view.butt_visualisation_eigenfaces.config(command=self.display_eigenfaces)

    def change_dataset(self):
        """
        Fonction permettant de changer le dataset en cours d'utilisation
        :return:
        """
        try:
            self.dataset = scipy.io.loadmat(os.path.join('..','datas','allFaces.mat'))
        except:
            showerror(title='Erreur', message="Le fichier n'est pas du bon format")

        # Changer tous les attributs relatifs au dataset
        try:
            self.faces = self.dataset['faces']
            self.m = int(self.dataset['m'])
            self.n = int(self.dataset['n'])
            self.nfaces = np.ndarray.flatten(self.dataset['nfaces'])
        except KeyError:
            showerror(title='Erreur', message="Le fichier .mat ne contient pas tous les champs requis:\n"
                                              "faces/m/n/nfaces")

    def display_dataset_images(self):
        """
        Fonction qui affiche sur une frame quelques images du dataset
        :return:
        """

        if self.faces is None or self.m is None or self.n is None:
            showerror(title="Erreur", message="Problème avec le dataset ou bien dataset non importé")
        else:
            display_dataset_controller = DisplayDatasetController(self)
            display_dataset_controller.plot_images()

    def display_eigenfaces(self):
        """
        Fonction qui affiche sur une frame les eigenfaces du dataset
        Returns:

        """

        if self.faces is None or self.m is None or self.n is None:
            showerror(title="Erreur", message="Problème avec le dataset ou bien dataset non importé")
        else:
            display_eigenfaces_controller = DisplayEigenfacesController(self)
            display_eigenfaces_controller.plot_eigenfaces()


