# https://algo-method.com/tasks/567

l, r = map(int, input().split())
result = 0
for i in range(l, r+1):
    result += (2 * i - 1) ** 2
print(result)
