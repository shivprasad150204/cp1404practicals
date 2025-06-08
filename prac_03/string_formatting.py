#  string formatting example
#  use f-string formatting to produce the following output:
guitar = "Gibson L-5 CES"
year = 1922
cost = 16035.4

#  formatting the string with f-string
print(f"{year} {guitar} for about ${cost:,.0f}!")
# printed output

#  using a for loop with f-string formatting to display powers of 2
for i in range(0, 11):
    print(f"2 ^ {i:2} is {2 ** i:4}")
# printed output
