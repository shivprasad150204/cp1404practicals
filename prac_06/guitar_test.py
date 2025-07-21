
from prac_06.guitar import Guitar

def run_tests():
    """Test Guitar class functionality."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    cheap = Guitar("Another Guitar", 2013, 1234.56)

    print(f"{gibson.name} get_age() - Expected 100. Got {gibson.get_age()}")
    print(f"{cheap.name} get_age() - Expected 9. Got {cheap.get_age()}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{cheap.name} is_vintage() - Expected False. Got {cheap.is_vintage()}")

run_tests()
