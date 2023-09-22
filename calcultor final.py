from tkinter import *
import tkinter


root = Tk()
root.geometry("235x280")
root.resizable(False, False)
root.title("Calculator")
root.config(bg="powder blue")
#root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='/root/Desktop/py_github/logo/202.png'))
# ==================Function==========================
def clear():
    a.set("")

#---------------------------------button code gernater------------------------------------------
def btn_grnte():
    no = [7, 8, 9, 4, 5, 6, 1, 2, 3]
    g = 0
    for i in range(1, 4):
        for j in range(1, 4):
            print(
                f'Button(text="{no[g]}",bg="blue",fg="red",font=("Times new roman",14,"bold"),command=lambda : insert()).grid(row={i}column={j},ipadx=2,ipady=2,padx=2,pady=2)')
            g += 1
btn_grnte()
#-------------------------------------------------------------------------------------------------------

def sol():
    res = eval(a.get())
    a.set(res)

def insrt(q):
    a.set(f"{a.get()}{q}")


# ==============Button , Entry  and Label===================
a = StringVar()
main_entry = Entry(textvariable=a, font=('Times New Roman', 12, 'bold'), justify="right", bd=5).grid(row=1, column=1,
                                                                                                     columnspan=4,
                                                                                                     ipadx=20, ipady=8)

# ====================================1 t0 9 button ========================================
Button(text="7 ", bd=3, command=lambda: insrt(7), font=("Times New Roman", 12, "bold"), bg="#0038eb", fg="#ffffff").grid(
    row=3, column=1, ipadx=3, ipady=3)
Button(text="8 ", bd=3, command=lambda: insrt(8), font=("Times New Roman", 12, "bold"), bg="#0038eb", fg="#ffffff").grid(
    row=3, column=2, ipadx=3, ipady=3, padx=1, pady=1)
Button(text="9 ", bd=3, command=lambda: insrt(9), font=("Times New Roman", 12, "bold"), bg="#0038eb", fg="#ffffff").grid(
    row=3, column=3, ipadx=3, ipady=3, padx=1, pady=1)
Button(text="4 ", bd=3, command=lambda: insrt(4), font=("Times New Roman", 12, "bold"), bg="#0038eb", fg="#ffffff").grid(
    row=4, column=1, ipadx=3, ipady=3, padx=1, pady=1)
Button(text="5 ", bd=3, command=lambda: insrt(5), font=("Times New Roman", 12, "bold"), bg="#0038eb", fg="#ffffff").grid(
    row=4, column=2, ipadx=3, ipady=3, padx=1, pady=1)
Button(text="6 ", bd=3, command=lambda: insrt(6), font=("Times New Roman", 12, "bold"), bg="#0038eb", fg="#ffffff").grid(
    row=4, column=3, ipadx=3, ipady=3, padx=1, pady=1)
Button(text="1 ", bd=3, command=lambda: insrt(1), font=("Times New Roman", 12, "bold"), bg="#0038eb", fg="#ffffff").grid(
    row=5, column=1, ipadx=3, ipady=3, padx=1, pady=1)
Button(text="2 ", bd=3, command=lambda: insrt(2), font=("Times New Roman", 12, "bold"), bg="#0038eb", fg="#ffffff").grid(
    row=5, column=2, ipadx=3, ipady=3, padx=1, pady=1)
Button(text="3 ", bd=3, command=lambda: insrt(3), font=("Times New Roman", 12, "bold"), bg="#0038eb", fg="#ffffff").grid(
    row=5, column=3, ipadx=3, ipady=3, padx=1, pady=1)

# ==============================================================================

btn_1 = Button(text='C', bd=3, font=('Times New Roman', 12, 'bold'), command=clear, bg="#0038eb", fg="#ffffff").grid(row=2,
                                                                                                               column=1,
                                                                                                               ipadx=3,
                                                                                                               ipady=3,
                                                                                                               padx=1,
                                                                                                               pady=1)
btn_2 = Button(text="%", bd=3, font=('Times New Roman', 12, 'bold'), command=lambda: insrt(""), bg="#0038eb",
               fg="#ffffff").grid(row=2, column=2, ipadx=3, ipady=3, padx=1, pady=1)
btn_3 = Button(text=chr(1), bd=3, font=('Times New Roman', 12, 'bold'), bg="#0038eb", command=lambda: insrt(""),
               fg="#ffffff").grid(row=2, column=3, ipadx=3, ipady=3, padx=1, pady=1)
btn_4 = Button(text='/ ', bd=3, font=('Times New Roman', 12, 'bold'), bg="#0038eb", command=lambda: insrt("/"),
               fg="#ffffff").grid(row=2, column=4,
                                  ipadx=3, ipady=3,
                                  padx=1, pady=1)
btn_5 = Button(text='*', bd=3, font=('Times New Roman', 12, 'bold'), bg="#0038eb", command=lambda: insrt("*"),
               fg="#ffffff").grid(row=3, column=4,
                                  ipadx=3, ipady=3,
                                  padx=1, pady=1)
btn_6 = Button(text=' -', bd=3, font=('Times New Roman', 12, 'bold'), bg="#0038eb", command=lambda: insrt("-"),
               fg="#ffffff").grid(row=4, column=4,
                                  ipadx=3, ipady=3,
                                  padx=1, pady=1)
btn_7 = Button(text='+', bd=3, font=('Times New Roman', 12, 'bold'), bg="#0038eb", command=lambda: insrt("+ "),
               fg="#ffffff").grid(row=5, column=4, ipadx=3, ipady=3, padx=1, pady=1)
btn_8 = Button(text='00', bd=3, font=('Times New Roman', 12, 'bold'), bg="#0038eb", command=lambda: insrt("00"),
               fg="#ffffff").grid(row=6, column=1, ipadx=3, ipady=3, padx=1, pady=1)
btn_9 = Button(text='0 ', bd=3, font=('Times New Roman', 12, 'bold'), bg="#0038eb", command=lambda: insrt("0"),
               fg="#ffffff").grid(row=6, column=2, ipadx=3, ipady=3, padx=1, pady=1)
btn_10 = Button(text=' . ', bd=3, font=('Times New Roman', 12, 'bold'), bg="#0038eb", command=lambda: insrt("."),
                fg="#ffffff").grid(row=6, column=3, ipadx=3, ipady=3, padx=1, pady=1)
btn_11 = Button(text='=', bd=3, font=('Times New Roman', 12, 'bold'), bg="orange", command=lambda: sol(), fg="#ffffff").grid(
    row=6, column=4, ipadx=3, ipady=3, padx=1, pady=1)
root.mainloop()
