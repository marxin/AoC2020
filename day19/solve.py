#!/usr/bin/env python3

import re

data = open('input.txt').read()

first, second = data.split('\n\n')

rules = {}
for line in first.splitlines():
    lhs, rhs = line.split(': ')
    parts = rhs.strip('"').split(' ')
    rules[lhs] = parts

data = second.splitlines()
print(rules)

start = rules['0']
while any([c for c in start if c.isdigit()]):
    print(start)
    start2 = []
    for i, v in enumerate(start):
        if v.isdigit():
            start2.append('(')
            start2 += rules[v]
            start2.append(')')
        else:
            start2 += v
    start = start2

print(start)
regex = re.compile(''.join(start))
print(regex)

c = 0
for line in data:
    m = regex.fullmatch(line)
    if m:
        c +=1

print(c)
