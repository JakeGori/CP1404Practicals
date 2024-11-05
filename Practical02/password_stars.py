# Set minimum length requirement
MIN_LENGTH = 8


def main():
   # Get a valid password
   password = get_password()


   # Print asterisks matching the length of the password
   print_asterisks(password)


def get_password():
   # Ask the user for a password and repeat until the password meets the minimum length
   password = input("Enter a password: ")
   while len(password) < MIN_LENGTH:
       print(f"Password must be at least {MIN_LENGTH} characters long.")
       password = input("Enter a password: ")
   return password


def print_asterisks(password):
   # Print asterisks matching the length of the password
   print("*" * len(password))


# Call the main function
if __name__ == "__main__":
   main()
