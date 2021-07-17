def sum_expenses(production, accounting):
    year = 2
    result = (production * year + accounting * year )
    return result


def production_value(number):
    return number


def accounting_value(number):
    return number


final_value = sum_expenses(production_value(20), accounting_value(5))
print(final_value)
