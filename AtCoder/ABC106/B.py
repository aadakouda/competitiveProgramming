n = int(input())
nums = [i for i in range(1, n + 1, 2)]
cnt1 = 0
cnt2 = 0

for i in nums:
    cnt2 = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt2 += 1
    if cnt2 == 8:
        cnt1 += 1

print(cnt1)
