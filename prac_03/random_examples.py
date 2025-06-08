# Random number module
import random

#  line 1: generate a random integer between 5 and 20
print(random.randint(5, 20))

#  line 2: generate a random odd integer between 3 and 9
print(random.randrange(3, 10, 2))

#  line 3: generate a random float between 2.5 and 5.5
print(random.uniform(2.5, 5.5))
#  1. the smallest number on line 1 could be 5, the largest 20.
#  2. the smallest number on line 2 could be 3, the largest 9, and no, line 2 could not have produced a 4.
#  3. the smallest number on line 3 could be 2.5, the largest 5.5.

#  producing a random number between 1 and 100 inclusive:
print(random.randint(1, 100))
