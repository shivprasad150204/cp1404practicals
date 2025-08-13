"""Interactive Taxi Simulator using Taxi and SilverServiceTaxi."""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def list_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input; enter a whole number.")

def main():
    print("Let's drive!")
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4),
    ]
    bill_to_date = 0.0
    current_taxi = None

    choice = ""
    while choice.lower() != "q":
        print(MENU)
        choice = input(">>> ").strip().lower()

        if choice == "c":
            list_taxis(taxis)
            index = get_int("Choose taxi: ")
            if 0 <= index < len(taxis):
                current_taxi = taxis[index]
                # new meter whenever you pick a taxi (common expectation)
                current_taxi.start_fare()
            else:
                print("Invalid taxi choice")

        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = get_int("Drive how far? ")
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                bill_to_date += trip_cost
                # next trip should start a new fare automatically
                current_taxi.start_fare()
        elif choice == "q":
            break
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    list_taxis(taxis)

if __name__ == "__main__":
    main()
