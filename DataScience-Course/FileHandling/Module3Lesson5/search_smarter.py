def linear_search(items, target):
    """ Checks items one by one to see if the target is present. Returns True if found, False otherwise. """
    checks = 0
    for i in range(len(items)):
        checks = checks +1
        if items[i] == target:
            return i, checks
    return -1, checks

def report(checks,low,mid,high, value):
    """Print one round of binary search, showing the current low, mid, and high values.""" 

    print(" check", checks, "low =", low, "mid =", mid, "high =", high, "value =", value)

def binary_search(items, target, show=False):
    """ Return (index of target or -1, number of checks). items must be sorted """
    low = 0
    high = len(items) - 1
    checks = 0

    while low <= high:
        checks += 1
        mid = (low + high) // 2

        if items[mid] == target:
            if show:
                report(checks, low, mid, high, target)
            return mid, checks
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

        if show:
            report(checks, low, mid, high, target)

    return -1, checks


scores = [1, 3, 5, 7, 9, 11, 13, 15, 17]
print("Sorted list:", scores, " n =", len(scores))
present = int(input("Search for a number that IS in the list: "))
absent = int(input("Search for a number that is NOT in the list: "))
for target in [present, absent]:
    print()
    print("Binary search for", target)
    index, checks = binary_search(scores, target, show=True)
    if index == -1:
        print(f"Result: {target} is not in the list {checks} checks.")
    else:
        print(f"Result: {target} found at index {index} ({checks} checks.)")

print()
print("target | linear checks | binary checks")
for target in [1, 9, 17, 4]:
    print(f"{target:>6} | {linear_search(scores, target)[1]:>13} | {binary_search(scores, target)[1]:>13}")

print()
print("Worst case: search for a number bigger than every item in the list")
for n in [9, 100, 1000, 10000]:
    items = list(range(n))
    checks = binary_search(items, n)[1]
    print(f"n = {n:>9,}  binary checks = {checks}")

