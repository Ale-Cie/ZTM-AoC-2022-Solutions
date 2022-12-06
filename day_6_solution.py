# Day 6: Tuning Trouble

with open("PATH/TO/YOUR/input.txt", "r") as file:
    input = file.readlines()

def marker_finder(input):
    """Returns the integer of characters that have to be processed in order to find the marker."""
    marker_flag = True
    for code in input:
        i = 0
        while marker_flag:
            # We try to create a set of four characters as we go through the text in fours
            s_idx = 0 + i
            e_idx = 4 + i
            marker_set = {char for char in code[s_idx:e_idx]}
            if len(marker_set) == 4:
                marker_flag = False
            else:
                i += 1
    
    return f"{i + 4} characters have to be processed to find the marker."

def message_finder(input):
    message_flag = True
    for code in input:
        i = 0
        while message_flag:
            # We try to create a set of fourteen characters as we go through the text in fourteens
            s_idx = 0 + i
            e_idx = 14 + i
            message_set = {char for char in code[s_idx:e_idx]}
            if len(message_set) == 14:
                message_flag = False
            else:
                i += 1
    
    return f"{i + 14} characters have to be processed to find the message."

print(marker_finder(input))
print(message_finder(input))