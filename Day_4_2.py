import re
f = open("input_4.txt", "r")

lines = f.read()
line_array = lines.split("\n\n")

req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
field_dict = dict()

def reset_fields():
    for x in req_fields:
        field_dict[x] = False

def check_field(field_name, field_value):
    if field_name == "byr":
        if re.search("[1-9][0-9][0-9][0-9]", field_value) != None:
            field_value_int = int(field_value)
            return field_value_int >= 1920 and field_value_int <= 2002
    elif field_name == "iyr":
        if re.search("[1-9][0-9][0-9][0-9]", field_value) != None:
            field_value_int = int(field_value)
            return field_value_int >= 2010 and field_value_int <= 2020
    elif field_name == "eyr":
        if re.search("[1-9][0-9][0-9][0-9]", field_value) != None:
            field_value_int = int(field_value)
            return field_value_int >= 2020 and field_value_int <= 2030
    elif field_name == "hgt":
        a = 4
    return False

def check_passport(passport_entry):
    field_count_match = 0
    field_array = passport_entry.split()
    for x in field_array:
        field_parts_array = x.split(":")
        field_name = field_parts_array[0]
        field_value = field_parts_array[1]
        #print(field_dict.get(field_name))
        if field_dict.get(field_name) != None and field_dict.get(field_name) == 0 and check_field(field_name, field_value):
            field_dict.update({field_name : True})
            field_count_match += 1
    reset_fields()
    return field_count_match == len(req_fields)

valid_passport_count = 0

reset_fields()

for x in line_array:
    if check_passport(x):
        valid_passport_count += 1
    
print(valid_passport_count)

f.close()