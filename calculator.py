
import tkinter as tk
import math

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Function to handle trigonometric operations
def trig_function(event):
    func_name = event.widget.cget("text")
    try:
        value = float(entry.get())
        if func_name == "sin":
            result = math.sin(math.radians(value))
        elif func_name == "cos":
            result = math.cos(math.radians(value))
        elif func_name == "tan":
            result = math.tan(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Main application window
root = tk.Tk()
root.title("Simple Calculator By Riya Kushwah")
root.geometry("400x500")

# Entry widget to display the calculations and results
entry = tk.Entry(root, font=("Book Antiqua", 20), justify="right")
entry.pack(fill=tk.BOTH, expand=True)

# Buttons for numbers and operators
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+"),
    ("sin", "cos", "tan", "C")
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    for button_text in row:
        button = tk.Button(frame, text=button_text, font=("Book Antiqua", 20), relief=tk.GROOVE)
        button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        if button_text in ["sin", "cos", "tan"]:
            button.bind("<Button-1>", trig_function)
        else:
            button.bind("<Button-1>", on_click)

root.mainloop()
