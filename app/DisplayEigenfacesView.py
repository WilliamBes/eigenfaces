from tkinter import Frame, BOTH, YES, LEFT, RIGHT, TOP, BOTTOM, Button, LabelFrame, Label, Entry, StringVar

class DisplayEigenfacesView:
    """Classe DisplayEigenfacesView"""


    def __init__(self, window):
        """
        Constructeur de la classe DisplayEigenfacesView
        :param window:
        """

        # titre fenetre
        window.title("Visualisation des eigenfaces")

        # taille fenetre
        window.geometry("1080x720")
        # taille min
        window.minsize(480, 360)

        self.frame = LabelFrame(window)
        self.frame.pack()

        self.label = Label(self.frame, text="Pourcentage d'images utilisées pour générer les eigenfaces: 90%", font=("Arial", 15))
        self.label.pack()
