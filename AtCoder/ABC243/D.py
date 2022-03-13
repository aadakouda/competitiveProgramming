n, x = map(int, input().split())
s = list(input())
stack = []
for i in range(n):
    if len(stack) > 0 and (stack[-1] == 'R' or stack[-1] == 'L') and s[i] == 'U':
        stack.pop(-1)
        continue
    stack.append(s[i])
n = len(stack)
s = stack
for i in range(n):
    if s[i] == 'U':
        x //= 2
    elif s[i] == 'L':
        x = 2 * x
    elif s[i] == 'R':
        x = 2 * x + 1
print(x)