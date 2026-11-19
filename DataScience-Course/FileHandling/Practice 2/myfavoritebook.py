from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title("My Favorite Book")
window.geometry("400x460")
window.configure(bg="lightblue")

book_img = Image.open("download.jpg")
book_img = book_img.resize((250,220))
book_img = ImageTk.PhotoImage(book_img)
image_label = Label(window, image=book_img, bg="lightblue")
image_label.place(relx=0.5, y=175, anchor=CENTER)

title_label = Label(window, text="My favorite book", font=("Arial", 20, "bold"), bg="lightblue")
title_label.place(relx=0.5, y=340, anchor=CENTER)

def show_message():
    messagebox.showinfo("Why Read Books?", "Reading books makes us smarter!")

why_button = Button(window, text="Why Read Books?",
                     command=show_message, font=("Arial", 12), bg="brown", fg="white")
why_button.place(relx=0.5, y=320, anchor=CENTER)

def show_details():
    details = Toplevel(window)
    details.title("Book Details")
    details.geometry("300x200")
    details.configure(bg="lightyellow")

    Label(details, text="Book Name: The Jungle Book", font=("Arial", 12), bg="lightyellow").pack(pady=10)
    Label(details, text="Author: Rudyard Kipling", font=("Arial", 12), bg="lightyellow").pack(pady=10)
    Label(details, text="Genre: Adventure", font=("Arial", 12), bg="lightyellow").pack(pady=10)

details_button = Button(window, text="Book Details",
                        bg = "brown", fg="white", font=("Arial", 12), command=show_details)
details_button.place(relx=0.5, y=370, anchor=CENTER)


window.mainloop()