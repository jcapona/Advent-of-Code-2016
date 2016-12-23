#!/usr/bin/python3
# http://adventofcode.com/2016/day/3
import sys, re


def read(filename):
    triangles = []
    with open(filename, "r") as file:
        for line in file:
            triangles.append([int(x) for x in line.split()])
            triangles[-1].sort()
    return triangles


def get_valid_triangles(list):
    valid = []
    for item in list:
        if item[0] + item[1] > item[2]:
            valid.append(item)
    return valid


filename = 'day3_input1.txt' if len(sys.argv) == 1 else str(sys.argv[1])
triangles = read(filename)
print(len(get_valid_triangles(triangles)))

def init_sub_tri():
    sub_tri = []
    for i in range(3):
        sub_sub_tri = []
        sub_tri.append(sub_sub_tri)
    return sub_tri


def read_vertical(filename):
    triangles = []
    triangle_base = 0;
    line_index = 0
    triangles_sub = init_sub_tri()
    with open(filename, "r") as file:
        for line in file:
            for row in range(3):
                value = int(line.split()[row])
                triangles_sub[row].append(value)

            if (line_index + 1) % 3 == 0:
                for tr in triangles_sub:
                    triangles.append(sorted(tr))
                triangles_sub = init_sub_tri()

            line_index += 1

    return triangles


vertical_triangles = read_vertical(filename)
print(len(get_valid_triangles(vertical_triangles)))
