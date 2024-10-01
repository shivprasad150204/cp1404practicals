"""
CP1404/CP5632 - Practical
Simplified program to determine score status with a function
"""

def main():
    """Get a numeric score and display its status."""
    score = float(input("Enter score: "))
    print(determine_status(score))

def determine_status(score):
    """Return the status based on the score."""
    if not 0 <= score <= 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    return "Bad"

main()
