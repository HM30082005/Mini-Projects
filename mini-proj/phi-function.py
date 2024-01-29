def gcd(a, b):
    if b > a:
        a, b = b, a
    if a % b == 0:
        return b
    return gcd(b, a % b)

def prime(p):
    i = 2
    while i * i < p:
        if p % i == 0:
            return False
        i += 1
    return True

def phi_func(n):
    res = 0
    if prime(n):
        return n - 1
    for i in range(1, n):
        if gcd(n, i) == 1:
            res += 1
            print(f"i: {i}")
    return res


n = int(input('n: '))
print(f"phi(n) = {phi_func(n)}")
