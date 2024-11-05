"""
Wimbledon Champions Data Processing
Estimate time: 45 minutes
"""


import csv


def read_wimbledon_data(filename):
   """Read the Wimbledon data from a CSV file and return a list of lists."""
   with open(filename, "r", encoding="utf-8-sig") as in_file:
       reader = csv.reader(in_file)
       # Skip the header row
       next(reader)
       return [row for row in reader]


def count_champions(data):
   """Count the number of times each champion has won."""
   champions_count = {}
   for row in data:
       champion = row[2]  # Champion is in the third column
       if champion in champions_count:
           champions_count[champion] += 1
       else:
           champions_count[champion] = 1
   return champions_count


def get_unique_countries(data):
   """Get a sorted set of unique countries from the champions."""
   countries = set()
   for row in data:
       country = row[1]  # Country is in the second column
       countries.add(country)
   return sorted(countries)


def display_results(champions_count, countries):
   """Display the results of champions and countries."""
   print("Wimbledon Champions:")
   for champion, count in champions_count.items():
       print(f"{champion} {count}")


   print(f"\nThese {len(countries)} countries have won Wimbledon: ")
   print(", ".join(countries))


def main():
   """Main function to run the program."""
   filename = "wimbledon.csv"  # Ensure the CSV file is in the same directory
   data = read_wimbledon_data(filename)
   champions_count = count_champions(data)
   countries = get_unique_countries(data)
   display_results(champions_count, countries)


if __name__ == "__main__":
   main()
