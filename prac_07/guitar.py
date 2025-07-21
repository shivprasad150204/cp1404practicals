class Guitar:
    """Represent a guitar with a name, year, and cost."""

    def __init__(self, name, year, cost):
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __repr__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        """Less than, used for sorting by year."""
        return self.year < other.year
