import re
f = open("input_8.txt", "r")

lines = f.read()
line_array = lines.split("\n")

acc = 0

line_number_dict = dict()
current_line_number = 0

#While loop as long as command hasn't been repeated
while(line_number_dict.get(current_line_number) == None):
    #Enters current line number as used
    line_number_dict[current_line_number] = True
    current_line = line_array[current_line_number]

    #Extracts the line information
    instruction_command = re.search("[a-z]{3}", current_line).group()
    is_number_positive = re.search("\\+{1}", current_line) != None
    instruction_number = int(re.search("[0-9]+", current_line).group())

    #Either jumps or increments line number once
    if instruction_command == "jmp":
        current_line_number += instruction_number*(-1, 1)[is_number_positive]
    else:
        if instruction_command == "acc":
            acc += instruction_number*(-1, 1)[is_number_positive]
        current_line_number += 1
print(acc)
    