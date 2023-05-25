import tkinter
from tkinter import ttk

# Creating root window, it is the parent window for everything else.
window =  tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)   #parent of frame is window. that's why we out in window as a parent

frame.pack()

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=20)


first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)

last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

# Entry, is a textbox where user  will writes input
first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)


title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr", "Ms", "Mrs", "Dr"])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=100)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["","Africa", "Antarctica", "Asia", "Europe", "Oceania", "North America", "South America"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

'''
we have (3) different widgets such as Entry, Spinbox and Combobox
we have to give them the padding as the children contained into 
the label frame.

and also, remember "combobox" is used when you import the ttk from tkinter.
'''

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

window.mainloop()