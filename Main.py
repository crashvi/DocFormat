from tkinter import *
root = Tk()
root.title("Лабораторная работа №4 - git (вариант 1)")
root.geometry("400x300")
root.resizable(width=False, height = False)

def exit(self):
	root.destroy()

root.bind("<Escape>", exit)	


m=Menu(root)
root.config(menu=m)

m1=Menu(m)
m.add_cascade(label="File", menu=m1)
m1.add_command(label="F1")
m1.add_command(label="F2")
m1.add_command(label="F3")
m1.add_command(label="F4")

m2=Menu(m)
m.add_cascade(label="Print", menu=m2)
m2.add_command(label="P1")
m2.add_command(label="P2")
m2.add_command(label="P3")
m2.add_command(label="P4")

m3=Menu(m)
m.add_cascade(label="Settings", menu=m3)
m3.add_command(label="S1")

m4=Menu(m)
m.add_cascade(label="About", menu=m4)
m4.add_command(label="A1")

root.mainloop()