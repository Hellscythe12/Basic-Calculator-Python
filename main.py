import tkinter as tk

calculation = ""

#Functions
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

#GUI
root = tk.Tk()
root.geometry("300x275")

text_result = tk.Text(root, height=2, width=16, font=("Arial",24))
text_result.grid(columnspan=5)

#Button Values
bt_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width="5", font=("Arial", 14))
bt_1.grid(row=2, column=1)
bt_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width="5", font=("Arial", 14))
bt_2.grid(row=2, column=2)
bt_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width="5", font=("Arial", 14))
bt_3.grid(row=2, column=3)
bt_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width="5", font=("Arial", 14))
bt_4.grid(row=3, column=1)
bt_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width="5", font=("Arial", 14))
bt_5.grid(row=3, column=2)
bt_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width="5", font=("Arial", 14))
bt_6.grid(row=3, column=3)
bt_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width="5", font=("Arial", 14))
bt_7.grid(row=4, column=1)
bt_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width="5", font=("Arial", 14))
bt_8.grid(row=4, column=2)
bt_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width="5", font=("Arial", 14))
bt_9.grid(row=4, column=3)
bt_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width="5", font=("Arial", 14))
bt_0.grid(row=5, column=2)

#Button Operations
bt_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width="5", font=("Arial", 14))
bt_plus.grid(row=2, column=4)
bt_min = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width="5", font=("Arial", 14))
bt_min.grid(row=3, column=4)
bt_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width="5", font=("Arial", 14))
bt_mul.grid(row=4, column=4)
bt_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width="5", font=("Arial", 14))
bt_div.grid(row=5, column=4)
bt_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width="5", font=("Arial", 14))
bt_open.grid(row=5, column=1)
bt_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width="5", font=("Arial", 14))
bt_close.grid(row=5, column=3)
bt_clear = tk.Button(root, text="C", command=clear_field, width="11", font=("Arial", 14))
bt_clear.grid(row=6, column=1, columnspan=2)
bt_eq = tk.Button(root, text="=", command= evaluate_calculation, width="11", font=("Arial", 14))
bt_eq.grid(row=6, column=3, columnspan=2)
root.mainloop()


