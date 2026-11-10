input("Double Loop at n=4 took 10steps, watch it grow as n increases. Press enter to run ")

for n in [10, 100, 1000]:
    input("Double Loop at n=" + str(n) + " Press enter to run ")
    print(" steps =", n * (n + 1) // 2 )