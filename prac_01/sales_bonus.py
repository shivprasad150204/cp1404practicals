"""
CP1404/CP5632 - Practical
Sales bonus program
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print(f"Bonus is ${bonus:.2f}")
    sales = float(input("Enter sales: $"))

print("Invalid sales amount. Exiting.")
