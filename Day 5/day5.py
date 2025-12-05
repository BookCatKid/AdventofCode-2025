with open("day5input.txt") as f:
    ranges, ingredients = f.read().strip().split("\n\n")

total_correct_1 = 0
total_correct_2 = 0

intervals = []
merged = []

for ingredient in ingredients.split("\n"):
    found = False
    for r in ranges.split("\n"):
        if found:
            break
        first, second = r.split("-")
        ing_val = int(ingredient)
        if int(first) <= ing_val <= int(second):
            total_correct_1 += 1
            found = True

for r in ranges.split("\n"):
    first, second = r.split("-")
    intervals.append((int(first), int(second)))
intervals.sort()

for start, end in intervals:
    if not merged or start > merged[-1][1] + 1:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

for start, end in merged:
    total_correct_2 += (end - start + 1)

print("Total number of ingredients within the allowed ranges (Part 1):", total_correct_1)
print("Total number of ingredients within the allowed ranges (Part 2):", total_correct_2)
