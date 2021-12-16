from tkinter import *
from random import *
from math import *
from tkinter import messagebox
from tkinter import filedialog
import PIL.Image
import PIL.ImageTk

root = Tk()
root.geometry("100x150")
root.title("Main Menu")
root.configure(background="seashell")


def info():
    info = Toplevel(root)
    info.geometry("300x100")
    info.title("Information")
    info.configure(background="mistyrose")
    Label(info, text="Іванькова Анна Русланівна", background="peachpuff").pack()
    Label(info, text="ІВ-91", background="peachpuff").pack()
    Label(info, text="Номер у списку  11", background="peachpuff").pack()
    Label(info, text="Номер заліковки 9111", background="peachpuff").pack()


def task1():
    win1 = Toplevel(root)
    win1.title("Task 1")
    win1.geometry("450x150")
    win1.configure(background="azure")

    def result():
        a = int(A_entry.get())
        b = int(B_entry.get())
        if (sin(a / 6) + cos(b / 6) < 0):
            messagebox.showerror(
                "Error",
                "Negative value of the root")
        elif (2 * sin(a / 6) * cos(b / 6) < 0):
            messagebox.showerror(
                "Error",
                "Negative value of the root")
        else:
            y = (sqrt(sin(a / 6) + cos(b / 6))) + sqrt(2 * sin(a / 6) * cos(b / 6))
            Y_entry.delete(0, END)
            Y_entry.insert(INSERT, y)

    def rand_insert():
        a = randint(-15, 15)
        b = randint(-15, 15)
        A_entry.delete(0, END)
        A_entry.insert(INSERT, a)
        B_entry.delete(0, END)
        B_entry.insert(INSERT, b)

    def diagram_1():
        block_d1 = Toplevel(root)
        block_d1.title("Block diagram_1")
        image1 = PIL.Image.open("b_diagram1.jpg")
        photo1 = PIL.ImageTk.PhotoImage(image1)
        label = Label(block_d1, image=photo1)
        label.image = photo1
        label.pack()

    def file_reading():
        messagebox.showinfo(
            "Read from file",
            "The first string is the value A, the second string is the value B")

        file = filedialog.askopenfilename()
        with open(file, "r") as f:
            value_1 = f.readline()
            A_entry.delete(0, END)
            A_entry.insert(INSERT, value_1)
            value_2 = f.readline()
            B_entry.delete(0, END)
            B_entry.insert(INSERT, value_2)

    A_label = Label(win1, text="A = ", background="paleturquoise")
    A_label.place(relx=0.1, rely=0.1)
    B_label = Label(win1, text="B = ", background="paleturquoise")
    B_label.place(relx=0.1, rely=0.3)
    A_entry = Entry(win1)
    A_entry.place(relx=0.3, rely=0.1)
    B_entry = Entry(win1)
    B_entry.place(relx=0.3, rely=0.3)
    Y_label = Label(win1, text="Y = ", background="paleturquoise")
    Y_label.place(relx=0.1, rely=0.5)
    Y_entry = Entry(win1)
    Y_entry.place(relx=0.3, rely=0.5)

    res_but = Button(win1, text="Result", command=result, background="darkturquoise")
    res_but.place(relx=0.7, rely=0.5)
    rand_but = Button(win1, text="Random generation", command=rand_insert, background="paleturquoise")
    rand_but.place(relx=0.7, rely=0.35)
    file_but = Button(win1, text="Read from file", command=file_reading, background="darkturquoise")
    file_but.place(relx=0.7, rely=0.2)
    diagram_1 = Button(win1, text="Block diagram", command=diagram_1, background="paleturquoise")
    diagram_1.place(relx=0.7, rely=0.05)


