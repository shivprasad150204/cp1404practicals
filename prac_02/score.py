# This script lets the user enter a score and gives feedback

import random

def main():
    score = float(input("Score: "))
    message = check_score(score)
    print("Your result:", message)

    rand_score = random.randint(0, 100)
    print(f"Random score: {rand_score} -", check_score(rand_score))

def check_score(score):
    """Return a message based on the score value."""
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Failing"

main()
