file = open("bucket-list.txt", "w")
file.write("1. Visit the Eiffel Tower\n")
file.write("2. Go on a safari in Africa\n")
file.write("3. Learn to play the guitar\n")
file.close()

print("Bucket list has been created and saved to 'bucket-list.txt'.")

file = open("bucket-list.txt", "r")
content = file.read()
print("\n=== My Bucket List ===")
print(content)
file.close()


file = open("bucket-list.txt", "r")
lines = file.readlines()
print(f"You have {len(lines)} items in your bucket list.")
file.close()

file = open("bucket-list.txt", "a")
file.write("4. Skydive over the Grand Canyon\n")
file.write("5. Write a book\n")
file.close()
print("\n2 more items added")

file = open("bucket-list.txt", "r")
print("\n=== Updated Bucket List ===")
print(file.read())
file.close()