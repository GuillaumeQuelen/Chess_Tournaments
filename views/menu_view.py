class MenuView:
    def show_menu(self):
        print("\nBienvenue, quel menu souhaiteriez-vous accéder ?")
        print("1. Les joueurs")
        print("2. Les tournois")
        print("3. Les rapports")
        print("4. Quitter")
        return input("Votre choix : ")
