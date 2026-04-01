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