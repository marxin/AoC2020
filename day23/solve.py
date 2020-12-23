#!/usr/bin/env python3

from collections import deque

data = deque([3, 8,  9,  1,  2,  5,  4,  6,  7])
#data = deque([5, 9, 8, 1, 6, 2, 7, 3, 4])

#while len(data) != 1000000:
#    data.append(len(data))

def findnext(value, chunk):
    global data
    value -= 1
    while True:
        if value == 0:
            value = len(data) + 3
        if value not in chunk:
            return value
        value -= 1

def move():
    global data
    #print(data)
    v = data.popleft()
    chunk = []
    chunk.append(data.popleft())
    chunk.append(data.popleft())
    chunk.append(data.popleft())
    data.appendleft(v)

    index = data.index(findnext(v, chunk))
    for i in range(3):
        data.insert(index + 1, chunk.pop())
    data.rotate(-1)

for i in range(100):
    print(i)
    move()

s = ''
l = len(data)
start = data.index(1)

for i in range(l):
    j = (start + i) % l
    s += str(data[j])

print(s[1:])
