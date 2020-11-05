from tkinter import *
root = Tk()
root.title("Лабораторная работа №4 - git (вариант 1)")
root.geometry("400x300")
root.resizable(width=False, height = False)

def exit(self):
	root.destroy()

root.bind("<Escape>", exit)	

tex=Text(root)
tex.pack()



root.mainloop()