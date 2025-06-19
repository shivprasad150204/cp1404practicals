"""
This script generates user-defined 'quick pick' lottery games.
Each pick consists of 6 unique random numbers between 1 and 45.
"""

import random

NUMBERS_IN_PICK = 6
MINIMUM = 1
MAXIMUM = 45

def main():
    number_of_picks = int(input("How many quick picks? "))
    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in sorted(quick_pick)))


def generate_quick_pick():
    quick_pick = []
    while len(quick_pick) < NUMBERS_IN_PICK:
        number = random.randint(MINIMUM, MAXIMUM)
        if number not in quick_pick:
            quick_pick.append(number)
    return quick_pick


main()
