# @author Kamonyo

import pymongo
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import font as tk_font  # python 3


# #################### Main Class ####################

class MedicalRecordApp(Tk):
    """ Main class to handle the main Frame """

    def __init__(self):
        Tk.__init__(self)

        self.title_font = tk_font.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title("Medical Record")
        self.geometry('1000x600')

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # ##################### MENU ###########################

        bar_menu = Menu(self, bg="orange")

        menu_file = Menu(bar_menu, tearoff=0)
        bar_menu.add_cascade(label="File", menu=menu_file)
        menu_file.add_command(label="Exit", command=self.call_exit)

        menu_edit = Menu(bar_menu, tearoff=1)
        bar_menu.add_cascade(label="Edit", menu=menu_edit)
        menu_edit.add_command(label="Copy", command=self.call_exit)
        menu_edit.add_command(label="Paste", command=self.call_exit)

        menu_view = Menu(bar_menu, tearoff=0)
        bar_menu.add_cascade(label="View", menu=menu_view)
        menu_view.add_command(label="View", command=lambda: self.show_frame("View"))

        menu_about = Menu(bar_menu, tearoff=0)
        bar_menu.add_cascade(label="About", menu=menu_about)
        menu_about.add_command(label="About", command=lambda: self.show_frame("About"))

        self.config(menu=bar_menu)

        ####################################################

        self.frames = {}
        for F in (MedicalForm, About, View):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MedicalForm")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()

    # exiting the app
    def call_exit(self):
        """ Function called to exit the application """
        # collection.delete_many({}) # deleting from DB all the records.
        self.deiconify()
        self.destroy()
        self.quit()


# #################### CLASSES ###############################

class MedicalRecord:
    """ contains all information on the medical record object """
    count = 0
    _id = count

    def __init__(self, first_name, last_name, sex, age, city, country, has_diabetes):
        """ constructor that instantiate the class """

        MedicalRecord.count += 1
        # auto-incrementation of the _id
        self._id = MedicalRecord.count
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.city = city
        self.country = country
        self.has_diabetes = has_diabetes

    def description(self):
        return "{}. {} {} ({}), {} - {}({})".format(self._id, self.first_name, self.last_name, self.sex, self.age,
                                                    self.city, self.country)


def on_focusout(event, entry):
    if entry.get() == '':
        entry.insert(0, 'Patient name')
        entry.config(fg='grey')


def on_entry_click(event, entry):
    """function that gets called whenever entry is clicked"""
    if entry.get() == 'First name' or entry.get() == 'Last name':
        entry.delete(0, "end")  # delete all the text in the entry
        entry.insert(0, '')  # Insert blank for user input
        entry.config(fg='black')


# Clearing entry when focused
def clear_entry(event, entry):
    entry.delete(0, END)


