while True:
    try:
        result = int(input("Enter a valid integer: "))
        break  # Exit the loop if input is valid
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
