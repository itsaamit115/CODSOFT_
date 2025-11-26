import tkinter as tk
from tkinter import messagebox
data = []
def add():
    n=e1.get(); p=e2.get(); em=e3.get(); ad=e4.get()
    if n and p:
        data.append([n,p,em,ad])
        messagebox.showinfo("Done","Added")
        clr(); show()
    else:
        messagebox.showwarning("Error","Name and Phone needed")
def show():
    lb.delete(0,tk.END)
    for i in data:
        lb.insert(tk.END, i[0]+"  -  "+i[1])
def search():
    q=e5.get()
    lb.delete(0,tk.END)
    for i in data:
        if q.lower() in i[0].lower() or q in i[1]:
            lb.insert(tk.END, i[0]+"  -  "+i[1])
def select(evt):
    try:
        i=lb.curselection()[0]
        c=data[i]
        e1.delete(0,tk.END); e1.insert(0,c[0])
        e2.delete(0,tk.END); e2.insert(0,c[1])
        e3.delete(0,tk.END); e3.insert(0,c[2])
        e4.delete(0,tk.END); e4.insert(0,c[3])
    except:
        pass
def update():
    try:
        i=lb.curselection()[0]
        data[i]=[e1.get(),e2.get(),e3.get(),e4.get()]
        messagebox.showinfo("Done","Updated")
        clr(); show()
    except:
        messagebox.showwarning("Error","Select a contact")
def delete():
    try:
        i=lb.curselection()[0]
        data.pop(i)
        messagebox.showinfo("Done","Deleted")
        clr(); show()
    except:
        messagebox.showwarning("Error","Select a contact")
def clr():
    e1.delete(0,tk.END); e2.delete(0,tk.END)
    e3.delete(0,tk.END); e4.delete(0,tk.END)
r=tk.Tk()
r.title("Contact Book")
r.geometry("420x500")
r.config(bg="#222")
fg="white"
bg="#222"
btn="#555"
ent="#333"
lbcol="#000"
tk.Label(r,text="Name",bg=bg,fg=fg).place(x=20,y=20)
e1=tk.Entry(r,width=40,bg=ent,fg=fg,insertbackground="white"); e1.place(x=120,y=20)
tk.Label(r,text="Phone",bg=bg,fg=fg).place(x=20,y=60)
e2=tk.Entry(r,width=40,bg=ent,fg=fg,insertbackground="white"); e2.place(x=120,y=60)
tk.Label(r,text="Email",bg=bg,fg=fg).place(x=20,y=100)
e3=tk.Entry(r,width=40,bg=ent,fg=fg,insertbackground="white"); e3.place(x=120,y=100)
tk.Label(r,text="Address",bg=bg,fg=fg).place(x=20,y=140)
e4=tk.Entry(r,width=40,bg=ent,fg=fg,insertbackground="white"); e4.place(x=120,y=140)
tk.Button(r,text="Add",width=10,bg=btn,fg=fg,command=add).place(x=30,y=180)
tk.Button(r,text="Update",width=10,bg=btn,fg=fg,command=update).place(x=120,y=180)
tk.Button(r,text="Delete",width=10,bg=btn,fg=fg,command=delete).place(x=210,y=180)
tk.Button(r,text="Clear",width=10,bg=btn,fg=fg,command=clr).place(x=300,y=180)
tk.Label(r,text="Search",bg=bg,fg=fg).place(x=20,y=220)
e5=tk.Entry(r,width=30,bg=ent,fg=fg,insertbackground="white"); e5.place(x=120,y=220)
tk.Button(r,text="Go",width=5,bg=btn,fg=fg,command=search).place(x=330,y=218)
lb=tk.Listbox(r,width=55,height=12,bg=lbcol,fg="white")
lb.place(x=20,y=260)
lb.bind("ListboxSelect",select)
show()
r.mainloop()
