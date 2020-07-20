import sys

X = int(sys.stdin.readline())

L = [64]

while(X < sum(L)):
    s_idx = L.index(min(L))
    s = min(L)
    L[s_idx] = s/2

    if(X > sum(L)):
        L.append(s/2)
print(len(L))
