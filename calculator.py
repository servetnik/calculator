import tkinter as tk
import ast

number = 0

window = tk.Tk()
window.geometry("550x500")
window['bg'] = '#000000'
window.title('Maths')

okno = tk.Entry(window)
okno.grid(row = 0, column = 0, columnspan = 4, stick = 'wens')

def get_number(a):
    global okno
    global number
    number = okno.get() + str(a)
    okno.delete(0, tk.END)
    okno.insert(0, number)
    print(number)

def get_function(b):
    number = okno.get()
    if number[-1] in '+-*/':
        number = number[:-1]
        
    okno.delete(0, tk.END)
    okno.insert(0, number + b)
    print(number)
    
def calculation():
    global number
    result = eval(number)
    okno.delete(0, tk.END)
    okno.insert(0, result)
    
def delete():
    number = okno.get()
    okno.delete(0, tk.END)
    number = number[:-1]
    okno.insert(0, number)



window.grid_columnconfigure(0, minsize = 110)
window.grid_columnconfigure(1, minsize = 110)
window.grid_columnconfigure(2, minsize = 110)
window.grid_columnconfigure(3, minsize = 110)
window.grid_columnconfigure(4, minsize = 0)
window.grid_columnconfigure(5, minsize = 110)


window.grid_rowconfigure(1, minsize = 110)
window.grid_rowconfigure(2, minsize = 110)
window.grid_rowconfigure(3, minsize = 110)
window.grid_rowconfigure(4, minsize = 110)
window.grid_rowconfigure(5, minsize = 110)

tk.Button(text = '1', background="#bde0ff", font='Courier 10',
          command = lambda : get_number(1)).grid(row = 1, column = 0, stick = 'wens')
tk.Button(text = '2', background="#bde0ff", font='Courier 10',
          command = lambda : get_number(2)).grid(row = 1,column = 1, stick = 'wens')
tk.Button(text = '3', background="#bde0ff", font='Courier 10',
          command = lambda : get_number(3)).grid(row = 1,column = 2, stick = 'wens')
tk.Button(text = '4', background="#bde0ff", font='Courier 10',
          command = lambda : get_number(4)).grid(row = 2,column = 0, stick = 'wens')
tk.Button(text = '5', background="#bde0ff", font='Courier 10',
          command = lambda : get_number(5)).grid(row = 2,column = 1, stick = 'wens')
tk.Button(text = '6', background="#bde0ff", font='Courier 10',
          command = lambda : get_number(6)).grid(row = 2,column = 2, stick = 'wens')
tk.Button(text = '7', background="#bde0ff", font='Courier 10',
          command = lambda : get_number(7)).grid(row = 3,column = 0, stick = 'wens')
tk.Button(text = '8', background="#bde0ff", font='Courier 10',
          command = lambda : get_number(8)).grid(row = 3,column = 1, stick = 'wens')
tk.Button(text = '9', background="#bde0ff", font='Courier 10',
          command = lambda : get_number(9)).grid(row = 3,column = 2, stick = 'wens')
tk.Button(text = '0', background="#000000", font='Courier 10', fg='#ffffff',
          command = lambda : get_number(0)).grid(row = 4,column = 0, stick = 'wens',
                                                 columnspan = 2)



tk.Button(text = '+', background="#000000", font='Courier 10', fg='#ffffff',
          command = lambda : get_function('+')).grid(row = 1,column = 3, stick = 'wens')
tk.Button(text = '-', background="#000000", font='Courier 10', fg='#ffffff',
          command = lambda : get_function('-')).grid(row = 2,column = 3, stick = 'wens')
tk.Button(text = '*', background="#000000", font='Courier 10', fg='#ffffff',
          command = lambda : get_function('*')).grid(row = 3,column = 3, stick = 'wens')
tk.Button(text = '/', background="#000000", font='Courier 10', fg='#ffffff',
          command = lambda : get_function('/')).grid(row = 4,column = 3, stick = 'wens')

tk.Button(text = '=', background="#000000", font='Courier 10', fg='#ffffff',
          command = calculation).grid(row = 4, column = 2, stick = 'wens')

tk.Button(text = 'C', background="#000000", font='Courier 10', fg='#ffffff',
          command = delete).grid(row = 0, column = 5, stick = 'wens', rowspan = 5)


window.mainloop()