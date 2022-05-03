n = int(input())
a, b, c = map(int, input().split())
result = []
for i in range(min(n//a+1, 10**4)):
    for j in range(min(n//b+1, 10**4)):
        remain = n - a*i - b*j
        if i+j > 9999 or a*i + b*j > n:
            break
        if remain % c == 0:
            result.append(i+j+(remain//c))
print(min(result))