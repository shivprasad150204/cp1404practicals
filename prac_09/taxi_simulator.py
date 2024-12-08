"""
Taxi Simulator
"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Lexus", 200, 2),
        SilverServiceTaxi("Hummer", 150, 4)
    ]
    total_cost = 0.0
    chosen_taxi = None

    print("Let's drive!")
    while True:
        print("\nMenu: (q)uit, (c)hoose taxi, (d)rive")
        choice = input(">>> ").lower()

        if choice == "q":
            break
        elif choice == "c":
            chosen_taxi = choose_taxi(taxis)
        elif choice == "d":
            if chosen_taxi:
                total_cost += drive_taxi(chosen_taxi)
            else:
                print("You need to choose a taxi before you can drive!")
        else:
            print("Invalid choice. Please select from the menu options.")

    print("\nTotal trip cost: ${:.2f}".format(total_cost))
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis):
    print("Available taxis:")
    display_taxis(taxis)
    try:
        taxi_choice = int(input("Choose taxi: "))
        chosen_taxi = taxis[taxi_choice]
        print(f"You chose {chosen_taxi}")
        return chosen_taxi
    except (IndexError, ValueError):
        print("Invalid taxi choice")
        return None


def drive_taxi(chosen_taxi):
    try:
        distance = int(input("Drive how far? "))
        chosen_taxi.start_fare()
        distance_driven = chosen_taxi.drive(distance)
        fare = chosen_taxi.get_fare()
        print(f"Your {chosen_taxi.name} drove {distance_driven}km.")
        print(f"Fare: ${fare:.2f}")
        return fare
    except ValueError:
        print("Invalid distance")
        return 0.0


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == "__main__":
    main()
