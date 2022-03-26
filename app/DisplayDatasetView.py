from tkinter import Frame, BOTH, YES, LEFT, RIGHT, TOP, BOTTOM, Button, LabelFrame, Label, Entry


class DisplayDatasetView:


    def __init__(self, window):
        """

        :param window:
        """

        # titre fenetre
        window.title("Visualisation du dataset")

        # taille fenetre
        window.geometry("1080x720")
        # taille min
        window.minsize(480, 360)

        self.frame = LabelFrame(window)
        self.frame.pack()

        self.label = Label(self.frame, text="Quelques images aléatoires du dataset", font=("Arial", 15))
        self.label.pack()

