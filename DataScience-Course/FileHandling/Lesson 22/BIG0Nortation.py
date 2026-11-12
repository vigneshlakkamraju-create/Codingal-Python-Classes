n = 10

guess = input(" Double Loop at n = 10 checks n x b pairs. How many?")

input("Formula: one calculation, done. Press Enter to run ")
steps = 0
for i in range(n):
    steps += 1
print(" steps=", steps, " 0(1) constant time, steps never change" )

input("Loop: one step per time. Press Enter to run ")
steps = 0
for i in range(n):
    steps += 1
print(" steps=", steps, " 0(n) linear time, steps change with n" )

input("Double Loop: one step per time. Press Enter to run ")
steps = 0
for i in range(n):
    for j in range(n):
        steps += 1
print(" steps=", steps, " 0(n^2) quadratic time, steps change with n^2" )

input("Two more notations. Press Enter to run ")
print("Big Omega: best case lower bound for an algorithm, Big O: worst case upper bound for an algorithm, Big Theta: average case bound for an algorithm")