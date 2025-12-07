with open("day7input.txt") as f:
    grid = [list(line.strip()) for line in f.readlines()]

s_pos = grid[0].index("S")
rows, cols = len(grid), len(grid[0])

total_splits_1 = 0
ended = False

def get_cell(grid, row, col):
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        return grid[row][col]
    return None

def set_cell(grid, row, col, val):
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        grid[row][col] = val

def start_beam_top(grid, col):
    set_cell(grid, 0, col, "|")

def clear_cell(grid, row, col):
    set_cell(grid, row, col, '.')

def print_grid(grid):
    for row in grid:
        print("".join(row))

def find_all_beams(grid):
    beam_positions = []
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == "|":
                beam_positions.append((r, c))
    return beam_positions


def move_beam_down(grid, beam):
    row, col = beam
    clear_cell(grid, row, col)
    set_cell(grid, row + 1, col, "|")

def split_beam(grid, beam):
    global total_splits_1
    row, col = beam
    clear_cell(grid, row, col)
    set_cell(grid, row + 1, col - 1, "|")
    set_cell(grid, row + 1, col + 1, "|")
    total_splits_1 += 1

def advance_grid(grid):
    global ended
    for beam in find_all_beams(grid):
        if beam[0] + 1 >= len(grid):
            ended = True
            continue
        if grid[beam[0]+1][beam[1]] == "^":
            split_beam(grid, beam)
        else:
            move_beam_down(grid, beam)

start_beam_top(grid, s_pos)
for _ in range(rows):
    advance_grid(grid)

def count_paths(grid):
    ways = [[0 for _ in range(cols)] for _ in range(rows)]
    ways[0][s_pos] = 1

    for row_idx in range(rows - 1):
        for col_idx in range(cols):
            ways_here = ways[row_idx][col_idx]
            if ways_here == 0:
                continue
            if get_cell(grid, row_idx + 1, col_idx) == "^":
                ways[row_idx + 1][col_idx - 1] += ways_here
                ways[row_idx + 1][col_idx + 1] += ways_here
            else:
                ways[row_idx + 1][col_idx] += ways_here

    return sum(ways[-1])

total_paths_2 = count_paths(grid)

print("Total splits (Part 1):", total_splits_1)
print("Total different paths (Part 2):", total_paths_2)
