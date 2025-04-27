import random
import time

print ("Welcome to the ASCII forest generator!🌲🌳")
time.sleep(1)
print ("Choose between the 'linden tree' or the 'spruce'.")

tree_type = input("Enter the type of tree you want (linden tree/ spruce): ")
while tree_type not in ['linden tree', 'spruce']:
    tree_type = input ("Invalid input. Please choose between 'linden tree' and 'spruce': ")

number_of_trees = int(input("How many trees do you want in your forest? (1-10): \n "))
if 1 < number_of_trees > 10:
    int(input("Please enter a number between 1 and 10."))
height = int(input("How tall should the tree(s) be? (5-20): "))
if 5 < height > 20:
    int(input("Please enter a number between 5 and 20."))

user_leaves = input("Enter 1-5 characters to use as leaves in your forest (e.g.: * + @ # %), \n or press Enter to use random ones: ")
if 1 <= len(user_leaves) <= 5:
    leaf_options = list(user_leaves)
else:
    leaf_options = ["*", "+", "@", "#", "&", "%"]
    print ("Your tree(s) will consist of the default leaf symbols.")
time.sleep(1)
print ("Generating your forest...\n")
time.sleep(1)

# List for all trees
trees = []

if tree_type == 'linden tree':
    crown_width = height + 2
else:
    crown_width = None

# Generating the tree(s)
for _ in range(number_of_trees):
    tree = []
    max_width = 0
    for i in range (1, height + 1): # i - current row of trees
        leaf_symbol = random.choice(leaf_options)

        if tree_type == "spruce":
            spaces = " " * (height - i)
            leaves = "/" + leaf_symbol * (i * 2 -1) + "\\"
        elif tree_type == "linden tree":
            radius = (height - 1) // 2
            distance_from_middle = abs(i - radius)
            leaf_count = crown_width - distance_from_middle * 2
            spaces = " " * (crown_width// 2 - leaf_count // 2)
            leaves = leaf_symbol * max(1, leaf_count)

        row = spaces + leaves
        tree.append(row)

        if tree_type == "spruce":
            max_width = max(max_width, len(row)) # update for spruce

    trunk_width = 2
    if tree_type == "spruce":
        trunk = " " * (max_width // 2 - trunk_width // 2) # insert trunk below middle of tree
    else:
        trunk = " " * (crown_width // 2 - trunk_width // 2)
    for _ in range(3):
        tree.append(trunk + "||")

    trees.append((tree, max_width if tree_type == "spruce" else crown_width))

# Ensuring that the trees are printed side by side
for row in range(height + 3): # including trunk height
    for tree, width in trees:
        print(tree[row].ljust(width), end="   ")
    print ()
    time.sleep(0.5)

print ("Your forest is ready! 🌳🌲")



