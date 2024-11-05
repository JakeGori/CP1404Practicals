# files.py


# Task 1: Ask for a name and write it to a file
name = input("Enter your name: ")
with open('name.txt', 'w') as name_file:
   name_file.write(name)  # Write the name to the file


# Task 2: Read the name from the file and greet the user
with open('name.txt', 'r') as name_file:
   name_from_file = name_file.readline().strip()  # Read the name and remove any extra whitespace
print(f"Hi {name_from_file}!")  # Print the greeting with the name from the file


# Task 3: Create a text file 'numbers.txt' with numbers
with open('numbers.txt', 'w') as numbers_file:
   numbers_file.write("17\n")
   numbers_file.write("42\n")
   numbers_file.write("400\n")


# Read the first two numbers from numbers.txt and print their sum
with open('numbers.txt', 'r') as numbers_file:
   first_number = int(numbers_file.readline().strip())  # Read the first number
   second_number = int(numbers_file.readline().strip())  # Read the second number
   total = first_number + second_number
   print(total)  # Should print 59


# Task 4: Print the total for all numbers in numbers.txt
with open('numbers.txt', 'r') as numbers_file:
   total_all = 0
   for line in numbers_file:  # Iterate through each line in the file
       total_all += int(line.strip())  # Convert to int and add to the total
   print(total_all)  # Print the total of all numbers
