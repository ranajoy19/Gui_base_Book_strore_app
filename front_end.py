"""
a program that can store this book information:
Title,Author
Year,ISBN

user can:
view all record
search an entry
add entry
update entry
Delect
Close
"""


#import  database
from tkinter import *
from back_end import Database

database=Database("book.db")

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    #print(selected_tuple)
    e1.delete(0, END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END,selected_tuple[4])





def view():
    list1.delete("0",END)
    for row in database.view():
        list1.insert(END,row)

def search():
    list1.delete("0",END)
    for row in database.search(v1.get(),v2.get(),v3.get(),v4.get()):
        list1.insert(END,row)
def add():
    database.insert(v1.get(),v2.get(),v3.get(),v4.get())
    list1.delete(0,END)
    list1.insert(END,(v1.get(),v2.get(),v3.get(),v4.get()))
def delete():
    database.delete(selected_tuple[0])

def update():
    database.update(selected_tuple[0],v1.get(),v2.get(),v3.get(),v4.get())











window = Tk()
# Title of the window
window.title("BOOK STORE")

#ALL THE LABLE OF FRONTEND

L0=Label(window,text="Title")
L0.grid(row=0,column=0)

L1=Label(window,text="Author")
L1.grid(row=0,column=2)

L2=Label(window,text="Year")
L2.grid(row=1,column=0)

L3=Label(window,text="ISBN")
L3.grid(row=1,column=2)

#ALL THE ENTRIES OF THE FRONTEND


v1=StringVar()
e1=Entry(window,textvariable=v1)
e1.grid(row=0,column=1)

v2=StringVar()
e2=Entry(window,textvariable=v2)
e2.grid(row=0,column=3)

v3=StringVar()
e3=Entry(window,textvariable=v3)
e3.grid(row=1,column=1)

v4=StringVar()
e4=Entry(window,textvariable=v4)
e4.grid(row=1,column=3)

# ONE LISTBOX OF THE FRONTEND

list1=Listbox(window, height=6,width=36)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

list1.bind('<<ListboxSelect>>',get_selected_row)

#ONE SCROLLBAR ATTACH TO LISTBOX


sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6,)

list1.config(yscrollcommand=sb1.set)
sb1.config(command=list1.yview())

# ALL BUTTONS ATTACH FRONTEND

b1=Button(window,text="Veiw all", width=12,command=view)
b1.grid(row=2,column=3)
b2=Button(window,text="Search entry", width=12,command=search)
b2.grid(row=3,column=3)
b3=Button(window,text="Add entry", width=12,command=add)
b3.grid(row=4,column=3)
b4=Button(window,text="Update", width=12,command=update)
b4.grid(row=5,column=3)
b5=Button(window,text="Delete", width=12,command=delete)
b5.grid(row=6,column=3)
b5=Button(window,text="Close", width=12,command=window.destroy)
b5.grid(row=7,column=3)



window.mainloop()

