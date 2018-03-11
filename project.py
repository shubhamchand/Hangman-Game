import tkinter
root=tkinter.Tk()
root.title("HANGMAN GAME")
listbox=tkinter.Listbox(root,bg="black",fg="yellow",font="Elephant",bd=50,width=35)
listbox.insert(tkinter.END,"")
listbox.insert(tkinter.END,"                                        WELCOME")
listbox.insert(tkinter.END,"")
listbox.insert(tkinter.END,'                                                TO')
listbox.insert(tkinter.END,"")
listbox.insert(tkinter.END,'                                        HANGMAN')
'''img=ImageTk.PhotoImage(Image.open("3.png"))
panel=tk.Label(root,image=img)
panel.pack(side="bottom",fill="both",expand="yes")

PhotoImage(Image.open("3.png"))
listbox.insert(tkinter.END,PhotoImage)'''

def g():
    root.destroy()
    import page1
b=tkinter.Button(root,text="LET'S PLAY",bg="green",fg="black",command=g)
b1=tkinter.Button(root,text=" EXIT ",bg="red",fg="yellow",command=quit)
listbox.pack()
Title=tkinter.Label(root,text="Sneha,Sonali,Shubham,Ranjan")

b.pack(side="left",padx=10)
b1.pack(side='right',padx=10, pady=10)
#Title.grid(row=3, column=0)
Title.pack()

root.mainloop()
