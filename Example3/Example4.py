def sum_ages(person1, person2):
    year = 1
    result = (person1 * year) + (person2 * year)
    return result


def person1_value(age):
    return age


def person2_value(age):
    return age


final_age = sum_ages(person1_value(45), person2_value(45))
print(final_age)
