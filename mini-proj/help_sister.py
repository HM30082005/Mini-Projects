for i in range(0,100):
    u = 0.72 * float(i)
    l = 5.0 / 7.0 * float(i)
    if int(u) > l and int(u) < u:
        print(i, int(u))