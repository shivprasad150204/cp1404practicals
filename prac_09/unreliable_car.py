"""
FaultyCar Class - Inherits from Car
"""
import random
from prac_09.car import Car


class FaultyCar(Car):
    """A car that may not always drive the desired distance."""

    def __init__(self, model, fuel_amount, reliability_percentage):
        """Initialize the car with a name, fuel, and reliability."""
        super().__init__(model, fuel_amount)
        self.reliability = reliability_percentage

    def drive(self, intended_distance):
        """Attempt to drive based on reliability. Return actual distance driven."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(intended_distance)
        return 0

