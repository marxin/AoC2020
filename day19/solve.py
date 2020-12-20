#!/usr/bin/env python3

import re

data = open('input.txt').read()

first, second = data.split('\n\n')

rules = {}
for line in first.splitlines():
    lhs, rhs = line.split(': ')
    parts = rhs.strip('"').split(' ')
    if '|' in parts:
        i = parts.index('|')
        parts.append(')')
        parts.insert(i + 1, '(')
        parts.insert(i, ')')
        parts.insert(0, '(')
    rules[lhs] = parts

data = second.splitlines()
print(rules)

start = rules['0']
while any([c for c in start if c.isdigit()]):
    print(start)
    start2 = []
    for i, v in enumerate(start):
        if v == '|' or v == '(' or v == ')':
            start2.append(v)
        elif v.isdigit():
            start2 += rules[v]
    start = start2

print(start)
regex = re.compile('^' + ''.join(start) + '$')
print(regex)

c = 0
for line in data:
    print(regex.match(line))

print(c)
