n = int(input("How many characters to preview? "))
file = open("india.txt", "r")
print(file.read(n))
file.close()
print()

file = open("india.txt", "r")
lines = file.readlines()
file.close()
print("Total number of lines in the file: ", len(lines))
for i in range(len(lines)):
    print("Line", i + 1, ":", lines[i].strip())
print()

word = input("Skip lines starting with: ")
file = open("india.txt", "r")
for line in file:
    if not line.startswith(word):
        print("skipping line:", line.strip())
    else:
        print("printing line:", line.strip())
file.close()
print()

file = open("india.txt", "r")
lines = file.readlines()
file.close()
out = open("india_cleaned.txt", "w")
for i in range(len(lines)):
    if not lines[i].startswith(word):
        out.write(lines[i])
out.close()
print("Odd lines saved to india_cleaned.txt")