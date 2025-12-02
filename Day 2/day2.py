import re

with open("day2input.txt") as f:
    ranges = f.readline().strip().split(",")

total_invalid_count_1 = 0
total_invalid_count_2 = 0

def check_number_1(num):
    if str(num)[0] == "0":
        return False
    return bool(re.fullmatch(r"(\d+)\1", str(num)))

def check_number_2(num):
    if str(num)[0] == "0":
        return False
    return bool(re.fullmatch(r"(.+)\1+", str(num)))

def check_range_1(range_str):
    total_return = 0
    start, end = range_str.split("-")
    for num in range(int(start), int(end) + 1):
        if check_number_1(num):
            total_return += num
    return total_return

def check_range_2(range_str):
    total_return = 0
    start, end = range_str.split("-")
    for num in range(int(start), int(end) + 1):
        if check_number_2(num):
            total_return += num
    return total_return

for range_str in ranges:
    total_invalid_count_1 += check_range_1(range_str)
    total_invalid_count_2 += check_range_2(range_str)
    # print(f"Invalid numbers sum for range {range_str}: {check_range(range_str)}")

print("Total number of invalid numbers (Part 1):", total_invalid_count_1)
print("Total number of invalid numbers (Part 2):", total_invalid_count_2)
