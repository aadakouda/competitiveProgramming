n = int(input())
s = [''] * (n+1)
s[1] = '1'
for i in range(2, n+1):
    s[i] = ' '.join([s[i-1], str(i), s[i-1]])
s.pop(0)
print(s[-1])