import random


MAX_INCREASE = 0.175  # 17.5% increase
MAX_DECREASE = 0.05   # 5% decrease
MIN_PRICE = 1.0       # Minimum price is $1.00
MAX_PRICE = 100.0     # Maximum price is $100.00
INITIAL_PRICE = 10.0  # Starting price
FILENAME = "output.txt"


price = INITIAL_PRICE
number_of_days = 0


# Open the file for writing
out_file = open(FILENAME, 'w')


# Write the starting price to the file and console
print(f"Starting price: ${price:,.2f}")
print(f"Starting price: ${price:,.2f}", file=out_file)


while MIN_PRICE <= price <= MAX_PRICE:
   price_change = 0
   number_of_days += 1


   # Randomly decide if the price increases or decreases
   if random.randint(1, 2) == 1:
       price_change = random.uniform(0, MAX_INCREASE)  # Increase by up to MAX_INCREASE
   else:
       price_change = random.uniform(-MAX_DECREASE, 0)  # Decrease by up to MAX_DECREASE


   # Update the price
   price *= (1 + price_change)


   # Print the updated price with the day count both to the file and console
   print(f"On day {number_of_days} price is: ${price:,.2f}")
   print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)


# Close the file after the loop
out_file.close()


print(f"Simulation finished after {number_of_days} days. Output written to {FILENAME}.")
