import tkinter as tk

r = tk.Tk()
r.title("Calculator")
r.geometry("320x420")
r.resizable(False, False)


display = tk.Entry(r, font=("Comic Sans MS", 22), justify="right",
                   bd=5, relief="sunken", state="readonly")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

expression = ""        


def show(text):
    """Put text in the readonly display."""
    display.config(state="normal")
    display.delete(0, tk.END)
    display.insert(0, text)
    display.config(state="readonly")


def press(value):
    """Called when a digit, '.' or operator button is clicked."""
    global expression
    if expression == "Error":
        expression = ""
    expression += value
    show(expression)


def clear():
    global expression
    expression = ""
    show("")


def backspace():
    global expression
    expression = expression[:-1]
    show(expression)


def calculate():
    global expression
    if expression == "":
        return
    try:
        result = eval(expression)        
        if isinstance(result, float) and result.is_integer():
            result = int(result)         
        expression = str(result)
    except ZeroDivisionError:
        expression = "Error"
    except Exception:
        expression = "Error"
    show(expression)

buttons = [
    ("C", 1, 0, clear),         ("<-", 1, 1, backspace),
    ("%", 1, 2, lambda: press("%")), ("/", 1, 3, lambda: press("/")),
    ("7", 2, 0, lambda: press("7")), ("8", 2, 1, lambda: press("8")),
    ("9", 2, 2, lambda: press("9")), ("*", 2, 3, lambda: press("*")),
    ("4", 3, 0, lambda: press("4")), ("5", 3, 1, lambda: press("5")),
    ("6", 3, 2, lambda: press("6")), ("-", 3, 3, lambda: press("-")),
    ("1", 4, 0, lambda: press("1")), ("2", 4, 1, lambda: press("2")),
    ("3", 4, 2, lambda: press("3")), ("+", 4, 3, lambda: press("+")),
    ("0", 5, 0, lambda: press("0")), (".", 5, 1, lambda: press(".")),
    ("=", 5, 2, calculate),
]

for text, row, col, cmd in buttons:
    if text in ("C", "<-"):
        color = "#aea6f4"
    elif text in ("/", "*", "-", "+", "%"):
        color = "#ffd27f"
    elif text == "=":
        color = "#11da40"
    else:
        color = "#8B4F4F"
    span = 2 if text == "=" else 1
    tk.Button(r, text=text, font=("Comic Sans MS", 16), bg=color,
              command=cmd).grid(row=row, column=col, columnspan=span,
                                padx=4, pady=4, sticky="nsew")

for i in range(4):
    r.grid_columnconfigure(i, weight=1)
for i in range(6):
    r.grid_rowconfigure(i, weight=1)

r.mainloop()     