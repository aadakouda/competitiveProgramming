a, b, c, x, y = map(int, input().split())
price = 0
ab_price = min(a + b, c * 2)
remain_num = abs(x - y)
price += ab * min(x, y)
price += remain_num * min(c * 2, a if x > y else b)
print(price)
