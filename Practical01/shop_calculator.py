# Get the number of items from the user
# num_items = int(input("Enter the number of items: "))
#
# # Initialize the total price
# total_price = 0
#
# # Get the price of each item and add it to the total price
# for i in range(num_items):
#     price = float(input(f"Enter the price of item {i + 1}: "))
#     total_price += price
#
# # Check if a discount should be applied
# if total_price > 100:
#     discount = total_price * 0.10  # 10% discount
#     total_price -= discount
#     print(f"A 10% discount of ${discount:.2f} has been applied.")
#
# # Display the total price
# print(f"The total price is: ${total_price:.2f}")


# Get the number of items from the user with validation
num_items = int(input("Enter the number of items: "))
while num_items < 0:
   print("Invalid number of items!")
   num_items = int(input("Please enter a valid number of items: "))


# Initialize the total price
total_price = 0


# Get the price of each item and add it to the total price
for i in range(num_items):
   price = float(input(f"Enter the price of item {i + 1}: "))
   total_price += price


# Check if a discount should be applied
if total_price > 100:
   discount = total_price * 0.10  # 10% discount
   total_price -= discount
   print(f"A 10% discount of ${discount:.2f} has been applied.")


# Display the total price
print(f"The total price is: ${total_price:.2f}")
