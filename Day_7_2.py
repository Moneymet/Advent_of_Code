import re
f = open("input_7.txt", "r")

lines = f.read()
line_array = lines.split("\n")

#Key-Value dictionaries for bags names and bags objects in tree
tree_dict = dict()
counted_tree_dict = dict()

class BagTree:

    def __init__(self, name, parent_node):
        self.name = name
        self.parent_nodes = list()
        self.branches = list()
        self.amount_dict = dict()
        self.add_parent(parent_node)

    def add_branch(self, branch, amount):
        self.branches.append(branch)
        self.amount_dict[branch.name] = amount

    def add_parent(self, parent_node):
        if parent_node != None:
            self.parent_nodes.append(parent_node)

    def get_branch_by_name(self, branch_name):
        for x in self.branches:
            if x.name == branch_name:
                return x
        return None

    def __str__(self):
        return_string = "Name:\n"
        return_string += self.name + "\n"
        return_string += "Branches:\n"
        for x in self.branches:
            return_string += str(self.amount_dict[x.name]) + " " + x.name + "\n"
        return_string += "Parent branches:\n"
        #"Empty" lists only have a single None for some reason and I have no idea if that is how it's supposed to be
        if self.parent_nodes[0] != None:
            for x in self.parent_nodes:
                return_string += x.name + "\n"
        return return_string

def add_entry_to_tree(entry_line):
    #Finds name of bag in question
    bag_name = re.search(r'^[a-z]+ [a-z]+', entry_line).group()

    #Creates list of all bags contained in current bag
    contained_bags = re.findall(r'[0-9] [a-z]+ [a-z]+', entry_line)

    #Tries to get bag node
    bag_node = tree_dict.get(bag_name)

    #Creates new bag node if not made before
    if bag_node == None:
        #Creates new bag entry in tree and enters it in dictionary
        bag_node = BagTree(bag_name, None)
        tree_dict[bag_name] = bag_node

        
    #Adds all branches of bags
    for x in contained_bags:
        amount = int(re.search('[0-9]', x).group())
        branch_name = re.search('[a-z]+ [a-z]+', x).group()
        branch = tree_dict.get(branch_name)
        if branch == None:
            branch = BagTree(branch_name, bag_node)
        else:
            branch.add_parent(bag_node)
            
        bag_node.add_branch(branch, amount)
        tree_dict[branch_name] = branch

def recursive_bag_count(bag_node):
    count = 0
    #For each branch
    for x in bag_node.branches:
        amount = bag_node.amount_dict[x.name]
        #Counts amount of current bag
        count += amount
        #If branch has new branches, start new recursive loop for branch and multiply by amount of bags
        if len(x.branches) != 0:
            count += recursive_bag_count(x)*amount

    return count

def bag_count_containing_bag(bag_name):
    #Gets node for main bag
    root_bag = tree_dict[bag_name]
    #Starts recursive loop going through entire line of branches of main bag
    return recursive_bag_count(root_bag)

for x in line_array:
    add_entry_to_tree(x)

print(bag_count_containing_bag("shiny gold"))