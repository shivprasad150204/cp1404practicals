"""
CP1404/CP5632 Practical
Taxi class (extends Car)
"""
from prac_09.car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23  # Class variable for price per km

    def __init__(self, name, fuel):
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
