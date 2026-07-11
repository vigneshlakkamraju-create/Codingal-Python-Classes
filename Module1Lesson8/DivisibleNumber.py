numn = int(input("Enter a numerator: "))

numd = int(input("Enter a denominator: "))

if numn % numd == 0:
    print(str(numn) + " is divisible by " + str(numd))
else:
    print(str(numn) + " is not divisible by " + str(numd))