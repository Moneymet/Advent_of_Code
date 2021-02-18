sum_value = 2020
import re
f = open("input_1.txt", "r")

lines = f.read()
expenses_string = lines.split("\n")
expenses = list(map(int, expenses_string))
expenses.sort()

#Finds combination of 2 numbers in a sorted int list adding up to specified sum
def find_sum_multiplied_2(sum_value, expenses):   
    for x in expenses:
        for y in expenses[1:len(expenses)]:
            if x+y == sum_value:
                return x*y
            
multiplied_sum = find_sum_multiplied_2(sum_value, expenses)
print(multiplied_sum)