def multi_inputs(number1, number2):
    return number1 * number2


input_number_1 = int(input("Enter value of x:"))
input_number_2 = int(input("Enter value of y:"))

product_multi = multi_inputs(input_number_1, input_number_2)
print("The product of x * y is {}".format(product_multi))
