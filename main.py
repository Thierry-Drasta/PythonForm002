import tkinter
from tkinter import ttk
from tkinter import messagebox

def enter_data():
    
    accepted = accept_var.get()
    
    if accepted == "Accepted":
    
        # User Info
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        
        if first_name and last_name:
        
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
            
            # Course Info
            registration_status = reg_status_var.get()
            numcourse = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()
            
            print("first name:", first_name, "last name:", last_name)
            print("title:", title, "age:", age, "nationality:", nationality)
            print("# Courses:", numcourse, "# Semesters:", numsemesters)
            print("registration status: ", registration_status)
            print("********************************************")
            
        else:
            tkinter.messagebox.showwarning(title="Error", message="First name and Last name are required.")
    
    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms.")

# Creating root window, it is the parent window for everything else.
window =  tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)   #parent of frame is window. that's why we out in window as a parent

frame.pack()

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)


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
    

#Saving course info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(courses_frame, text="Registration status")

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently registered",
                                       variable=reg_status_var, onvalue="Registered", offvalue="Not Registered")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text="# Completed courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text= "# Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms and Condition")
terms_frame.grid(row=2, column=0, sticky='news', padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")

terms_check = tkinter.Checkbutton(terms_frame, text='I accept the terms and condition.', 
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")

terms_check.grid(row=0, column=0)

# Button

button = tkinter.Button(frame, text='Enter data', command=enter_data)
button.grid(row=3, column=0, sticky='news', padx=20, pady=10)




window.mainloop()