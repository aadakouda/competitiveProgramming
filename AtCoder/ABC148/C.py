a, b = map(int, input().split())

def max_div(a, b):
    if a % b == 0:
        return b
    return max_div(b, a%b)

mb = max_div(a, b)
a = a // mb
b = b // mb
print(mb * a * b)
