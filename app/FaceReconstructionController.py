import math
import tkinter as tk

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from eigenfaces.app.FaceReconstructionView import FaceReconstructionView


class FaceReconstructionController:
    """
        Classe controller faisant référence à la page qui affiche la reconstrucion d'une image
    """

    def __init__(self, maincontroller, num_person):
        """Constructeur de la classe FaceReconstructionController

        Params:
        maincontroller: classe MainController
        num_person: numéro de la personne pour la reconstitution
        """

        self.window = tk.Tk()
        self.maincontroller = maincontroller
        self.view = FaceReconstructionView(self.window)
        self.fig, self.axs = None, None
        self.num_person = int(num_person)
        self.r_list = [1, 5, 10, 25, 50, 100, 200, 400, 800]
        self.configure_action_buttons()

    def configure_action_buttons(self):
        """fonction qui configure les actions des boutons de la page FaceReconstructionController"""
        pass

    def plot_face_reconstruction(self):
        """Méthode affichant sur la page la reconstruction étape par étape d'une image via les eigenvectors
        """

        # Récupération de l'image original
        face = self.maincontroller.faces[:, np.sum(self.maincontroller.nfaces[:self.num_person-1])]

        # Récupération des données du dataset en vue de leur utilisation
        eigenvectors = self.maincontroller.eigenvectors
        mean_training_face = self.maincontroller.mean_training_face
        face_diff = face - mean_training_face
        n, m = self.maincontroller.n, self.maincontroller.m

        # On divise le graph en sous graph contenant len(self.r_list))+1 images et on le pack à la frame
        r_sqrt_len = int(math.sqrt(len(self.r_list)))
        self.fig, self.axs = plt.subplots(r_sqrt_len, r_sqrt_len)
        self.fig.set_dpi(200)
        canvas = FigureCanvasTkAgg(self.fig, self.view.frame)
        canvas.get_tk_widget().pack()

        # Première image = image d'origine
        img_ori = self.axs[0, 0].imshow(np.reshape(face, (m, n)).T)
        img_ori.set_cmap('gray')
        self.axs[0, 0].set_title("Image d'origine", fontsize=5)
        self.axs[0, 0].axis('off')

        # Affichage de la reconstruction progressive de l'image original
        for i in range(1, len(self.r_list)):
            # Calcul de l'image indice r
            r_value = self.r_list[i]
            face_r = mean_training_face + eigenvectors[:, :r_value] @ eigenvectors[:, :r_value].T @ face_diff

            img_r = self.axs[int(i/r_sqrt_len), i % r_sqrt_len].imshow(np.reshape(face_r, (m, n)).T)
            img_r.set_cmap('gray')
            self.axs[int(i/r_sqrt_len), i % r_sqrt_len].set_title("r = {}".format(r_value), fontsize=5)
            self.axs[int(i/r_sqrt_len), i % r_sqrt_len].axis('off')
