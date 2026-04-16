from datetime import datetime


class TournamentsView:
    def get_info(self):
        name = input("Nom du tournoi : ")

        while True:
            starting_date = input("Date de début (JJ/MM/AAAA) : ")
            try:
                datetime.strptime(starting_date, "%d/%m/%Y")
                break
            except ValueError:
                print("Date invalide ! Format : JJ/MM/AAAA")

        while True:
            ending_date = input("Date de fin (JJ/MM/AAAA) : ")
            try:
                datetime.strptime(ending_date, "%d/%m/%Y")
                break
            except ValueError:
                print("Date invalide ! Format : JJ/MM/AAAA")

        location = input("Lieu : ")
        description = input("Description : ")
        while True:
            rounds_input = input("Nombre de tours (4 par défaut) : ") or "4"
            try:
                number_of_rounds = int(rounds_input)
                if number_of_rounds > 0:
                    break
                print("Le nombre de tours doit être positif !")
            except ValueError:
                print("Entrez un nombre valide !")
        return name, starting_date, ending_date, location, description, number_of_rounds

    def tournament_menu(self):
        print("\n=== GESTION DES TOURNOIS ===")
        print("1. Créer un tournoi")
        print("2. Ouvrir un tournoi")
        print("3. Retour au menu principal")
        return input("Votre choix : ")

    def chosen_tournament_menu(self, tournament_name):
        print(f"\n=== {tournament_name} ===")
        print("1. Ajouter un joueur au tournoi")
        print("2. Démarrer un round")
        print("3. Entrer les résultats")
        print("4. Retour au menu précédent")
        return input("Votre choix : ")
