sum_value = 2020
f = open("input_1.txt", "r")

lines = f.read()
expenses_string = lines.split("\n")
expenses = list(map(int, expenses_string))
expenses.sort()

#Finds combination of 3 numbers in a sorted int list adding up to specified sum
def find_sum_multiplied_3(sum_value, expenses):
    for x in expenses:
        for y in expenses[1:len(expenses)]:
            #Skips checking z values if the sum of the first and second number is too high to possibly find a low enough third value
            if x + y < sum_value-expenses[0]:
                for z in expenses[2:len(expenses)]:
                    if x+y+z == sum_value:
                        return x*y*z

multiplied_sum = find_sum_multiplied_3(sum_value, expenses)
print(multiplied_sum)