scores = [3, 7 , 2, 9, 5 , 5 ,6 , 8, 1]

input("List: " + str(scores) + " Linear search - Press Enter to run ")

target = int(input("Enter a target value to search for: "))

input("Searching for " + str(target) + " in the list. Press Enter to run ")
steps = 0
for score in scores:
    steps += 1
    if score == target:
        print("Found " + str(target) + " in the list after " + str(steps) + " steps.")
        break


input("Compare with the best case and worst case scenarios. Press Enter to run ")
mid = len(scores) // 2
print("Best: 1 check - 0(1) constant time, Average:", mid, "checks - 0(n) linear time, Worst: 9 checks - 0(n) linear time")

input("All three cases. press Enter to run ")
print("Best: 1 check - 0(1) constant time, Average:", mid, "checks - 0(n) linear time, Worst: 9 checks - 0(n) linear time")
