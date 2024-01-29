import numpy as nmp

def gen_norm_test(a):
    sd = 500
    mean = 0
    random_numbers = nmp.random.normal(loc = mean, scale = sd, size=a)

    f = open("prizes.txt", "w")
    for i in random_numbers:
        f.write(str(i) + "\n")
        # print(i, end = ",")