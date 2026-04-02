from models.tournaments import Tournament
from models.round import Round
from models.match import Match


def dict_to_match(data):
    match = Match.__new__(Match)
    match.players = [data["players"][0], data["players"][1]]
    return match


def dict_to_round(data):
    r = Round(data["name"])
    r.start_datetime = data["start_datetime"]
    r.end_datetime = data["end_datetime"]
    r.matches = [dict_to_match(m) for m in data["matches"]]
    return r


def dict_to_tournament(data):
    t = Tournament(
        data["name"],
        data["starting_date"],
        data["ending_date"],
        data["location"],
        data["description"],
        data["number_of_rounds"]
    )
    t.current_round = data["current_round"]
    t.players_list = data["players_list"]
    t.rounds = [dict_to_round(r) for r in data["rounds"]]
    return t
