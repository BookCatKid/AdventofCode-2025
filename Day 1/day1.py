with open("day1input.txt") as f:
    moves = f.readlines()

CURRENT_POSITION = 50
NUMBER_0_PART_1 = 0
NUMBER_0_PART_2 = 0

for move in moves:
    previous_position = CURRENT_POSITION
    direction, steps = move[0], int(move[1:])
    for _ in range(steps):
        if direction == "R":
            CURRENT_POSITION += 1
            if CURRENT_POSITION > 99:
                CURRENT_POSITION = 0
        elif direction == "L":
            CURRENT_POSITION -= 1
            if CURRENT_POSITION < 0:
                CURRENT_POSITION = 99
        if CURRENT_POSITION == 0:
            NUMBER_0_PART_2 += 1

    if CURRENT_POSITION == 0:
        NUMBER_0_PART_1 += 1

print("Total number of times position 0 was reached (Part 1):", NUMBER_0_PART_1)
print("Total number of times position 0 was reached (Part 2):", NUMBER_0_PART_2)
