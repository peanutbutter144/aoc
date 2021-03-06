#!/usr/bin/env python3

from wires import parse, find_intersects, Coordinate, Direction, manhattan_distance

with open("input", "r") as f:
    wires = parse(f)

# part 1

origin = Coordinate(0,0)
wire1 = wires[0]
wire2 = wires[1]
intersects = find_intersects(wire1, wire2)

least_distance = None
for intersect in intersects:
    coordinate = intersect.get_coordinate()
    distance = manhattan_distance(origin, coordinate)
    if (least_distance == None) or (distance < least_distance):
        least_distance = distance

print(least_distance)
