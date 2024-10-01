"""
CP1404/CP5632 - Practical
Convert temperatures between files
"""

import random

def main():
    """Convert temperatures from input file to output file."""
    with open("temps_input.txt", "r") as input_file, open("temps_output.txt", "w") as output_file:
        for line in input_file:
            result = convert_fahrenheit_to_celsius(float(line))
            print(result, file=output_file)

def create_input_file(quantity):
    """Write a specified number of random temperatures to a file."""
    with open("temps_input.txt", "w") as temperatures_file:
        for _ in range(quantity):
            temperature = random.uniform(-200, 200)
            print(temperature, file=temperatures_file)

def convert_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5 + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

main()
