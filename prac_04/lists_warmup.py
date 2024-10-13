# Initial list
numbers = [3, 1, 4, 1, 5, 9, 2]

# Predictions for expressions
# numbers[0] -> 3
# numbers[-1] -> 2
# numbers[3] -> 1
# numbers[:-1] -> [3, 1, 4, 1, 5, 9]
# numbers[3:4] -> [1]
# 5 in numbers -> True
# 7 in numbers -> False
# "3" in numbers -> False (because "3" is a string, not an integer)
# numbers + [6, 5, 3] -> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Now, running the code to verify:
print(numbers[0])  # 3
print(numbers[-1])  # 2
print(numbers[3])  # 1
print(numbers[:-1])  # [3, 1, 4, 1, 5, 9]
print(numbers[3:4])  # [1]
print(5 in numbers)  # True
print(7 in numbers)  # False
print("3" in numbers)  # False
print(numbers + [6, 5, 3])  # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Tasks:
# Change the first element of numbers to "ten" (the string)
numbers[0] = "ten"

# Change the last element of numbers to 1
numbers[-1] = 1

# Print all elements except the first two (slice)
print(numbers[2:])

# Print whether 9 is an element of numbers
print(9 in numbers)
