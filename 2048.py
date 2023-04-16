from random import randint

a = [ [0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0] ]

def clear():
    for l in root.pack_slaves():
        l.destroy()

def newgame():
    clear()
    for i in range(4):
        for j in range(4):
            a[i][j]=0
    randgen()
    randgen()
    printlabels()

def printlabels():
    f=Frame(root)
    for i in range(4):
        for j in range(4):
            t = a[i][j] if a[i][j]!=0 else ''
            t = str(t).center(5, ' ')
            Label(f, text=t, padx=10, pady=10, font=('courier new', 15)).grid(row=i, column=j)
    Label(f, text=' ', padx=10, pady=10).grid(row=4, column=0, columnspan=4)
    Button(f, text='New Game', command=newgame, font=('courier new', 15)).grid(row=5, column=0, columnspan=2)
    Button(f, text='  Exit  ', command=root.destroy, font=('courier new', 15)).grid(row=5, column=2, columnspan=2) #'Exit'.center(8)
    f.pack()

def checkfinish():
    for i in a:
        if 0 in i:
            return
        if 2048 in i:
            print('You Won')
            exit()
    print('Game Over')
    newgame() # exit()

def randgen():
    i, j = 0, 0
    while True:
        if j == 4:
            j = 0
            i += 1
        if i == 4:
            i = 0
        if a[i][j] == 0 and randint(1, 16) == 1:
            a[i][j] = 2 if randint(1, 10) in [1, 2, 3] else 4
            return
        j += 1

def drop(n):
    if n == 8:
        for col in range(4):
            t=[]
            for row in range(4):
                if not a[row][col] == 0:
                    t.append(a[row][col])
            t+=[0, 0, 0, 0]
            for row in range(4):
                a[row][col]=t[row]
    if n == 4:
        for row in range(4):
            t=[]
            for col in range(4):
                if not a[row][col] == 0:
                    t.append(a[row][col])
            t+=[0, 0, 0, 0]
            for col in range(4):
                a[row][col]=t[col]
    if n == 2:
        for col in range(4):
            t=[]
            for row in range(3, -1, -1):
                if not a[row][col] == 0:
                    t.append(a[row][col])
            t+=[0, 0, 0, 0]
            for row in range(3, -1, -1):
                a[row][col]=t[3-row]
    if n == 6:
        for row in range(4):
            t=[]
            for col in range(3, -1, -1):
                if not a[row][col] == 0:
                    t.append(a[row][col])
            t+=[0, 0, 0, 0]
            for col in range(3, -1, -1):
                a[row][col]=t[3-col]

def merge(n):
    if n == 8:
        for i in range(3):
            for j in range(4):
                if a[i][j] == a[i+1][j]:
                    a[i][j] *= 2
                    a[i+1][j] = 0
                    drop(n)
    if n == 4:
        for i in range(4):
            for j in range(3):
                if a[i][j] == a[i][j+1]:
                    a[i][j] *= 2
                    a[i][j+1] = 0
                    drop(n)
    if n == 2:
        for i in range(3, 0, -1):
            for j in range(3, -1, -1):
                if a[i][j] == a[i-1][j]:
                    a[i][j] *= 2
                    a[i-1][j] = 0
                    drop(n)
    if n == 6:
        for i in range(3, -1, -1):
            for j in range(3, 0, -1):
                if a[i][j] == a[i][j-1]:
                    a[i][j] *= 2
                    a[i][j-1] = 0
                    drop(n)

def left(event):
    n=4
    b = [row[:] for row in a]
    drop(n)
    merge(n)
    checkfinish()
    if not a == b:
        randgen()
        clear()
        printlabels()
def right(event):
    n=6
    b = [row[:] for row in a]
    drop(n)
    merge(n)
    checkfinish()
    if not a == b:
        randgen()
        clear()
        printlabels()
def up(event):
    n=8
    b = [row[:] for row in a]
    drop(n)
    merge(n)
    checkfinish()
    if not a == b:
        randgen()
        clear()
        printlabels()
def down(event):
    n=2
    b = [row[:] for row in a]
    drop(n)
    merge(n)
    checkfinish()
    if not a == b:
        randgen()
        clear()
        printlabels()

from tkinter import *
root = Tk()
root.title('2048')
root.iconbitmap('C:\\Users\\Jinay Vora\\Documents\\Python Programs\\Oxygen-Icons.org-Oxygen-Actions-document-edit.ico')
root.geometry('340x285')

root.bind('<Left>', left)
root.bind('<Right>', right)
root.bind('<Up>', up)
root.bind('<Down>', down)
root.bind('a', left)
root.bind('d', right)
root.bind('w', up)
root.bind('s', down)


randgen()
randgen()
printlabels()

root.mainloop()