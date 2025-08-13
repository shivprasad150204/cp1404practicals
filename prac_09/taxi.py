"""CP1404/CP5632 Practical
Taxi class that extends Car and includes fare logic.
"""
from prac_09.car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""
    # One price shared by all taxis unless overridden per-instance
    price_per_km = 1.23

    def __init__(self, name: str, fuel: float):
        """Initialise a Taxi with a name and fuel; start with no active fare."""
        super().__init__(name, fuel)
        # distance for the current fare (resets when starting a new fare)
        self.current_fare_distance = 0

    def __str__(self):
        """Return Car info plus current fare distance and price per km."""
        return (f"{super().__str__()}, {self.current_fare_distance}km on current fare, "
                f"${self.price_per_km:.2f}/km")

    def get_fare(self) -> float:
        """Return cost for the current fare, rounded to the nearest 10c.

        Rounded here so that any subclasses that call super().get_fare()
        inherit the '10c rounding' rule (DRY).
        """
        raw_cost = self.price_per_km * self.current_fare_distance
        return round(raw_cost, 1)  # nearest 10c

    def start_fare(self) -> None:
        """Begin a new fare by resetting the fare distance."""
        self.current_fare_distance = 0

    def drive(self, distance: float) -> float:
        """Drive like a Car but also accumulate fare distance."""
        actual = super().drive(distance)
        self.current_fare_distance += actual
        return actual
