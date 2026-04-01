from data_manager import load_players, load_tournaments


class ReportController:
    def list_all_players(self):
        players = load_players()
        sorted_players = sorted(players, key=lambda p: p["last_name"])
        for p in sorted_players:
            print(f"{p['last_name']} {p['first_name']} - {p['national_id']}")

    def list_all_tournaments(self):
        tournaments = load_tournaments()
        for t in tournaments:
            print(f"{t.name} | {t.starting_date} → {t.ending_date} | {t.location}")

    def tournament_details(self):
        tournaments = load_tournaments()
        for i, t in enumerate(tournaments):
            print(f"{i+1}. {t.name}")
        choix = int(input("Choisir un tournoi : ")) - 1
        t = tournaments[choix]
        print(f"\n{t.name} | {t.starting_date} → {t.ending_date}")

    def list_tournament_players(self):
        tournaments = load_tournaments()
        for i, t in enumerate(tournaments):
            print(f"{i+1}. {t.name}")
        choix = int(input("Choisir un tournoi : ")) - 1
        players = sorted(tournaments[choix].players_list, key=lambda p: p["last_name"])
        for p in players:
            print(f"{p['last_name']} {p['first_name']} - {p['national_id']}")

    def list_tournament_rounds(self):
        tournaments = load_tournaments()
        for i, t in enumerate(tournaments):
            print(f"{i+1}. {t.name}")
        choix = int(input("Choisir un tournoi : ")) - 1
        t = tournaments[choix]
        for r in t.rounds:
            print(f"\n=== {r.name} ===")
            for m in r.matches:
                p1 = m.players[0][0]
                p2 = m.players[1][0]
                s1 = m.players[0][1]
                s2 = m.players[1][1]
                print(f"  {p1['first_name']} {s1} - {s2} {p2['first_name']}")