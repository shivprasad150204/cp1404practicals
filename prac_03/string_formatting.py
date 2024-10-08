# Given details
name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

# Task 1: Use f-string formatting to produce this output:
# "1922 Gibson L-5 CES for about $16,036!"
print(f"{year} {name} for about ${cost:,.0f}!")

# Task 2: Using a for loop with the range function and f-string formatting,
# produce the right-aligned output
for i in range(11):  # Generates numbers from 0 to 10
    print(f"2 ^ {i:2} is {2**i:4}")
