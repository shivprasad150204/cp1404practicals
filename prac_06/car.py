
class Car:
    """A simple Car class to track fuel and distance travelled."""

    def __init__(self, name="Car", fuel=0):
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def add_fuel(self, litres):
        """Add fuel to the car."""
        self.fuel += litres

    def drive(self, km):
        """Drive the car for a distance, reducing fuel."""
        distance = min(km, self.fuel)
        self.fuel -= distance
        self.odometer += distance
        return distance

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"
