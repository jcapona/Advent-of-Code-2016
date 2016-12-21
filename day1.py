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
        pos = [ins[1]*x for x in self.speed[self.dir]]
        self.x += pos[0]
        self.y += pos[1]

    def walk(self, ins):
        instruction = self.readInstruction(ins)
        self.step(instruction)

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

print(abs(me.x) + abs(me.y))
