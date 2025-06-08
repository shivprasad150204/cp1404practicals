MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARACTERS_REQUIRED = True
SPECIAL_CHARACTERS = "!@# $%^&*()_-=+`~,./'[]<>?{}|\\"

def is_valid_password(password):
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    count_lower = sum(1 for char in password if char.islower())
    count_upper = sum(1 for char in password if char.isupper())
    count_digit = sum(1 for char in password if char.isdigit())
    count_special = sum(1 for char in password if char in SPECIAL_CHARACTERS)

    if count_lower and count_upper and count_digit:
        if SPECIAL_CHARACTERS_REQUIRED and count_special == 0:
            return False
        return True
    return False

print(f"Please enter a valid password\nYour password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:\n"
      "1 or more uppercase characters\n1 or more lowercase characters\n1 or more numbers")

if SPECIAL_CHARACTERS_REQUIRED:
    print(f"and 1 or more special characters:  {SPECIAL_CHARACTERS}")
# printed output

password = input("> ")
while not is_valid_password(password):
    print("Invalid password!")
# printed output
    password = input("> ")
print(f"Your {len(password)} character password is valid: {password}")
# printed output
