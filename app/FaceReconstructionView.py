from tkinter import Frame, BOTH, YES, LEFT, RIGHT, TOP, BOTTOM, Button, LabelFrame, Label, Entry, StringVar


class FaceReconstructionView:
    """
    Classe FaceReconstructionView
    """

    def __init__(self, window):
        """
        Constructeur de la classe FaceReconstructionView

        :param window: tk window
        """

        # titre fenetre
        window.title("Reconstitution d'une image via les eigenvectors")

        # taille fenetre
        window.geometry("1080x720")
        # taille min
        window.minsize(480, 360)

        self.frame = LabelFrame(window)
        self.frame.pack()

        self.label_str = StringVar()
        self.label = Label(self.frame, textvariable=self.label_str, font=("Arial", 15))
        self.label.pack()

