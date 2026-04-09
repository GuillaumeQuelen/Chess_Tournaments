from models.players import Player
from models.tournaments import Tournament
from data_manager import dict_to_tournament
from views.report_view import ReportView
from models.base import Base


class ReportController:
    def __init__(self):
        self.view = ReportView()

    def list_all_players(self, players):
        sorted_players = sorted(players, key=lambda p: p["last_name"])
        choix_f = self.view.report_format()
        if choix_f == "1":
            for p in sorted_players:
                print(f"{p['last_name']} {p['first_name']} - {p['national_id']}")
        elif choix_f == "2":
            headers = ["last_name", "first_name", "birth_date", "national_id", "score"]
            rows = [[p[h] for h in headers] for p in sorted_players]
            filepath = Base.export_csv("players_report.csv", headers, rows)
            self.view.confirm_export(filepath)

    def list_all_tournaments(self, tournaments):
        choix_f = self.view.report_format()
        if choix_f == "1":
            for t in tournaments:
                print(f"{t.name} | {t.starting_date} → {t.ending_date} | {t.location}")

        elif choix_f == "2":
            headers = ["name", "starting_date", "ending_date", "location"]
            rows = [[t.name, t.starting_date, t.ending_date, t.location] for t in tournaments]

            filepath = Base.export_csv("tournaments_report.csv", headers, rows)
            self.view.confirm_export(filepath)

    def tournament_details(self, tournaments):
        if not tournaments:
            print("Aucun tournoi disponible !")
            return
        for i, t in enumerate(tournaments):
            print(f"{i+1}. {t.name}")
        choix = int(input("Choisir un tournoi : ")) - 1
        t = tournaments[choix]
        choix_f = self.view.report_format()
        if choix_f == "1":
            print(f"\n=== {t.name} ===")
            print(f"Dates : {t.starting_date} → {t.ending_date}")
            print(f"Lieu : {t.location}")
            print(f"Description : {t.description}")
            print(f"Nombre de rounds : {t.number_of_rounds}")
            print(f"Joueurs inscrits : {len(t.players_list)}")
        elif choix_f == "2":
            headers = ["name", "starting_date", "ending_date", "location", "description", "number_of_rounds"]
            rows = [[t.name, t.starting_date, t.ending_date, t.location, t.description, t.number_of_rounds]]

            filepath = Base.export_csv(f"{t.name}_details.csv", headers, rows)
            self.view.confirm_export(filepath)

    def list_tournament_players(self, tournaments):
        if not tournaments:
            print("Aucun tournoi disponible !")
            return
        for i, t in enumerate(tournaments):
            print(f"{i+1}. {t.name}")
        choix = int(input("Choisir un tournoi : ")) - 1
        players = sorted(tournaments[choix].players_list, key=lambda p: p["last_name"])
        choix_f = self.view.report_format()
        if choix_f == "1":
            for p in players:
                print(f"{p['last_name']} {p['first_name']} - {p['national_id']}")
        elif choix_f == "2":
            headers = ["last_name", "first_name", "birth_date", "national_id", "score"]
            rows = [[p[h] for h in headers] for p in players]

            filepath = Base.export_csv(f"{tournaments[choix].name}_players.csv", headers, rows)
            self.view.confirm_export(filepath)

    def list_tournament_rounds(self, tournaments):
        if not tournaments:
            print("Aucun tournoi disponible !")
            return
        for i, t in enumerate(tournaments):
            print(f"{i+1}. {t.name}")
        choix = int(input("Choisir un tournoi : ")) - 1
        t = tournaments[choix]
        choix_f = self.view.report_format()
        if choix_f == "1":
            for r in t.rounds:
                print(f"\n--- {r.name} ---")
                for m in r.matches:
                    p1 = m.players[0][0]
                    p2 = m.players[1][0]
                    score1 = m.players[0][1]
                    score2 = m.players[1][1]
                    print(
                        f"{p1['first_name']} {p1['last_name']}"
                        f" ({score1}) vs"
                        f" {p2['first_name']} {p2['last_name']}"
                        f" ({score2})"
                    )
        elif choix_f == "2":
            headers = ["round_name", "player1", "score1", "player2", "score2"]
            rows = []
            for r in t.rounds:
                for m in r.matches:
                    p1 = m.players[0][0]
                    p2 = m.players[1][0]
                    score1 = m.players[0][1]
                    score2 = m.players[1][1]
                    rows.append([
                        r.name,
                        f"{p1['first_name']} {p1['last_name']}",
                        score1,
                        f"{p2['first_name']} {p2['last_name']}",
                        score2
                    ])

            filepath = Base.export_csv(f"{t.name}_rounds.csv", headers, rows)
            self.view.confirm_export(filepath)

    def run(self):
        players = Player.load_all()
        tournaments = [dict_to_tournament(t) for t in Tournament.load_all()]
        while True:
            choix = self.view.show_menu()
            if choix == "1":
                self.list_all_players(players)
            elif choix == "2":
                self.list_all_tournaments(tournaments)
            elif choix == "3":
                self.tournament_details(tournaments)
            elif choix == "4":
                self.list_tournament_players(tournaments)
            elif choix == "5":
                self.list_tournament_rounds(tournaments)
            elif choix == "6":
                break
