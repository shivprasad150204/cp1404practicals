
MIN_LENGTH = 8  # This is the minimum password length allowed

def main():
    password = get_password()  # Ask the user for a valid password
    print_asterisks(password)  # Print stars equal to the password length

def get_password():
    password = input("Enter your password: ")
    while len(password) < MIN_LENGTH:
        print("Too short! Password must be at least", MIN_LENGTH, "characters.")
        password = input("Try again: ")
    return password

def print_asterisks(password):
    print("*" * len(password))  # Print as many * as the password length

main()  # Start the program
