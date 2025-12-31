# A simple GUI calculator using tkinter
import tkinter as tk

# Creating a window
root = tk.Tk()
root.title("GUI Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Displaying it
display = tk.Entry(
    root,
    font=("sans serif", 20),
    bd=10,
    relief="ridge",
    justify="right"
)
display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# the functions
def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(value))

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for text, row, col in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, font=("Arial", 16), command=calculate)
    else:
        btn = tk.Button(
            root,
            text=text,
            font=("Arial", 16),
            command=lambda t=text: button_click(t)
        )
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# the Clear button
clear_btn = tk.Button(root, text="C", font=("Arial", 16), command=clear_display)
clear_btn.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Making the grid responsive
for i in range(6):
    root.rowconfigure(i, weight=1)
for j in range(4):
    root.columnconfigure(j, weight=1)

root.mainloop()
