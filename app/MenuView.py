from tkinter import Frame, BOTH, YES, LEFT, RIGHT, TOP, BOTTOM, Button, LabelFrame, Label, Entry, StringVar, BooleanVar


class MenuView:
    """Classe MenuView: vue principale"""

    def __init__(self, window):
        """
        Constructeur de la classe MenuView
        :param window:
        """

        # titre fenetre
        window.title("Eigenfaces")

        # taille fenetre
        window.geometry("1080x720")
        # taille min
        window.minsize(480, 360)

        self.frame_menu = LabelFrame(window)
        self.frame_menu.pack()

        self.frame_gauche = LabelFrame(self.frame_menu)
        self.frame_gauche.pack(side=LEFT, padx=50)

        self.frame_droite = LabelFrame(self.frame_menu)
        self.frame_droite.pack(side=RIGHT)

        self.frame_droite_haut = LabelFrame(self.frame_droite)
        self.frame_droite_haut.pack(side=TOP)

        self.frame_droite_bas = LabelFrame(self.frame_droite)
        self.frame_droite_bas.pack(side=BOTTOM,  pady=150)

        # Boutons

        self.butt_import = Button(self.frame_gauche, text="Importer dataset (.mat)", font=("Arial", 14), bg='white',
                                  fg='black')
        self.butt_import.pack()

        self.label_definition_var = StringVar()
        self.label_definition = Label(self.frame_gauche, textvariable=self.label_definition_var)
        self.label_definition.pack(side=BOTTOM)

        self.label_nb_images_var = StringVar()
        self.label_nb_images = Label(self.frame_gauche, textvariable=self.label_nb_images_var)
        self.label_nb_images.pack(side=BOTTOM)

        self.label_nb_persones_var = StringVar()
        self.label_nb_persones = Label(self.frame_gauche, textvariable=self.label_nb_persones_var)
        self.label_nb_persones.pack(side=BOTTOM)

        self.label_train_pourcentage_var = StringVar()
        self.label_train_pourcentage = Label(self.frame_gauche, textvariable=self.label_train_pourcentage_var)
        self.label_train_pourcentage.pack(side=BOTTOM)

        self.label_import_var = StringVar()
        self.label_import = Label(self.frame_gauche, textvariable=self.label_import_var)
        self.label_import.pack(side=BOTTOM)


        self.butt_visualisation_dataset = Button(self.frame_droite_haut, text="Visualisation du dataset",
                                                    font=("Arial", 14), bg='white',
                                                    fg='black')
        self.butt_visualisation_dataset.pack(side=LEFT, padx=5)

        self.butt_visualisation_eigenfaces = Button(self.frame_droite_bas, text="Visualisation des eigenfaces", font=("Arial", 14), bg='white',
                                  fg='black')
        self.butt_visualisation_eigenfaces.pack(padx=5)

        self.frame_reco = Frame(self.frame_droite_bas)
        self.frame_reco.pack(side=BOTTOM)
        self.butt_reco_image = Button(self.frame_reco, text="Reconstitution d'une image", font=("Arial", 14), bg='white',
                                  fg='black')
        self.butt_reco_image.pack(side=LEFT, padx=5)

        self.label_reco_image_var = StringVar()
        self.label_reco_image = Label(self.frame_reco, textvariable=self.label_reco_image_var)
        self.label_reco_image.pack(side=LEFT)
        self.entry_reco_image = Entry(self.frame_reco)
        self.entry_reco_image.pack(side=RIGHT)

        self.butt_script_match = Button(self.frame_droite_bas, text="Script pour match", font=("Arial", 14), bg='white',
                                  fg='black')
        self.butt_script_match.pack(padx=5)
