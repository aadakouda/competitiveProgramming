n = int(input())
result = set()

i = 1
# range(1, n**0.5)はintにしてもうまくいかない
while i*i <= n:
    if n % i == 0:
        result.add(i)
        result.add(n//i)
    i += 1
print('\n'.join(map(str, sorted(list(result)))))
