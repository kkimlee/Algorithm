import sys

N, K = map(int, sys.stdin.readline().split())

person = []

for i in range(N):
    person.append(i+1)

remove_seq = []
remove_idx = 0
while(len(person) != 0):
    for i in range(K):
        remove_idx += 1
        if remove_idx > N:
            remove_idx -= N
            N = len(person)

    remove_seq.append(person[remove_idx - 1])
    del person[remove_idx-1]
    remove_idx -= 1
    N = len(person)

print('<', end='')
print(', '.join(map(str, remove_seq)), end='')
print('>')