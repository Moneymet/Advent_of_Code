import re
f = open("input_8.txt", "r")

lines = f.read()
line_array = lines.split("\n")

#Dictionary for lines. Used to both check if in a loop and each value refers to the key of the previous line.
line_number_dict = dict()

#Remembers index of the last line executed
last_line_number = -1

def flip(line):
    return (line.replace("nop","jmp"), line.replace("jmp","nop"))["jmp" in line]

def execute_lines(execution_line_array):
    acc = 0
    current_line_number = 0
    prev_line_number = -1
    #Clean dictionary
    line_number_dict.clear()
    #While loop as long as command hasn't been repeated
    while(line_number_dict.get(current_line_number) == None):

        #Enters current line number as used
        line_number_dict[current_line_number] = prev_line_number
        prev_line_number = current_line_number
        current_line = execution_line_array[current_line_number]

        #Extracts the line information
        instruction_command = re.search("[a-z]{3}", current_line).group()
        is_number_positive = re.search("\\+{1}", current_line) != None
        instruction_number = int(re.search("[0-9]+", current_line).group())

        #Registers current line number as the last
        #Using global doesn't feel right, but it will do
        global last_line_number
        last_line_number = current_line_number

        #Either jumps or increments line number once
        if instruction_command == "jmp":
            current_line_number += instruction_number*(-1, 1)[is_number_positive]
        else:
            if instruction_command == "acc":
                acc += instruction_number*(-1, 1)[is_number_positive]
            current_line_number += 1

        if current_line_number > len(execution_line_array)-1:
            return acc

    return None

#Fixes the code by finding the infinite loop and one by one changing the commands in reverse chronological order
#Returns acc if solution is found
def fix_incorrect_command(execution_line_array):
    #Executes the "program" once to find infinite loop, where it happened, and history of commands
    execute_lines(execution_line_array)
    #Copies the
    cur_line_focus = last_line_number
    while cur_line_focus > -1:
        #Flips the current focus command
        execution_line_array[cur_line_focus] = flip(execution_line_array[cur_line_focus])
        #Tries executing with the new flip
        execute_value = execute_lines(execution_line_array)
        if execute_value != None:
            return execute_value
        #Flips the current focus command back, restoring the dictionary to its original form
        execution_line_array[cur_line_focus] = flip(execution_line_array[cur_line_focus])
        cur_line_focus = line_number_dict[cur_line_focus]

    return None

cur_acc = fix_incorrect_command(line_array)
print(cur_acc)
    