from z3 import Optimize, Int, Sum, sat
from itertools import combinations

with open("day10input.txt") as file:
    lines = [line.strip().split() for line in file.readlines()]

indicators, button_lists, joltages = [line[0] for line in lines], [line[1:-1] for line in lines], [line[-1] for line in lines]
indicators = [list(indicator.strip("[]")) for indicator in indicators]
button_lists = [[list(map(int, item.strip("()").split(","))) for item in group] for group in button_lists]
joltages = [list(map(int, joltage.strip("{}").split(","))) for joltage in joltages]

def apply_button(indicator, button):
    for char in button:
        indicator[char] = "." if indicator[char] == "#" else "#"
    return indicator

total_presses_1 = 0

for i, indicator in enumerate(indicators):
    buttons = button_lists[i]

    for r in range(len(buttons) + 1):
        for button_subset in combinations(buttons, r):
            current_state = indicator.copy()

            for button in button_subset:
                current_state = apply_button(current_state, button)

            if all(char == "." for char in current_state):
                total_presses_1 += r
                break

        else:
            continue
        break

total_presses_2 = 0

for i, joltage in enumerate(joltages):
    buttons = button_lists[i]

    solver = Optimize()

    button_vars = [Int(f'button_{idx}') for idx in range(len(buttons))]
    for b in button_vars:
        solver.add(b >= 0)

    for k in range(len(joltage)):
        buttons_affecting_k = []
        for button_idx, button_indices in enumerate(buttons):
            if k in button_indices:
                buttons_affecting_k.append(button_vars[button_idx])

        solver.add(Sum(buttons_affecting_k) == joltage[k])

    solver.minimize(Sum(button_vars))

    if solver.check() == sat:
        model = solver.model()
        presses = sum(model[v].as_long() for v in button_vars)
        total_presses_2 += presses
    else:
        print(f"FAIL {i+1}")

print("Total fewest buttons needed (Part 1):", total_presses_1)
print("Total fewest buttons needed (Part 2):", total_presses_2)
