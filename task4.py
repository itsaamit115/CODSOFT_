import tkinter as tk
import random
def play(c):
    cc = random.choice(["Rock","Paper","Scissors"])
    ucl.config(text="You: "+c)
    ccl.config(text="Comp: "+cc)
    if c==cc:
        rl.config(text="Tie")
    elif (c=="Rock" and cc=="Scissors") or (c=="Scissors" and cc=="Paper") or (c=="Paper" and cc=="Rock"):
        rl.config(text="Win")
        us.config(text=str(int(us.cget("text"))+1))
    else:
        rl.config(text="Lose")
        cs.config(text=str(int(cs.cget("text"))+1))
r=tk.Tk()
r.title("RPS")
r.geometry("280x310")
r.config(bg="lightblue")
tk.Label(r,text="Rock Paper Scissors",font=("Arial",15,"bold"),bg="lightblue").pack(pady=5)
ucl=tk.Label(r,text="You:",font=("Arial",12),bg="lightblue"); ucl.pack()
ccl=tk.Label(r,text="Comp:",font=("Arial",12),bg="lightblue"); ccl.pack()
rl=tk.Label(r,text="",font=("Arial",14,"bold"),bg="lightblue"); rl.pack(pady=5)
f=tk.Frame(r,bg="lightblue"); f.pack()
tk.Button(f,text="Rock",width=8,command=lambda:play("Rock")).grid(row=0,column=0,padx=5)
tk.Button(f,text="Paper",width=8,command=lambda:play("Paper")).grid(row=0,column=1,padx=5)
tk.Button(f,text="Scissors",width=8,command=lambda:play("Scissors")).grid(row=0,column=2,padx=5)
tk.Label(r,text="Score",font=("Arial",13,"bold"),bg="lightblue").pack(pady=5)
sf=tk.Frame(r,bg="lightblue"); sf.pack()
tk.Label(sf,text="You",font=("Arial",12),bg="lightblue").grid(row=0,column=0,padx=20)
tk.Label(sf,text="Comp",font=("Arial",12),bg="lightblue").grid(row=0,column=1,padx=20)
us=tk.Label(sf,text="0",font=("Arial",12),bg="lightblue"); us.grid(row=1,column=0)
cs=tk.Label(sf,text="0",font=("Arial",12),bg="lightblue"); cs.grid(row=1,column=1)
r.mainloop()
