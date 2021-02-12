import re
f = open("input_3.txt", "r")

lines = f.read()
line_array = lines.split("\n")
total_tree_count = 1
tree_line_length = len(line_array[0])
tree_line_height = len(line_array)

def count_trees_in_slope(right_interval, down_interval):
    right_total = 0
    down_total = 0
    tree_count = 0

    while down_total < tree_line_height:
        cur_right = right_total%tree_line_length
        cur_down = down_total%tree_line_height
        if line_array[cur_down] != '' and line_array[cur_down][cur_right] == '#':
            tree_count += 1
        right_total += right_interval
        down_total += down_interval
    return tree_count

all_slopes_array = [1,1],[3,1],[5,1],[7,1],[1,2]

for x in all_slopes_array:
    total_tree_count *= count_trees_in_slope(x[0],x[1])




print(total_tree_count)