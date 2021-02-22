f = open("input_5.txt", "r")

lines = f.read()
line_array = lines.split("\n")

#Finds decimal value from string as if letter_1 has value 1, letter_0 has value 0 and string is binary.
def find_value_from_binary_string(letters, letter_1, letter_0):
    value = 0
    for x in letters:
        value = value << 1
        if x == letter_1:
            value += 1
        elif x != letter_0:
            return -1
    return value

#Finds the seat id based on seat_code
def find_seat_id(seat_code):
    id = 0
    id = find_value_from_binary_string(seat_code[0:7],"B","F")*8
    id += find_value_from_binary_string(seat_code[7:len(seat_code)],"R", "L")
    return id

#Finds the highest seat id from list of seat code entries
def find_highest_seat_id(entries):
    highest_id = -1
    for x in entries:
        id = find_seat_id(x)
        if id > highest_id:
            highest_id = id
    return highest_id

#Takes a list of entires and converts the seat codes to seat numbers then returns new list
def get_numbered_list(entries):
    entry_list = []
    for x in entries:
        entry_list.append(find_seat_id(x))
    return entry_list

#Find first place on the sorted, numbered list where there is a gap between seat numbers
def find_missing_seat_id(numbered_entries):
    prev_id = numbered_entries[0]
    for x in numbered_entries:
        if x > prev_id + 1:
            return x-1
        prev_id = x

numbered_list = get_numbered_list(line_array)
numbered_list.sort()
print(find_missing_seat_id(numbered_list))