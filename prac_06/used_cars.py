
from prac_06.car import Car

def main():
    """Demo to show car fuel usage and driving."""
    car1 = Car("My Car", 180)
    car1.drive(30)
    print(f"{car1.name} has {car1.fuel} fuel left.")
    print(car1)

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    limo.drive(115)
    print(limo)

main()
