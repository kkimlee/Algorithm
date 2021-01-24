import sys
import numpy as np

num = list(map(int, sys.stdin.readline().split()))

divisor = [0 for _ in range(100)]

for i in num:
    while i != 1:
        for j in range(2, i+1):
            if i % j == 0:
                i //= j
                divisor[j] += 1
                break
divisor2 = []
for i in range(len(divisor)):
    if divisor[i] >= 3:
        divisor2.append(i)

print(divisor2)