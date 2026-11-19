from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Shopping Bill Calculator")
root.configure(bg="lightblue")

upload = Image.open("shopping_img.jpg")
upload = upload.resize((300,300))
upload_image = ImageTk.PhotoImage(upload)

label1 = Label(root, text="Hey there! Welcome to the Shopping Bill Calculator!", font=("Helvetica", 16), bg="lightblue")

def msg():
    MsgBox = messagebox.showinfo("Do you want to calculate your bill?")
    if MsgBox == 'ok':
        topwin()

button1 = Button(root, text="Lets get started!",
                 bg = "brown",
                 fg = "white", command=msg)
button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Shopping Bill Calculator")
    top.configure(bg="light grey")
    top.geometry("650x350+50+50")

    label1 = Label(top, text="Enter number of items you purchased:", font=("Helvetica", 14), bg="light grey")
    entry = Entry(top)
    lb1 = Label(top, text="Here are the prices for each item:", font=("Helvetica", 14), bg="light grey")

    l1 = Label(top, text= "Notebook: $50", font=("Helvetica", 12), bg="light grey")
    l2 = Label(top, text= "Pen: $10", font=("Helvetica", 12), bg="light grey")
    l3 = Label(top, text= "Pencil: $5", font=("Helvetica", 12), bg="light grey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculate():
        try:
            global amount
            amount = int(entry.get())
            notebook_qty = amount // 50
            amount %= 50
            pen_qty = amount // 10
            amount %= 10
            pencil_qty = amount // 5

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(0, str(notebook_qty))
            t2.insert(0, str(pen_qty))
            t3.insert(0, str(pencil_qty))
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")
    btn = Button(top, text="Calculate", command=calculate, bg="green", fg="white")

    label1.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lb1.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()
root.mainloop()

