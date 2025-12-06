from itertools import zip_longest, groupby

with open("day6input.txt") as f:
    file = f.read()
    numbers_1 = list(map(str.split, file.strip().split("\n")[:-1]))
    numbers_2 = file.split("\n")[:-2]
    operations = file.split("\n")[-2].split()

total_2 = sum(eval(operations[i].join("".join(col) for col in group)) for i, group in enumerate([list(cols) for is_blank, cols in groupby(zip_longest(*numbers_2, fillvalue=""), lambda col: all(char == " " for char in col)) if not is_blank]))

total_1 = sum(eval(operations[i].join((numbers_1[j][i] for j in range(len(numbers_1))))) for i in range(len(numbers_1[0])))

print("Total (Part 1):", total_1)
print("Total (Part 2):", total_2)
