"""SilverServiceTaxi inherits from Taxi and adds fanciness and flagfall."""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A fancier Taxi that charges flagfall and scales price-per-km by fanciness."""
    flagfall = 4.50

    def __init__(self, name: str, fuel: float, fanciness: float):
        """Construct with name, fuel; apply fanciness multiplier to price per km."""
        super().__init__(name, fuel)
        # Start with the base class price then customise per-instance
        self.price_per_km = Taxi.price_per_km * fanciness
        self.fanciness = fanciness

    def get_fare(self) -> float:
        """Return total fare = rounded distance cost (via super) + flagfall."""
        distance_cost = super().get_fare()  # already rounded to 10c
        return distance_cost + self.flagfall

    def __str__(self):
        """String showing base info, price per km, and flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
