a = int(input("Gimme a: "))
b = int(input("Gimme b: "))

def gcd(a: int, b: int):
    print(f"Current pair is {a} and {b}")
    if b > a:
        a, b = b, a
    t, a = divmod(a, b)
    if a == 0:
        return b
    
    return gcd(a, b)

print(gcd(a, b))