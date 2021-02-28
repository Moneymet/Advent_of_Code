import re
f = open("input_6.txt", "r")

lines = f.read()
line_array = lines.split("\n\n")
line_index = 0
for x in line_array:
    line_array[line_index] = x.split("\n")
    line_index += 1


def answer_count_group(group_answer):
    count = 0
    answer_array = dict()

    #States for answer
    #DISQUALIFIED means that the answer letter has not appeared in at least one previous answer and will not be counted
    #NOT_ANSWERED means that the answer letter has not appeared in yet in this answer, turns into DISQUALIFIED if answer doesn't contain letter
    #ANSWERED means that the answer letter appears in the current answer
    class AnswerStates:
        DISQUALIFIED = 0 
        NOT_ANSWERED = 1
        ANSWERED = 2

    for x in group_answer:

        #Turns all non-disqualified answers into NOT_ANSWERED
        for y in map(chr, range(97, 123)):
            if answer_array.get(y) != AnswerStates.DISQUALIFIED:
                answer_array[y] = AnswerStates.NOT_ANSWERED

        #Records letter as answered if not yet disqualified
        for y in x:
            if re.search("[a-z]", y) != None and answer_array.get(y) != AnswerStates.DISQUALIFIED:
                answer_array[y] = AnswerStates.ANSWERED

        #Disqualifies unanswered questions
        for y in map(chr, range(97, 123)):
            if answer_array.get(y) != AnswerStates.ANSWERED:
                answer_array[y] = AnswerStates.DISQUALIFIED

    #Counts groups total letter count
    for x in map(chr, range(97, 123)):
        if x in answer_array:
            if answer_array.get(x) == AnswerStates.ANSWERED:
                count += 1
    return count

def answer_count_total(all_answers):
    total_count = 0
    for x in all_answers:
        total_count += answer_count_group(x)    
    return total_count

print(str(answer_count_total(line_array)))