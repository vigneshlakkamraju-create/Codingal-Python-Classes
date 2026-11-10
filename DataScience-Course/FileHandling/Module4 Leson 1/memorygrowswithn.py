n = 4

guess = input("Predict: how many times in the list for n = 4? ")
points = list(range(1, n + 1))
print(" your guess:", guess, "points =", points, " items:", len(points))

input("Predict: what happnes to List size as n grows? Press enter to run ")
for size in [4, 10, 100, 1000]:
    print(f"n = {size:<5} List uses {size:<5} items in memory")