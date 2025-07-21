
from prac_06.guitar import Guitar

def main():
    """Program to let user enter guitars and display them."""
    my_guitars = []
    print("Let's record your guitars!")

    guitar_name = input("Name: ")
    while guitar_name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        my_guitars.append(Guitar(guitar_name, year, cost))
        print(f"{guitar_name} added.\n")
        guitar_name = input("Name: ")

    print("\nThese are your guitars:")
    for i, guitar in enumerate(my_guitars, start=1):
        vintage_note = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar} {vintage_note}")

main()
