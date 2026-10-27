#This is where we import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

#Setting up Main Window
root = Tk()
root.title("Denomination Counter")
root.configure(bg="light blue")
root.geometry("650x400")

#Adding Image and Labels in the Main Window
upload = Image.open("app_img.jpg")
#Resize the image using resize() method
upload = upload.resize((300, 300))
upload = ImageTk.PhotoImage(upload)
label = Label(root, image=upload, bg="light blue")
label.place(x=180, y=20)

#This is where we create the label
label1 = Label(root, text="Hey User! Welcome to the Denomination Counter Application", font=("Helvetica", 20), bg="light blue")
label1.place(relx=0.5, y=340, anchor=CENTER)

#Function to display a messagebox and proceed if OK is clicked
def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomination count?")
    if MsgBox == "ok":
        topwin()

#Adding Buttons to the main window
button1 = Button(root,
                  text="Lets get started", 
                    bg = "brown",
                    fg = "white", command=msg)
button1.place(x=260, y = 360)

def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg="light grey")
    top.geometry("650x350+50+50")

    label1 = Label(top, text="Enter the amount to calculate the denomination count", font=("Helvetica", 15), bg="light grey")
    entry = Entry(top)
    lbl = Label(top, text="Here are the number of counts for each denomination:", font=("Helvetica", 15), bg="light grey")

    l1 = Label(top, text="2000: ", font=("Helvetica", 15), bg="light grey")
    l2 = Label(top, text="500: ", font=("Helvetica", 15), bg="light grey")
    l3 = Label(top, text="200: ", font=("Helvetica", 15), bg="light grey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer amount.")
    btn = Button(top, text="Calculate", command=calculator, bg="brown", fg="white")

    # Centering Widgets in the Top Window
    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()
root.mainloop()