from guitar import Guitar


def main():
    """A program to manage a collection of guitars."""
    print("My guitars!")

    # Create an empty list to store guitar objects
    guitars = []

    # Input loop to gather guitar information from the user
    while True:
        name = input("Name: ")
        if not name:  # Exit the loop if the name is blank
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        # Create a Guitar object and add it to the list
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")

    # Print the details of all guitars
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i:>2}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == "__main__":
    main()
