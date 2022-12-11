# Day 11: Monkey in the Middle
from math import floor

def instructor():
    with open("PATH/TO/YOUR/input.txt", "r") as file:
        instructions = []
        for line in file.readlines():
            if "Monkey" in line:
                monkey = {}
                monkey["inspected"] = 0
            elif "Starting items" in line:
                items = line.replace("\n", "").split(":")
                items = items[1].strip(" ").split(",")
                monkey["items"] = [int(item) for item in items] 
            elif "Operation" in line:
                operation = line.replace("\n", "").split(":")
                operation = operation[1].strip(" ").replace("new = ", "")
                monkey["operation"] = operation
            elif "Test" in line:
                test = line.replace("\n", "").split(":")
                test = int(test[1].replace("divisible by ", ""))
                monkey["test"] = test
            elif "If true" in line:
                if_true = line.replace("\n", "").split(":")
                if_true = int(if_true[1].replace(" throw to monkey ", ""))
                monkey["true"] = if_true
            elif "If false" in line:
                if_false = line.replace("\n", "").split(":")
                if_false = int(if_false[1].replace(" throw to monkey ", ""))
                monkey["false"] = if_false
                instructions.append(monkey)
    return instructions

def answer_generator(rounds):
    """Returns the answer based on how many rounds it is given."""
    instructions = instructor()
    # Here we create a modulus which will be used in the second part of the task. If it wasn't for reddit I wouldn't have guessed
    modulus = 1
    for monkey in instructions:
        divisor = monkey["test"]
        modulus *= divisor

    for _ in range(rounds):
        for monkey in instructions:
            if len(monkey["items"]) > 0:
                items = monkey["items"][::]
                for item in items:
                    old = item
                    if rounds == 20:
                        # We ue floor function from the math module since these numbers will be relatively small
                        new = floor(eval(monkey["operation"]) / 3)
                    else:
                        # Here if it wasn't for reddit I wouldn't have guessed to do that, so shout outs to these guys
                        new = eval(monkey["operation"]) % modulus
                    if new % monkey["test"] == 0:
                        if_true = monkey["true"]
                        instructions[if_true]["items"].append(new)
                    else:
                        if_false = monkey["false"]
                        instructions[if_false]["items"].append(new)
                    monkey["items"].pop(0)
                    monkey["inspected"] += 1
            else:
                pass
    # Here we create a list of the inspections performed by each monkey, which we will then sort and take the last two numbers to calculate the answers
    inspections = []
    for monkey in instructions:
        inspections.append(monkey["inspected"])

    inspections = sorted(inspections)
    shenaningans = inspections[-1] * inspections[-2]
    
    return f"The level of monkey buisness after {rounds} equals {shenaningans}"

print(answer_generator(20))
print(answer_generator(10000))
    
