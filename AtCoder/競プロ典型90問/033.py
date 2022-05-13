h, w = map(int, input().split())
h_max = h//2 if h % 2 == 0 else h//2+1
w_max = w//2 if w % 2 == 0 else w//2+1
if h == 1 or w == 1:
    print(h*w)
else:
    print(h_max * w_max)
