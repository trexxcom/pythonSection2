from tkinter import *

def printhello():
    print('Hi')

root = Tk()


w = Label(root, text='Python Test')
b = Button(root, text='Click', command=printhello)
c = Button(root, text='Quit', command=root.quit)

w.pack()
b.pack()
c.pack()

root.mainloop()
