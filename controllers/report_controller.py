from models.players import Player
from models.tournaments import Tournament
from data_manager import dict_to_tournament

# remplace load_players() par :
Player.load_all()

# remplace load_tournaments() par :
[dict_to_tournament(t) for t in Tournament.load_all()]