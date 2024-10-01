"""
CP1404/CP5632 - Practical
Get a password with minimum length and display asterisks
"""

MINIMUM_LENGTH = 4

def main():
    """Get and print password with asterisks."""
    password = get_password(MINIMUM_LENGTH)
    print('*' * len(password))

def get_password(minimum_length):
    """Prompt for a valid password with a minimum length."""
    password = input(f"Enter password of at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Password too short")
        password = input(f"Enter password of at least {minimum_length} characters: ")
    return password

main()
