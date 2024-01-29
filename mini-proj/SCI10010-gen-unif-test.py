import numpy as nmp

a = int(input("Enter the amount of non-empty doors wanted: "))
lb = float(input("Enter the low boundary wanted: "))
hb = float(input("Enter the high boundary wanted: "))
random_numbers_gen = nmp.random.default_rng()
random_numbers = random_numbers_gen.integers(low = lb, high = hb, size=a)

f = open("prizes.txt", "w")
for i in random_numbers:
    f.write(str(i) + "\n")
    print(i, end = ",")