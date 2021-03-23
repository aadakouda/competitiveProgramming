a, b, k = map(int, input().split())
cnt_k = 0

for i in range(max(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        cnt_k += 1
    if cnt_k == k:
        print(i)
        break
