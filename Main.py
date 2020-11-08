from tkinter import *
#from PIL import Image, ImageTk
from tkinter.filedialog import *

root = Tk()
root.title("Лабораторная работа №4 - git (вариант 1)")
root.geometry("400x300")
root.resizable(width=False, height = False)

def close_win(self):
	root.destroy()

def new_win():
	win=Toplevel(root)

def about_win():
	win=Toplevel()
	win.title("О программе")
	win.geometry("580x175")
	win.resizable(width=False, height = False)
	zad=Text(win, font="Arial")
	file=open("задание.txt",'r',encoding="utf-8")
	for line in file:
		zad.insert(END,line)
	file.close()
	zad.pack()
	
root.bind("<Escape>", close_win)	

tex=Text(root)
tex.pack()

m=Menu(root)
root.config(menu=m)






m1=Menu(m)
m.add_cascade(label="File", menu=m1)
m1.add_command(label="Открыть")
m1.add_command(label="Сохранить")
m1.add_command(label="Ввод нового имени файла")
m1.add_command(label="Выход")

m2=Menu(m)
m.add_cascade(label="Print", menu=m2)
m2.add_command(label="Печать на принтер")
m2.add_command(label="Печать в файл")
m2.add_command(label="Печать на экран")


m3=Menu(m)
m.add_cascade(label="Settings", menu=m3)
m3.add_command(label="Установить число строк для печати")
m3.add_command(label="Задать отступ слева")
m3.add_command(label="Распечать текущую дату и время")

m4=Menu(m)
m.add_cascade(label="About", menu=m4)
m4.add_command(label="О программе", command=about_win)

root.mainloop()