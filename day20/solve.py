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

print(len(tiles))
d = {(0, 0): tiles[0]}

def rotate(tile):
    tile[1].rotate()

def flip(tile):
    tmp = tile[1][0][::-1]
    tile[1][0] = tile[1][2][::-1]
    tile[1][2] = tmp

    tile[1][1] = tile[1][1][::-1]
    tile[1][3] = tile[1][3][::-1]

def have_match(t0, t1, direction):
    direction2 = (direction + 2) % 4
    for j in range(2):
        if j == 1:
            flip(t1)
        for i in range(4):
            rotate(t1)
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
                    good = True
                    for j in range(4):
                        mov2 = moves[j]
                        pos2 = (pos[0] + mov2[0], pos[1] + mov2[1])
                        if pos2 in d:
                            if not have_match(tile, d[pos2], j):
                                good = False
                    if good:
                        d[pos] = tile
                        return True
    return False


moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
tiles = tiles[1:]

while tiles:
    print(len(d))
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

mult = d[(min_x, min_y)][0] * d[(max_x, min_y)][0] * d[(min_x, max_y)][0] * d[(max_x, max_y)][0]

print(mult)
