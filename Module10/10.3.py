import csv

with open("airtravel.csv") as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')
    for row in readCSV:  # how these codes arrange the data into the rows
        print(row)

