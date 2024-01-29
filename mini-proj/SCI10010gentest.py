import random as r
def gen_unif_rand(n, low, high):
    # Open a file to store the prizes
    f = open("prizes.txt", "w")

    # User input for the number of non-empty doors
    # n = int(input('Enter the amount of non-empty doors wanted: '))

    # Generate random prizes for each non-empty door
    prizes = []
    for i in range(n - 1):
        element = r.randint(low, high)
        prizes.append(element)

    # Write prizes to the file
    for i in range(len(prizes) - 1):
        f.write(str(prizes[i]) + "\n")
        # print(str(prizes[i]) + ",", end="")

    # Write the last prize
    f.write(str(prizes[-1]) + "\n")

    # Close the file
    f.close()

    # Print the last prize
    # print(str(prizes[-1]), end="\n")
