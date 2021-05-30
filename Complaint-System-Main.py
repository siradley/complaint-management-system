from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

from complaintListing import ComplaintListing
from configdb import ConnectionDatabase


#Config

conn = ConnectionDatabase()
master = Tk()
master.geometry('650x550')
master.title('Complaint Management System')
master.configure(bg='gray85')

p1 = PhotoImage(file = 'srs.png')

master.iconphoto(False, p1)

#Style

style = Style()
style.theme_use('clam')
for styles in ['TLabel', 'TButton', 'TRadioButton']:
    style.configure(styles, bg='ghost white')

labels = ['First Name:', 'Last Name:', 'Address:', 'Gender:', 'Comment:']
for i in range(5):
        Label(master, font = 'Helvetica 14', text=labels[i]).grid(row=i, column=0, padx=15, pady=15)


ButtonList = Button(master, text='View Complain')
ButtonList.grid(row=7, column=1)


ButtonSubmit = Button(master, text='Submit Now')
ButtonSubmit.grid(row=7, column=2)

# Entries
firstname = Entry(master, width=40, font=('Arial', 14))
firstname.grid(row=0, column=1, columnspan=2)

lastname = Entry(master, width=40, font=('Arial', 14))
lastname.grid(row=1, column=1, columnspan=2)

telephone_no = Entry(master, width=40, font=('Arial', 14))
telephone_no.grid(row=2, column=1, columnspan=2)

address = Entry(master, width=40, font=('Arial', 14))
address.grid(row=4, column=1, columnspan=2)

GenderGroup = StringVar(master, "1")
Radiobutton(master, text='Male', value='male', variable=GenderGroup).grid(row=3, column=1)
Radiobutton(master, text='Female', value='female', variable=GenderGroup).grid(row=3, column=2)


comment = Text(master, width=40, height=8, font=('Arial', 14))
comment.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

def SaveData():
    message = conn.Add(firstname.get(), lastname.get(), address.get(), GenderGroup.get(), comment.get(1.0, 'end'))
    firstname.delete(0,'end')
    lastname.delete(0, 'end')
    address.delete(0, 'end')
    comment.delete(1.0, 'end')
    showinfo(title='Add Information', message=message)

def ShowComplainList():

    listrequest = ComplaintListing()


ButtonSubmit.config(command=SaveData)
ButtonList.config(command=ShowComplainList)

mainloop()
master.mainloop()
