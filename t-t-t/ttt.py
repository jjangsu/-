from tkinter import *
import random

class TicTacToc:
    def newGame(self):
        self.againButton.pack_forget()
        self.turn = True
        self.label.configure(text="o차례")
        for r in range(3):
            for c in range(3):
                self.buttonList[r*3+c].configure(image=self.imageList[2], text='')
    def endGame(self):
        for r in range(3):
            for c in range(3):
                self.buttonList[r*3+c].configure(text='e')
        self.againButton.pack()

    def pressed(self,Row,Col):
        if self.buttonList[Row*3+Col]["text"]=='':
            if self.turn == True:   #o차례
                self.buttonList[Row*3+Col].configure(image=self.imageList[0], text='o')
                self.label.configure(text='x차례')
            else:
                self.buttonList[Row*3+Col].configure(image=self.imageList[1], text='x')
                self.label.configure(text='o차례')
            self.turn = not self.turn
            self.check()

    def check(self):
        self.full = True

        for item in self.checkList:
            for r in range(3):
                if self.buttonList[r*3]["text"]==self.buttonList[r*3+1]["text"]==self.buttonList[r*3+2]["text"]==item:
                    self.label.configure(text=item+" 우승!!")
                    self.endGame()
                    return None
                if self.buttonList[0*3+r]["text"]==self.buttonList[1*3+r]["text"]==self.buttonList[2*3+r]["text"]==item:
                    self.label.configure(text=item+" 우승!!")
                    self.endGame()
                    return None
                if self.buttonList[0]["text"]==self.buttonList[4]["text"]==self.buttonList[8]["text"]==item:
                    self.label.configure(text=item+" 우승!!")
                    self.endGame()
                    return None
                if self.buttonList[2]["text"]==self.buttonList[4]["text"]==self.buttonList[6]["text"]==item:
                    self.label.configure(text=item+" 우승!!")
                    self.endGame()
                    return None
        for r in range(3):
            for c in range(3):
                if self.buttonList[r*3+c]["text"] == '':
                    self.full = False
        if self.full==True:
            self.label.configure(text="무승부!")
            self.endGame()


    def __init__(self):
        window = Tk()
        self.turn = True
        self.checkList = ['o','x']
        self.imageList = []
        self.imageList.append(PhotoImage(file="image/o.gif"))
        self.imageList.append(PhotoImage(file="image/x.gif"))
        self.imageList.append(PhotoImage(file="image/empty.gif"))
        self.buttonList = []
        self.full = True
        frame1 = Frame(window)
        frame1.pack()
        for r in range(3):
            for c in range(3):
                self.buttonList.append(Button(frame1, image=self.imageList[2], command=lambda Row=r, Col=c: self.pressed(Row,Col), text=''))
                self.buttonList[r*3+c].grid(row=r, column=c)
        frame2 = Frame(window)
        frame2.pack()
        self.label = Label(frame2, text="o 차례")
        self.label.pack()
        self.againButton = Button(frame2,text='다시하기',command=self.newGame)

        window.mainloop()

TicTacToc()
