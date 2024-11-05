"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""


try:
   numerator = int(input("Enter the numerator: "))
   denominator = int(input("Enter the denominator: "))


   # Ensure denominator is not zero
   while denominator == 0:
       print("Denominator cannot be zero! Please enter a valid number.")
       denominator = int(input("Enter the denominator: "))


   # Perform the division after validation
   fraction = numerator / denominator
   print(f"The result is: {fraction}")


except ValueError:
   print("Numerator and denominator must be valid numbers!")


print("Finished.")
