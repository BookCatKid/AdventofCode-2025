with open("day3input.txt") as f:
    j_ratings = f.readlines()

total_j_1 = 0
total_j_2 = 0

def get_highest(rating):
    rating_list = list(map(int, rating))
    highest = rating_list.index(max(rating_list)), max(rating_list)
    return highest

def find_highest_rating(rating, amount_finding):
    nums = list(map(int, rating))
    total = ""
    offset = 0

    for picked in range(amount_finding):
        remaining = amount_finding - picked - 1
        end = len(nums) - remaining
        window = nums[offset:end]
        idx, val = get_highest(window)
        total += str(val)
        offset += idx + 1

    return total

for rating in j_ratings:
    rating = rating.strip()
    total_j_1 += int(find_highest_rating(rating, 2))
    total_j_2 += int(find_highest_rating(rating, 12))

print("Total of all highest J ratings (Part 1):", total_j_1)
print("Total of all highest J ratings (Part 2):", total_j_2)
