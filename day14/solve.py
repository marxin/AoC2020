#!/usr/bin/env python3

BITS = 36

data = open('input.txt').read()
lines = data.splitlines()

mask_and = None
mask_or = None
mem = {}

for line in lines:
    lhs, rhs = line.split(' = ')
    if lhs == 'mask':
        assert len(rhs) == BITS
        mask_and = int(rhs.replace('X', '1'), 2)
        mask_or = int(rhs.replace('X', '0'), 2)
    else:
        assert lhs.startswith('mem')
        index = int(lhs.replace('[', ']').split(']')[1])
        value = int(rhs)
        mem[index] = (value & mask_and) | mask_or
        print(f'{mem[index]:b}')

print(sum(mem.values()))
