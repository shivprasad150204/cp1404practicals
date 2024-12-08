"""
SilverServiceTaxi class (extends Taxi)
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def get_fare(self):
        return round(super().get_fare() + self.flagfall, 1)

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
