import sys

num = int(sys.stdin.readline())

divisor = list(sys.stdin.readline().split())

for i in range(num):
    divisor[i] = int(divisor[i])

print(min(divisor)*max(divisor))
