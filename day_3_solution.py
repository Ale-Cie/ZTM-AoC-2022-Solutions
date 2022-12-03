# Day 3 - Rucksack sorter

with open("PATH/TO/YOUR/input.txt", "r") as file:
    rucksacks = file.readlines()

def counter(intersection):
    # Universal counter for all priorities - they don't change values
    score = 0
    for item in intersection:
        for char in item:
            try:
                if char.isupper():
                    score += ord(char)-38
                else:
                    score += ord(char)-96
            except:
                print(char)
    return score

# Here it creates the list of sets of unique priorities for all rucksacks
intersection = []
for item in rucksacks:
    half_1 = set(char for char in item[:int(len(item)/2)])
    half_2 = set(char for char in item[int(len(item)/2):])
    intersection.append(half_1.intersection(half_2))

# Here we create a group list of three rucksack
group = []
badges = []
for i in range(int(len(rucksacks)/3)):
    # Parsing through the whole list of rucksacks in groups of three
    s_idx = 3 * i
    e_idx = 3 * (i + 1)
    group = rucksacks[s_idx:e_idx]
    # We turn first of three rucksacks into a set of unique characters to check against the next two rucksacks
    keys = {char for char in group[0]}
    for char in keys:
        if char == "\n":
            pass
        elif char in group[1] and char in group[2]:
            badges.append({char})
        else:
            pass

print(f"All priorities equal to {counter(intersection)}")
print(f"Group priorities equal to {counter(badges)}")