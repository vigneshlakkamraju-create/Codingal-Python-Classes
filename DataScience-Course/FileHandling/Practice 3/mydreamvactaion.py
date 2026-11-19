from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title("My Dream Vacation")
window.geometry("450x480")
window.configure(bg="lightcyan")

title_label = Label(window, text="My Dream Vacation", font=("Arial", 20, "bold"), bg="blue", fg="white")
title_label.place(relx=0.5, y=30, anchor=CENTER)

beach_image = Image.open("Beach.jpg")
beach_image = beach_image.resize((320, 200))
beach_img = ImageTk.PhotoImage(beach_image)
image_label = Label(window, image=beach_img, bg ="lightcyan")
image_label.place(relx=0.5, y=165, anchor=CENTER)


def show_message():
    messagebox.showinfo("Why I Love this Place", "The beach is a perfect place to relax!")

why_button = Button(window, text="Why I Love this Place", command=show_message, bg="blue", fg="white")
why_button.place(relx=0.5, y=320, anchor=CENTER)

def show_details():
    details = Toplevel(window)
    details.title("Vacation Details")
    details.geometry("300x200")
    details.configure(bg="lightyellow")

    Label(details, text="Destination: Goa", font=("Arial", 16,), bg="lightyellow").pack(pady=10)
    Label(details, text="Country: India", font=("Arial", 14), bg="lightyellow").pack(pady=10)
    Label(details, text="Favorite Activity: Swimming", font=("Arial", 12), bg="lightyellow").pack(pady=10)

details_button = Button(window, text="Vacation Details", command=show_details, bg="blue", fg="white")
details_button.place(relx=0.5, y=370, anchor=CENTER)


window.mainloop()