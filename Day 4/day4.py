with open("day4test.txt") as f:
    grid = [list(line.strip()) for line in f]

total_allowed = 0

def check_surroundings(x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] == "@":
                count += 1
    return count

while True:
    before_count = total_allowed
    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            if col == "@":
                adjacent_count = check_surroundings(x, y)
                if adjacent_count < 4:
                    total_allowed += 1
                    grid[x][y] = "."
    if before_count == total_allowed:
        break

print("Total number of boxes characters with less than 4 adjacent boxes:", total_allowed)
