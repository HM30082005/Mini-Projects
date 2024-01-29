import random as r
import numpy as nmp
import math as mt

from SCI10010gentest import gen_unif_rand
from SCI10010gennormaltest import gen_norm_test
from SCI10010genrangetest import gen_range_test
from SCI10010MontyHallSim import Sim

# n = int(input("Aount of prizes: "))
# m = int(input("Amount of empty doors: "))
# t = int(input("Amount of trials: "))
# low = int(input('Lower: '))
# high = int(input('Higher: '))

low = -1000
high = 1000
t = 1000000
m = 2

sample = 10

# n_arr = [10, 100, 1000, 10000, 50000, 100000, 1000000]
n_arr = range(1000, 1001000, 100000)

res = []
pererr = []
av_pererr = [0, 0]

count = 1

for i in n_arr:
    for j in range(sample):
        gen_range_test(i)
        pererr = Sim(m, t)
        print(f"{count}/{len(n_arr) * sample}")
        count += 1
        av_pererr[0] += pererr[0]
        av_pererr[1] += pererr[1]
        res.append([i, pererr[0], pererr[1], pererr[2], pererr[3]])
    av_pererr[0] /= sample
    av_pererr[1] /= sample
    

f1 = open("PopulationSize.txt", "w")
f2 = open("PerErrNoS.txt", "w")
f3 = open("PerErrS.txt", "w")
f4 = open("PopulationStandardDeviation.txt", "w")
f5 = open("PopilationSum.txt", "w")    
for i in res:
    f1.write(str(i[0]) + "\n")
    f2.write(str(i[1]) + "\n")
    f3.write(str(i[2]) + "\n")
    f4.write(str(i[3]) + "\n")
    f5.write(str(i[4]) + "\n")
    # print(f'\n\n\nPopulation size:{i[0]} \n \t Percentage error no switch:{i[1]} \n \t Percentage error switch:{i[2]}')

import random as r
import numpy as nmp
import math as mt

from SCI10010gentest import gen_unif_rand
from SCI10010gennormaltest import gen_norm_test
from SCI10010genrangetest import gen_range_test
from SCI10010MontyHallSim import Sim

# n = int(input("Aount of prizes: "))
# m = int(input("Amount of empty doors: "))
# t = int(input("Amount of trials: "))
# low = int(input('Lower: '))
# high = int(input('Higher: '))

low = -1000
high = 1000
t = 1000000
m = 2

sample = 10
# n_arr = [10, 100, 1000, 10000, 50000, 100000, 1000000]
n_arr = range(100, 100100, 10000)

res = []
conj = [[0, 0], [0, 0], [0, 0]]
av_pererr = [0, 0]

count = 0

for i in n_arr:
    for j in range(sample):
        gen_range_test(i)
        res = Sim(m, t)
        count += 1
        print(f"{count}/{len(n_arr) * sample * 3}")
        if ((res[0] < res[1] and res[2] >= 0) or (res[0] > res[1] and res[2] <= 0)):
            conj[0][0] += 1
        else:
            conj[0][1] += 1
        
        gen_unif_rand(i, low, high)
        res = Sim(m, t)
        count += 1
        print(f"{count}/{len(n_arr) * sample * 3}")
        if ((res[0] < res[1] and res[2] >= 0) or (res[0] > res[1] and res[2] <= 0)):
            conj[1][0] += 1
        else:
            conj[1][1] += 1
        
        gen_norm_test(i)
        res = Sim(m, t)
        count += 1
        print(f"{count}/{len(n_arr) * sample * 3}")
        if ((res[0] < res[1] and res[2] >= 0) or (res[0] > res[1] and res[2] <= 0)):
            conj[2][0] += 1
        else:
            conj[2][1] += 1

    
print("\n", conj)
print(f"\nRange test: {(float(conj[0][0])/float(conj[0][0] + conj[0][1])) * 100}% confirming \t {(float(conj[0][1])/float(conj[0][0] + conj[0][1])) * 100}% disproving \n")
print(f"Uniform randomisation test: {(float(conj[1][0])/float(conj[1][0] + conj[1][1])) * 100}% confirming \t {(float(conj[1][1])/float(conj[1][0] + conj[1][1])) * 100}% disproving \n")
print(f"Normal distribution randomisation test: {(float(conj[2][0])/float(conj[2][0] + conj[2][1])) * 100}% confirming \t {(float(conj[2][1])/float(conj[2][0] + conj[2][1])) * 100}% disproving \n")