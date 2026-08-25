classmates = ["Aarav", "Priya", "Rahul", "Sneha", "Dev"]
print("Classmates List:", classmates)

print("Total Students:", len(classmates))
print("First Student:", classmates[0])
print("Last Student:", classmates[-1])
print("First three:", classmates[:3])

classmates.append("Meera")
print("\nAfter adding Meera:", classmates)
classmates.remove("Dev")
print("After removing Dev:", classmates)
classmates.sort()
print("Sorted Classmates List:", classmates)
classmates.reverse()
print("Reversed Classmates List:", classmates)

teacher = {"name": "Mr. Sharma", "subject": "Python", "experinece": 5}
print("\nTeacher Details:", teacher)

print("Subject:", teacher["subject"])
print("Experience:", teacher.get("experience", "Not Found"))
teacher["experience"] = 6
teacher["email"] = "sharma@school.com"
teacher.pop("experinece")
print("\nUpdated Teacher Details:", teacher)

roll_numbers = [1,2,3,4,5]
names = ["Aarav", "Priya", "Rahul", "Sneha", "Dev"]
student_directory = dict(zip(roll_numbers, names))
print("\nStudent Directory:", student_directory)
print("Student with Roll Number 3:", student_directory[3])