class MedicalForm(Frame):
    """ Form to save and list Medical Record """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.var = StringVar()
        self.diab = StringVar()
        # Creating and initialising a dictionary of objects
        my_dict = {}
        # inserting the three objects that were created
        # my_dict.update({count1: record1})
        # my_dict.update({count2: record2})
        # my_dict.update({count3: record3})

        # inserting the dictionary into DB straight
        # collection.insert_one(record1.__dict__)
        # collection.insert_one(record2.__dict__)
        # collection.insert_one(record3.__dict__)

        # #################### DB Access #############################

        uri = "mongodb://127.0.0.1:27017"
        client = pymongo.MongoClient(uri)
        database = client['medicalrecord']
        self.collection = database['record']

        # checking if the database was successfully created
        dblist = client.list_database_names()
        if "medicalrecord" in dblist:
            print("**** The database 'medicalrecord' exists.")

        # checking if the collection was successfully created
        collist = database.list_collection_names()
        if "record" in collist:
            print("**** The collection 'record' exists.")

        # iterating through the database...
        for key in my_dict:
            print(key, " -> ", my_dict[key].description())

        # Fetching into DB:
        self.all_data = self.collection.find()

        # Adding a top frame to hold my data entry form
        frm_top = Frame(master=self,
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
        self.ent_firstName = Entry(lblfrm_form,
                                   font=('arial', 12, 'normal'),
                                   width=30)
        # Positioning the firstName textbox on the window
        # ent_firstName.pack(ipady=20)
        self.ent_firstName.grid(column=0, row=1)
        self.ent_firstName.insert(0, "First name")
        self.ent_firstName.bind("<Button-1>", lambda event: clear_entry(event, self.ent_firstName))

        # adding a last name textbox with a limited width
        self.ent_lastName = Entry(lblfrm_form,
                                  font=('arial', 12, 'normal'),
                                  width=30)
        # Positioning the lastName textbox on the window
        self.ent_lastName.grid(column=1, row=1)
        self.ent_lastName.insert(0, "Last name")
        self.ent_lastName.bind("<Button-1>", lambda event: clear_entry(event, self.ent_lastName))

        # Adding a Label Frame to contain the Gender radio buttons
        lblfrm_labelframe = LabelFrame(lblfrm_form,
                                       width=100,
                                       bg="lightblue")
        lblfrm_labelframe.grid(column=0, row=2)
        # Adding radio button for sex

        rdo_male = Radiobutton(lblfrm_labelframe,
                               text="Male",
                               font=('arial', 12, 'normal'),
                               variable=self.var,
                               value="Male",
                               command=self.sel(),
                               bg="lightblue")
        rdo_male.pack(side=LEFT)

        rdo_female = Radiobutton(lblfrm_labelframe,
                                 text="Female",
                                 font=('arial', 12, 'normal'),
                                 variable=self.var,
                                 value="Female",
                                 command=self.sel(),
                                 bg="lightblue")
        rdo_female.pack(side=LEFT)

        # Adding a Spin Box to enter the Age
        self.sbox_age = Spinbox(lblfrm_form,
                                font=('arial', 12, 'normal'),
                                from_=0,
                                to=150)
        self.sbox_age.grid(column=1, row=2)
        # sbox_age.insert(1, "Age")
        # sbox_age.bind("<Button-1>", lambda event: clear_entry(event, sbox_age))

        # Adding a combo box to list the cities
        self.combo_city = Combobox(lblfrm_form,
                                   font=('arial', 12, 'normal'))
        self.combo_city['values'] = ("- City -",
                                     "Bujumbura",
                                     "Abidjan",
                                     "Kigali",
                                     "Brazzaville",
                                     "Dakar")
        self.combo_city.current(0)  # set the selected item
        self.combo_city.grid(column=0, row=3)

        # Adding a combo box to list the countries
        self.combo_country = Combobox(lblfrm_form,
                                      font=('arial', 12, 'normal'))
        self.combo_country['values'] = ("- Country -",
                                        "Burundi",
                                        "Cote d'Ivoire",
                                        "Rwanda",
                                        "Congo",
                                        "Senegal")
        self.combo_country.current(0)  # set the selected item
        self.combo_country.grid(column=1, row=3)

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
        # YES radio button definition
        rdo_yes = Radiobutton(lblfrm2,
                              text="Yes",
                              font=('arial', 12, 'normal'),
                              variable=self.diab,
                              value="Yes",
                              command=self.sel(),
                              bg="lightblue")
        rdo_yes.pack(side=LEFT)
        # NO radio button definition
        rdo_no = Radiobutton(lblfrm2,
                             text="No",
                             font=('arial', 12, 'normal'),
                             variable=self.diab,
                             value="No",
                             command=self.sel(),
                             bg="lightblue")
        rdo_no.pack(side=LEFT)
        # UNKNOWN radio button definition
        rdo_unknown = Radiobutton(lblfrm2,
                                  text="Unknown",
                                  font=('arial', 12, 'normal'),
                                  variable=self.diab,
                                  value="Unknown",
                                  command=self.sel(),
                                  bg="lightblue")
        rdo_unknown.pack(side=LEFT)

        # Adding a button to submit form data
        btn_save = Button(lblfrm_form,
                          command=self.save_record,
                          width=60,
                          text="SAVE",
                          font=('arial', 14, 'bold'),
                          fg="black",
                          bg="orange")
        btn_save.grid(columnspan=2)

        ####################################################

        # Adding a bottom frame to hold my list of medical records
        frm_bottom = Frame(master=self,
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
                             width=500,
                             bg="lightblue")
        lblfrm2.grid(columnspan=2, row=2)

        # Adding a scrollbar as we may need to see the full list of items
        scrollbar = Scrollbar(lblfrm2)
        scrollbar.pack(side=RIGHT, fill=BOTH)

        # Adding a list to populate the frame
        self.my_list = Listbox(lblfrm2,
                               width=120,
                               yscrollcommand=scrollbar.set)

        # Fetching through db:
        all_data = self.collection.find()

        # displaying all the data in collection 'record'
        for record in all_data:
            self.my_list.insert(END, record)

        self.my_list.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=self.my_list.yview)

    def sel(self):
        # my_gender = "You selected the option " + str(self.var.get())
        pass

    def sel_dia(self):
        # my_diabetes = "You selected the option " + str(self.diab.get())
        pass

    # Saving form data
    def save_record(self):
        confirmation = messagebox.askyesno("Confirmation", "Do you want to save the record?", icon="question")
        if confirmation:
            first_name = self.ent_firstName.get()
            last_name = self.ent_lastName.get()
            sex = self.var.get()
            age = self.sbox_age.get()
            city = self.combo_city.get()
            country = self.combo_country.get()
            has_diabetes = self.diab.get()

            # ######## Here we save to the DB...
            medical_record = MedicalRecord(first_name, last_name, sex, age, city, country, has_diabetes)
            self.collection.insert_one(medical_record.__dict__)
            # ########

            self.my_list.insert(END, medical_record.__dict__)
            messagebox.showinfo("Success", "Record saved successfully!", icon="info")

        elif not confirmation:
            messagebox.showerror("Refused", "Record not saved!", icon="error")

        elif confirmation is None:
            messagebox.showwarning("Cancellation", "Record cancelled!", icon="warning")


class About(Frame):
    """ Page with all information about our Medical Records App """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="This is ABOUT page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Go to the start page", command=lambda: controller.show_frame("MedicalForm"))
        button.pack()


class View(Frame):
    """ Page with all information to View on our Medical Records App """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="This is View page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Go to the Medical Record page",
                        command=lambda: controller.show_frame("MedicalForm"))
        button.pack()


# Running the App...
app = MedicalRecordApp()
app.mainloop()
