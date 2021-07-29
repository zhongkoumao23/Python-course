count = 0
while count < 3:
    count = count + 1
    print("An iteration")
else:
    print("In Else Block")

a_list = [11, 2, 3, 4, 5]
# what if i want to search 11 out of so many numbers to know what type it is acc expenses
# or market expenses
for element in a_list:
    if element % 2 == 0:
        print("{} Even number".format(element))
    else:
        print("{} Odd number".format(element))
