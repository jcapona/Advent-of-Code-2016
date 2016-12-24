#!/usr/bin/python3
# http://adventofcode.com/2016/day/4
import sys, re, collections, string
import pprint

def get_data(filename):
    arr = []
    regex = r"^([a-z\-]+)([0-9]+)\[([a-z]+)\]$"
    reg = re.compile(regex)
    sum = 0
    with open(filename, "r") as file:
        for line in file:
            for base, num, checksum in reg.findall(line):
                obj = {
                    'text': ''.join(s for s in base if s in string.ascii_lowercase),
                    'number': int(num),
                    'checksum': checksum
                }
                if valid(obj):
                    obj['decoded'] = decode(base, int(num))
                    arr.append(obj)
                    sum += int(num)
    print(sum)
    return arr


def valid(data):
    results = collections.Counter(data['text'])
    common = [(-num, letter) for letter, num in results.most_common()]
    chksm = ''.join(letter for num, letter in sorted(common))
    if data['checksum'] in chksm:
        return True


def decode(text, number):
    word = ''
    letterArr = range(ord('a'), ord('z')+1)
    for char in text:
        rchar = (ord(char) - letterArr[0] + number) % len(letterArr)
        word += chr(letterArr[rchar]) if char != '-' else ' '
    return word

def find_in_arr_by_key(arr, key, val):
    for data in arr:
        if data[key] and val in data[key]:
            return data


filename = 'day4_input1.txt' if len(sys.argv) == 1 else str(sys.argv[1])
data = get_data(filename)
print(find_in_arr_by_key(data, 'decoded', 'northpole object storage'))
