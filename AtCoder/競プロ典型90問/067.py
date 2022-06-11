def to_9(n):
    result = ''
    n = to_10(n)
    while n >= 9:
        result = str(n%9) + result
        n //= 9
    result = str(n) + result
    return result

def to_10(n):
    n = str(n)[::-1]
    return sum([int(n[i]) * (8**i) for i in range(len(n))])

n, k = map(int, input().split())
result = n
for i in range(k):
    result = to_9(int(result)).replace('8', '5')
print(result)
