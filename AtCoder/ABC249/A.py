a, b, c, d, e, f, x = map(int, input().split())
t_dis = x // (a+c) * a * b
t_dis += b * (x%(a+c)) if x%(a+c) <= a else b * a
a_dis = x // (d+f) * d * e
a_dis += e * (x%(d+f)) if x%(d+f) <= d else e * d
print('Takahashi' if t_dis > a_dis else 'Aoki' if a_dis > t_dis else 'Draw')