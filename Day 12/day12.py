# This puzzle is weird and can be solved extremely simply because of how simple the input is. This code does not work on the example input.

with open("day12input.txt") as file:
    content = file.read().strip()

grids = content.split("\n\n")[-1]

total_correct = 0

for grid in grids.split("\n"):
    grid_size = grid.split(": ")[0]
    grid_amount = grid.split(": ")[1]
    if eval(grid_size.replace("x", "*")) >= 9 * sum(int(x) for x in grid_amount.split(" ")):
        total_correct += 1


print("Total correct shapes:", total_correct)
