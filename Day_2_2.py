import re
f = open("input_2.txt", "r")

lines = f.read()
line_array = lines.split("\n")
valid_count = 0

for x in line_array:
    word_array = x.split(" ")
    if len(word_array) >= 3:
        word_numbers = word_array[0].split("-")
        first_pos = int(word_numbers[0])-1
        last_pos = int(word_numbers[1])-1

        first_pos_letter = word_array[2][first_pos]
        last_pos_letter = word_array[2][last_pos]

        repeat_letter = word_array[1].replace(':', '')

        if repeat_letter == first_pos_letter and repeat_letter != last_pos_letter or repeat_letter != first_pos_letter and repeat_letter == last_pos_letter:
            valid_count += 1

print(valid_count)

f.close()