"""
CP1404/CP5632 Practical
Wimbledon data-reading, processing, and displaying
"""
FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read data file and print details about Wimbledon champions and countries."""
    # Load records from file
    with open(FILENAME, "r", encoding="utf-8-sig") as file:
        next(file)  # Skip the header line
        records = [line.strip().split(",") for line in file]

    # Analyze records to get champions and countries
    champion_wins = {}
    countries = set()
    for record in records:
        country = record[INDEX_COUNTRY]
        champion = record[INDEX_CHAMPION]

        countries.add(country)
        champion_wins[champion] = champion_wins.get(champion, 0) + 1

    # Display results
    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_wins.items()):
        print(f"{champion}: {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()

