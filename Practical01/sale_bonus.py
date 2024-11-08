"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


# Get the sales amount from the user
sales = float(input("Enter the total sales amount: "))


# Calculate the bonus based on sales
if sales < 1000:
   bonus = sales * 0.10  # 10% bonus
else:
   bonus = sales * 0.15  # 15% bonus


# Display the bonus amount
print(f"Your bonus is: ${bonus:.2f}")
