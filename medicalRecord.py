# @author Kamonyo

import pymongo
from tkinter import *
# handles radio buttons click
from tkinter.ttk import Combobox

# #################### DB Access #############################

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['medicalrecord']
collection = database['record']

# checking if the database was successfully created
dblist = client.list_database_names()
if "medicalrecord" in dblist:
  print("**** The database 'medicalrecord' exists.")

# checking if the collection was successfully created
collist = database.list_collection_names()
if "record" in collist:
  print("**** The collection 'record' exists.")

# #################### CLASSES ###############################

class MedicalRecord:
    """ contains all information on the medical record """
    count = 0

    def __init__(self, first_name, last_name, sex, age, city, country, has_diabetes):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.city = city
        self.country = country
        self.has_diabetes = has_diabetes
        MedicalRecord.count += 1

    def description(self):
        return "{} {} ({}), {} - {}({})".format(self.first_name, self.last_name, self.sex, self.age, self.city,
                                                self.country)


# ################### DICTIONARY #############################

# Instantiating 3 objects of medical record
record1 = MedicalRecord("Kamonyo", "Mugabo", "Male", 42, "Kigali", "Rwanda", "No")
count1 = record1.count
record2 = MedicalRecord("Richard", "Herve", "Female", 42, "Abidjan", "Cote d'Ivoire", "Yes")
count2 = record1.count
record3 = MedicalRecord("Iradukunda", "Solal", "Male", 17, "Kigali", "Rwanda", "No")
count3 = record1.count

# Creating and initialising a dictionary of objects
mydict = {}
# inserting the three objects that were created
mydict.update({count1: record1})
mydict.update({count2: record2})
mydict.update({count3: record3})

# iterating through the database...
for key in mydict:
    print(key, " -> ", mydict[key].description())

# Inserting into DB:
collection.insert_one(record1.__dict__)
collection.insert_one(record2.__dict__)
collection.insert_one(record3.__dict__)

# Fetching through db:
alldata = collection.find()

# displaying all the data in collection 'record'
for record in alldata:
    print(record['first_name'])

# #################### METHODS ###############################

def on_entry_click(event, entry):
    """function that gets called whenever entry is clicked"""
    if entry.get() == 'First name' or entry.get() == 'Last name':
        entry.delete(0, "end")  # delete all the text in the entry
        entry.insert(0, '')  # Insert blank for user input
        entry.config(fg='black')


def on_focusout(event, entry):
    if entry.get() == '':
        entry.insert(0, 'Patient name')
        entry.config(fg='grey')


def sel():
    my_gender = "You selected the option " + str(var.get())


def sel_dia():
    my_diabetes = "You selected the option " + str(diab.get())


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
                height="100")
frm_top.pack(fill=BOTH, expand=TRUE)

# Adding a label to add title to the form
lbl_form = Label(master=frm_top,
                 font=('arial', 18, 'bold'),
                 text="Medical Record",
                 bg="lightblue")

# Arranging the label on the top of the Frame
lbl_form.pack(side=TOP)

lblfrm_form = LabelFrame(frm_top,
                         width=800,
                         height=180,
                         bg="lightblue")

# Arranging the label frame on the LEFT side
lblfrm_form.pack(fill=Y, side=LEFT)

# adding a first name textbox with a limited width
ent_firstName = Entry(lblfrm_form,
                      font=('arial', 12, 'normal'),
                      width=30)
# Positioning the firstName textbox on the window
# ent_firstName.pack(ipady=20)
ent_firstName.grid(column=0, row=1)
ent_firstName.insert(0, "First name")
ent_firstName.bind("<Button-1>", lambda event: clear_entry(event, ent_firstName))

# adding a last name textbox with a limited width
ent_lastName = Entry(lblfrm_form,
                     font=('arial', 12, 'normal'),
                     width=30)
# Positioning the lastName textbox on the window
ent_lastName.grid(column=1, row=1)
ent_lastName.insert(0, "Last name")
ent_lastName.bind("<Button-1>", lambda event: clear_entry(event, ent_lastName))

# Adding a Label Frame to contain the Gender radio buttons
lblfrm_labelframe = LabelFrame(lblfrm_form,
                               width=100,
                               bg="lightblue")
lblfrm_labelframe.grid(column=0, row=2)
# Adding radio button for sex
var = StringVar()
rdo_male = Radiobutton(lblfrm_labelframe,
                       text="Male",
                       font=('arial', 12, 'normal'),
                       variable=var,
                       value="Male",
                       command=sel(),
                       bg="lightblue")
