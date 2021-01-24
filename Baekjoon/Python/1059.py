import sys

num = int(sys.stdin.readline())

section = list(sys.stdin.readline().split())

for i in range(num):
    section[i] = int(section[i])

section.sort()

n = int(sys.stdin.readline())

count = 0

for i in range(num-1):
    if (i == 0 and n < section[0]):
        for j in range(1, section[0]):
            if(n > j):
                count += section[0] - n
            elif(n == j):
                count += section[0] - n - 1

    elif(n > section[i]  and n < section[i+1]):
        for j in range(section[i]+1, section[i+1]):
            if(n > j):
                count += section[i+1] - n
            elif(n == j):
                count += section[i+1] - n - 1

print(count)