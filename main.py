import tkinter as tk
from tkinter import ttk
import sqlite3
from ttkthemes import ThemedStyle


# Enabling High DPI Awareness
try :
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except :
    pass


def update_records():
    pass


def view_records():
    pass


# Tkinter app properties
root = tk.Tk()
theme = ThemedStyle(theme="breeze")
root.title('Textbook Tracker v1.0.1')
root.resizable(False, False)
root.geometry('560x200')
root.wm_iconbitmap(r'favicon.ico')
name = tk.StringVar()

alphabet = tk.StringVar()
book_name = tk.StringVar()
#standalone_path.set("C:\\")
#autopilot_path.set("C:\\")

# Widget Definition
l1 = ttk.Label(text='Alphabet')
l2 = ttk.Label(text='Book Name')
l3 = ttk.Label(text='https://github.com/Prathapdom/Textbook_Tracker')
e1 = ttk.Entry(width=30, textvariable=alphabet)
e2 = ttk.Entry(width=30, textvariable=book_name)
btn1 = ttk.Button(root, text='Add', command=lambda: update_records())
btn2 = ttk.Button(root, text='View', command=lambda: view_records())

# Widget Presentation
l1.grid(row=0, column=0, pady=10, padx=10)
l2.grid(row=1, column=0, pady=10, padx=10)
e1.grid(row=0, column=1, pady=10, padx=10)
e2.grid(row=1, column=1, pady=10, padx=10)
btn1.grid(row=2, column=0, pady=10, padx=10)
btn2.grid(row=2, column=1, pady=10, padx=10)
l3.grid(row=3, column=1, pady=10, padx=10)


# App loop
root.mainloop()
