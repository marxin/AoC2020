#!/usr/bin/env python3

import re
import copy

back_rules = {}

lines = open('input.txt').read().splitlines()

for line in lines:
    parts = line.split(' ')
    lhs = parts[0] + ' ' + parts[1]

    line = ' '.join(parts[3:])
    for m in re.findall('(\d+) ([\w ]+) bag', line):
        rhs = m[1]
        if rhs not in back_rules:
            back_rules[rhs] = set()
        back_rules[rhs].add(lhs)

start = {'shiny gold'}

while True:
    print(start)
    l = len(start)
    for item in list(start):
        if item in back_rules:
            start |= back_rules[item]
    if l == len(start):
        break

print(len(start) - 1)
