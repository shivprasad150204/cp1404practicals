# Random number module
import random

MAX_INCREASE = 0.175  #  17.5%
MAX_DECREASE = 0.05  #  5%
MIN_PRICE = 1.00
MAX_PRICE = 100.00
INITIAL_PRICE = 10.00

stock_price = INITIAL_PRICE
number_of_days = 0
OUTPUT_FILE = "stock_prices.txt"

#  opening the output f
out_file = open(OUTPUT_FILE, 'w')

#  print the starting stock_price
print(f"Starting stock_price: ${stock_price:,.2f}", f=out_file)

#  simulate the stock stock_price changes
while MIN_PRICE <= stock_price <= MAX_PRICE:
    price_change = 0
    number_of_days += 1
    #  randomly decide if the stock_price goes up or down
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = -random.uniform(0, MAX_DECREASE)

    #  update the stock_price
    stock_price *= (1 + price_change)
    print(f"On day {number_of_days} stock_price is: ${stock_price:,.2f}", f=out_file)

#  closing the f
out_file.close()
