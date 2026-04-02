from views.player_view import PlayerView
from models.players import Player


class PlayerController:
    def __init__(self):
        self.view = PlayerView()
        self.players = Player.load_all()

    def create_player(self):
        first_name, last_name, birth_date, national_id = self.view.get_player()
        player = Player(last_name, first_name, birth_date, national_id)
        self.players.append(player.to_dict())
        Player.save_all_dicts(self.players)
        if self.view.ask_continue():
            self.create_player()
