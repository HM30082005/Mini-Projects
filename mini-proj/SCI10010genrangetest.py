# import numpy as nmp

# n = int(input("Enter the amount of non-empty doors wanted: "))
def gen_range_test(n):    
    random_numbers = []
    for i in range(int(n / 2)):
        random_numbers.append(i + 1)
        random_numbers.append(i + 1)
    f = open("prizes.txt", "w")
    for i in random_numbers:
        f.write(str(i) + "\n")
        # print(i, end = ",")
# n = int(input("Enter the amount of non-empty doors wanted: "))
# random_numbers = []
# for i in range(int(n / 2)):
#     random_numbers.append(i + 1)
#     random_numbers.append(i + 1)
# f = open("prizes.txt", "w")
# for i in range(len(random_numbers) - 1):
#     f.write(str(random_numbers[i]) + ",")
#     print(random_numbers[i], end = ",")

# f.write(str(random_numbers[-1]))
# print(random_numbers[-1])
