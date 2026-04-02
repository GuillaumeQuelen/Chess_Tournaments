import re
from datetime import datetime


class PlayerView:
    def get_player(self):
        first_name = input("Entrez le prénom du joueur : ")
        last_name = input("Entrez le nom du joueur : ")

        while True:
            birth_date = input("Date de naissance (JJ/MM/AAAA) : ")
            try:
                date = datetime.strptime(birth_date, "%d/%m/%Y")
                if (datetime.now() - date).days > 150 * 365:
                    print("Âge invalide !")
                else:
                    break
            except ValueError:
                print("Format invalide ! Ex: 15/03/1990")

        while True:
            national_id = input("Identifiant (ex: AB12345) : ").upper()
            if re.match(r"^[A-Z]{2}\d{5}$", national_id):
                break
            print("Format invalide ! Ex: AB12345")

        return first_name, last_name, birth_date, national_id

    def ask_continue(self):
        return input("Ajouter un autre joueur ? (O/N) : ").upper() == "O"