"""Wimbledon Results Summary
Estimate: 30 minutes
Actual: 2025-06-23 11:21
"""

FILE = "wimbledon.csv"

def main():
    raw_data = load_data(FILE)
    champions, countries = summarize_data(raw_data)
    display_champions(champions)
    display_countries(countries)

def load_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as file:
        file.readline()
        return [line.strip().split(",") for line in file]

def summarize_data(data):
    wins = {}
    country_set = set()
    for entry in data:
        champion = entry[2]
        country = entry[1]
        wins[champion] = wins.get(champion, 0) + 1
        country_set.add(country)
    return wins, country_set

def display_champions(champions):
    print("Wimbledon Champions:")
    for name, count in champions.items():
        print(f"{name} {count}")

def display_countries(countries):
    print(f"\nThese {len(countries)} countries have produced winners:")
    print(", ".join(sorted(countries)))

if __name__ == "__main__":
    main()
