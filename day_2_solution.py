# Day 2 - Rock Paper Scissors

with open("YOUR/PATH/TO/input.txt", "r") as file:
    matches = file.readlines()

def supposed_interpretation(matches):
    """Returns the score calculated according to the supposed interpretation of the secret instructions."""
    score = 0
    # A X - Rock (1 point), B Y - Paper (2 points), C Z - Scissors (3 points)
    # Win - 6 points, Draw - 3 points, Lose - 0 points
    for item in matches:
        match item[0]:
            case "A":
                if item[2] == "Y":
                    outcome = 6 + 2
                elif item[2] == "Z":
                    outcome = 3
                else:
                    outcome = 3 + 1
                score += outcome
            case "B":
                if item[2] == "Z":
                    outcome = 6 + 3
                elif item[2] == "X":
                    outcome = 1
                else:
                    outcome = 3 + 2
                score += outcome
            case _:
                if item[2] == "X":
                    outcome = 6 + 1
                elif item[2] == "Y":
                    outcome = 2
                else:
                    outcome = 3 + 3
                score += outcome
    return score

def actual_interpretation(matches):
    """Returns the actual score, calculated according to elves interpretation of the secret key."""
    score = 0
    # A - Rock (1 point), B - Paper (2 points), C - Scissors (3 points)
    # Z - Win (6 points), Y - Draw (3 points), X - Lose (0 points) 
    for item in matches:
        match item[2]:
            case "Z":
                score += 6
                if item[0] == "A":
                    score += 2
                elif item[0] == "B":
                    score += 3
                elif item[0] == "C":
                    score += 1
            case "Y":
                score += 3
                if item[0] == "A":
                    score += 1
                elif item[0] == "B":
                    score += 2
                elif item[0] == "C":
                    score += 3
            case _:
                if item[0] == "A":
                    score += 3
                elif item[0] == "B":
                    score += 1
                elif item[0] == "C":
                    score += 2
    return score


print(f"Your way of reading the set of instructions would result in the score equal to {supposed_interpretation(matches)}")
print(f"Actual score that the elf envisioned should be {actual_interpretation(matches)}")