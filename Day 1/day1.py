with open("day1input.txt") as f:
    moves = f.readlines()

current_position = 50
zero_hits_part1 = 0
zero_hits_part2 = 0

for move in moves:
    direction, steps = move[0], int(move[1:])
    for _ in range(steps):
        if direction == "R":
            current_position += 1
            if current_position > 99:
                current_position = 0
        elif direction == "L":
            current_position -= 1
            if current_position < 0:
                current_position = 99
        if current_position == 0:
            zero_hits_part2 += 1

    if current_position == 0:
        zero_hits_part1 += 1

print("Total number of times position 0 was reached (Part 1):", zero_hits_part1)
print("Total number of times position 0 was reached (Part 2):", zero_hits_part2)
