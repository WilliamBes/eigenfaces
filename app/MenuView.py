from tkinter import Frame, BOTH, YES, LEFT, RIGHT, TOP, BOTTOM, Button, LabelFrame, Label, Entry


class MenuView:


    def __init__(self, window):
        """

        :param window:
        """

        # titre fenetre
        window.title("Eigenfaces")

        # taille fenetre
        window.geometry("1080x720")
        # taille min
        window.minsize(480, 360)

        self.frame_menu = LabelFrame(window, text="Window")
        self.frame_menu.pack()

        self.frame_gauche = LabelFrame(self.frame_menu, text="frame_gauche")
        self.frame_gauche.pack(side=LEFT, padx=50)

        self.frame_droite = LabelFrame(self.frame_menu, text="frame_droite")
        self.frame_droite.pack(side=RIGHT)

        self.frame_droite_haut = LabelFrame(self.frame_droite, text="frame_droite_haut")
        self.frame_droite_haut.pack(side=TOP)

        self.frame_droite_bas = LabelFrame(self.frame_droite, text="frame_droite_bas")
        self.frame_droite_bas.pack(side=BOTTOM,  pady=150)

        # Boutons

        self.butt_import = Button(self.frame_gauche, text="Importer datasert (.mat)", font=("Arial", 14), bg='white',
                                  fg='black')
        self.butt_import.pack()

        self.butt_import = Button(self.frame_droite_haut, text="Importer datasert (.mat)", font=("Arial", 14), bg='white',
                                  fg='black')
        self.butt_import.pack()

        self.butt_visualisation_eigenfaces = Button(self.frame_droite_bas, text="Visualisation des eigenfaces", font=("Arial", 14), bg='white',
                                  fg='black')
        self.butt_visualisation_eigenfaces.pack(side=LEFT, padx=5)

        self.butt_reco_image = Button(self.frame_droite_bas, text="Reconstitution d'une image", font=("Arial", 14), bg='white',
                                  fg='black')
        self.butt_reco_image.pack(side=LEFT, padx=5)

        self.butt_script_match = Button(self.frame_droite_bas, text="Script pour match", font=("Arial", 14), bg='white',
                                  fg='black')
        self.butt_script_match.pack(side=RIGHT, padx=5)
