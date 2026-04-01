from views.player_view import PlayerView
from models.players import Player
from data_manager import save_players, load_players


class PlayerController:
    def __init__(self):
        self.view = PlayerView()
        self.players = load_players()

    def create_player(self):
        first_name, last_name, birth_date, national_id = self.view.get_player()
        player = Player(last_name, first_name, birth_date, national_id)
        self.players.append(player.to_dict())
        save_players(self.players)
        if self.view.ask_continue():
            self.create_player()