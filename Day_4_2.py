import re
f = open("input_4.txt", "r")

lines = f.read()
line_array = lines.split("\n\n")

req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
field_dict = dict()
possible_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

#Resets fields for dict, might be unnecessary if a new dict were to be created each time check_passport is called
def reset_fields():
    for x in req_fields:
        field_dict[x] = False

#Returns True if field value is valid for field name
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
        if re.search("\\d+cm", field_value) != None:
            field_value_int = int(re.search("\\d+", field_value)[0])
            return field_value_int >= 150 and field_value_int <= 193
        if re.search("\\d+in", field_value) != None:
            field_value_int = int(re.search("\\d+", field_value)[0])
            return field_value_int >= 59 and field_value_int <= 76
    elif field_name == "hcl":
        if re.search("#([0-9]|[a-f]){6}", field_value) != None:
            return True
    elif field_name == "ecl":
        for x in possible_eye_colors:
            if x == field_value:
                return True
    elif field_name == "pid":
        if re.search("^[0-9]{9}$", field_value) != None:
            return True

    return False

#Returns True if the required fields are valid for passport
def check_passport(passport_entry):
    #Counter for valid fields
    field_count_match = 0
    field_array = passport_entry.split()
    #Goes through each field of an entry
    for x in field_array:
        field_parts_array = x.split(":")
        field_name = field_parts_array[0]
        field_value = field_parts_array[1]
        #Counts up 1 if the current field is valid and field name not already tried for this entry
        if field_dict.get(field_name) != None and check_field(field_name, field_value):
            #Sets field name as counted
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