# Program to determine score status


# Get the score from the user
score = float(input("Enter score: "))


# Determine score status
if score < 0 or score > 100:
   print("Invalid score")
elif score > 90:
   print("Excellent")
elif score >= 50:
   print("Passable")
else:
   print("Bad")
