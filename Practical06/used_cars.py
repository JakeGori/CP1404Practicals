from Practical06.car import Car

def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, "My Car")
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    # Create a new Car object called "limo" that is initialized with 100 units of fuel
    limo = Car(100, "Limo")  # Add name during initialization

    # Add 20 more units of fuel to this new car object using the add method
    limo.add_fuel(20)

    # Print the amount of fuel in the car
    print(f"Limo has fuel: {limo.fuel}")

    # Attempt to drive the car 115 km using the drive method
    distance_driven = limo.drive(115)
    print(f"Limo drove: {distance_driven} km")

    # Print the limo object to see the __str__ method in action
    print(limo)


main()
