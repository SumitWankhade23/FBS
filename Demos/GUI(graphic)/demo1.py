import tkinter as tk
r = tk.Tk()
r.title("GUI appliction")
r.geometry("500x500")
#l1 = tk.Label(r,text="This is my GUI function",background="orange",font=("comic sans MS",18))
# l1 = tk.Label(r,text="First",background="orange",font=("comic sans MS",18))
# l2 = tk.Label(r,text="Second",background="green",font=("comic sans MS",18))
# l3 = tk.Label(r,text="Third",background="orange",font=("comic sans MS",18))
# l4 = tk.Label(r,text="Forth",background="blue",font=("comic sans MS",18))
# l1.pack(side="top")
# l2.pack(side="bottom")
# l3.pack(side="right")
# l4.pack(side="left")

tk.Label(r,text="Enter your name ").pack()
e= tk.Entry(r)
#e.insert(0,"Enter your name: ")
e.pack()
l2=tk.Label(r,text="",bg="Yellow",fg="Orange",font=("Comic sans MS",18))
l2.pack()
def show():
    r=e.get()
    print(r)
    l2.config(text=r)
btn =tk.Button(r,text="Submit",command=show)
btn.pack() 

# tk.Label(r,text="First",background="orange",font=("comic sans MS",18)).grid(row=1,column=1)
# tk.Label(r,text="second",background="Blue",font=("comic sans MS",18)).grid(row=2,column=1)
# tk.Label(r,text="Third",background="Green",font=("comic sans MS",18)).grid(row=2,column=2)

# tk.Label(r,text="First",background="orange",font=("comic sans MS",18)).place(x=40,y=30)
# tk.Label(r,text="second",background="Blue",font=("comic sans MS",18)).place(x=140,y=150)
# tk.Label(r,text="Third",background="Green",font=("comic sans MS",18)).place(x=96,y=96)

gender = tk.StringVar()
tk.Radiobutton(r,text="Male",variable=gender).pack()
tk.Radiobutton(r,text="Femal",variable=gender).pack()
tk.Radiobutton(r,text="Third",variable=gender).pack()



r.mainloop()      # It will hold the window until you close the window

