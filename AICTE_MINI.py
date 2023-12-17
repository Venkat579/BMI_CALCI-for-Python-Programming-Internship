from tkinter import *

def calculate():
    try:
        a = float(e1.get())
        b = float(e2.get())
        if operation.get() == '+':
            result = a + b
        elif operation.get() == '-':
            result = a - b
        elif operation.get() == '*':
            result = a * b
        elif operation.get() == '/':
            result = a / b
        elif operation.get() == '%':
            result = a % b
        myText.set(f"{a} {operation.get()} {b} = {result:.2f}")
    except ValueError:
        myText.set("Invalid input")

m = Tk()
m.title('Arithmetic Calculator')
m.resizable(False, False)
m.configure(background='#f2f2f2')

myText = StringVar()

Label(m, text='First Number', font='Helvetica 12 bold', bg='#f2f2f2').grid(row=0, padx=10, pady=10)
Label(m, text='Second Number', font='Helvetica 12 bold', bg='#f2f2f2').grid(row=1, padx=10, pady=10)
Label(m, text='Operation', font='Helvetica 12 bold', bg='#f2f2f2').grid(row=2, padx=10, pady=10)
Label(m, text='Result', font='Helvetica 12 bold', bg='#f2f2f2').grid(row=3, padx=10, pady=10)

e1 = Entry(m, font='Helvetica 12')
e2 = Entry(m, font='Helvetica 12')
e1.grid(row=0, column=1, padx=10, pady=10)
e2.grid(row=1, column=1, padx=10, pady=10)

operation = StringVar()
operation.set('+')
Radiobutton(m, text='+', variable=operation, value='+', font='Helvetica 12', bg='#f2f2f2').grid(row=2, column=1)
Radiobutton(m, text='-', variable=operation, value='-', font='Helvetica 12', bg='#f2f2f2').grid(row=2, column=2)
Radiobutton(m, text='*', variable=operation, value='*', font='Helvetica 12', bg='#f2f2f2').grid(row=2, column=3)
Radiobutton(m, text='/', variable=operation, value='/', font='Helvetica 12', bg='#f2f2f2').grid(row=2, column=4)
Radiobutton(m, text='%', variable=operation, value='%', font='Helvetica 12', bg='#f2f2f2').grid(row=2, column=5)

result = Label(m, textvariable=myText, font='Helvetica 16 bold', bg='#f2f2f2')
result.grid(row=3, column=1, columnspan=5)

b1 = Button(m, text='Calculate', font='Helvetica 12 bold', width=25, command=calculate, bg='#33cc33', fg='white', activebackground='#33cc33', activeforeground='white')
b1.grid(row=4, column=1, columnspan=5, pady=20)

m.mainloop()
