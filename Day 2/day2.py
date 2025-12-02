import re

with open("day2input.txt") as f:
    ranges = f.readline().strip().split(",")

total_invalid_count_1 = 0
total_invalid_count_2 = 0

def check_number(num, pattern):
    num_str = str(num)
    if num_str[0] == "0":
        return False
    return bool(re.fullmatch(pattern, num_str))

def sum_invalid_numbers(range_str, checker):
    total_return = 0
    start, end = range_str.split("-")
    for num in range(int(start), int(end) + 1):
        if checker(num):
            total_return += num
    return total_return


def is_invalid_part1(num):
    return check_number(num, r"(\d+)\1")


def is_invalid_part2(num):
    return check_number(num, r"(.+)\1+")

for range_str in ranges:
    total_invalid_count_1 += sum_invalid_numbers(range_str, is_invalid_part1)
    total_invalid_count_2 += sum_invalid_numbers(range_str, is_invalid_part2)

print("Total number of invalid numbers (Part 1):", total_invalid_count_1)
print("Total number of invalid numbers (Part 2):", total_invalid_count_2)
