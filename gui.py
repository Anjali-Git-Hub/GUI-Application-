import tkinter as tk
import os
from tkinter import ttk
from csv import DictWriter
win=tk.Tk()
win.title("My application")


# creating labels using ttk module
name_label=ttk.Label(win,text="enter your name :")
name_label.grid(row=0,column=0,sticky=tk.W)

age_label=ttk.Label(win,text="enter your age :")
age_label.grid(row=1,column=0,sticky=tk.W)

email_label=ttk.Label(win, text="enter your email :")
email_label.grid(row=2,column=0,sticky=tk.W)

gender_label=ttk.Label(win,text='select your gender :')
gender_label.grid(row=3,column=0,sticky=tk.W)


# creating entrybox

name_var=tk.StringVar()
name_entrybox=ttk.Entry(win,width=16,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()


age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=16,textvariable=age_var)
age_entrybox.grid(row=1,column=1)


email_var=tk.StringVar()
email_entrybox=ttk.Entry(win,width=16,textvariable=email_var)
email_entrybox.grid(row=2,column=1)

# create combo box
comboBox_val=tk.StringVar()
comboBox=ttk.Combobox(win,width=10,textvariable=comboBox_val,state='readonly')
comboBox['values']=('Male','Female','Other')
comboBox.current(2)
comboBox.grid(row=3,column=1)


# create radio buttons
userinput=tk.StringVar()
student=ttk.Radiobutton(win,text='student',value='student',variable=userinput)
student.grid(row=4,column=0)
teacher=ttk.Radiobutton(win,text='teacher',value='teacher',variable=userinput)
teacher.grid(row=4,column=1)


# check button
checkbtn_val=tk.IntVar()
checkbutton=ttk.Checkbutton(win,text="Subscribe to our Newsletter",variable=checkbtn_val)
checkbutton.grid(row=5,column=0)



# submit button 
def action():
    username=name_var.get()
    userage=age_var.get()
    useremail=email_var.get()
    usergender=comboBox_val.get()
    profession=userinput.get()
    if checkbtn_val.get()==1:
        subscribe=True
    else:
        subscribe=False

    # with csv file

    with open('file.csv','a',newline='')as f:
        dictwriter=DictWriter(f,fieldnames=['username','user age','user email','gender','status','subscribe'])
        if os.stat('file.csv').st_size==0:
            dictwriter.writeheader()
        dictwriter.writerow({
            'username':username,
            'user age':userage,
            'user email':useremail,
            'gender':usergender,
            'status':profession,
            'subscribe':subscribe
        })





    # with text file 

    # with open('file.txt','a') as f:
    #     f.write(f"{username},{userage},{useremail},{usergender},{profession},{subscribe}\n")
   
   
   
    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    name_label.configure(foreground='Blue')



submit_entrybox=ttk.Button(win,text="submit",command=action)
submit_entrybox.grid(row=6,column=0)

win.mainloop()