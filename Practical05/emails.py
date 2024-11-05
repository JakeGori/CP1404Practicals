"""
Email Storage Program
Estimate time: 30 minutes
"""




def extract_name(email):
   """Extract the name from the email address."""
   # Split the email by the '@' character and take the first part
   name_part = email.split('@')[0]
   # Replace dots with spaces and capitalize each word
   name = name_part.replace('.', ' ').title()
   return name




def main():
   """Main function to run the email storage program."""
   email_dict = {}


   while True:
       email = input("Email: ").strip()  # Get email input from user


       if email == "":  # Exit if input is blank
           break


       name = extract_name(email)  # Extract the name from the email
       confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()  # Confirm the name


       if confirm != "" and confirm != "y":  # If not confirmed, ask for name
           name = input("Name: ").strip()


       # Store the email and name in the dictionary
       email_dict[email] = name


   # Print all email-name pairs from the dictionary
   print("\nEmail List:")
   for email, name in email_dict.items():
       print(f"{name} ({email})")




if __name__ == "__main__":
   main()
