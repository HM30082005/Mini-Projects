def factor(n):
    i = 2
    res = {}
    while i <= n:
        while n % i == 0:
            if i in res.keys():
                res[i] += 1
            else:
                res[i] = 1
            n /= i
        i += 1
    return res

def phi(n):
    res = 1
    f = factor(n)
    for p in f.keys():
        # print(f"p: {p}\tmult: {(p - 1) * (p^(f[p] - 1))}\tpow: {(f[p] - 1)}")
        res *= (p - 1) * (pow(p, (f[p] - 1)))
    return res

print(factor(int(input('n: '))))
print(phi(int(input('n: '))))
# print(pow(11, 0))