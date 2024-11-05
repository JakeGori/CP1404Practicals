"""
Hexadecimal Colour Lookup
"""


# Constant dictionary of colour names and their hex codes
COLOR_NAMES = {
   "ABSOLUTE_ZERO": "#0048ba",
   "BLACK_COFFEE": "#3b2f2f",
   "BLUE2": "#0000ee",
   "BRICK_RED": "#cb4154",
   "BROWN2": "#ee3b3b",
   "BYZANTINE": "#bd33a4",
   "CADETBLUE1": "#98f5ff",
   "CITRINE": "#e4d00a",
   "CORAL1": "#ff7256",
   "DARKORANGE2": "#ee7600"
}


print("Welcome to the Hexadecimal Colour Lookup!")
print("Enter a color name to get its hex code. Press Enter to exit.")


# Loop for user input
while True:
   color_name = input("Enter a color name: ").strip()  # Remove leading/trailing whitespace
   if color_name == "":
       break  # Exit the loop if input is blank


   # Convert input to uppercase to handle case insensitivity
   color_name_upper = color_name.upper()


   # Look up the color name in the dictionary
   if color_name_upper in COLOR_NAMES:
       print(f"{color_name} has the hex code {COLOR_NAMES[color_name_upper]}")
   else:
       print("Invalid color name. Please try again.")
