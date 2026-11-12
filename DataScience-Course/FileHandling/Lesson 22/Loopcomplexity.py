n = int(input("Enter any n (try 5, 10, or 50): "))

input("One loop: one step per time. Press Enter to run ")
for i in range(n):
    pass
print(" steps=", n, " 0(n) linear time, steps change with n" )

input("Two nested loops - run n x n times. Press Enter to run ")
for i in range(n):
    for j in range(n):
        pass
print(" steps=", n*n, " 0(n^2) quadratic time, steps change with n" )

input("Rule: count the loops. Press Enter to run ")
print("One loop = 0(n) linear time, Two nested loops = 0(n^2) quadratic time, Three nested loops = 0(n^3) cubic time, Four nested loops = 0(n^4) quartic time, Five nested loops = 0(n^5) quintic time")