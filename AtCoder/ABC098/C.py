# TLE
#n = int(input())
#s = input()
#result = [0] * n
#for i in range(n):
#    for j in range(i):
#        if s[j] == 'W':
#            result[i] += 1
#    for j in range(i+1, n):
#        if s[j] == 'E':
#            result[i] += 1
#print(min(result))

n = int(input())
s = input()
w = [0] * n
e = [0] * n
w[0] = 1 if s[0] == 'W' else 0
e[-1] = 1 if s[-1] == 'E' else 0
for i in range(1, n):
    w[i] = w[i-1]
    w[i] += 1 if s[i] == 'W' else 0
for i in range(n-2, -1, -1):
    e[i] = e[i+1]
    e[i] += 1 if s[i] == 'E' else 0
min_count = n
for i in range(n):
    count = w[i] + e[i] - 1
    if count < min_count:
        min_count = count
print(min_count)