"""
This script performs basic list operations:
1. Accepts five numbers from user input and displays summary statistics.
2. Checks if a username exists in a predefined list for a simple login simulation.
"""

# Basic list operations
numbers = []
for i in range(5):
    number = int(input(f"Number {i + 1}: "))
    numbers.append(number)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

# Security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
             'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter your username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
