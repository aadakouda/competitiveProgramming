n, k = map(int, input().split())
S = [input() for _ in range(n)]
result = []

for i in range(2**n):
    temp = ''
    for j in range(n):
        if ((i >> j) & 1):
            temp += S[j]
    char_dict = {}
    for t in temp:
        if t not in char_dict:
            char_dict[t] = 1
        else:
            char_dict[t] += 1
    cnt = 0
    for v in char_dict.values():
        if v == k:
            cnt += 1
    result.append(cnt)

print(max(result))