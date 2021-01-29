number = input("Enter Number")
for value in range(1,11):
    multiply = value * int(number)
    line = str(number) + " X " + str(value) + " = " + str(multiply)
    print(line)