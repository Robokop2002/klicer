import tkinter as tk
import random
win = tk.Tk()
win.config(bg='#D4FFD4')
win.title('Ультра кликер')
win.geometry('270x280+100+200')
win.resizable(False,False)
win.iconbitmap('cursor.ico')
i= 0
bonus = 1
def draw():
    text['text'] = str(i)
    bonu['text'] = str(bonus)
def clic():
    global bonus
    global i
    if random.randint(0,10) == 5:
        bonus += 0.5
    i += bonus
    if random.randint(0,100) == 5:
        bonus += 100
    i += bonus
    i = int(i)
    draw()
def spis(sp):
    global i
    b = sp
    i = i - b
    draw()
def kalk():
    global bonus
    if i >= 10:
        spis(10)
        bonus+=0.5
        draw()
def tel():
    global bonus
    if i >= 100:
        spis(100)
        bonus += 5
        draw()
def maining():
    global bonus
    if i >= 1000000:
        spis(1000000)
        bonus += 5000
        draw()
def black():
    global bonus
    if i >= 10000000000:
        spis(10000000000)
        bonus += 1000000000
        draw()
klic = tk.Button(text='click',command=clic,bg='red',font=('Courier',40, 'bold'),activebackground='red')
text = tk.Label(text=i,bg='#D4FFD4')
bonu = tk.Label(text=f'Бонус - {bonus}',bg='#D4FFD4', font=('Arial',20, 'bold'), activebackground='red')
store1 = tk.Button(text='калькулятор +0.1 цена -10', command=kalk, bg='blue', font=('Courier', 10, 'bold'), activebackground='red')
store2 = tk.Button(text='телефон +5 цена -100', command=tel, bg='blue', font=('Courier', 10, 'bold'), activebackground='red')
store3 = tk.Button(text='майнинг-ферма +5000 цена -1000000', command=maining, bg='blue', font=('Courier', 8, 'bold'), activebackground='red')
store4 = tk.Button(text='чёрная-дыра +1 B цена -10 B', command=black, bg='blue', font=('Courier', 8, 'bold'), activebackground='red')

def packing():
    text.pack()
    klic.pack()
    bonu.pack()
    store1.pack()
    store2.pack()
    store3.pack()
    store4.pack()
packing()

tk.mainloop()
