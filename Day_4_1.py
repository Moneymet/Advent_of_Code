import re
f = open("input_4.txt", "r")

lines = f.read()
line_array = lines.split("\n\n")

req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
field_dict = dict()

def reset_fields():
    for x in req_fields:
        field_dict[x] = False

def check_passport(passport_entry):
    field_count_match = 0
    field_array = passport_entry.split()
    for x in field_array:
        field_parts_array = x.split(":")
        field_name = field_parts_array[0]
        #print(field_dict.get(field_name))
        if field_dict.get(field_name) != None and field_dict.get(field_name) == 0:
            field_dict.update({field_name : True})
            field_count_match += 1
            #print(field_name)
    reset_fields()
    return field_count_match == len(req_fields)

valid_passport_count = 0

reset_fields()

for x in line_array:
    if check_passport(x):
        valid_passport_count += 1
    
print(valid_passport_count)

f.close()