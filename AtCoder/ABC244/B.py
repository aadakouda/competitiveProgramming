n = int(input())
t = input()
x = y = 0
d = 0
d_list = [[1, 0], [0, -1], [-1, 0], [0, 1]]

for i in range(n):
    if t[i] == 'S':
        x += d_list[d][0]
        y += d_list[d][1]
    elif t[i] == 'R':
        d += 1
        d %= 4
print(x, y)