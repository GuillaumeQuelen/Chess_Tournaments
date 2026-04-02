class Round:
    def __init__(self, name):
        self.name = name
        self.matches = []
        self.start_datetime = None
        self.end_datetime = None

    def to_dict(self):
        return {
            "name": self.name,
            "matches": [match.to_dict() for match in self.matches],
            "start_datetime": self.start_datetime,
            "end_datetime": self.end_datetime
        }