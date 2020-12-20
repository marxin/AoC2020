#!/usr/bin/env python3

from collections import deque

data = open('input.txt').read()

tiles = []

for part in data.split('\n\n'):
    lines = part.splitlines()
    id = int(lines[0].split(' ')[-1][:-1])
    lines = lines[1:]

    top = lines[0]
    bottom = ''.join(reversed(lines[-1]))
    left = ''.join([x[0] for x in reversed(lines)])
    right = ''.join([x[-1] for x in lines])
    tiles.append((id, deque([top, right, bottom, left])))

d = {(0, 0): tiles[0]}
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
tiles = tiles[1:]

def rotate(tile, n):
    tile[1].rotate(1)

def flip(tile):
    tile[1][0] = tile[1][0][::-1]
    tile[1][2] = tile[1][2][::-1]

def have_match(t0, t1, direction):
    direction2 = (direction + 2) % 4
    for j in range(2):
        if j == 1:
            flip(t1)
        for i in range(0, 5):
            rotate(t1, i)

            if t0[1][direction] == t1[1][direction2][::-1]:
                return True
    return False

def place_one(tile):    
    for k, v in d.items():
        for i in range(4):
            mov = moves[i]
            pos = (k[0] + mov[0], k[1] + mov[1])
            if pos not in d:
                if have_match(v, tile, i):
                    d[pos] = tile
                    return True
    return False

while tiles:
    for tile in tiles:
        if place_one(tile):
            tiles.remove(tile)
            break

print(d.keys())

x = [p[0] for p in d.keys()]
y = [p[1] for p in d.keys()]

min_x = min(x)
max_x = max(x)
min_y = min(y)
max_y = max(y)

dx = max_x - min_x + 1
dy = max_y - min_y + 1

print(dx, dy)
print(len(d))
assert dx == dy and dx * dy == len(d)

for i in range(min_x, max_x + 1):
    for j in range(min_y, max_y + 1):
        print(d[(i, j)][0], end=' ')
    print()

mult = 1
for k, v in d.items():
    if k[0] == min_x and k[1] == min_y:
        print(v[0])
        mult *= v[0]
    if k[0] == min_x and k[1] == max_y:
        print(v[0])
        mult *= v[0]

    if k[0] == max_x and k[1] == min_y:
        print(v[0])
        mult *= v[0]
    if k[0] == max_x and k[1] == max_y:
        print(v[0])
        mult *= v[0]

print(mult)
