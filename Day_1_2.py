sum_value = 2020
import re
f = open("input_1.txt", "r")

lines = f.read()
expenses = lines.split("\n")
number1 = 0
number2 = 0
number3 = 0
for x in expenses:
    for y in expenses:
        for z in expenses:
            if int(x) + int(y) + int(z) == sum_value:
                number1 = x
                number2 = y
                number3 = z
            

print(str(number1) + " " + str(number2) + " " + str(number3))
print(int(number1)*int(number2)*int(number3))