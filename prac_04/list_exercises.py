# List Exercises

def main():
    numbers = []
    for i in range(5):
        number = int(input(f"Number {i + 1}: "))
        numbers.append(number)

    print("\nThe first number is", numbers[0])
    print("The last number is", numbers[-1])
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))
    print("The average of the numbers is", sum(numbers) / len(numbers))

    # Woefully inadequate security checker
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    username = input("\nEnter your username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")
