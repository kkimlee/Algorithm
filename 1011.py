import sys

num = int(sys.stdin.readline())

start = []
end = []
for i in range(num):
    _start, _end = map(int, sys.stdin.readline().split())

    start.append(_start)
    end.append(_end)

count = []
for i in range(len(start)):
    loc = start[i]
    cnt = 0
    tmp = 0
    dist = end[i] - loc

    while(tmp**2 <= dist):
        tmp += 1
    tmp -= 1

    if dist == tmp**2:
        cnt = 2 * tmp - 1
    elif dist <= (tmp**2 + (tmp+1)**2)/2:
        cnt = 2 * tmp
    else:
        cnt = 2 * tmp + 1

    count.append(cnt)

for i in count:
    print(i)