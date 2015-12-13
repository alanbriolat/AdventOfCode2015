from __future__ import print_function


# Part 1
sum1 = 0
for line in open('input2.txt'):
    dims = sorted(map(int, line.split('x')))
    sum1 += (3 * dims[0] * dims[1] +
             2 * dims[1] * dims[2] +
             2 * dims[2] * dims[0])
print('Part 1:', sum1)

# Part 2
sum2 = 0
for line in open('input2.txt'):
    dims = sorted(map(int, line.split('x')))
    sum2 += (2 * dims[0] +
             2 * dims[1] +
             dims[0] * dims[1] * dims[2])
print('Part 2:', sum2)