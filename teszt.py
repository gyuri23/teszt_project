#!/usr/bin/python
import tkinter

main_window = tkinter.Tk()      # http://effbot.org/tkinterbook/wm.htm
main_window.title('Ablak neve')
main_window.geometry('300x500+500+100') #széles x magas + bal elűről jobbra + bal felűről lefelé

left_frame = tkinter.Frame(main_window, bg='red')
left_frame.grid(row=0, column=0, sticky='w')

right_frame = tkinter.Frame(main_window, bg='blue')
right_frame.grid(row=0, column=1, sticky='e')

msg = tkinter.Message(left_frame)
msg = tkinter.Message(left_frame, bg='brown', pady=20, text='1234567890')
msg.pack()
msg.place(rely=0.2)
# #
#
# password_button = tkinter.Button(left_frame, text="Jelszó")
# password_button.pack()
# password_button.place(rely=0.2,
#                       relheight=0.2,
#                       relwidth=0.6,
#                       anchor='s',
#                       x=10
#                       )
#
# connect_button = tkinter.Button(left_frame, text="Kapcsolódás")
# connect_button.pack()
#
# refresh_button = tkinter.Button(left_frame, text="Frissítés")
# refresh_button.pack()
#






# var = tkinter.StringVar()
# label = tkinter.Message(main_window, textvariable=var, relief='raised')
# var.set("Hey!? How are you doing?")
# label.pack()
#
#
# #msg = tkinter.Message(main_window, anchor='w', width=80, justify='left', bg='blue', text='szöveg')
# msg = tkinter.Message(main_window, bg='brown', pady=20, text='1234567890')
# msg.pack()
# msg.place(#rely=0.2
#           #relheight=0.2,
#           #relwidth=0.6,
#           #anchor='s'
#           #x=10
#           )
#
# msg2 = tkinter.Message(main_window, bg='blue', text='1234567890')
# msg2.pack()
# msg2.place(rely=0.4
#           #relheight=0.2,
#           #relwidth=0.6,
#           #anchor='s'
#           #x=10
#           )

# Code to add widgets will go here...

main_window.mainloop()