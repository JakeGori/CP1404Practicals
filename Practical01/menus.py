# Get the user's name
name = input("Enter name: ")


# Display the menu options
def display_menu():
   print("(H)ello")
   print("(G)oodbye")
   print("(Q)uit")


# Display the menu and get the user's choice
display_menu()
choice = input(">>> ").upper()  # Make choice case-insensitive


# Menu loop until the user chooses to quit
while choice != 'Q':
   if choice == 'H':
       print(f"Hello {name}")
   elif choice == 'G':
       print(f"Goodbye {name}")
   else:
       print("Invalid choice")


   # Display the menu again and get the next choice
   display_menu()
   choice = input(">>> ").upper()


# When the user chooses to quit
print("Finished.")
