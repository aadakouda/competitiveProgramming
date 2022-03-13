abcd = input()
for i in range(2**3):
    val = ''
    for j in range(3):
        val += abcd[j]
        if (i >> j) & 1:
            val += '+'
        else:
            val += '-'
    val += abcd[3]
    if eval(val) == 7:
        print(val, '=7', sep='')
        break