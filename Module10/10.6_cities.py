import csv


def get_latd_data(data, city, latd):
    for line in data:
        if line["City"] == city:
            return line[latd]


def get_city_data(data, city):
    for line in data:
        if line["City"] == city:
            return line


def get_file_content(file_name):
    with open(file_name) as csv_file:
        file_reader = csv.DictReader(csv_file, delimiter=',')
        result = []
        for line in file_reader:
            result.append(line)
    return result


file_content = get_file_content("cities.csv")

# data = get_latd_data(file_content, "Ravenna", "LatD")
data = get_city_data(file_content,  "Ravenna")

print(data["LatD"])

#  now it is single what about mutiple cases if i want search lonm and latd and so on in one model through cities
