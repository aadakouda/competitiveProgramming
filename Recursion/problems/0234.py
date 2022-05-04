# https://recursionist.io/dashboard/problems/234

def maximizeCount(intArr, target):
    cache = [0] * 10_000
    for i in intArr:
        cache[i] += 1

    result_cnt = 0
    total = 0

    for i, v in enumerate(cache):
        if target < total + i*v:
            result_cnt += (target - total) // i
            break
        else:
            total += i*v
            result_cnt += v

    return result_cnt
