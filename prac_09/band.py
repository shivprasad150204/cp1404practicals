"""
Band class
"""
class Band:

    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        for musician in self.musicians:
            if musician.instruments:
                print(f"{musician.name} is playing: {musician.instruments[0]}")
            else:
                print(f"{musician.name} needs an instrument!")

    def __str__(self):
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"
