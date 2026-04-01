import random
from views.tournament_view import TournamentView
from models.tournament import Tournament
from data_manager import save_tournaments, load_tournaments, load_players


class TournamentController:
    def __init__(self):
        self.view = TournamentView()
        self.tournaments = load_tournaments()
        self.current_tournament = None

    def create_tournament(self):
        name, starting_date, ending_date, location, description, number_of_rounds = self.view.get_info()
        tournament = Tournament(name, starting_date, ending_date, location, description, number_of_rounds)
        self.tournaments.append(tournament)
        save_tournaments(self.tournaments)
        return tournament

    def select_tournament(self):
        if not self.tournaments:
            print("❌ Aucun tournoi disponible !")
            return
        for i, t in enumerate(self.tournaments):
            print(f"{i+1}. {t.name}")
        choix = int(input("Choisir un tournoi : ")) - 1
        if 0 <= choix < len(self.tournaments):
            self.current_tournament = self.tournaments[choix]
        else:
            print("❌ Numéro invalide !")

    def add_player_to_tournament(self, tournament):
        players_data = load_players()
        for i, p in enumerate(players_data):
            print(f"{i+1}. {p['first_name']} {p['last_name']} - {p['national_id']}")

        choix_str = input("Numéro(s) du joueur à ajouter (ex: 1,3,5) : ")
        choix_list = [int(x.strip()) - 1 for x in choix_str.split(",")]

        for choix in choix_list:
            if 0 <= choix < len(players_data):
                already_in = any(
                    p["national_id"] == players_data[choix]["national_id"]
                    for p in tournament.players_list
                )
                if already_in:
                    print(f"❌ {players_data[choix]['first_name']} est déjà dans le tournoi !")
                else:
                    tournament.players_list.append(players_data[choix])
                    print(f"✅ {players_data[choix]['first_name']} ajouté !")
            else:
                print(f"❌ Numéro {choix+1} invalide !")

        save_tournaments(self.tournaments)
    
    def generate_pairs(self, tournament):
        players = tournament.players_list.copy()
        if tournament.current_round == 0:
            random.shuffle(players)
        else:
            players.sort(key=lambda p: p["score"], reverse=True)
        pairs = []
        for i in range(0, len(players) - 1, 2):
            pairs.append((players[i], players[i + 1]))
        return pairs

    def start_round(self, tournament):
        from models.round import Round
        from models.match import Match
        tournament.current_round += 1
        new_round = Round(f"Round {tournament.current_round}")
        pairs = self.generate_pairs(tournament)
        for player1, player2 in pairs:
            new_round.matches.append(Match(player1, player2))
        tournament.rounds.append(new_round)
        save_tournaments(self.tournaments)
        return new_round

    def enter_results(self, tournament):
        current_round = tournament.rounds[-1]
        for match in current_round.matches:
            p1 = match.players[0][0]
            p2 = match.players[1][0]
            print(f"\n{p1['first_name']} vs {p2['first_name']}")
            print("1. Joueur 1 gagne")
            print("2. Joueur 2 gagne")
            print("3. Match nul")
            result = input("Résultat : ")
            if result == "1":
                match.players[0][1] = 1
                match.players[1][1] = 0
                p1["score"] += 1
            elif result == "2":
                match.players[0][1] = 0
                match.players[1][1] = 1
                p2["score"] += 1
            else:
                match.players[0][1] = 0.5
                match.players[1][1] = 0.5
                p1["score"] += 0.5
                p2["score"] += 0.5
        save_tournaments(self.tournaments)

    def run(self):
        while True:
            choix = self.view.tournament_menu()
            if choix == "1":
                self.create_tournament()
            elif choix == "2":
                self.select_tournament()
            elif choix == "3" and self.current_tournament:
                self.add_player_to_tournament(self.current_tournament)
            elif choix == "4" and self.current_tournament:
                new_round = self.start_round(self.current_tournament)
                print(f"\n✅ {new_round.name} démarré avec {len(new_round.matches)} matchs !")
                for match in new_round.matches:
                    print(f"  ⚔️  {match.players[0][0]['first_name']} vs {match.players[1][0]['first_name']}")
            elif choix == "5" and self.current_tournament:
                self.enter_results(self.current_tournament)
            elif choix == "6":
                break