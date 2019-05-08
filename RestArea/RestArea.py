from tkinter import *

class RestArea:
    def __init__(self):
        window = Tk()
        window.title = 'ReatArea'
        window.geometry('600x800+100+0')
        frame1 = Frame(window)
        frame1.pack()
        RAPhoto = PhotoImage(file='resource\R.gif')
        mailPhoto = PhotoImage(file='resource\mail.gif')
        Label(frame1, image=RAPhoto).pack(side=LEFT)
        Button(frame1, image=mailPhoto).pack(side=RIGHT)

        window.mainloop()

RestArea()
