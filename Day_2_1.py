import re
f = open("input_2.txt", "r")

lines = f.read()
line_array = lines.split("\n")
valid_count = 0

for x in line_array:
    #print(x)
    word_array = x.split(" ")
    if len(word_array) >= 3:
        word_numbers = word_array[0].split("-")
        min_num = int(word_numbers[0])
        max_num = int(word_numbers[1])

        repeat_letter = word_array[1].replace(':', '')

        repeat_letter_amount = len(re.findall(repeat_letter, word_array[2]))
        if repeat_letter_amount >= min_num and repeat_letter_amount <= max_num:
            valid_count += 1

print(valid_count)

f.close()