try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print(f"The result is {result}")
# printed output
except ZeroDivisionError:
    print("Cannot divide by zero!")
# printed output
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# printed output
#  1. a valueerror will occur when the input is not an integer.
#  2. a zerodivisionerror occurs when the denominator is zero.
#  3. yes, we can avoid the zerodivisionerror by adding a condition before division.
