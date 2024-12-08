"""
Taxi Class - A Specialized Version of Car
"""
from prac_09.car import Car


class Cab(Car):
    """Represents a taxi with fare calculation."""

    cost_per_km = 1.25  # Cost rate for the taxi service

    def __init__(self, model_name, fuel_level):
        """Initialize the taxi with its attributes."""
        super().__init__(model_name, fuel_level)
        self.distance_fare = 0

    def __str__(self):
        return f"{super().__str__()}, {self.distance_fare}km for current fare, ${self.cost_per_km:.2f}/km"

    def calculate_fare(self):
        """Compute the total fare for the trip."""
        return self.cost_per_km * self.distance_fare

    def reset_fare(self):
        """Start a new fare calculation."""
        self.distance_fare = 0

    def drive(self, distance):
        """Drive the taxi and track fare distance."""
        driven_distance = super().drive(distance)
        self.distance_fare += driven_distance
        return driven_distance
