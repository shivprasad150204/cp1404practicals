# Part 1: Write the user's name to a file called name.txt
name = input("Enter your name: ")
with open("name.txt", 'w') as file:
    file.write(name)

# Part 2: Read the name from name.txt and print a greeting
with open("name.txt", 'r') as file:
    name = file.read().strip()  # Read the content and remove any surrounding whitespace
    print(f"Hi {name}!")

# Part 3: Read and add the first two numbers from numbers.txt, then print the result
with open("numbers.txt", 'r') as file:
    number1 = int(file.readline())  # Read the first number
    number2 = int(file.readline())  # Read the second number
    result = number1 + number2
    print(f"The sum of the first two numbers is: {result}")

# Part 4: Read all the lines from numbers.txt, sum them, and print the total
total = 0
with open("numbers.txt", 'r') as file:
    for line in file:
        total += int(line.strip())  # Convert each line to an integer and add to the total
    print(f"The total of all numbers is: {total}")
