"""
CP1404/CP5632 Practical
Wimbledon data-reading, processing and displaying
"""
FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read data file, process champions and countries, and display the results."""
    records = read_file_data(FILENAME)
    champions_dict, country_set = analyze_records(records)
    show_results(champions_dict, country_set)


def analyze_records(data):
    """Analyze the records to build a dictionary of champions and a set of countries."""
    champions = {}
    countries = set()
    for entry in data:
        country = entry[INDEX_COUNTRY]
        champion = entry[INDEX_CHAMPION]
        countries.add(country)
        champions[champion] = champions.get(champion, 0) + 1
    return champions, countries


def show_results(champions, countries):
    """Display the champions and the countries that have won Wimbledon."""
    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion}: {wins}")
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def read_file_data(filename):
    """Read data from the given file and return it as a list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as file:
        file.readline()  # Skip header
        return [line.strip().split(",") for line in file]


main()


