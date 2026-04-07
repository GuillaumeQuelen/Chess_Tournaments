import re
from datetime import datetime


class PlayerView:
    def get_player(self):
        first_name = self.get_valid_first_name()
        last_name = self.get_valid_last_name()
        birth_date = self.get_valid_birth_date()
        national_id = self.get_national_id()
        return first_name, last_name, birth_date, national_id


    def ask_continue(self):
        return input("Ajouter un autre joueur ? (O/N) : ").upper() == "O"
    
    def player_menu(self):
        print("\n=== GESTION DES JOUEURS ===")
        print("1. Créer un joueur")
        print("2. Retour au menu principal")
        return input("Votre choix : ")
    
    def get_valid_birth_date(self):
        while True:
            birth_date = input("Date de naissance (JJ/MM/AAAA) : ")
            try:
                date = datetime.strptime(birth_date, "%d/%m/%Y")
                if (datetime.now() - date).days > 150 * 365:
                    print("Âge invalide !")
                else:
                    return birth_date
            except ValueError:
                print("Format invalide ! Ex: 15/03/1990")

    def get_national_id(self):
        while True:
            national_id = input("Identifiant (ex: AB12345) : ").upper()
            if re.match(r"^[A-Z]{2}\d{5}$", national_id):
                return national_id
            print("Format invalide ! Ex: AB12345")
    def get_valid_first_name(self):
        while True:
            first_name = input("Entrez le prénom du joueur : ")
            if first_name.strip():
                return first_name
            print("Le prénom est obligatoire !")
    def get_valid_last_name(self):
        while True:
            last_name = input("Entrez le nom du joueur : ")
            if last_name.strip():
                return last_name
            print("Le nom est obligatoire !")
