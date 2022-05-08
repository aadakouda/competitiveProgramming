n = int(input())
cnt = 0

for i in range(1, n+1):
    i_list = list(str(i))
    if '7' in i_list:
        continue
    i8_list = []
    while i > 8:
        i8_list.append(i%8)
        i //= 8
    i8_list.append(i)
    if 7 in i8_list:
        continue
    cnt += 1

print(cnt)
