import random as r
import math as mt

def Sim(n, trials):
    # Reading the list of prizes from a file
    print('Prizes list will be read from the prepared file...', end="")
    f = open("prizes.txt", "r")
    a = f.readlines()
    m = len(a)
    for i in range(m):
        a[i] = float(a[i])

    # Creating a list of doors, with n doors having nothing behind them and m doors with prizes
    doors = [0 for i in range(n)]
    doors += a
    # print(doors)

    # Initializing variables to count wins with and without switching
    wins = 0
    wins_s = 0
    average_winnings = 0
    average_winnings_s = 0

    # Running the simulation for the specified number of trials
    for iter in range(trials):
        # Making an initial choice
        choice = r.randint(0, m + n - 1)

        # Checking if the chosen door has a prize
        if doors[choice] != 0:
            wins += 1
        if doors[choice] != 0:
            average_winnings += doors[choice]

        # Switching doors
        l = 0
        if choice == 0:
            l = 1
        choice_switch = r.randint(0, m + n - 1)

        # Host opened the first door with nothing (a goat) behind it
        while choice_switch == choice or choice_switch == l:
            choice_switch = r.randint(0, m + n - 1)

        # Checking if the switched door has a prize
        if doors[choice_switch] != 0:
            wins_s += 1
        if doors[choice_switch] != 0:
            average_winnings_s += doors[choice_switch]

    # Calculating expected winnings using the formula
    total_sum = sum(doors)
    sump, sumn = 0, 0
    for i in doors:
        if i > 0:
            sump += i
        else:
            sumn -= i

    ex_w = total_sum / (m + n)
    ex_s_w = ((m + n - 1) * total_sum) / ((m + n) * (m + n - 2))
    if ex_w == 0:
        ex_w += 0.000000001
    if ex_s_w == 0:
        ex_s_w += 0.000000001
    # Calculating probability to open non-empty door (win in variation with goats and cars)
    p_win = m / (m + n)
    p_s_win = (m * (m - 1) + m * n) / ((m + n) * (m + n - 2))

    # Standard deviation
    qq = 0
    mean = total_sum / len(doors)
    for i in doors:
        qq += (i - mean) * (i - mean)
    sd = mt.sqrt(qq / len(doors))

    # print(f"\n\tStandard deviation: {sd}")

    # # Printing the results
    # print(f"\nSum of all prizes is {total_sum}, sum of prizes is {sump}, the absolute value of penalties is {sumn}")
    # print(f"\nAmoint of times when non-empty door was picked if decided not to switch {wins}")
    # print(f"Amoint of times when non-empty door was picked if decided to switch {wins_s}\n")

    # print(f"\nAverage winnings if decided not to switch {average_winnings / trials} compared to theoretical expected winnings of {ex_w}")
    # print(f"\tHence the percentage error is {abs(((average_winnings / trials) - ex_w) / ex_w) * 100}%")
    # print(f"Average winnings if decided to switch {average_winnings_s / trials} compared to theoretical expected winnings of {ex_s_w}")
    # print(f"\tHence the percentage error is {abs(((average_winnings_s / trials) - ex_s_w) / ex_s_w) * 100}%\n")

    # # Calculating and printing the win ratio without switching
    ratio = wins / trials
    # print(f"If decide not to switch the percentage of picking a non-empty door is {ratio * 100}% compared to theoretical percentage of {p_win * 100}%")
    # print(f"\tHence the percentage error is {abs((ratio - p_win) / p_win) * 100}%")

    # # Calculating and printing the win ratio with switching
    ratio = wins_s / trials
    # print(f"If decide to switch the percentage of picking a non-empty door is {ratio * 100}% compared to theoretical percentage of {p_s_win * 100}%")
    # print(f"\tHence the percentage error is {abs((ratio - p_s_win) / p_s_win) * 100}%")

    # Closing the file
    f.close()

    return [(average_winnings / trials), (average_winnings_s / trials), total_sum]


