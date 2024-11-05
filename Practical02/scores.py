import random




def determine_score_status(score):
   # Determine score status based on the given score
   if score < 0 or score > 100:
       return "Invalid score"
   elif score > 90:
       return "Excellent"
   elif score >= 50:
       return "Passable"
   else:
       return "Bad"




def main():
   # Get the score from the user
   score = float(input("Enter score: "))


   # Determine and print the result for the user's score
   result = determine_score_status(score)
   print(result)


   # Generate a random score and print the result
   random_score = random.randint(0, 100)  # Generate a random score between 0 and 100
   random_result = determine_score_status(random_score)
   print(f"Random score: {random_score}, Status: {random_result}")




# Call the main function
if __name__ == "__main__":
   main()
