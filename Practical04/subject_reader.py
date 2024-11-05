FILENAME = "subject_data.txt"




def main():
   """Load subject data and display it."""
   data = load_data()  # Load data from the file as a list of lists
   display_subject_details(data)  # Display the subject details in a formatted manner




def load_data():
   """Read data from file formatted like: subject,lecturer,number of students and return it as a list of lists."""
   subject_data = []
   with open(FILENAME) as input_file:
       for line in input_file:
           line = line.strip()  # Remove any leading/trailing whitespace including newline
           parts = line.split(',')  # Split the line by commas into a list of parts
           parts[2] = int(parts[2])  # Convert the number of students from string to integer
           subject_data.append(parts)  # Add the list of parts to the overall data list
   return subject_data




def display_subject_details(subject_data):
   """Display subject details in a nicely formatted way."""
   for subject in subject_data:
       subject_code, lecturer, number_of_students = subject
       print(f"{subject_code} is taught by {lecturer} and has {number_of_students} students")




main()
