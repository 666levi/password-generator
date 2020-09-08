# imports
import random
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

# window settings
root.resizable(width = False, height = False)
root.geometry('250x290')
root.title('Password Generator')
root['bg'] = '#ffffff'
root.iconbitmap('./img/logo.ico')

# functions
def password_gen(event):

    # all variables
    allSymbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    password = []
    count = 0

    # get service name and password length
    service = entry_service.get()
    length = entry_length.get()

    # create and write down the password
    if service and length:
        if length.isdigit():
            while count < int(length):
                password += random.sample(allSymbols, 1)
                count += 1
            global readyPW 
            readyPW = ''.join(password)
            messagebox.showinfo('Done.', f'Your password: {readyPW}')
        else:
            messagebox.showerror('Error.', 'Enter the number to the "Length" box.') 
        with open('myPWs.txt', 'a', encoding='utf-8') as writePW:
            writePW.write(f'Service: {service}\nPassword: {readyPW}\n\n')
            writePW.close()
    
    # if any box is empty
    elif not service and length:
        messagebox.showerror('Error.', '"Service" box is empty.')
    elif service and not length:
        messagebox.showerror('Error.', '"Length" box is empty.')
    else:
        messagebox.showerror('Error.', 'Both boxes are empty.')

# events
frame_green = tk.Frame(bg = '#91ffc2', width = 250, height = 15)
frame_green.grid(row = 0, column = 0)
text_service = tk.Label(text = 'Service', font = ('SF Pro Display', 22), fg = '#333333', bg = '#fff')
text_service.grid(row = 1, column = 0, pady = 5)
entry_service = tk.Entry(root, font = ('Consolas', 14), fg = '#333333', bg = '#e6e6fa', relief = 'solid', justify = 'center', width = 16)
entry_service.grid(row = 2, column = 0, pady = 0)
frame_white = tk.Frame(bg = '#fff', width = 250, height = 1)
frame_white.grid(row = 3, column = 0, pady = 8)
text_length = tk.Label(text = 'Length', font = ('SF Pro Display', 22), fg = '#333333', bg = '#fff')
text_length.grid(row = 4, column = 0, pady = 5)
entry_length = tk.Entry(root, font = ('Consolas', 14), fg = '#333333', bg = '#e6e6fa', relief = 'solid', justify = 'center', width = 8)
entry_length.grid(row = 5, column = 0, pady = 0)
button_generate = tk.Button(text = 'Generate', font = ('SF Pro Display', 16), relief = 'solid', fg = '#333333', bg = '#91ffc2', activeforeground = '#333333', activebackground = '#91ffc2', borderwidth = 0)
button_generate.grid(row = 6, column = 0, pady = 35)

# binds
button_generate.bind('<Button-1>', password_gen)

root.mainloop()