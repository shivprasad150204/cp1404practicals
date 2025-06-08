#  program that safely gets an integer from the user
is_valid_input = False
while not is_valid_input:
    try:
        result = int(input("Enter a valid integer: "))
        is_valid_input = True
    except ValueError:
        print("Invalid input; please enter a valid integer.")
# printed output
print(f"You entered: {result}")
# printed output