def task2():
    win2 = Toplevel(root)
    win2.title("Task 2")
    win2.geometry("450x150")
    win2.configure(background="lavenderblush")

    def result():
        k = int(K_entry.get())
        x = int(X_entry.get())
        if x < 0:
            messagebox.showerror(
                "Error",
                "Negative value of the root")
        elif (x*k)<=0:
            messagebox.showerror(
                "Error",
                "Negative value under the logarithmic expression")
        else:
            y=k*pow(x,2)*log10(k*x)+sqrt(x)
            Y_entry.delete(0, END)
            Y_entry.insert(INSERT, y)

    def rand_insert():
        x = randint(-15, 15)
        k = randint(-15, 15)
        X_entry.delete(0, END)
        X_entry.insert(INSERT, x)
        K_entry.delete(0, END)
        K_entry.insert(INSERT, k)

    def diagram_2():
        block_d2 = Toplevel(root)
        block_d2.title("Block diagram 2")
        image2 = PIL.Image.open("b_diagram2.jpg")
        photo2 = PIL.ImageTk.PhotoImage(image2)
        label = Label(block_d2, image=photo2)
        label.image = photo2
        label.pack()

    def file_reading():
        messagebox.showinfo(
            "Read from file",
            "The first string is the value K, the second string is the value X")

        file = filedialog.askopenfilename()
        with open(file, "r") as f:
            value_1 = f.readline()
            K_entry.delete(0, END)
            K_entry.insert(INSERT, value_1)
            value_2 = f.readline()
            X_entry.delete(0, END)
            X_entry.insert(INSERT, value_2)

    K_label = Label(win2, text="K = ", background="lightpink")
    K_label.place(relx=0.1, rely=0.1)
    X_label = Label(win2, text="X = ", background="lightpink")
    X_label.place(relx=0.1, rely=0.3)
    K_entry = Entry(win2)
    K_entry.place(relx=0.3, rely=0.1)
    X_entry = Entry(win2)
    X_entry.place(relx=0.3, rely=0.3)
    Y_label = Label(win2, text="Y = ", background="lightpink")
    Y_label.place(relx=0.1, rely=0.5)
    Y_entry = Entry(win2)
    Y_entry.place(relx=0.3, rely=0.5)

    res_but = Button(win2, text="Result", command=result, background="salmon")
    res_but.place(relx=0.7, rely=0.5)
    rand_but = Button(win2, text="Random generation", command=rand_insert, background="lightpink")
    rand_but.place(relx=0.7, rely=0.35)
    file_but = Button(win2, text="Read from file", command=file_reading, background="salmon")
    file_but.place(relx=0.7, rely=0.2)
    diagram_2 = Button(win2, text="Block diagram", command=diagram_2, background="lightpink")
    diagram_2.place(relx=0.7, rely=0.05)


def task3():
    win3 = Toplevel(root)
    win3.title("Task 3")
    win3.geometry("450x150")
    win3.configure(background="honeydew")

    def result():
        n = int(N_entry.get())
        b = int(B_entry.get())
        sum = 0
        prod = 1
        for a in range(1, n + 1):
            for k in range(1, a + 1):
                sum += (pow(a, k)) + (b / k)
            prod *= sum
            sum = 0
        Y_entry.delete(0, END)
        Y_entry.insert(INSERT, prod)

    def rand_insert():
        n = randint(1, 15)
        b = randint(1, 15)
        N_entry.delete(0, END)
        N_entry.insert(INSERT, n)
        B_entry.delete(0, END)
        B_entry.insert(INSERT, b)

    def diagram_3():
        block_d3 = Toplevel(root)
        block_d3.title("Block diagram 3")
        image3 = PIL.Image.open("b_diagram3.jpg")
        photo3 = PIL.ImageTk.PhotoImage(image3)
        label = Label(block_d3, image=photo3)
        label.image = photo3
        label.pack()

    def file_reading():
        messagebox.showinfo(
            "Read from file",
            "The first string is the value N, the second string is the value B")

        file = filedialog.askopenfilename()
        with open(file, "r") as f:
            value_1 = f.readline()
            N_entry.delete(0, END)
            N_entry.insert(INSERT, value_1)
            value_2 = f.readline()
            B_entry.delete(0, END)
            B_entry.insert(INSERT, value_2)

    N_label = Label(win3, text="K = ", background="aquamarine")
    N_label.place(relx=0.1, rely=0.1)
    B_label = Label(win3, text="X = ", background="aquamarine")
    B_label.place(relx=0.1, rely=0.3)
    N_entry = Entry(win3)
    N_entry.place(relx=0.3, rely=0.1)
    B_entry = Entry(win3)
    B_entry.place(relx=0.3, rely=0.3)
    Y_label = Label(win3, text="Y = ", background="aquamarine")
    Y_label.place(relx=0.1, rely=0.5)
    Y_entry = Entry(win3)
    Y_entry.place(relx=0.3, rely=0.5)

    res_but = Button(win3, text="Result", command=result, background="turquoise")
    res_but.place(relx=0.7, rely=0.5)
    rand_but = Button(win3, text="Random generation", command=rand_insert, background="aquamarine")
    rand_but.place(relx=0.7, rely=0.35)
    file_but = Button(win3, text="Read from file", command=file_reading, background="turquoise")
    file_but.place(relx=0.7, rely=0.2)
    diagram_3 = Button(win3, text="Block diagram", command=diagram_3, background="aquamarine")
    diagram_3.place(relx=0.7, rely=0.05)


but1 = Button(root, text="Task 1", command=task1, background="peachpuff")
but1.place(relx=0.3, rely=0.08)
but2 = Button(root, text="Task 2", command=task2, background="peachpuff")
but2.place(relx=0.3, rely=0.4)
but3 = Button(root, text="Task 3", command=task3, background="peachpuff")
but3.place(relx=0.3, rely=0.72)

mainmenu = Menu(root)
mainmenu.add_command(label='Info', command=info)
root.config(menu=mainmenu)


root.mainloop()