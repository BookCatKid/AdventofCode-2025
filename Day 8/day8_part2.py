import math
from itertools import combinations

class Box():
    def __init__(self, pos):
        self.pos = pos
        self.circuit = None

    def __repr__(self):
        return str(self.pos)

class Circuit():
    def __init__(self):
        self.boxes = []

    def add_box(self, box):
        self.boxes.append(box)
        box.circuit = self

with open("day8input.txt") as file:
# with open("day8input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

points = [list(map(int, line.strip().split(","))) for line in lines]
points = [Box(point) for point in points]

connected_points = []

CONNECTION_AMOUNT = 10 # 1000 for real input, 10 for test input
# CONNECTION_AMOUNT = 1000 # 1000 for real input, 10 for test input

combs_dist = [(math.dist(point_list[0].pos, point_list[1].pos), *point_list) for point_list in combinations(points, 2)]
combs_dist.sort(key=lambda x: x[0])

# print(combs_dist)

circuits = []
last_two_boxes = []

for combs in combs_dist:
    if combs[1].circuit == combs[2].circuit and combs[1].circuit != None:
        continue
    elif combs[1].circuit and combs[2].circuit:
        orig_circuit = combs[2].circuit
        for box in combs[2].circuit.boxes:
            combs[1].circuit.add_box(box)
        orig_circuit.boxes = []
    elif combs[1].circuit:
        combs[1].circuit.add_box(combs[2])
    elif combs[2].circuit:
        combs[2].circuit.add_box(combs[1])
    else:
        circuit = Circuit()
        circuit.add_box(combs[1])
        circuit.add_box(combs[2])
        circuits.append(circuit)

    last_two_boxes = [combs[1], combs[2]]

print("X coordinate of last two connected junction boxes multiplied together (Part 2):", last_two_boxes[0].pos[0] * last_two_boxes[1].pos[0])
