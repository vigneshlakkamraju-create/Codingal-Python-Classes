import os

print("===Science Notes===")
with open("science_notes.txt", "r") as f:
    for line in f:
        print(line.strip())
print()


print("=== Word Count ===")
with open("math_notes.txt", "r") as f:
    for line in f:
        words = line.split()
        print(f"Line: {line.strip()} - Word Count: {len(words)}")
print()

print("=== Merging Notes ===")
if os.path.exists("all_notes.txt"):
    print("all_notes.txt already exists. Merging notes into it.")
else:
    print("Creating all_notes.txt and merging notes into it.")

content = ""
with open("science_notes.txt", "r") as f:
    content += "--- Science Notes ---\n"
    content += f.read() + "\n"
with open("math_notes.txt", "r") as f:
    content += "--- Math Notes ---\n"
    content += f.read() + "\n"
with open("all_notes.txt", "w") as out:
    out.write(content)
print("Notes merged into all_notes.txt successfully.")
print()

if os.path.exists("all_notes.txt"):
    os.remove("all_notes.txt")
    print("all_notes.txt has been deleted.")
else:
    print("all_notes.txt does not exist")