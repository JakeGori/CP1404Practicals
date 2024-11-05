def celsius_to_fahrenheit(celsius):
   # Convert Celsius to Fahrenheit
   return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
   # Convert Fahrenheit to Celsius
   return (fahrenheit - 32) * 5/9


def main():
   # Get user input for Celsius to Fahrenheit conversion
   celsius = float(input("Enter temperature in Celsius: "))
   fahrenheit = celsius_to_fahrenheit(celsius)
   print(f"{celsius}°C is {fahrenheit}°F")


   # Get user input for Fahrenheit to Celsius conversion
   fahrenheit = float(input("Enter temperature in Fahrenheit: "))
   celsius = fahrenheit_to_celsius(fahrenheit)
   print(f"{fahrenheit}°F is {celsius}°C")


# Call the main function
if __name__ == "__main__":
   main()