rdo_male.pack(side=LEFT)

rdo_female = Radiobutton(lblfrm_labelframe,
                         text="Female",
                         font=('arial', 12, 'normal'),
                         variable=var,
                         value="Female",
                         command=sel(),
                         bg="lightblue")
rdo_female.pack(side=LEFT)

# Adding a Spin Box to enter the Age
sbox_age = Spinbox(lblfrm_form,
                   font=('arial', 12, 'normal'),
                   from_=0,
                   to=150)
sbox_age.grid(column=1, row=2)
# sbox_age.insert(1, "Age")
# sbox_age.bind("<Button-1>", lambda event: clear_entry(event, sbox_age))

# Adding a combo box to list the cities
combo_city = Combobox(lblfrm_form,
                      font=('arial', 12, 'normal'))
combo_city['values'] = ("- City -",
                        "Bujumbura",
                        "Abidjan",
                        "Kigali",
                        "Brazzaville",
                        "Dakar")
combo_city.current(0)  # set the selected item
combo_city.grid(column=0, row=3)

# Adding a combo box to list the countries
combo_country = Combobox(lblfrm_form,
                         font=('arial', 12, 'normal'))
combo_country['values'] = ("- Country -",
                           "Burundi",
                           "Cote d'Ivoire",
                           "Rwanda",
                           "Congo",
                           "Senegal")
combo_country.current(0)  # set the selected item
combo_country.grid(column=1, row=3)

# Adding a label to display "Living with Diabetes"
lbl_diabetes = Label(lblfrm_form,
                     text="Living with Diabetes?",
                     font=('arial', 12, 'normal'),
                     bg="lightblue")
lbl_diabetes.grid(column=0, row=4)

# Adding a Label Frame to contain the diabetes radio buttons
lblfrm2 = LabelFrame(lblfrm_form,
                     width=100,
                     bg="lightblue")
lblfrm2.grid(column=1, row=4)

# Adding radio button for sex
diab = StringVar()
# YES radio button definition
rdo_yes = Radiobutton(lblfrm2,
                      text="Yes",
                      font=('arial', 12, 'normal'),
                      variable=diab,
                      value="Yes",
                      command=sel(),
                      bg="lightblue")
rdo_yes.pack(side=LEFT)
# NO radio button definition
rdo_no = Radiobutton(lblfrm2,
                     text="No",
                     font=('arial', 12, 'normal'),
                     variable=diab,
                     value="No",
                     command=sel(),
                     bg="lightblue")
rdo_no.pack(side=LEFT)
# UNKNOWN radio button definition
rdo_unknown = Radiobutton(lblfrm2,
                          text="Unknown",
                          font=('arial', 12, 'normal'),
                          variable=diab,
                          value="Unknown",
                          command=sel(),
                          bg="lightblue")
rdo_unknown.pack(side=LEFT)

# Adding a button to submit form data
btn_save = Button(lblfrm_form,
                  width=60,
                  text="SAVE",
                  font=('arial', 14, 'bold'),
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
                  font=('arial', 18, 'bold'),
                  text="List of medical records",
                  bg="lightblue")
lbl_title.grid(column=0, row=0)

# Find record is displayed here
lblfrm_search = LabelFrame(frm_bottom,
                           width=200,
                           bg="lightblue")
lblfrm_search.grid(column=0, row=1)

# Adding a label for search
lbl_search = Label(lblfrm_search,
                   text="Find record   ",
                   font=('arial', 14, 'normal'),
                   bg="lightblue")
lbl_search.pack(side=LEFT)

# Adding a text field to search
ent_search = Entry(lblfrm_search,
                   font=('arial', 14, 'normal'),
                   width=20)
ent_search.pack(side=LEFT)

# Only minors is displayed here
chk_minor_state = BooleanVar()
# chk_minor_state.set(True) #set check state
chk_minors = Checkbutton(frm_bottom,
                         bg="lightblue",
                         text='Only minors',
                         font=('arial', 14, 'normal'),
                         var=chk_minor_state)
chk_minors.grid(column=1, row=1)

# Adding a label frame to contain the scrollbar
lblfrm2 = LabelFrame(frm_bottom,
                     width=100,
                     bg="lightblue")
lblfrm2.grid(column=0, row=2)

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
