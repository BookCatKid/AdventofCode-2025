with open("day11input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

def count_paths(graph, start, end, track_stuff=False, has_fft=False, has_dac=False, memo={}):
    key = (start, has_fft, has_dac) if track_stuff else start
    if key in memo:
        return memo[key]
    if start == end:
        if track_stuff:
            return 1 if has_fft and has_dac else 0
        else:
            return 1
    new_has_fft = has_fft or start == "fft" if track_stuff else has_fft
    new_has_dac = has_dac or start == "dac" if track_stuff else has_dac
    count = 0
    for neighbor in graph.get(start, []):
        count += count_paths(graph, neighbor, end, track_stuff, new_has_fft, new_has_dac, memo)
    memo[key] = count
    return count

graph = {}

for line in lines:
    node, neighbors_str = line.split(":")
    neighbors = [neighbor.strip() for neighbor in neighbors_str.split()]
    graph[node] = neighbors

print("Total paths from you to out (Part 1):", count_paths(graph, "you", "out"))
print("Total paths from svr to out with dac and fft (Part 2):", count_paths(graph, "svr", "out", track_stuff=True))
