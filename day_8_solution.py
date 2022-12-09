# Day 8: Treetop Tree House

with open("PATH/TO/YOUR/input.txt", "r") as file:
    input = file.readlines()
    trees_map = []
    for line in input:
        trees_map.append(line.replace("\n", ""))

visible_trees = 0
scenic_scores = [] 

# We're gonna calculate everything as we go through each tree

for x in range(len(trees_map)):
    # First we check if we are either in the first or last row of trees. 
    # We add all of them to the visible ones and don't consider any of them for the scenic score
    if x == 0 or x == len(trees_map) - 1:
        visible_trees += len(trees_map[x])

    #Here we start evaluating trees that can be hidden and provide some scenic value
    elif 0 < x < len(trees_map) - 1:
        cur_line = trees_map[x]
        # We start going tree by tree
        for y in range(len(cur_line)):
            # If the tree is on either of the edges of the row we add it to the visible sum and discard it's scenic appeal
            if y == 0 or y == len(cur_line) - 1:
                visible_trees += 1
            # And here we'll get into the nitty gritty of the evaluation
            elif 0 < y < len(cur_line) - 1:
                # We start by creating four lists of tree heights in four diretions from currnetly evaluated tree
                vertical_up = [int(item[y]) for item in trees_map[:x]][::-1] #We list the heights in reverse so that we can evaluate their height as compared to the position of the tree
                vertical_down = [int(item[y]) for item in trees_map[(x+1):]]
                horizontal_left = [int(item) for item in cur_line[:y]][::-1] #We list the heights in reverse so that we can evaluate their height as compared to the position of the tree
                horizontal_right = [int(item) for item in cur_line[(y+1):]]
                # Here we create four multiplicators for each tree, we will assigne their valeus as we go on
                vert_up_mult = 0
                vert_down_mult = 0
                hor_lef_mult = 0
                hor_right_mult = 0
                # This line determines if the tree is visible, since if it's higher than the highest tree in any row it must be visible
                if int(cur_line[y]) > max(vertical_up) or int(cur_line[y]) > max(vertical_down) or int(cur_line[y]) > max(horizontal_right) or int(cur_line[y]) > max(horizontal_left):
                    visible_trees += 1
                # The next four for loops will evaluate the scenic appeal of each tree in all four directions, 
                # breaking out of the loop when they encounter a tree as tall or higher than current one
                for num in vertical_up:
                    if num < int(cur_line[y]):
                        vert_up_mult += 1
                    elif num >= int(cur_line[y]):
                        vert_up_mult += 1
                        break
                for num in vertical_down:
                    if num < int(cur_line[y]):
                        vert_down_mult += 1
                    elif num >= int(cur_line[y]):
                        vert_down_mult += 1
                        break
                for num in horizontal_left:
                    if num < int(cur_line[y]):
                        hor_lef_mult += 1
                    elif num >= int(cur_line[y]):
                        hor_lef_mult += 1
                        break
                for num in horizontal_right:
                    if num < int(cur_line[y]):
                        hor_right_mult += 1
                    elif num >= int(cur_line[y]):
                        hor_right_mult += 1
                        break
                scenic_scores.append(vert_up_mult*vert_down_mult*hor_right_mult*hor_lef_mult)
                        
               


print(f"There are {visible_trees} visible trees")
print(f"The tree with the highest scenic score measures {max(scenic_scores)} points")