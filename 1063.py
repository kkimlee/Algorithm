import sys

k_pos, r_pos, num = sys.stdin.readline().split()

num = int(num)

k_x_pos = ord(k_pos[0]) - ord('A')
k_y_pos = 8 - int(k_pos[1])

r_x_pos = ord(r_pos[0]) - ord('A')
r_y_pos = 8 - int(r_pos[1])

r_move = False
for i in range(num):

    x_pos = 0
    y_pos = 0

    r_move = False
    move = sys.stdin.readline()

    for j in range(len(move)):
        if(move[j] == 'R'):
            x_pos = 1
        elif(move[j] == 'L'):
            x_pos = -1
        elif(move[j] == 'B'):
            y_pos = 1
        elif(move[j] == 'T'):
            y_pos = -1

    k_x_pos += x_pos
    k_y_pos += y_pos

    if(k_x_pos == r_x_pos and k_y_pos == r_y_pos):
        r_move = True
        r_x_pos += x_pos
        r_y_pos += y_pos

    if(k_x_pos < 0 or k_x_pos >= 8 or k_y_pos < 0 or k_y_pos >= 8 or r_x_pos < 0 or r_x_pos >= 8 or r_y_pos < 0 or r_y_pos >= 8):
        k_x_pos -= x_pos
        k_y_pos -= y_pos

        if(r_move):
            r_x_pos -= x_pos
            r_y_pos -= y_pos

k_x_pos = chr(k_x_pos + ord('A'))
k_y_pos = 8 - k_y_pos

r_x_pos = chr(r_x_pos + ord('A'))
r_y_pos = 8 - r_y_pos

print(k_x_pos + str(k_y_pos))
print(r_x_pos + str(r_y_pos))