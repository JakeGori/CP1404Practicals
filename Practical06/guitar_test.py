from guitar import Guitar

def main():
    """Test the Guitar class methods."""
    # Create guitar instances for testing
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 500.00)

    # Test get_age() method
    expected_age_guitar1 = 100
    actual_age_guitar1 = guitar1.get_age(2022)
    print(f"{guitar1.name} get_age() - Expected {expected_age_guitar1}. Got {actual_age_guitar1}")

    expected_age_guitar2 = 9
    actual_age_guitar2 = guitar2.get_age(2022)
    print(f"{guitar2.name} get_age() - Expected {expected_age_guitar2}. Got {actual_age_guitar2}")

    # Test is_vintage() method
    expected_vintage_guitar1 = True
    actual_vintage_guitar1 = guitar1.is_vintage()
    print(f"{guitar1.name} is_vintage() - Expected {expected_vintage_guitar1}. Got {actual_vintage_guitar1}")

    expected_vintage_guitar2 = False
    actual_vintage_guitar2 = guitar2.is_vintage()
    print(f"{guitar2.name} is_vintage() - Expected {expected_vintage_guitar2}. Got {actual_vintage_guitar2}")

if __name__ == "__main__":
    main()
