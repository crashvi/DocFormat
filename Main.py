from datetime import datetime  	#дата и время
from tkinter import *			#Графический интерфейс
import	 fileinput				#файлы
from tkinter.filedialog import *	#диалоговые окна
from tkinter import messagebox		#диалоговые окна
import os

root = Tk()						
#FileDir='C:\\temp\\DocFormat\\'
P1=5		#задание значений по умолчанию
P2=10 
P3=1
filename="Default.txt"

root.title("Лабораторная работа №4 - git (вариант 1)")
root.geometry("400x300")
root.resizable(width=False, height = False)

def close_win(self):	
	root.destroy()

def win_set():	#модальное окно изменения настроек печати
	global P1,P2,P3
	def save_s():
		global P1,P2,P3
		P1=int(Param1.get())
		P2=int(Param2.get())
		if P3_0.get()==1:
			P3=1
		else:
			P3=0
		win_s.destroy()
	P3_0=IntVar()
	win_s=Toplevel()
	win_s.title("Параметры печати")
	win_s.geometry("380x95")
	win_s.resizable(width=False, height = False)
	L1=Label(win_s, text="Число строк для печати").grid(row=0,column=0)
	L2=Label(win_s, text="Отступ слева").grid(row=1,column=0)
	L3=Label(win_s, text="Распечать текущую дату и время").grid(row=2,column=0)
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

def win_about(): #окно меню о программе
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

def _open():	#функция октрытия документа
	global filename
	try:
		tex.delete(1.0,END)
		op=askopenfilename()
		for l in fileinput.input(op):
			tex.insert(END,l)
		filename=op.rpartition('/')[2]
		root.title(filename)
	except: #обработка ошибки закрытия окна выбора файла без выбора файла
		print("не указал имя файла, могла бы быть ошибка, но обработчик сработал")

def _save(): #функция сохранения документа
	global filename
	try:
		sa=asksaveasfilename(defaultextension='.txt',initialfile=filename)
		letter=tex.get(1.0,END)
		file=open(sa, "w")
		file.write(letter)
		filename=file.name.rpartition('/')[2]
		root.title(filename)
		file.close()
	except: #обработка ошибки закрытия окна сохранения
		print("не указал имя файла, могла бы быть ошибка, но обработчик сработал")

def _rename(): #функция переименования документа
	global filename
	def close_ren(self):
		global filename
		filename=nname.get()
		root.title(filename)
		ren.destroy()
	ren=Toplevel()
	ren.geometry("200x50")
	lab=Label(ren,text="Введите новое имя файла")
	lab.pack()
	ren.title("RENAME")
	ren.resizable(width=False, height = False)
	nname=Entry(ren, textvariable=filename)
	nname.pack()
	nname.focus()
	nname.bind("<Return>", close_ren)
	
def win_devs(): #функция информация о разработчиках
	messagebox.showinfo("Разработчики",	"Выполнили студенты группы ИСМ-20-2\nАнтонов, Болатов")

def PRINTER(): #функция вывода печати на принтер
	global FileDir
	if filename != "Default.txt":
		#os.chdir(FileDir)
		os.startfile(filename, "print")
	else:
		messagebox.showinfo("Ошибка-1",	"Выполните сохранение файла")	

def PrintToScreen(): #функция печати на экран
	global P1,P2,P3
	s= []
	print()
	for i in range(1,int(P1)+1,1):
		s.append(tex.get(str(i)+'.0',str(i)+'.end'))
		s[i-1]=' '*int(P2)+s[i-1]
	for i in range(1,int(P1)+1,1):
		print(s[i-1])
	if P3==1:
		current_datetime = datetime.now()
		DT = str(current_datetime).partition('.')[0]
		print(' '*int(P2)+DT)
	else:
		print('\n')

def PrintToFile(): #функция печати в файл
	global P1,P2,P3,filename
	s=[]
	for i in range(1,int(P1)+1,1):
		s.append(tex.get(str(i)+'.0',str(i)+'.end'))
		s[i-1]=' '*int(P2)+s[i-1]
	try:
		sa=asksaveasfilename(defaultextension='.ttt',initialfile="Print_"+filename)
		file=open(sa, "w")
		for j in range(1,P1+1,1):
			file.write(s[j-1]+'\n')
		if P3==1:
			current_datetime = datetime.now()
			DT = str(current_datetime).partition('.')[0]
			file.write(' '*int(P2)+DT)
			file.close()
	except:
		print("могла бы быть ошибка, но обработчик сработал")	

root.bind("<Escape>", close_win)	

tex=Text(root, font="12", width=400,)
tex.pack()

m=Menu(root)
root.config(menu=m) #настройка пунктов меню программы

m1=Menu(m)
m.add_cascade(label="File", menu=m1)
m1.add_command(label="Открыть", command=_open)
m1.add_command(label="Сохранить", command=_save)
m1.add_command(label="Ввод нового имени файла", command=_rename)
m1.add_command(label="Выход", command=close_win)

m2=Menu(m)
m.add_cascade(label="Print", menu=m2)
m2.add_command(label="Печать на принтер", command=PRINTER)
m2.add_command(label="Печать в файл", command=PrintToFile)
m2.add_command(label="Печать на экран", command=PrintToScreen)


m3=Menu(m)
m.add_cascade(label="Settings", menu=m3)
m3.add_command(label="Настройки", command=win_set)

m4=Menu(m)
m.add_cascade(label="About", menu=m4)
m4.add_command(label="О программе", command=win_about)
m4.add_command(label="Разработчики", command=win_devs)

root.mainloop()