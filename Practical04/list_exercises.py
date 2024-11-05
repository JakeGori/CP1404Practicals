def main():
   """Collect 5 numbers from the user and display information about the numbers."""
   numbers = []


   # Get 5 numbers from the user and store them in a list
   for i in range(5):
       number = float(input(f"Number {i + 1}: "))
       numbers.append(number)


   # Display information about the numbers
   print(f"The first number is {numbers[0]}")
   print(f"The last number is {numbers[-1]}")
   print(f"The smallest number is {min(numbers)}")
   print(f"The largest number is {max(numbers)}")
   print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")


   # Check user access
   usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


   username = input("Enter your username: ")
   if username in usernames:
       print("Access granted")
   else:
       print("Access denied")




main()
