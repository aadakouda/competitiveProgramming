n = int(input())
s = input()
flg1 = [0 for _ in range(10)]
cnt = 0

for i in range(10):
    if str(i) not in s:
        continue
    if flg1[i] == 1:
        continue
    flg1[i] = 1
    flg2 = [0 for _ in range(10)]
    for j in range(10):
        if str(j) not in s[s.find(str(i)) + 1:]:
            continue
        if flg2[j] == 1:
            continue
        flg2[j] = 1
        for k in range(10):
            if str(k) not in s[s.find(str(j), s.find(str(i)) + 1) + 1:]:
                continue
            cnt += 1

print(cnt)
