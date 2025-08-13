import csv
from guitar import Guitar

def load_guitars(filename="guitars.csv"):
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, year, cost))
    return guitars

def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)

def main():
    guitars = load_guitars()
    print("Loaded guitars:")
    display_guitars(guitars)

    guitars.sort()
    print("\nSorted guitars by year:")
    display_guitars(guitars)

if __name__ == "__main__":
    main()
