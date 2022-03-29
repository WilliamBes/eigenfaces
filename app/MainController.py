import os
import tkinter as tk
from tkinter.messagebox import showerror

import numpy as np
import scipy.io


from MenuView import MenuView
from eigenfaces.app.DisplayDatasetController import DisplayDatasetController
from eigenfaces.app.DisplayEigenfacesController import DisplayEigenfacesController
from eigenfaces.app.FaceReconstructionController import FaceReconstructionController


class MainController():
    """

    Classe correspondant au controller principal

    """

    def __init__(self):
        """Constructeur de la classe MainController"""

        self.window = tk.Tk()
        self.imported = False
        self.faces = None
        self.m = None
        self.n = None
        self.nfaces = None
        self.dataset = None
        self.eigenvectors = None
        self.mean_training_face = None
        self.singular_values = None
        self.train_purcentage = 0.9
        self.test_purcentage = 1 - self.train_purcentage
        self.nb_train_faces = None
        self.training_faces = None
        self.eigenvectors = None
        self.singular_values = None

        # liste des interfaces
        self.menu_view = MenuView(self.window)

        self.change_label("Non", None, None, None, None, self.train_purcentage)

        # configuration des boutons
        self.configure_action_buttons_menu_view()

        # afficher fenetre
        self.window.mainloop()

    def configure_action_buttons_menu_view(self):
        """fonction qui configure les actions des boutons de la page d'acceuil"""

        self.menu_view.butt_import.config(command=self.change_dataset)
        self.menu_view.butt_visualisation_dataset.config(command=self.display_dataset_images)
        self.menu_view.butt_visualisation_eigenfaces.config(command=self.display_eigenfaces)
        self.menu_view.butt_reco_image.config(command=self.display_reco_image)

    def change_dataset(self):
        """
        Fonction permettant de changer le dataset en cours d'utilisation
        :return:
        """
        try:
            self.dataset = scipy.io.loadmat(os.path.join('..','datas','allFaces.mat'))
        except:
            showerror(title='Erreur', message="Le fichier n'est pas du bon format")
            return

        # Changer et charger tous les attributs relatifs au dataset
        try:
            self.faces = self.dataset['faces']
            self.m = int(self.dataset['m'])
            self.n = int(self.dataset['n'])
            self.nfaces = np.ndarray.flatten(self.dataset['nfaces'])
            self.nb_train_faces = int(self.train_purcentage * len(self.nfaces))
            self.imported = True
            self.training_faces = self.faces[:, :np.sum(self.nfaces[:self.nb_train_faces])]
            self.mean_training_face = np.mean(self.training_faces, axis=1)
            self.compute_eigenvectors()  # time consumming

        except KeyError:
            showerror(title='Erreur', message="Le fichier .mat ne contient pas tous les champs requis:\n"
                                              "faces/m/n/nfaces")
            return

        self.change_label("Oui", len(self.nfaces), self.faces.shape[1], self.m, self.n, self.train_purcentage)

    def display_dataset_images(self):
        """
        Fonction qui affiche sur une frame quelques images du dataset
        :return:
        """

        if self.check_if_dataset_is_imported():
            display_dataset_controller = DisplayDatasetController(self)
            display_dataset_controller.plot_images()

    def display_eigenfaces(self):
        """
        Fonction qui affiche sur une frame les eigenfaces du dataset
        Returns:

        """

        if self.check_if_dataset_is_imported():
            display_eigenfaces_controller = DisplayEigenfacesController(self)
            display_eigenfaces_controller.plot_eigenfaces()

    def display_reco_image(self):
        """
        Fonction qui affiche sur une frame le reconstruction d'une image d'une personne
        Returns:

        """
        error = False
        cond = False
        number = self.menu_view.entry_reco_image.get()
        if self.check_if_dataset_is_imported():
            if self.menu_view.entry_reco_image.get() is None:
                showerror(title="Erreur", message="Veuillez renseigner le champ associé"
                                                  " au numéro de personne pour effectuer la reconstitution de l'image")
                return
            else:
                try:
                    int(number)
                except ValueError:
                    error = True
                if not error:
                    cond = int(number) < self.nb_train_faces+1 or int(number) > len(self.nfaces)
            if error or cond:
                print(error, cond)
                showerror(title="Erreur", message="Veuillez entrer un numéro entier compris entre {} et {}".format(
                                                self.nb_train_faces+1, len(self.nfaces)))
            else:
                face_reco_controller = FaceReconstructionController(self, number)
                face_reco_controller.plot_face_reconstruction()

    def check_if_dataset_is_imported(self):
        """Fonction qui affiche un message d'erreur si le dataset n'est pas importé

        Returns:
            bool if imported"""

        if not self.imported:
            showerror(title="Erreur", message="Problème avec le dataset ou bien dataset non importé")
            return False
        return True

    def compute_eigenvectors(self):
        """
        Fonction calculant les eigenvectors ainsi que le visage moyen du dataset.
        """

        # utilisation du svd pour la détermination des eigenvectors
        X = self.training_faces - np.tile(self.mean_training_face, (self.training_faces.shape[1], 1)).T
        U, S, VT = np.linalg.svd(X, full_matrices=False)

        self.eigenvectors = U
        self.singular_values = S


    def change_label(self, imported, nb_personnes, nb_images, x, y, train_purcentage):
        """Fonction mettant à jour les labels du menu
        """

        label_nb_images_var_str = "Nombre d'images : {}".format(nb_images)
        self.menu_view.label_nb_images_var.set(label_nb_images_var_str)
        label_definition_var_str = "Définition des images : {} x {}".format(x, y)
        self.menu_view.label_definition_var.set(label_definition_var_str)
        label_import_var_str = "Dataset importé : {}".format(imported)
        self.menu_view.label_import_var.set(label_import_var_str)
        label_nb_persones_var_str = "Nombre de personnes : {}".format(nb_personnes)
        self.menu_view.label_nb_persones_var.set(label_nb_persones_var_str)
        label_train_pourcentage_var_str = "Part dataset d'entraînement : {}%".format(int(train_purcentage*100))
        self.menu_view.label_train_pourcentage_var.set(label_train_pourcentage_var_str)

        # Reconstitution de l'image
        try:
            i_first_test_person = self.nb_train_faces+1
            i_last_test_person = len(self.nfaces)
        except TypeError:
            i_first_test_person = None
            i_last_test_person = None

        label_num_personne_reco_var_str = "Choisir un numéro de personne: (Compris entre {} et {})".format(
                                            i_first_test_person, i_last_test_person)
        self.menu_view.label_reco_image_var.set(label_num_personne_reco_var_str)




