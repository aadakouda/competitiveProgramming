a, b, c = map(int, input().split())
s_lst = [a*i%b for i in range(1, b+1)]
print('YES' if c in s_lst else 'NO')