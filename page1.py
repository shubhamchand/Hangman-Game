import tkinter
global root
root=tkinter.Tk()
root.title("HANGMAN GAME")

def g():
    root.destroy()
    import page2
def h():
    root.destroy()
    import page3
def o():
    root.destroy()
    import online
    
frame=tkinter.Frame(root)

frame.pack()
pp=tkinter.Entry(frame,bg="black") 
topframe=tkinter.Frame(root)
topframe.pack()


root.geometry('400x600+400+400')
l=tkinter.Label(root,text="PLAYING OPTIONS", font=("bold"),width=35)
b0=tkinter.Button(root,text="SINGLE PLAYER",font=("bold"),width=25,height=5,bg="gold",command=g,cursor='man',relief=tkinter.RAISED)
b1=tkinter.Button(root,text="DOUBLE PLAYER",font=("bold"),width=25,height=5,bg="gold",command=h,cursor='man',relief=tkinter.RAISED)
b2=tkinter.Button(root,text="PLAY ONLINE",font=("bold"),width=25,height=5,bg="gold",command=o,cursor='man', relief=tkinter.RAISED)
l.pack(padx=5,pady=20)
b0.pack(padx=20,pady=20)
b1.pack(padx=20,pady=20)
b2.pack(padx=20,pady=20)




root.mainloop()




'''

from Tkinter import * #this imports the tkinter module 

root = Tk()

listbox = Listbox(root)

listbox.pack()

b0=tkinter.Button(root,text="SINGLE PLAYER")

b1=tkinter.Button(root,text="DOUBLE PLAYER")

b0.pack()
b1.pack()



root.mainloop()'''
