from datetime import datetime


class TournamentView:
    def get_info(self):
        name = input("Nom du tournoi : ")

        while True:
            starting_date = input("Date de début (JJ/MM/AAAA) : ")
            try:
                datetime.strptime(starting_date, "%d/%m/%Y")
                break
            except ValueError:
                print("❌ Date invalide ! Format : JJ/MM/AAAA")

        while True:
            ending_date = input("Date de fin (JJ/MM/AAAA) : ")
            try:
                datetime.strptime(ending_date, "%d/%m/%Y")
                break
            except ValueError:
                print("❌ Date invalide ! Format : JJ/MM/AAAA")

        location = input("Lieu : ")
        description = input("Description : ")
        number_of_rounds = int(input("Nombre de tours (4 par défaut) : ") or "4")

        return name, starting_date, ending_date, location, description, number_of_rounds

    def tournament_menu(self):
        print("\n=== GESTION DES TOURNOIS ===")
        print("1. Créer un tournoi")
        print("2. Ouvrir un tournoi")
        print("3. Ajouter un joueur au tournoi")
        print("4. Démarrer un round")
        print("5. Entrer les résultats")
        print("6. Retour au menu principal")
        return input("Votre choix : ")