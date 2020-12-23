#!/usr/bin/env python3

from collections import deque

data = [3, 8,  9,  1,  2,  5,  4,  6,  7]
data = [5, 9, 8, 1, 6, 2, 7, 3, 4]

def findnext(value):
    global data
    value -= 1
    while value > 0:
        if value in data:
            return value
        value -= 1
    return max(data)

def move():
    global data
    print(data)
    v = data[0]
    chunk = data[1:4]
    data = data[:1] + data[4:]
    index = data.index(findnext(v))
    for i in range(3):
        data.insert(index + 1, chunk.pop())
    data = data[1:] + data[:1]

for i in range(100):
    move()

s = ''
l = len(data)
start = data.index(1)

for i in range(l):
    j = (start + i) % l
    s += str(data[j])

print(s[1:])
