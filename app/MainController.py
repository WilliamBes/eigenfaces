import tkinter as tk

from app.MenuView import MenuView


class MainController():
    """

    Classe correspondant au controller principal

    """

    def __init__(self):
        self.window = tk.Tk()
        self.dataset = None


        # liste des interfaces
        self.menu_view = MenuView(self.window)

        # configuration des boutons
        self.configure_action_buttons_menu_view()

        # afficher fenetre
        self.window.mainloop()

    def configure_action_buttons_menu_view(self):
        """fonction qui configure les actions des boutons de la page d'acceuil"""

    def change_dataset(self):
        """
        Fonction permettant de changer le dataset en cours d'utilisation
        :return:
        """

        self.display_dataset_images_menu()

    def display_dataset_images_menu(self):
        """
        Fonction qui affiche sur le menu quelques images du dataset
        :return:
        """

        pass


