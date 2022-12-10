# Day 10: Cathode-Ray Tube

with open("PATH/TO/YOUR/input.txt", "r") as file:
    user_input = []
    for line in file.readlines():
        user_input.append(tuple(line.replace("\n", "").split(" ")))
# We start by creating the reg_x variable with 1 assigned
# Then we create two empty lists - one that we will need in the second part of the challenge and the other one needed now
# The cycle values are just for simplicity later on
reg_x = 1
reg_x_values = []
sig_scores = []
cycles = [20, 60, 100, 140, 180, 220]
for line in user_input:
    # We look into the value of command. If it's the 'noop' we append current value of reg_x to one list, and the signal score to the other
    if line[0] == "noop":
        reg_x_values.append(reg_x)
        sig_scores.append(reg_x * (len(sig_scores)+1)) # We use len(sig_scores)+1 since the list is always one int shorter than the cycle number
    elif line[0] == "addx":
        for _ in range(2):
            # This was confusing for me at first, but then I read the instructions carefully
            # We append the current reg_x to the list twice, extending it both times, because the value of reg_ex is changed AFTER the end of second cycle
            reg_x_values.append(reg_x)
            sig_scores.append(reg_x * (len(sig_scores)+1)) # We use len(sig_scores)+1 since the list is always one int shorter than the cycle number
        reg_x += int(line[1]) # Second cycle in 'addx' ended so we calculate new reg_x

# Quick calculation of the sum. We have to use the score-1 index, since the list indices start at 0 and go from there
the_sum = 0
for score in cycles:
    the_sum += sig_scores[score-1]

print(f"The sum of 20, 60, 100, 140, 180, 220 signal scores equals {the_sum}")
print("Turning on the machine...\nDisplaying the message...\n")

# We create the display by making 6 rows of 40 dots
display = [f"{'.'*40}" for _ in range(6)]
for row_idx in range(6):
    # We access each row separately and in next step start going through each row pixel by pixel
    row = display[row_idx]    
    for pixel in range(40):
        x = reg_x_values[pixel+(40*row_idx)]
        # This ugly looking if/elif/else statement makes it possible to convert the usually high value of X into the 0-39 index of the pixels
        if x < 40:
            pass
        elif 40 <= x < 80:
            x -= 40
        elif 80 <= x < 120:
            x -= 80
        elif 120 <= x < 160:
            x -= 120
        elif 160 <= x < 200:
            x -= 160
        else:
            x -= 200
        # For simplicity we slice through the dots up to the pixel we're supposed to turn into the '#', add the sign and continue with slicing
        if pixel in range(x-1, x+2):
            row = row[:pixel] + "#" + row[pixel+1:]
        else:
            pass
    # As we exit out of this loop we print the row in it's entirety
    print(row)
print("Interpretation left up to the user")





