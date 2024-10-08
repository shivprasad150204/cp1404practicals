import random

# Line 1
print(random.randint(5, 20))  # random integer between 5 and 20 (inclusive)

# Line 2
print(random.randrange(3, 10, 2))  # random odd integer between 3 and 9 (3, 5, 7, 9)

# Line 3
print(random.uniform(2.5, 5.5))  # random float between 2.5 and 5.5

# Answers to the questions:

# Line 1: Produces a random integer between 5 and 20 (inclusive).
# Smallest number: 5, Largest number: 20

# Line 2: Produces a random number from the sequence [3, 5, 7, 9].
# Smallest number: 3, Largest number: 9
# No, it cannot produce a 4 because the step is 2, so only odd numbers are generated.

# Line 3: Produces a random float between 2.5 and 5.5.
# Smallest possible number: 2.5, Largest possible number: 5.5

# Random number between 1 and 100 inclusive
random_number = random.randint(1, 100)
print(random_number)
