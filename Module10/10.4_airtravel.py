import csv


def get_month_data(data, month, year):
    for line in data:
        print(line)
        if line["Month"] == month:
            return line[year]


def get_file_content(file_name):
    with open(file_name) as csv_file:
        file_reader = csv.DictReader(csv_file, delimiter=',')
        result = []
        for line in file_reader:
            result.append(line)
    return result


file_content = get_file_content("airtravel.csv")
month_data = get_month_data(file_content, "DEC", "1959")
print(month_data)

# row = get_month_row("JUL", file_data)
# print(row[3])  # what does the 622 means?
