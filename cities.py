import csv

# Read data from CSV file
with open('cities.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    list_of_cities = [row for row in csv_reader]

# Display the list of lists
print(list_of_cities)