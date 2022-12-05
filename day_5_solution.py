# Day 5: Supply Stacks

with open("PATH/TO/YOUR/input.txt", "r") as file:
    input = file.readlines()
    
def storage_maker(input):
    """This function takes lines from the input file and turns them into a dictionary representation of the item stacks"""
    storage = {}
    dict_flag = True
    for line in input:
        idx = 1
        if dict_flag:
            # Here we create empty lists in places of numbered stacks
            for x in range(9):
                storage[f"{x+1}"]=[]
            dict_flag = False
        if "[" in line:
            # We find a line that contains any of the boxes and assign the letters to columns
            boxes = line[1::4]
            for char in boxes:
                if char.isalpha():
                    storage[f"{idx}"].append(char)
                else:
                    pass
                idx +=1  

    return storage

def instruction_maker(input):
    """This function takes the instructions and cleans up the strings a bit. We remove all words and split remaining integers into lists of three"""
    instructions = []
    for line in input:
        instruction = []
        if "move" in line:
            unneeded = ["move ", "from ", "to ", "\n"]
            for string in unneeded:
                line = line.replace(string, "")
            instruction = line.split(" ")
            instructions.append(instruction)
    
    return instructions
        
def manipulator_9000():
    """This function calculates the answer to the first part of the problem"""
    storage = storage_maker(input)
    instructions = instruction_maker(input)
    for instruction in instructions:
        # For simplicity we create three variables - how much to 'move', where 'fro'm and where 'to'
        move = instruction[0]
        fro = instruction[1]
        to = instruction[2]
        for i in range(int(move)):
            # We always insert the box at index 0 since the machine's supposed to pickup boxes one by one
            char = storage[fro][0]
            storage[to].insert(0, char)
            storage[fro].remove(char)
           
    answer = ""
    for item in storage.values():
        answer += item[0]
    return f"The top rows as arranged by the Machine 9000 are {answer}"

def manipulator_9001():
    """This function calculates the answer to the second part of the problem"""
    storage = storage_maker(input)
    instructions = instruction_maker(input)
    for instruction in instructions:
        move = instruction[0]
        fro = instruction[1]
        to = instruction[2]
        chars = []
        for i in range(int(move)):
            # We insert each box at their index since the machine's supposed to pickup them up in bulks
            char = storage[fro][i]
            storage[to].insert(i, char)
            chars.append(char)
        for char in chars:
            # We use a list of moved characters to remove them afterwards so we don't break the indexes   
            storage[fro].remove(char)
           
    answer = ""
    for item in storage.values():
            answer += item[0]
    return f"The top rows as arranged by the Machine 9001 are {answer}"

print(manipulator_9000())
print(manipulator_9001())



