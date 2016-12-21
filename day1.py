#!/usr/bin/pytho3
# http://adventofcode.com/2016/day/1
import sys

class Walker:
    speed = {
        "N": [0, 1],
        "S": [0, -1],
        "E": [1, 0],
        "W": [-1, 0]
    }

    def __init__(self):
        self.x = 0
        self.y = 0
        self.dir = "N"
        self.waypoint = []

    def rotate(self, direction):
        rotationMatrix = {
            "L": {"N":"W", "S":"E", "E":"N", "W":"S"},
            "R": {"N":"E", "S":"W", "E":"S", "W":"N"}
        }
        return rotationMatrix[direction][self.dir]

    def readInstruction(self, ins):
        return [ins[0], int(ins[1:])]

    def step(self, ins):
        self.dir = self.rotate(ins[0])
        for i in range(ins[1]):
            directions = [x for x in self.speed[self.dir]]
            self.x += directions[0]
            self.y += directions[1]
            self.waypoint.append([self.x, self.y])

    def walk(self, ins):
        instruction = self.readInstruction(ins)
        self.step(instruction)

    def get_distance(self, x = None, y = None):
        if (x and y):
            return abs(x) + abs(y)
        return abs(me.x) + abs(me.y)

    def get_repeated(self):
        return [x for x in self.waypoint if self.waypoint.count(x) > 1]


def get_steps(filename):
    with open(filename, "r") as file:
        for line in file:
            steps = line.split(', ')
    return steps

me = Walker()
filename = 'day1_input1.txt' if len(sys.argv) == 1 else str(sys.argv[1])
steps = get_steps(filename)
for step in steps:
    me.walk(step)

print(me.get_distance())
[x_rep, y_rep] = me.get_repeated()[0]
print(me.get_distance(x_rep, y_rep))
