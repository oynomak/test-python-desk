# @author Kamonyo

from tkinter import *
# handles radio buttons click
from tkinter.ttk import Combobox

####################################################


def sel():
    myGender = "You selected the option " + str(var.get())

def selDia():
    myDiabetes = "You selected the option " + str(diab.get())


####################################################

# instantiation of tkinter
window = Tk()
# title the window
window.title("Medical Record")
# size of the window
window.geometry('1000x600')

####################################################
# Adding a top frame to hold my data entry form
topFrame = Frame(master=window, bg="lightblue", height="200")
topFrame.pack(fill=BOTH, expand=TRUE)

# adding a first name textbox with a limited width
firstName = Entry(topFrame, width=30)
# Positioning the firstName textbox on the window
firstName.grid(column=0, row=1)

# adding a last name textbox with a limited width
lastName = Entry(topFrame, width=30)
# Positioning the lastName textbox on the window
lastName.grid(column=1, row=1)

# Adding a Label Frame to contain the Gender radio buttons
labelframe = LabelFrame(topFrame, width=100, bg="lightblue")
labelframe.grid(column=0, row=2)
# Adding radio button for sex
var = StringVar()
maleRadio = Radiobutton(labelframe, text="Male", variable=var, value="Male", command=sel(), bg="lightblue")
maleRadio.pack(side=LEFT)

femaleRadio = Radiobutton(labelframe, text="Female", variable=var, value="Female", command=sel(), bg="lightblue")
femaleRadio.pack(side=LEFT)

# Adding a Spin Box to enter the Age
w = Spinbox(topFrame, from_=0, to=150)
w.grid(column=1, row=2)

# Adding a combo box to list the cities
cityList = Combobox(topFrame)
cityList['values']= ("- City -", "Bujumbura", "Abidjan", "Kigali", "Brazzaville", "Dakar")
cityList.current(0) #set the selected item
cityList.grid(column=0, row=3)

# Adding a combo box to list the countries
countryList = Combobox(topFrame)
countryList['values']= ("- Country -", "Burundi", "Cote d'Ivoire", "Rwanda", "Congo", "Senegal")
countryList.current(0) #set the selected item
countryList.grid(column=1, row=3)

# Adding a label to display "Living with Diabetes"
diabetesLbl = Label(topFrame, text="Living with Diabetes?", bg="lightblue")
diabetesLbl.grid(column=0, row=4)

# Adding a Label Frame to contain the diabetes radio buttons
labelframe2 = LabelFrame(topFrame, width=100, bg="lightblue")
labelframe2.grid(column=1, row=4)

# Adding radio button for sex
diab = StringVar()
yesRadio = Radiobutton(labelframe2, text="Yes", variable=diab, value="Yes", command=sel(), bg="lightblue")
yesRadio.pack(side=LEFT)

noRadio = Radiobutton(labelframe2, text="No", variable=diab, value="No", command=sel(), bg="lightblue")
noRadio.pack(side=LEFT)

unknownRadio = Radiobutton(labelframe2, text="Unknown", variable=diab, value="Unknown", command=sel(), bg="lightblue")
unknownRadio.pack(side=LEFT)

# Adding a button to submit form data
saveBtn = Button(topFrame, text="Red", fg="red")
saveBtn.grid(column=1, row=5)

####################################################

# Adding a bottom frame to hold my list of medical records
bottomFrame = Frame(master=window, bg="lightblue", height="400")
bottomFrame.pack(fill=BOTH, expand=TRUE)

# Adding a label to add title to the list
listTitle = Label(master=bottomFrame, text="List of medical records", bg="lightblue")
listTitle.grid(column=0, row=0)

# Adding a label frame to contain the scrollbar
labelframe2 = LabelFrame(bottomFrame, width=100, bg="lightblue")
labelframe2.grid(column=0, row=1)

# Adding a scrollbar as we may need to see the full list of items
scrollbar = Scrollbar(labelframe2)
scrollbar.pack(side=RIGHT, fill=BOTH)
# scrollbar.grid(column=0, row=1)

# Adding a list to populate the frame
myList = Listbox(labelframe2, yscrollcommand=scrollbar.set)

for line in range(100):
   myList.insert(END, "This is line number " + str(line))

myList.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=myList.yview)

####################################################

# running the application
window.mainloop()
