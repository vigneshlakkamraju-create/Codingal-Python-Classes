import os

# Part 1
with open("student.txt", "r") as f:
    print(f.read(50))

# Part 2
with open("student.txt", "r") as f:
    lines = f.readlines()
print("Total records:", len(lines))
number = 1
for line in lines:
    print(number, line.strip())
    number = number + 1

# Part 3
count = 0
with open("student.txt", "r") as f:
    for line in f:
        data = line.strip().split(",")
        print("Name:", data[1].strip(), "Marks:", data[3].strip())
        count += 1
print("Total records:", count)

# Part 4
with open("student.txt", "r") as f:
    for line in f:
        data = line.strip().split(",")
        if data[2].strip() == "Python":
            print(line.strip())

# Part 5
with open("student.txt", "r") as f:
    with open("python_students.txt", "w") as new:
        for line in f:
            data = line.strip().split(",")
            if data[2].strip() == "Python":
                new.write(line)
print("python_students.txt file created successfully.")

# Part 6
important = 0
todo = 0
with open("activities.txt", "r") as f:
    for line in f:
        if line.startswith("IMPORTANT"):
            print(line.strip())
            important = important + 1
        if line.startswith("TODO"):
            print(line.strip())
            todo = todo + 1
print("IMPORTANT count:", important)
print("TODO count:", todo)

# Part 7
with open("activities.txt", "r") as f:
    with open("important_tasks.txt", "w") as new:
        for line in f:
            if line.startswith("IMPORTANT"):
                new.write(line)
print("important_tasks.txt file created successfully.")

# Part 8
with open("subjects.txt", "r") as f:
    subjects = f.read()
with open("important_tasks.txt", "r") as f:
    tasks = f.read()
with open("final_notes.txt", "w") as f:
    f.write(subjects + "\n" + tasks)
print("final_notes.txt file created successfully.")

# Part 9
if os.path.exists("final_notes.txt"):
    print("final_notes.txt file exists.")
else:
    print("final_notes.txt file does not exist.")

# Part 10
if os.path.exists("python_students.txt"):
    os.remove("python_students.txt")
    print("python_students.txt file deleted successfully.")
else:
    print("python_students.txt file does not exist.")