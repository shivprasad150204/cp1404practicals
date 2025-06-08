#  --- part 1: write user_name to f
user_name = input("What is your user_name? ")
with open("user_name.txt", "w") as f:
    f.write(user_name)

#  --- part 2: read user_name from f and print greeting
with open("user_name.txt", "r") as f:
    user_name = f.read().strip()
    print(f"Hi {user_name}!")
# printed output

#  --- part 3: add the first two numbers from numbers.txt
with open("numbers.txt", "r") as f:
    first_number = int(f.readline())
    second_number = int(f.readline())
    print(f"The sum of the first two numbers is {first_number + second_number}")
# printed output

#  --- part 4: sum all numbers in numbers.txt
total = 0
with open("numbers.txt", "r") as f:
    for line in f:
        total += int(line)
    print(f"The total of all numbers is {total}")
# printed output
