import csv


def get_age_data(data, name, age):  # any ways to lower case all of them instead mannually change
    for line in data:
        print(line)
        if line["Name"] == name:
            return line[age]


def get_file_content(file_name):
    with open(file_name) as csv_file:
        file_reader = csv.DictReader(csv_file, delimiter=',')
        result = []
        for line in file_reader:
            result.append(line)
    return result


file_content = get_file_content("biostats.csv")

age_data = get_age_data(file_content, "Ruth", "Age")
print(age_data)
