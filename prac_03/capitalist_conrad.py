import random

MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0

price = INITIAL_PRICE
print(f"${price:,.2f}")  # Display the initial price

while MIN_PRICE <= price <= MAX_PRICE:
    # Determine if the price will increase or decrease
    if random.randint(1, 2) == 1:
        # Randomly increase the price by up to MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # Randomly decrease the price by up to MAX_DECREASE
        price_change = random.uniform(-MAX_DECREASE, 0)

    # Update the price based on the change
    price *= (1 + price_change)
    # Display the new price rounded to 2 decimal places
    print(f"${price:,.2f}")
