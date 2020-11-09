from tkinter import *
import	 fileinput
from tkinter.filedialog import *
from tkinter import messagebox
root = Tk()

P1=0
P2=0 
P3=0


root.title("Лабораторная работа №4 - git (вариант 1)")
root.geometry("400x300")
#root.resizable(width=False, height = False)
filename="Default.txt"

def close_win(self):
	root.destroy()

def win_set():
	global P1,P2,P3
	def save_s():
		global P1,P2,P3
		P1=int(Param1.get())
		P2=int(Param2.get())
		if P3_0.get()==1:
			P3=1
		else:
			P3=0
		print(P3)
		win_s.destroy()
	P3_0=IntVar()
	win_s=Toplevel()
	win_s.title("Параметры печати")
	win_s.geometry("380x95")
	win_s.resizable(width=False, height = False)
	L1=Label(win_s, text="Число строк для печати").grid(row=0,column=0)
	L2=Label(win_s, text="Отступ слева").grid(row=1,column=0)
	L3=Label(win_s, text="Распечать текущую дату и время").grid(row=2,column=0)
	print(P3)
	Param1=Entry(win_s)
	Param1.insert(0, str(P1))
	Param2=Entry(win_s)
	Param2.insert(0, str(P2))
	Param1.grid(row=0,column=1)
	Param2.grid(row=1,column=1)
	if P3==1:
		P3_0.set(1)
	Che1=Checkbutton(win_s, variable=P3_0, onvalue=1, offvalue=0).grid(row=2,column=1)
	B1=Button(win_s, text="сохранить изменения", command=save_s).grid(row=3,column=1)

def win_about():
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
	def close_ren(self):
		filename=nname.get()
		root.title(filename)
		ren.destroy()
	ren=Toplevel()
	ren.geometry("150x50")
	lab=Label(ren,text="Введите новое имя файла")
	lab.pack()
	ren.title("RENAME")
	ren.resizable(width=False, height = False)
	nname=Entry(ren, textvariable=filename)
	nname.pack()
	nname.bind("<Return>", close_ren)
	
def win_devs():
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
m3.add_command(label="Настройки", command=win_set)

m4=Menu(m)
m.add_cascade(label="About", menu=m4)
m4.add_command(label="О программе", command=win_about)
m4.add_command(label="Разработчики", command=win_devs)

root.mainloop()