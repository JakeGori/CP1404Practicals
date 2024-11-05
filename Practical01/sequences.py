def display_menu():
   print("Menu:")
   print("1. Show the even numbers from x to y")
   print("2. Show the odd numbers from x to y")
   print("3. Show the squares of the numbers from x to y")
   print("4. Exit the program")




# Get inputs for x and y
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))


# Display the menu and get user's choice
display_menu()
choice = input("Enter your choice (1-4): ")


while choice != '4':  # Loop until the user chooses to exit
   if choice == '1':
       print(f"Even numbers from {x} to {y}:")
       for i in range(x, y + 1):
           if i % 2 == 0:
               print(i, end=' ')
       print()  # For a new line after the numbers


   elif choice == '2':
       print(f"Odd numbers from {x} to {y}:")
       for i in range(x, y + 1):
           if i % 2 != 0:
               print(i, end=' ')
       print()


   elif choice == '3':
       print(f"Squares of numbers from {x} to {y}:")
       for i in range(x, y + 1):
           print(i ** 2, end=' ')
       print()


   else:
       print("Invalid choice, please select from the menu.")


   # Display the menu again and get the next choice
   display_menu()
   choice = input("Enter your choice (1-4): ")


print("Exiting the program. Goodbye!")
