from guitar import Guitar

def run_tests():
    """Tests for the Guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2012, 1512.9)

    print(f"{guitar.name} get_age() - Expected {datetime.now().year - 1922}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {datetime.now().year - 2012}. Got {other.get_age()}\n")

    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected False. Got {other.is_vintage()}")

if __name__ == '__main__':
    run_tests()