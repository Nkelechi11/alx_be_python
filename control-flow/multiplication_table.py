number = int(input(" Enter a number to see its multiplication table: "))

for input in range(1,11):
    result = number * input
    print(number, '*', input, "=", result)
    # print(number, '*', input, "=", number*input)


