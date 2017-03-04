# Mortgage calculator by me :)

import tkinter as tk

# create frame
window = tk.Tk()

# create frame size
window.geometry("400x300")

# create frame title
window.title("Mortgage calculator")

# add labels
loan_label = tk.Label(text="Loan amount")
loan_label.grid(column=0, row=0)
currency_label = tk.Label(text="$")
currency_label.grid(column=2, row=0)

rate_label = tk.Label(text="Annual interest rate")
rate_label.grid(column=0, row=1)
percentage_label = tk.Label(text="%")
percentage_label.grid(column=2, row=1)

payments_label = tk.Label(text="Number of payments")
payments_label.grid(column=0, row=2)
month_label = tk.Label(text="Months")
month_label.grid(column=2, row=2)

#add entry
loan_entry = tk.Entry()
loan_entry.grid(column=1, row=0)

rate_entry = tk.Entry()
rate_entry.grid(column=1, row=1)

payments_entry = tk.Entry()
payments_entry.grid(column=1, row=2)

def mortgage_calc():
	print(loan_entry.get())
	print(rate_entry.get())
	print(payments_entry.get())
	# Bank formula for mortgage--> M = L*[i*(1+i)**n]/[(1+i)**n-1]
	# M(monthly_payment) - Monthly payment
	# L(loan_entry) - Loan
	# i(rate_entry) - annual interest rate (%); rate--> 6% = 6/100 = 0,06
	#     to get monthly rate;              0,06/12 = 0,005
	#     that's why i divided with 1200 (100*12)
	# n(payments_entry) - number of payments
	monthly_payment = int(loan_entry.get()) * ((float(rate_entry.get())/1200) * (1 + (float(rate_entry.get())/1200)) ** int(payments_entry.get())) / ((1 + (float(rate_entry.get())/1200)) ** int(payments_entry.get()) - 1)
	print(monthly_payment)

	text_answer = tk.Text(master=window, height=10, width=20)
	text_answer.grid(column=1, row=3)
	# text formating with 2 decimals
	answer_text = "Your monthly payment is {0:.2f} $".format(monthly_payment)
	text_answer.insert(tk.END, answer_text)

# add calculate button
calculate_button = tk.Button(text="Calculate Mortgage", command=mortgage_calc)
calculate_button.grid(column=1, row=4)


window.mainloop()