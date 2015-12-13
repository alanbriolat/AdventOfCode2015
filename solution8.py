from __future__ import print_function
import re


# Part 1
code1 = 0
mem1 = 0
transform = re.compile(r'\\\\|\\"|\\x[0-9a-f]{2}')
for line in open('input8.txt'):
    line = line.strip()
    clean = transform.sub('_', line)
    code1 += len(line)
    mem1 += len(clean) - 2
print('Part 1:', code1 - mem1)

# Part 2
mem2 = 0
code2 = 0
for line in open('input8.txt'):
    line = line.strip()
    new = line.replace('\\', '\\\\').replace('"', '\\"')
    mem2 += len(line)
    code2 += len(new) + 2
print('Part 2:', code2 - mem2)