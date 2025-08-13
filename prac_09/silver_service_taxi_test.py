"""Tests for SilverServiceTaxi fare calculations."""
from silver_service_taxi import SilverServiceTaxi

def main():
    limo = SilverServiceTaxi("Limo", 100, fanciness=2)
    limo.drive(18)
    fare = limo.get_fare()
    # Expect 18 km * (1.23*2) = 44.28 -> rounded 44.3, + 4.5 = 48.8
    assert abs(fare - 48.8) < 1e-9, f"Expected $48.80, got ${fare:.2f}"
    print(f"18km Limo fare: ${fare:.2f} (OK)")

if __name__ == "__main__":
    main()
