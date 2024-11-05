import random


NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45




def main():
   """Generate quick picks for lottery numbers."""
   quick_picks = int(input("How many quick picks? "))


   for _ in range(quick_picks):
       quick_pick = generate_quick_pick()
       print(" ".join(f"{num:2}" for num in sorted(quick_pick)))




def generate_quick_pick():
   """Generate a single quick pick of unique random numbers."""
   quick_pick = []
   while len(quick_pick) < NUMBERS_PER_PICK:
       number = random.randint(MIN_NUMBER, MAX_NUMBER)
       if number not in quick_pick:  # Ensure no repeated numbers
           quick_pick.append(number)
   return quick_pick




main()
