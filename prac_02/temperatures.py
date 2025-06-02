# A program that asks for temps and converts between Celsius and Fahrenheit

def main():
    temp_c = float(input("Celsius temp: "))
    temp_f = to_fahrenheit(temp_c)
    print(f"{temp_c}°C is {temp_f:.1f}°F")

    temp_f = float(input("Fahrenheit temp: "))
    temp_c = to_celsius(temp_f)
    print(f"{temp_f}°F is {temp_c:.1f}°C")

def to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

def to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

main()
