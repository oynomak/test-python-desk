# @author Kamonyo

from tkinter import *
# handles radio buttons click
from tkinter.ttk import Combobox


####################################################


def sel():
    myGender = "You selected the option " + str(var.get())

def selDia():
    myDiabetes = "You selected the option " + str(diab.get())

# Clearing entry when focused
def clear_entry(event, entry):
    entry.delete(0, END)

####################################################

# instantiation of tkinter
window = Tk()
# title the window
window.title("Medical Record")
# size of the window
window.geometry('1000x600')

####################################################
# Adding a top frame to hold my data entry form
frm_top = Frame(master=window,
                 bg="lightblue",
                 height="200")
frm_top.pack(fill=BOTH, expand=TRUE)

# adding a first name textbox with a limited width
ent_firstName = Entry(frm_top, width=30)
# Positioning the firstName textbox on the window
ent_firstName.grid(column=0, row=1)
ent_firstName.insert(0, "First name")
ent_firstName.bind("<Button-1>", lambda event: clear_entry(event, ent_firstName))

# adding a last name textbox with a limited width
ent_lastName = Entry(frm_top, width=30)
# Positioning the lastName textbox on the window
ent_lastName.grid(column=1, row=1)
ent_lastName.insert(0, "Last name")
ent_lastName.bind("<Button-1>", lambda event: clear_entry(event, ent_lastName))

# Adding a Label Frame to contain the Gender radio buttons
lblfrm_labelframe = LabelFrame(frm_top,
                               width=100,
                               bg="lightblue")
lblfrm_labelframe.grid(column=0, row=2)
# Adding radio button for sex
var = StringVar()
rdo_male = Radiobutton(lblfrm_labelframe,
                       text="Male",
                       variable=var,
                       value="Male",
                       command=sel(),
                       bg="lightblue")
rdo_male.pack(side=LEFT)

rdo_female = Radiobutton(lblfrm_labelframe,
                         text="Female",
                         variable=var,
                         value="Female",
                         command=sel(),
                         bg="lightblue")
rdo_female.pack(side=LEFT)

# Adding a Spin Box to enter the Age
sbox_age = Spinbox(frm_top, from_=0, to=150)
sbox_age.grid(column=1, row=2)
# sbox_age.insert(1, "Age")
# sbox_age.bind("<Button-1>", lambda event: clear_entry(event, sbox_age))

# Adding a combo box to list the cities
combo_city = Combobox(frm_top)
combo_city['values'] = ("- City -",
                      "Bujumbura",
                      "Abidjan",
                      "Kigali",
                      "Brazzaville",
                      "Dakar")
combo_city.current(0)  # set the selected item
combo_city.grid(column=0, row=3)

# Adding a combo box to list the countries
combo_country = Combobox(frm_top)
combo_country['values'] = ("- Country -",
                         "Burundi",
                         "Cote d'Ivoire",
                         "Rwanda",
                         "Congo",
                         "Senegal")
combo_country.current(0)  # set the selected item
combo_country.grid(column=1, row=3)

# Adding a label to display "Living with Diabetes"
lbl_diabetes = Label(frm_top,
                     text="Living with Diabetes?",
                     bg="lightblue")
lbl_diabetes.grid(column=0, row=4)

# Adding a Label Frame to contain the diabetes radio buttons
lblfrm2 = LabelFrame(frm_top,
                         width=100,
                         bg="lightblue")
lblfrm2.grid(column=1, row=4)

# Adding radio button for sex
diab = StringVar()
# YES radio button definition
rdo_yes = Radiobutton(lblfrm2,
                      text="Yes",
                      variable=diab,
                      value="Yes",
                      command=sel(),
                      bg="lightblue")
rdo_yes.pack(side=LEFT)
# NO radio button definition
rdo_no = Radiobutton(lblfrm2,
                     text="No",
                     variable=diab,
                     value="No",
                     command=sel(),
                     bg="lightblue")
rdo_no.pack(side=LEFT)
# UNKNOWN radio button definition
rdo_unknown = Radiobutton(lblfrm2,
                          text="Unknown",
                          variable=diab,
                          value="Unknown",
                          command=sel(),
                          bg="lightblue")
rdo_unknown.pack(side=LEFT)

# Adding a button to submit form data
btn_save = Button(frm_top,
                  text="SAVE",
                  fg="black",
                  bg="orange")
btn_save.grid(columnspan=2)

####################################################

# Adding a bottom frame to hold my list of medical records
frm_bottom = Frame(master=window,
                    bg="lightblue",
                    height="400")
frm_bottom.pack(fill=BOTH, expand=TRUE)

# Adding a label to add title to the list
lbl_title = Label(master=frm_bottom,
                  text="List of medical records",
                  bg="lightblue")
lbl_title.grid(column=0, row=0)

# Adding a label frame to contain the scrollbar
lblfrm2 = LabelFrame(frm_bottom,
                     width=100,
                     bg="lightblue")
lblfrm2.grid(column=0, row=1)

# Adding a scrollbar as we may need to see the full list of items
scrollbar = Scrollbar(lblfrm2)
scrollbar.pack(side=RIGHT, fill=BOTH)

# Adding a list to populate the frame
myList = Listbox(lblfrm2,
                 yscrollcommand=scrollbar.set)

for line in range(100):
    myList.insert(END, "Patient Names " + str(line + 1))

myList.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=myList.yview)

####################################################

# running the application
window.mainloop()
