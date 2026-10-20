# Part 1 - Import libraries and set up the main window
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
window = Tk()
window.title("My Photo Album")
window.geometry("400x420")

# Part 2 - Add a title label and display an image
title = Label(window, text="My Photo Album", fg="white", bg="purple", width=40)
title.pack(pady=10)
img_file = Image.open("C:\Codingal Python Classes\DataScience-Course\FileHandling\Module3Lesson5\OIP.webp")
img = img_file.resize((300, 100))
photo = ImageTk.PhotoImage(img)
pic = Label(window, image=photo)
pic.pack(pady=5)

#Part 3 - Create a function to show a message box
def show_message():
    messagebox.showinfo("Message", "Welcome to My Photo Album!")
msg_btn = Button(window, text="Click to React", bg="blue", command=show_message)
msg_btn.pack(pady=5)

#Part 4 - Create a function to open a new window with photo details
def show_details():
    details_window = Toplevel(window)
    details_window.title("Photo Details")
    details_window.geometry("200x120")
    details_label = Label(details_window, text="Photo Details:\n- Name: img.jfif\n- Size: 300x100", fg="black", bg="lightgray", width=40)
    details_label.pack(pady=5)
    place = Label(details_window, text="Location: My Garden")
    place.pack()
    details_window.mainloop()
details_btn = Button(window, text="Show Photo Details", bg="green", command=show_details)
details_btn.pack(pady=5)

# Part 5 - Run the main loop
window.mainloop()
