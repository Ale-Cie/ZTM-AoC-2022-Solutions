# Day 9: Rope Bridge

with open("PATH/TO/YOUR/input.txt", "r") as file:
    input = file.readlines()
    instructions = []
    for line in input:
        line = line.replace("\n", "")
        instructions.append(line.split(" "))

def answer_1(instructions):
    head_pos = [0, 0]
    tail_pos = [0, 0]
    tail_hist = []
    for line in instructions:
        for x in range(int(line[1])):
            if line[0] == "U":
                head_pos[1] += 1
            elif line[0] == "D":
                head_pos[1] -= 1
            elif line[0] == "L":
                head_pos[0] -= 1
            elif line[0] == "R":
                head_pos[0] += 1
            x_dif = abs(head_pos[0] - tail_pos[0])
            y_dif = abs(head_pos[1] - tail_pos[1])
            if x_dif > 1 or y_dif > 1:
                if not x_dif:
                    if tail_pos[1] > head_pos[1]:
                        tail_pos[1] -= 1
                    else:
                        tail_pos[1] += 1
                elif not y_dif:
                    if tail_pos[0] > head_pos[0]:
                        tail_pos[0] -= 1
                    else:
                        tail_pos[0] += 1
                else:
                    if tail_pos[0] > head_pos[0]:
                        tail_pos[0] -= 1
                    else:
                        tail_pos[0] += 1
                    if tail_pos[1] > head_pos[1]:
                        tail_pos[1] -= 1
                    else:
                        tail_pos[1] += 1 
            tail_hist.append(f"{tail_pos}")
    
    return len(set(tail_hist))

def answer_2(instructions):
    end_hist = []
    long_rope = [[0,0] for _ in range(10)]
    for line in instructions:
        for x in range(int(line[1])):
            if line[0] == "U":
                long_rope[0][1] += 1
            elif line[0] == "D":
                long_rope[0][1] -= 1
            elif line[0] == "L":
                long_rope[0][0] -= 1
            elif line[0] == "R":
                long_rope[0][0] += 1
            
            for i in range(1,10):
                x_dif = abs(long_rope[i][0] - long_rope[i-1][0])
                y_dif = abs(long_rope[i][1] - long_rope[i-1][1])
                if x_dif > 1 or y_dif > 1:
                    if not x_dif:
                        if long_rope[i][1] > long_rope[i-1][1]:
                            long_rope[i][1] -= 1
                        else:
                            long_rope[i][1] += 1
                    elif not y_dif:
                        if long_rope[i][0] > long_rope[i-1][0]:
                            long_rope[i][0] -= 1
                        else:
                            long_rope[i][0] += 1
                    else:
                        if long_rope[i][0] > long_rope[i-1][0]:
                            long_rope[i][0] -= 1
                        else:
                            long_rope[i][0] += 1
                        if long_rope[i][1] > long_rope[i-1][1]:
                            long_rope[i][1] -= 1
                        else:
                            long_rope[i][1] += 1   
                if i == 9:
                    end_hist.append(f"{long_rope[i]}")
               
    
    return len(set(end_hist))

print(f"The tail visits {answer_1(instructions)} positions")
print(f"The tail of the large rope visits {answer_2(instructions)} positions")
    