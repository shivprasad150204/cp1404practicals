"""UnreliableCar that sometimes refuses to drive, based on reliability."""
import random
from prac_09.car import Car


class UnreliableCar(Car):
    """A Car with a chance to not move when asked to drive."""
    def __init__(self, name: str, fuel: float, reliability: float):
        """Construct with base Car fields plus a 0–100 reliability percentage."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance: float) -> float:
        """Attempt to drive; only succeeds if random roll < reliability."""
        roll = random.uniform(0, 100)
        if roll < self.reliability:
            # Drive as per normal Car
            return super().drive(distance)
        # Failed to drive this time
        return 0.0
