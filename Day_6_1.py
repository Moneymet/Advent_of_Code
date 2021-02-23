import re
f = open("input_6.txt", "r")

lines = f.read()
line_array = lines.split("\n\n")
#line_array = list(map(str.split("\n"), line_array))
line_index = 0
for x in line_array:
    line_array[line_index] = x.split("\n")
    line_index += 1


def answer_count_group(group_answer):
    count = 0
    answer_array = dict()
    for x in group_answer:
        for y in x:
            if re.search("[a-z]", y) != None:
                answer_array[y] = True

    for x in map(chr, range(97, 123)):
        if x in answer_array:
            count += 1
    return count

def answer_count_total(all_answers):
    total_count = 0
    for x in all_answers:
        total_count += answer_count_group(x)    
    return total_count

print(str(answer_count_total(line_array)))