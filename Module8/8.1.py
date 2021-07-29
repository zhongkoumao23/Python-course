companies = [{"name": "Tencent", "volume": 1000, "stock price": 120, "market value": 3000000},
             {"name": "JD", "volume": 2000, "stock price": 100, "market value": 1000000},
             {"name": "Riot", "volume": 3000, "stock price": 150, "market value": 2000000},
             {"name": "TB", "volume": 4000, "stock price": 200, "market value": 4000000}]

sum_volume = 0


def volume_limit():
    return 2000


vlimit = volume_limit()

for company in companies:
    # sum_volume = company["volume"] + sum_volume
    stock_price = company["stock price"]
    volume_number = company["volume"]
    market_value = company["market value"]

    # if volume_number > vlimit:
    # print(company["name"])

    if volume_number > 1000 and stock_price > 120 and market_value > 1000000:

        # print(company["name"])
        # what if i want two results to be represented at the same time name and stock price
        # print(company["stock price"])

        print("the company is {} and its stock price is {}".format(company["name"], company["stock price"]))


# avg = sum_volume / len(companies)
# print(avg)
