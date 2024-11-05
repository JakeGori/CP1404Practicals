class Guitar:
    """Represent a guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year):
        """Return the age of the guitar."""
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is vintage (50 years or older)."""
        return self.get_age(2022) >= 50  # Assuming the current year is 2022
