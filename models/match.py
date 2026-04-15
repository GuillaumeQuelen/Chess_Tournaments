class Match:
    def __init__(self, player1, player2):
        self.players = ([player1, 0], [player2, 0])

    def to_dict(self):
        return {
            "players": [
                [player[0], player[1]]
                for player in self.players
            ]
        }
    @classmethod
    def from_dict(cls, data):
        from models.players import Player
        match = cls.__new__(cls)
        match.players = (
            [Player.from_dict(data["players"][0][0]), data["players"][0][1]],
            [Player.from_dict(data["players"][1][0]), data["players"][1][1]],
        )
        return match