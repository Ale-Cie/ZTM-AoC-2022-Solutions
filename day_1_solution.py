# Day 1 - Counting calories

def calories_devider():
    """Returns a dictionary of all the Elf: Calories tuple
    
    This function takes the input given by the website and after reading all the lines it creates a dictionary of elves and their corresponding treats as tuples of integers."""

    with open("PATH/TO/YOUR/input.txt", "r") as file:
        calories_list = file.readlines()
        elf_calories_dict = {}
        idx = 0
        for item in range(calories_list.count("\n")):
            # We'll use a shorthand way to create the dictionary by searching for the first appearance of the '\n' and slicing the list to this up to this index.
            # Next we reasign the list from the index one higher than the '\n' and do it all over again
            # Last step is to make sure that the final elf is also assigned, thus the try: except: for simplicity
            try: 
                elf_calories_dict[f"Elf {item}"] = tuple(int(item) for item in calories_list[:calories_list.index("\n")])
                calories_list = calories_list[calories_list.index("\n")+1:]
                idx += 1 
            except:
                elf_calories_dict[f"Elf {idx}"] = tuple(int(item) for item in calories_list)            
    
    return elf_calories_dict

def calories_adder(elf_calories_dict):
    """Returns a dictionary of all the Elf: Summed calories tuple
    
    This function takes a dictionary of elves and corresponding tuples of calories. It summarises the calories inside of each tuple and assigns it to the corresponding elf."""
    elf_sums_dict = {}
    for elf, calories in elf_calories_dict.items():
        elf_sums_dict[elf] = sum(calories)
    
    return elf_sums_dict

def answer(calories_summed_dict):
    """Returns an answer to the first day of AoC in string format"""
    max_calories = max(calories_summed_dict.values())
    top_three_elves = sorted(calories_summed_dict.values(), reverse=True)[:3]
    top_three_summed = sum(top_three_elves)
    return f"The elf with the highest calories has {max_calories}.\nTop three elves have {top_three_elves} and that adds up to {top_three_summed}."

elf_calories_dict = calories_devider()
calories_summed_dict = calories_adder(elf_calories_dict)

print(answer(calories_summed_dict))