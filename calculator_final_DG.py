import tkinter as tk
import math

calculation = ""

def add_to_calculaton(symbol):
    global calculation 
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "error")
    



def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

    pass


root = tk.Tk()
root.geometry("300x275")

text_result = tk.Text(root, height=2, width=16, font=("Ariel", 24))
text_result.grid(columnspan=5)
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculaton(1), width=5, font= ("Ariel", 14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculaton(2), width=5, font= ("Ariel", 14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculaton(3), width=5, font= ("Ariel", 14))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculaton(4), width=5, font= ("Ariel", 14))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculaton(5), width=5, font= ("Ariel", 14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculaton(6), width=5, font= ("Ariel", 14))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculaton(7), width=5, font= ("Ariel", 14))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculaton(8), width=5, font= ("Ariel", 14))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculaton(9), width=5, font= ("Ariel", 14))
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculaton(0), width=5, font= ("Ariel", 14))
btn_0.grid(row=5, column=2)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculaton("+"), width=5, font= ("Ariel", 14))
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculaton("-"), width=5, font= ("Ariel", 14))
btn_minus.grid(row=3, column=4)
btn_mult = tk.Button(root, text="*", command=lambda: add_to_calculaton("*"), width=5, font= ("Ariel", 14))
btn_mult.grid(row=4, column=4)
btn_div = tk.Button(root, text="/", command=lambda: add_to_calculaton("/"), width=5, font= ("Ariel", 14))
btn_div.grid(row=5, column=4)
btn_equ = tk.Button(root, text="=", command=evaluate_calculation, width=5, font= ("Ariel", 14))
btn_equ.grid(row=5, column=2)
btn_del = tk.Button(root, text="clear", command=clear_field, width=5, font= ("Ariel", 14))
btn_del.grid(row=1, column=4)
btn_exp = tk.Button(root, text="^x", command=lambda: add_to_calculaton("**"), width=5, font= ("Ariel", 14))
btn_exp.grid(row=5, column=1)
btn_sqrt = tk.Button(root, text="^-x", command=lambda: add_to_calculaton("**(1/"), width=5, font= ("Ariel", 14))
btn_sqrt.grid(row=5, column=3)
btn_PL = tk.Button(root, text="(", command=lambda: add_to_calculaton("("), width=5, font= ("Ariel", 14))
btn_PL.grid(row=1, column=1)
btn_PR =tk.Button(root, text=")", command=lambda: add_to_calculaton(")"), width=5, font= ("Ariel", 14))
btn_PR.grid(row=1, column=3)
root.mainloop()
