from tkinter import *
import tkinter.messagebox as tmsg
from tkinter import filedialog as fd

# from tkinter.filedialog import  askopenfilename,asksaveasfilename

root = Tk()
root.title("Data Entry App")
root.minsize(334, 400)
root.maxsize(300, 450)
root.config(bg="powder blue")

#-----------------------------Function---------------------------------------
def about():
    tmsg.showinfo("Contact", "Technical Aryaji \n Mob : 9812806564 \n Email:Shivamkamboj322@gmail.com")
def ext():
    a = tmsg.askyesno("Exit", "Are You Sure To Exit")
    if a == 1:
        root.destroy()
    else:
        pass
def clear():
    nam.set("")
    eml.set("")
    mob.set("")
def sumt():
    f = open("demo.txt", "a")
    f.write(f"\n\nName : {nam.get()} \nEmail : {eml.get()} \nPhone : {mob.get()}")
    f.close()
    # tf = fd.askopenfilename(filetypes=filetypes, title="open file")
    tf = open("demo.txt", 'r')
    data = tf.read()
    tex.insert(END, data)
    tf.close()

    nam.set("")
    eml.set("")
    mob.set("")
#-------------------variable--------------------------------
nam = StringVar()
eml = StringVar()
mob = StringVar()
#-----------------Menu-----------------------------
m_menu = Menu(root, font=("mono9", 7, "bold"))
m1 = Menu(m_menu, tearoff=0, font=("mono9", 7, "bold"))
m1.add_command(label="new")
m1.add_command(label="Save")
m1.add_command(label="Save as")
m1.add_command(label="Exit", command=ext)
m_menu.add_cascade(label="File", menu=m1)

m2 = Menu(m_menu, tearoff=0, font=("ROMAN", 7, "bold"))
m2.add_command(label="Copy")
m2.add_command(label="Cut")
m2.add_command(label="Delete")
m_menu.add_cascade(label="Edit", menu=m2)

# m_menu.add_command(label="Edit")
m_menu.add_command(label="Help")

m3 = Menu(m_menu, tearoff=0, font=("mono9", 5, "bold"))
m3.add_command(label="Technical Aryaji", command=about)
# m3.add_command(label="shivamkamboj322@gmail.com")
m_menu.add_cascade(label="About", menu=m3)

root.config(menu=m_menu)
#----------------------------Label,Entry and Button-------------------
ml = Label(text="Enter Your Detail ", font=("digital- 7", 12, "bold"), fg="blue", bg="powder blue").place(x=60, y=5)
l1 = Label(text="Name ", font=("future", 8, "bold"), fg="green", bg="powder blue").place(x=15, y=40)
e1 = Entry(textvariable=nam).place(x=70, y=40)
l2 = Label(text="Email ", font=("future", 8, "bold"), fg="green", bg="powder blue").place(x=15, y=80)
e2 = Entry(textvariable=eml).place(x=70, y=80)
l3 = Label(text="Phone ", font=("future", 8, "bold"), fg="green", bg="powder blue").place(x=15, y=120)
e3 = Entry(textvariable=mob).place(x=70, y=120)

b1 = Button(text="Clear", bg="red", command=clear).place(x=20, y=160)
b2 = Button(text="Submit", bg="sky blue", command=sumt).place(x=120, y=160)
b3 = Button(text="Exit", bg="red", command=quit).place(x=230, y=160)

frame1 = Frame(root).place(x=300, y=250)

scrollbar=Scrollbar(frame1)
scrollbar.pack( side=RIGHT,fill=Y)

tex = Text(frame1,yscrollcommand=scrollbar.set)
tex.place(x=10, y=200, width=310, height=180)

scrollbar.config(command=tex.yview)
#---------------------------------
tf = open("demo.txt", 'r')
data = tf.read()
tex.insert(END, data)
#---------------add more option ---------------
# delete data from text box
# save data after deleting data



root.mainloop()
