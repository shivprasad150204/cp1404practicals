"""Tests for UnreliableCar behaviour."""
import random
from unreliable_car import UnreliableCar

def main():
    # Make tests reproducible
    random.seed(42)

    car = UnreliableCar("Sketchy", 100, reliability=50.0)
    attempts = 100
    requested_each = 1
    total_driven = 0.0

    for _ in range(attempts):
        total_driven += car.drive(requested_each)

    # Basic sanity checks
    assert 0 <= total_driven <= attempts  # never exceeds requests
    # With reliability=50% and 100 attempts, we expect ~50 distance (allow wide band)
    assert 20 <= total_driven <= 80, f"Unexpected total_driven={total_driven}"

    print(f"Total driven in {attempts} x {requested_each}km attempts: {total_driven:.1f} km")
    print("UnreliableCar tests passed.")

if __name__ == "__main__":
    main()
