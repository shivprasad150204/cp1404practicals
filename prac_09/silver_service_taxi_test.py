"""
Test SilverServiceTaxi class
"""
from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Test the SilverServiceTaxi class."""
    silver_taxi = SilverServiceTaxi("Lexus", 100, 2)
    silver_taxi.drive(18)
    fare = silver_taxi.get_fare()
    print(silver_taxi)
    print(f"Fare for 18km: ${fare:.2f}")
    assert round(fare, 1) == 48.8, "Fare should be $48.80"

if __name__ == "__main__":
    main()
