def sum_expenses(production, accounting):
    year = 2
    result1 = (production * year + accounting * year)
    return result1


def production_value(number):
    return number


def accounting_value(number):
    return number


final_value = sum_expenses(production_value(20), accounting_value(5))
print(final_value)

print("Hello{}, your account has a balance of {} to repay {} {} debt.".format("jack", 1500, "Ben", 1500))

print("your account has a balance of{}, Hello {}".format(1500, "Jack"))

print("one piece of {}, adding {}, another piece of {}".format("cake", "sugar", "ham"))

print("{x1}, adding {x2}, {x3}".format(x1="one piece of cake", x2="2 sugar", x3="another piece of cake"))


def product_two_numbers(number1, number2):
    result2 = number1 * number2
    return result2


initial_number1 = 6
initial_number2 = 5
resulting_product = product_two_numbers(intial_number1, intial_number2)
print("The product of {} which are working hours and {} which is wage rate is {}".format(initial_number1,
                                                                                         initial_number2,
                                                                                         resulting_product))

if resulting_product < 0:
    print("negative")
elif resulting_product > 100:
    print("not reasonable")
else:
    print(resulting_product)


def sum_two_numbers(number3, number4):
    result3 = number3 + number4
    return result3


initial_number3 = 4
initial_number4 = 3
resulting_sum = sum_two_numbers(initial_number3, initial_number4)
print(
    "The sum of {} which is depreciation/unit/machine and {} which is raw material/unit is {}".format(initial_number3,
                                                                                                      initial_number4,
                                                                                                      resulting_sum))
# can you keep the name of number 3 and number 4, for example the sum of number3 and number4 is 7 instead of 4 and 3


if resulting_sum < 0:
    print("negative")
elif resulting_sum > 10:
    print("not reasonable")
else:
    print(resulting_sum)


def sum_cost(cost_sum, cost_product):
    result4 = cost_sum + cost_product
    return result4


final_cost = sum_cost(resulting_sum, resulting_product)
print("The total cost per day is {} + {} which is the sum of dead part and labour part".format(resulting_product,
                                                                                               resulting_sum, sum_cost))
