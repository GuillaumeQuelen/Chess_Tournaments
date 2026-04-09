class ReportView:
    def show_menu(self):
        print("\n=== RAPPORTS ===")
        print("1. Tous les joueurs")
        print("2. Tous les tournois")
        print("3. Détails d'un tournoi")
        print("4. Joueurs d'un tournoi")
        print("5. Rounds et matchs d'un tournoi")
        print("6. Retour")
        return input("Votre choix : ")
    
    def report_format(self):
        print("\n=== FORMAT DE RAPPORT ===")
        print("1. Affichage console")
        print("2. Export JSON")
        print("3. Export CSV")
        return input("Votre choix : ")
