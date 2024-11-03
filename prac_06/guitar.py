from datetime import datetime

VINTAGE_AGE = 50

class Guitar:
    """Guitar class for storing details of a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of the guitar based on the current year."""
        current_year = datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        """Determine if the guitar is considered vintage based on age."""
        return self.get_age() >= VINTAGE_AGE
