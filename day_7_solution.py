# Day 7: No Space Left On Device

with open("PATH/TO/YOUR/input.txt", "r") as file:
    input = file.readlines()

def dir_tree_maker(input):
    # We follow instructions and save each path's size of raw files (no dirs) as a dictionary of path: sizes
    dir_tree = {}
    path = ""
    for line in input:
        line = line.replace("\n", "")
        if "$ cd .." in line:
            e_idx = path.rfind("/")
            path = path[:e_idx]
        elif "$ cd /" in line:
            path = "root"
            dir_tree[path] = 0
        elif "$ cd" in line:
            pwd = line.replace("$ cd ", "")
            path += ("/" + pwd)
        elif "dir" in line:
            dir = line.replace("dir ", "")
            dir_tree[f"{path}/{dir}"] = 0
        elif line[0].isnumeric():
            size = int(line.split(" ")[0])
            dir_tree[path] += size

    return dir_tree

dir_tree = dir_tree_maker(input)

for path in sorted(dir_tree.keys(), key=(lambda item: item.count("/")), reverse=True):
    # One after one we go adding the value of deeper dir to the one above
    size = dir_tree[path]
    try:
        e_idx = path.rfind("/")
        dir_tree[path[:e_idx]] += size
    except:
        print("You've probably reached /root")

score = 0
max_space = 70000000
req_space = 30000000 - (max_space - dir_tree["root"])
deletable = []
for size in dir_tree.values():
    # We do two things at once - if the file is smaller than 100000 we calculate the answer to part 1, if the file size is at least the required amount we append it to deletable list

    if size <= 100000:
        score += size
    if size >= req_space:
        deletable.append(size)

print(f"Total size of directories >= 100000 is {score}")

print(f"To free up enough storage you should delete the file of size {min(deletable)}")

