Class Tournaments:
    def __init__(self, name, starting_date, ending_date, location, description, number_of_rounds=4):
        self.name = name
        self.starting_date = starting_date
        self.ending_date = ending_date
        self.location = location
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.current_round = 0
        self.rounds = []
        self.players_lists = []

        def to_dict(self):
            return {
                "name": self.name,
                "starting_date": self.starting_date,
                "ending_date": self.ending_date,
                "location": self.location,
                "description": self.description,
                "number_of_rounds": self.number_of_rounds,
                "current_round": self.current_round,
                "rounds": [round.to_dict() for round in self.rounds],
                "players_lists": [player.to_dict() for player in self.players_lists]
            }