from calculator import Calculator
import tkinter as tk

def get_values():
    purchase_price = float(purchase_price_entry.get())
    down_payment = float(down_payment_entry.get())
    interest_rate = float(interest_rate_entry.get())
    loan_term = int(loan_term_entry.get())
    mortgage = Calculator(year_count=loan_term, interest_rate=interest_rate, purchase_price=purchase_price, down_payment=down_payment)
    print(mortgage._calculate_monthly_payment())

root = tk.Tk()
root.title("Amortization Schedule Calculator")
root.config(width=800, height=450, padx=50, pady=50)

title_label = tk.Label(text="Amortization Schedule Calculator", font=("Arial", 24, "bold"))
title_label.grid(column=0, row=0, columnspan=2)

purchase_price_label = tk.Label(text="Purchase Price", font=("Arial", 18, "normal"), padx=20, pady=20)
purchase_price_label.grid(column=0, row=1)

purchase_price_entry = tk.Entry()
purchase_price_entry.grid(column=1, row=1)

down_payment_label = tk.Label(text="Down Payment", font=("Arial", 18, "normal"), padx=20, pady=20)
down_payment_label.grid(column=0, row=2)

down_payment_entry = tk.Entry()
down_payment_entry.grid(column=1, row=2)

interest_rate_label = tk.Label(text="Interest Rate (Decimal)", font=("Arial", 18, "normal"), padx=20, pady=20)
interest_rate_label.grid(column=0, row=3)

interest_rate_entry = tk.Entry()
interest_rate_entry.grid(column=1, row=3)

loan_term_label = tk.Label(text="Loan Term (Years)", font=("Arial", 18, "normal"), padx=20, pady=20)
loan_term_label.grid(column=0, row=4)

loan_term_entry = tk.Entry()
loan_term_entry.grid(column=1, row=4)

submit_values_button = tk.Button(text="Calculate", command=get_values)
submit_values_button.grid(column=0, row=5, columnspan=2)

# mortgage = Calculator(year_count=30, interest_rate=0.0287, purchase_price=245000, down_payment=12000)
# print(mortgage._calculate_monthly_payment())



tk.mainloop()