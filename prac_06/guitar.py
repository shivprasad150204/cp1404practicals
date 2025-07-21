
class Guitar:
    """Class representing a guitar with name, year and price."""

    def __init__(self, name="", year=0, price=0):
        self.name = name
        self.year = year
        self.price = price

    def get_age(self):
        """Return the age of the guitar based on current year."""
        return 2022 - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage (50 years or older)."""
        return self.get_age() >= 50

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.price:,.2f}"
