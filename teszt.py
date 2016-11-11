#!/usr/bin/python
import tkinter
# from tkinter import messagebox

main_window = tkinter.Tk()      # http://effbot.org/tkinterbook/wm.htm
main_window.title('Ablak neve')
main_window.geometry('300x500+500+100') #széles x magas + bal elűről jobbra + bal felűről lefelé

password_button = tkinter.Button(main_window, text="Jelszó")
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