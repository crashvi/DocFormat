from tkinter import *
import	 fileinput
from tkinter.filedialog import *
#from tkinter.messagebox import *
from tkinter import messagebox


root = Tk()
root.title("Лабораторная работа №4 - git (вариант 1)")
root.geometry("400x300")
#root.resizable(width=False, height = False)
filename="1.txt"

def close_win(self):
	root.destroy()

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

def _open():
	global filename
	op=askopenfilename()
	for l in fileinput.input(op):
		tex.insert(END,l)
	filename=op.rpartition('/')[2]
	root.title(filename)

def _save():
	global filename
	sa=asksaveasfilename(initialfile=filename)
	letter=tex.get(1.0,END)
	file=open(sa, "w")
	file.write(letter)
	filename=file.name.rpartition('/')[2]
	root.title(filename)
	file.close()

def _rename():
	global filename
	def close_ren():
		filename=nname.get()
		root.title(filename)
		ren.destroy()
	ren=Toplevel()
	ren.geometry("150x50")
	lab=Label(ren,text="Введите новое имя файла")
	lab.pack()
	ren.title("RENAME")
	ren.resizable(width=False, height = False)
	nname=Entry(ren)
	nname.pack()
	nname.bind("<Enter>", close_ren)
	
def devs():
	messagebox.showinfo("Разработчики",	"Выполнили студенты группы ИСМ-20-2\nАнтонов, Болатов")		
	
root.bind("<Escape>", close_win)	

tex=Text(root, font="12")
tex.pack()



m=Menu(root)
root.config(menu=m)






m1=Menu(m)
m.add_cascade(label="File", menu=m1)
m1.add_command(label="Открыть", command=_open)
m1.add_command(label="Сохранить", command=_save)
m1.add_command(label="Ввод нового имени файла", command=_rename)
m1.add_command(label="Выход", command=close_win)

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
m4.add_command(label="Разработчики", command=devs)

root.mainloop()