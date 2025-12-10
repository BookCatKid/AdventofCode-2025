from shapely.geometry import Polygon, box

with open("day9input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

red_tiles = [list(map(int, line.strip().split(","))) for line in lines]

def largest_rectangle_anywhere(red_tiles):
    max_area = 0
    for point in red_tiles:
        for point2 in red_tiles:
            if point != point2:
                rect_area = (abs(point2[0] - point[0]) + 1) * (abs(point2[1] - point[1]) + 1)
                max_area = max(max_area, rect_area)
    return max_area


def largest_rectangle_inside(red_tiles):
    polygon = Polygon(red_tiles)
    max_area = 0
    for point in red_tiles:
        for point2 in red_tiles:
            rect = box(point[0], point[1], point2[0], point2[1])
            if polygon.covers(rect):
                area = (abs(point2[0] - point[0]) + 1) * (abs(point2[1] - point[1]) + 1)
                max_area = max(max_area, area)
    return max_area


print("Largest rectangle area (Part 1):", largest_rectangle_anywhere(red_tiles))
print("Largest rectangle area (Part 2):", largest_rectangle_inside(red_tiles))
