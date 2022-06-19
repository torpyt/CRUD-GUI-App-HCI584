from tkinter import *

#Create GUI
app = Tk()
app.title('JDF Equipment Managment System')
app.geometry('700x350')

#Dealer
dealer_text = StringVar()
dealer_label = Label(app, text='Dealer Name', font=('bold', 14), pady=20)
dealer_label.grid(row=0, column=0, sticky=W)
dealer_entry = Entry(app, textvariable=dealer_text)
dealer_entry.grid(row=0, column=1)

#Customer
customer_text = StringVar()
customer_label = Label(app, text='Customer Name', font=('bold', 14), pady=20)
customer_label.grid(row=1, column=0, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=1, column=1)

#Equipment
equipment_text = StringVar()
equipment_label = Label(app, text='Equipment Name', font=('bold', 14), pady=20)
equipment_label.grid(row=0, column=2, sticky=W)
equipment_entry = Entry(app, textvariable=equipment_text)
equipment_entry.grid(row=0, column=3)

#Price
price_text = StringVar()
price_label = Label(app, text='Equipment Price', font=('bold', 14), pady=20)
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)

#Listbox
equipment_list = Listbox(app, height=8, width=50, border=0)
equipment_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

#Scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

#Align the scroll bar to the listbox
equipment_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=equipment_list.yview)




#Start program
app.mainloop()

