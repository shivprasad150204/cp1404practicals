MIN_LENGTH = 2
MAX_LENGTH = 6
IS_SPECIAL_CHARACTER_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters long.")
    print("It must contain at least:")
    print("- 1 uppercase character")
    print("- 1 lowercase character")
    print("- 1 number")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print(f"- 1 special character: {SPECIAL_CHARACTERS}")

    password = input("Enter password: ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("Enter password: ")

    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Check if the provided password is valid."""
    if not (MIN_LENGTH <= len(password) <= MAX_LENGTH):
        return False

    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in SPECIAL_CHARACTERS for char in password)

    # Check required character types
    if not (has_lower and has_upper and has_digit):
        return False

    # Check if special characters are required
    if IS_SPECIAL_CHARACTER_REQUIRED and not has_special:
        return False

    return True


main()
