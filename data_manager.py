import os
import json
from models.tournament import Tournament
from models.round import Round
from models.match import Match


def save_players(players):
    os.makedirs("data", exist_ok=True)
    with open("data/players.json", "w") as f:
        json.dump([p.to_dict() for p in players], f, indent=4)


def load_players():
    if os.path.exists("data/players.json"):
        with open("data/players.json", "r") as f:
            content = f.read()
            if not content.strip():
                return []
            return json.loads(content)
    return []


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


def save_tournaments(tournaments):
    os.makedirs("data", exist_ok=True)
    with open("data/tournaments.json", "w") as f:
        json.dump([t.to_dict() for t in tournaments], f, indent=4)


def load_tournaments():
    if os.path.exists("data/tournaments.json"):
        with open("data/tournaments.json", "r") as f:
            content = f.read()
            if not content.strip():
                return []
            data = json.loads(content)
            return [dict_to_tournament(t) for t in data]
    return []