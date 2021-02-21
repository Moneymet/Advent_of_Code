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

print(find_highest_seat_id(line_array))
