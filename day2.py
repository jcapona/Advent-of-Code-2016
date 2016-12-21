#!/usr/bin/python3
# http://adventofcode.com/2016/day/2
import sys

class bathroomKeypadCracker():
    height = 3
    width = 3

    def up(self, num, row):
        return [num, row - 1 if row > 0 else 0]
    def down(self, num, row):
        return [num, row + 1 if row < self.height - 1 else self.height - 1]
    def left(self, num, row):
        return [num - 1 if num > 0 else 0, row]
    def right(self, num, row):
        return [num + 1 if num < self.width - 1 else self.width - 1, row]
    def translate(self, x, y):
        return (x + 1) + 3*y;
    def validate(self, x, y):
        return True

    def cracker(self, filename, row_0 = 1, digit_0 = 1):
        response = []

        with open(filename, "r") as file:
            num = digit_0
            row = row_0
            for line in file:
                for char in list(line):
                    num_base = num
                    row_base = row
                    if char == 'U':
                        [num, row] = self.up(num, row)
                    elif char == 'D':
                        [num, row] = self.down(num, row)
                    elif char == 'L':
                        [num, row] = self.left(num, row)
                    elif char == 'R':
                        [num, row] = self.right(num, row)

                    if self.validate(num, row) == False:
                        num = num_base
                        row = row_base

                response.append(self.translate(num, row))

            print(''.join(str(e) for e in response).upper())

class bathroomKeypadCracker2(bathroomKeypadCracker):
    height = 5
    width = 5

    # ugly :(
    def translate(self, x, y):
        if y == 0 and x == 2:
            return 1
        elif y == 1 and x in [1, 2, 3]:
            return x + 1
        elif y == 2:
            return x + 5
        elif y == 3 and x in [1, 2, 3]:
            return hex(x+9).split('x')[1]
        elif y == 4 and x == 2:
            return 'd'
        else:
            return ''

    def validate(self, num, row):
        return False if self.translate(num, row) == '' else True


filename = 'day2_input1.txt' if len(sys.argv) == 1 else str(sys.argv[1])
bath1 = bathroomKeypadCracker()
bath1.cracker(filename)
bath2 = bathroomKeypadCracker2()
bath2.cracker(filename, 2, 0)
