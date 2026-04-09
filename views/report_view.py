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
        print("1. Afficher à l'écran")
        print("2. Exporter en CSV")
        return input("Votre choix : ")

    def confirm_export(self, filename):
        print(f"\n {filename} exporté")
