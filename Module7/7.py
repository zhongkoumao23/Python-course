jose_money = 15000
rich_level = 10000


def is_rich(person_money, rich_money):
    return person_money > rich_money


is_jose_rich = is_rich(jose_money, rich_level)


if is_jose_rich:
    print("yes, he is rich")
else:
    print("no, he is not")
