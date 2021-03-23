s = input()
acgt = ['A', 'C', 'G', 'T']
max_cnt = 0
cnt = 0

for i in range(len(s)):
    if s[i] in acgt:
        cnt += 1
    else:
        if cnt > max_cnt:
            max_cnt = cnt
        cnt = 0

print(max(cnt, max_cnt))
