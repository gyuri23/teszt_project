#!/usr/bin/python
import tkinter

main_window = tkinter.Tk()      # http://effbot.org/tkinterbook/wm.htm
main_window.title('Ablak neve')
main_window.geometry('300x500+500+100') #széles x magas + bal elűről jobbra + bal felűről lefelé


var = tkinter.StringVar()
label = tkinter.Message(main_window, textvariable=var, relief='raised')
var.set("Hey!? How are you doing?")
label.pack()


#msg = tkinter.Message(main_window, anchor='w', width=80, justify='left', bg='blue', text='szöveg')
msg = tkinter.Message(main_window, bg='brown', pady=20, text='1234567890')
msg.pack()
msg.place(#rely=0.2
          #relheight=0.2,
          #relwidth=0.6,
          #anchor='s'
          #x=10
          )

msg2 = tkinter.Message(main_window, bg='blue', text='1234567890')
msg2.pack()
msg2.place(rely=0.4
          #relheight=0.2,
          #relwidth=0.6,
          #anchor='s'
          #x=10
          )

# Code to add widgets will go here...

main_window.mainloop()