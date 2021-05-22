import os
from tkinter import *
import uuid
from elevate import elevate
import time
import webbrowser
from PIL import ImageTk,Image

elevate(show_console=False)

root = Tk()
root.geometry('500x180')
root.title('ID Changer by tijan')
root.iconbitmap('app1.ico')

cur = Label(root, font=('Consolas', 11))
cur.place(x=50,y=10)

def get_data():
	os.system("REG QUERY HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SQMClient /V MachineId > info.txt")
	with open ('info.txt', 'r') as file:
		r = file.readlines()
		w = (r[-2]).split()
		cur.config(text="ID actuel : " + w[2])
get_data()

def sett():
	new_id = en.get()
	new_id_f = '{'+new_id+'}'
	os.system("REG ADD HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SQMClient /v MachineId /d {} /f".format(new_id_f))
	label_info.config(text="Appliqué avec Success", fg='green')
	get_data()
	root.update()
	time.sleep(3)
	label_info.destroy()
	root.update()


def gen():
	en.delete(0, 'end')
	id = uuid.uuid1()
	en.insert(0, id)
	root.update()
def callback(e):
	webbrowser.open_new('https://t.me/Informageek')


lab = Label(root, text='ID : ', font=('Consolas', 11))
lab.place(x=20,y=50)
en = Entry(root, font=('Consolas', 11), width=50)
en.place(x=50,y=50)

but_gen= Button(root, text='Générer', font=('Consolas', 11), command=gen)
but_gen.place(x=150,y=90)
but_set= Button(root, text='Appliquer', font=('Consolas', 11), command=sett)
but_set.place(x=250,y=90)


	
label_info = Label(root, font=('Consolas', 13))
label_info.place(x=150, y= 135)

my_pic1 = Image.open('tg.png')
resized1 = my_pic1.resize((30, 30), Image.ANTIALIAS)
img = ImageTk.PhotoImage(resized1)
label_link = Label(root, text="Follow Me" , image=img, compound=LEFT , fg="#37a0f2")
label_link.place(x=390,y=140)
label_link.bind("<Button-1>", callback)

root.mainloop()