# Day 4 - Camp Cleanup

with open("PATH/TO/YOUR/input.txt", "r") as file:
    pairs = file.readlines()
    all_ranges = []
    for pair in pairs:
        # We clean up the input here a bit - we remove the unnecessary '\n' from the end of each line 
        # Then split pair into a list of ranges
        
        pair = pair.replace("\n", "")
        all_ranges.append(pair.split(","))

pair_count = 0
overlap_count = 0
for elf_range in all_ranges:
    # Here we devide the pairs a bit more - we split the pairs of ranges into separate strings (in style 'X-Y'). 
    # Next we remove the '-' from each string and create a list of [starting_index, ending_index] for each elf of the pair.
    
    elf_0 = elf_range[0].split("-")
    elf_1 = elf_range[1].split("-")

    # We create a set of each elves cleaning ranges 
    # They start from starting_index to their ending_index + 1 (so we capture the ending index as well)
    elf_0_set = {item for item in range(int(elf_0[0]), int(elf_0[1])+1)}
    elf_1_set = {item for item in range(int(elf_1[0]), int(elf_1[1])+1)}

    # We create a test_set that helps us see if one or the other elf is essentialy covered by their friend
    # Since if the length of the test set is equal to the length of an elf set it must mean, that one of the elves
    # intersects fully with their friend.

    test_set = elf_0_set.intersection(elf_1_set)
    if len(test_set) == len(elf_1_set) or len(test_set) == len(elf_0_set):
        pair_count += 1

        # We one up the overlap counter since the elf fully overlaps 

        overlap_count += 1
    elif test_set:
        # Here by simple logic - if the test set is not empty there is overlap. It might not be a full coverage as above
        # But it's overlap none the less

        overlap_count += 1
    else:
        pass

print(f"There are {pair_count} ranges fully covered by the other one in this assignment")
print(f"In {overlap_count} pairs the ranges overlap")
