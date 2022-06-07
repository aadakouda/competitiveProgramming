n = int(input())
s = [input() for _ in range(n)]
sec = [0] * 10
for i in range(10):
    pushed = [False] * n
    cnt = 0
    while not all(pushed):
        sec[i] = 10 * cnt
        for j in range(10):
            for k in range(n):
                if not pushed[k] and s[k][j] == str(i):
                    pushed[k] = True
                    sec[i] = cnt * 10 + j
                    break
        cnt += 1
print(min(sec))