sum_value = 2020
import re
f = open("input_1.txt", "r")

lines = f.read()
expenses = lines.split("\n")
number1 = 0
number2 = 0
for x in expenses:
    for  y in expenses:
        if int(x) + int(y) == sum_value:
            number1 = x
            number2 = y
        #print(x + y)
            

print(str(number1) + " " + str(number2))
print(int(number1)*int(number2))