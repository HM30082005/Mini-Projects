a = int(input('a: '))
b = int(input('b: '))
if a < b:
    a, b = b, a
tab = [[1, 0, a], [0, 1, b]]

def gcd(a, b):
    if a < b:
        a, b = b, a
    q, r = divmod(a, b)
    n = tab[len(tab) - 2][0] - tab[len(tab) - 1][0] * q
    m = tab[len(tab) - 2][1] - tab[len(tab) - 1][1] * q
    tab.append([n, m, r])
    if r == 0: return 0
    gcd(b, r)

gcd(a, b)
for i in range(len(tab)):
    for j in range(3):
        print(tab[i][j], end=" ")
    print()
