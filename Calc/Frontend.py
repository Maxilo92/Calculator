from Backend import calc
from tkinter import Tk, Label, Button, Entry
from tkinter import ttk

def calculate():
    term = entry.get()
    result = calc(term)
    result_label.config(text=f"= {result}")

root = Tk()
root.title("Calculator 0.1.4 Beta")
root.minsize(400, 150)
frm = ttk.Frame(root, padding=10)
frm.grid(sticky="nsew")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frm.columnconfigure(0, weight=3)
frm.columnconfigure(1, weight=2)
frm.rowconfigure(0, weight=1)
frm.rowconfigure(1, weight=1)

entry = ttk.Entry(frm, width=30)
entry.grid(column=0, row=0, sticky="ew", padx=5, pady=5)
result_label = ttk.Label(frm, text="")
result_label.grid(column=1, row=0, sticky="ew", padx=5, pady=5)
ttk.Button(frm, text="=", command=calculate).grid(column=0, row=1, sticky="ew", padx=5, pady=5)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1, sticky="ew", padx=5, pady=5)
root.mainloop()