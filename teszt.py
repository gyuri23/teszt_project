#!/usr/bin/python
import tkinter
# from tkinter import messagebox

def password_input():
    pwd_window = tkinter.Toplevel(main_window)
    pwd_window.geometry('+550+150')
    plabel = tkinter.Label(pwd_window, text='Jelszó:').pack()
    pinput = tkinter.Entry(pwd_window, textvariable=pwd, show='*').pack()
    pbutton = tkinter.Button(pwd_window, text="Ok",
                             command=lambda: password_ok(pwd_window)).pack()

def password_ok(pwd_window):
    # plabel = tkinter.Label(main_window, textvariable=pwd)
    # plabel.grid(row=2, column=2)
    password_label = tkinter.Message(main_window, text='Jelszó állapot',
                                     bg='yellow', bd=3, relief='groove',
                                     width=80)
    password_label.grid(row=0, column=1)
    pwd_window.destroy()

main_window = tkinter.Tk()
pwd = tkinter.StringVar()
main_window.title('Ablak neve')
main_window.geometry('300x500+500+100')

password_button = tkinter.Button(main_window, text="Jelszó",
                                 command=password_input)
password_button.grid(row=1, column=0, sticky='w')
# password_button.pack()

connect_button = tkinter.Button(main_window, text="Kapcsolódás")
connect_button.grid(row=2, column=0, sticky='w')
# connect_button.pack()

refresh_button = tkinter.Button(main_window, text="Frissítés")
refresh_button.grid(row=3, column=0, sticky='w')
# refresh_button.pack()

password_label = tkinter.Message(main_window, text='Jelszó állapot', bg='red',
                                 bd=3, relief='groove', width=80)
password_label.grid(row=0, column=1)

connect_label = tkinter.Message(main_window, text='Kapcsolat', bg='red', bd=3,
                                relief='groove', width=80)
connect_label.grid(row=0, column=2)

main_window.mainloop()