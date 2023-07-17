import tkinter as tk
from PIL import Image, ImageTk
from tkinter.font import Font
from tkinter.ttk import Combobox
from queue_data_struct import QueueAdapter
from dynamic_array import  listADT
import random
import string
import csv
import os.path
import os
panel = tk.Tk()
panel.geometry("800x500")
panel.title("SSN HELPDSK MANAGEMENT")

bg_colour="#273b7a"

login_icon=tk.PhotoImage(file="login_student_img.png")
admin_icon=tk.PhotoImage(file="admin_img.png")
add_persn_icon=tk.PhotoImage(file="add_student_.png")
locked_icon=tk.PhotoImage(file="locked.png")
unlocked_icon=tk.PhotoImage(file="unlocked.png")
add_account_icon=tk.PhotoImage(file="add_image.png")
create_icon=tk.PhotoImage(file="new_create.gif")
display_icon=tk.PhotoImage(file="new_disp.gif")
name_var=tk.StringVar()

def welcome_page_fn():

    def forward_student():
        welcome.destroy()
        panel.update()
        student_log_page_fn()
        

    def forward_admin():
        welcome.destroy()
        panel.update()
        admin_login_page_fn()

    def forward_add_account():
        welcome.destroy()
        panel.update()
        add_account_fn()

    welcome=tk.Frame(panel,highlightbackground="blue",highlightthickness=3)
    heading=tk.Label(welcome,text="Login",font=("bold", 15),bg="blue",fg="white")
    heading.place(x=0,y=0,width=400)
    #button
    student_login_but=tk.Button(welcome,text="Student Login",bg="blue",font=("bold", 15),fg="white",bd=0,command=forward_student)
    student_login_but.place(x=120,y=125,width=200)
    #icon
    student_login_image=tk.Button(welcome,image=login_icon,bd=0,command=forward_student)
    student_login_image.place(x=60,y=100)
    #-----------------------------------------------------------------
    #button
    admin_login_but=tk.Button(welcome,text="Admin Login",bg="blue",font=("bold", 15),fg="white",bd=0,command=forward_admin)
    admin_login_but.place(x=120,y=225,width=200)
    #icon
    admin_login_image=tk.Button(welcome,image=admin_icon,bd=0,command=forward_admin)
    admin_login_image.place(x=60,y=200)
    #-----------------------------------------------
    #button
    addstudent_but=tk.Button(welcome,text="Add Student",bg="blue",font=("bold", 15),fg="white",bd=0,command=forward_add_account)
    addstudent_but.place(x=120,y=325,width=200)
    #icon
    addstudent_image=tk.Button(welcome,image=add_persn_icon,bd=0,command=forward_add_account)
    addstudent_image.place(x=60,y=300)
    #-----------------------------------------------
    welcome.pack(pady=100)
    welcome.pack_propagate(False)
    welcome.configure(width=400,height=650)
def student_log_page_fn():
    def show_hide_pass():
        if password_ent['show']=="*":
            password_ent.config(show='')
            show_password.config(image=unlocked_icon)
        else:
            password_ent.config(show='*')
            show_password.config(image=locked_icon)

    def backward_fn():
        student_login_page.destroy()
        panel.update()
        welcome_page_fn()

    student_login_page=tk.Frame(panel,highlightbackground="blue",highlightthickness=3)
    heading_lab=tk.Label(student_login_page,text="Student Login Page",font=("bold", 15),bg="blue",fg="white")
    heading_lab.place(x=0,y=0,width=400)
    #----------------------------------
    back_button=tk.Button(student_login_page, text="←", fg=bg_colour, bd=0,command=backward_fn)
    back_button.place(x=5,y=40)
    #------------------------------
    stu_page_icon=tk.Label(student_login_page,image=login_icon)
    stu_page_icon.place(x=150,y=40)
    #-------------------------------------------
    id_no=tk.Label(student_login_page,text="Enter Student ID Number:",font=("bold", 15),fg="blue")
    id_no.place(x=80,y=140)
    #-----------------------------
    id_no_ent=tk.Entry(student_login_page,font=("bold", 15),justify=tk.CENTER,highlightcolor="light blue",highlightbackground="gray",highlightthickness=2)
    id_no_ent.place(x=80,y=190)
    #----------------------------
    password=tk.Label(student_login_page,text="Enter Password:",font=("bold", 15),fg="blue")
    password.place(x=80,y=240)
    #-----------------------------
    password_ent=tk.Entry(student_login_page,font=("bold", 15),justify=tk.CENTER,highlightcolor="green",highlightbackground="gray",highlightthickness=2,show='*')
    password_ent.place(x=80,y=290)
    #------------------------
    show_password=tk.Button(student_login_page, image=locked_icon, bd=0,command=show_hide_pass)
    show_password.place(x=310,y=280)
    #---------------------------
    login_button = tk.Button(student_login_page, text="Login", font=("bold", 14),bg=bg_colour, fg="white")
    login_button.place(x=95,y=340,width=200,height=40)
    #------------------------------
    forgot_password_button = tk.Button(student_login_page, text="🗝️\nForgot Password", fg=bg_colour, bd=0)
    forgot_password_button.place(x=150,y=390)
    #----------------------------
    student_login_page.pack(pady=100) 
    student_login_page.pack_propagate(False)
    student_login_page.configure(width=400,height=450)
    #------------------------------------------------
def admin_login_page_fn():
    def show_hide_pass():
            if password_ent['show']=="*":
                password_ent.config(show='')
                show_password.config(image=unlocked_icon)
            else:
                password_ent.config(show='*')
                show_password.config(image=locked_icon)
    def backward_fn():
        admin_login_page.destroy()
        panel.update()
        welcome_page_fn()
    admin_login_page=tk.Frame(panel,highlightbackground=bg_colour,highlightthickness=3)

    heading_label=tk.Label(admin_login_page,text="Admin Login Page",font=("bold", 15),bg=bg_colour,fg="white")
    heading_label.place(x=0,y=0,width=400)
    #-----------------------------------------
    
    back_button= tk.Button(admin_login_page, text="←", fg=bg_colour, bd=0,command=backward_fn)
    back_button.place(x=5,y=40)
    #------------------------------
    
    admin_page_icon=tk.Label(admin_login_page,image=admin_icon)
    admin_page_icon.place(x=150,y=40)
    #--------------------------------------
    username=tk.Label(admin_login_page,text="Enter admin Name:",font=("bold", 15),fg="blue")
    username.place(x=80,y=140)
    #-----------------------------
    username_ent=tk.Entry(admin_login_page,font=("bold", 15),justify=tk.CENTER,highlightcolor="light blue",highlightbackground="gray",highlightthickness=2)
    username_ent.place(x=80,y=190)
    #----------------------------
    password=tk.Label(admin_login_page,text="Enter Password:",font=("bold", 15),fg=bg_colour)
    password.place(x=80,y=240)
    #-----------------------------
    password_ent=tk.Entry(admin_login_page,font=("bold", 15),justify=tk.CENTER,highlightcolor="green",highlightbackground="gray",highlightthickness=2,show='*')
    password_ent.place(x=80,y=290)
    #------------------------
    show_password=tk.Button(admin_login_page, image=locked_icon, bd=0,command=show_hide_pass)
    show_password.place(x=310,y=280)
    #---------------------------
    login_button = tk.Button(admin_login_page, text="Login", font=("bold", 14),bg=bg_colour, fg="white")
    login_button.place(x=95,y=340,width=200,height=40)
    #----------------------------------
    admin_login_page.pack(pady=30) 
    admin_login_page.pack_propagate(False)
    admin_login_page.configure(width=400,height=430)
    #---------------------------------------------
student_gender=tk.StringVar()
#--------------------------------------
year_list=['First Year(1st)','Second Year(2nd)','Third Year(3rd)','Fourth Year(4th)']
#--------------------------------------------------------------------------------------
department_list=['IT','CSE','ECE','EEE','CHEM','CIVIL','MECH','BME']
#---------------------------------------------------------------------------------------
def add_account_fn():
    def backward_home_fn():
        add_account.destroy()
        panel.update()
        welcome_page_fn()

    def forward_choosing_page():
        add_account.pack_forget()
        panel.update()
        ticket_generation_page_fn()
    
    name=name_var.get()
    print("The name is : " + name)
    name_var.set("")

    #------------------------------------------------------------------------------------
    add_account=tk.Frame(panel,highlightbackground=bg_colour,highlightthickness=3)
    add_pic=tk.Frame(add_account,highlightbackground=bg_colour,highlightthickness=2)
    add_pic_button=tk.Button(add_pic, image=add_account_icon, bd=0)
    add_pic_button.pack()
    add_pic.place(x=5,y=5,width=105,height=105) 
    #------------------------------------------------
    stu_name_lab=tk.Label (add_account,text="Enter Student Name:",font=("bold", 15))
    stu_name_lab.place(x=5,y=130)
    #------------------------------------------------
    stu_name_ent=tk.Entry(add_account,textvariable=name_var,font=("bold", 15),highlightcolor=bg_colour,highlightbackground="gray",highlightthickness=2)
    stu_name_ent.place(x=5,y=160,width=180)
    #-----------------------------------------------------
    stu_gender_lab=tk.Label (add_account,text="Enter Student Gender:",font=("bold", 15))
    stu_gender_lab.place(x=5,y=210)
    #------------------------------------------------
    male_button=tk.Radiobutton(add_account, text="Male", font=("bold", 15),variable=student_gender,value="male")
    male_button.place(x=5,y=235)
    #--------------------------------------------------
    female_button=tk.Radiobutton(add_account, text="Female", font=("bold", 15),variable=student_gender,value="female")
    female_button.place(x=75,y=235)
    #----------------------------------------------------
    student_gender.set('male')
    #---------------------------------------------------
    stu_age=tk.Label(add_account,text="Enter Student Age:",font=("bold", 15))
    stu_age.place(x=5,y=275)
    #-----------------------------
    stu_age_ent=tk.Entry(add_account,font=("bold", 15),highlightcolor="green",highlightbackground="gray",highlightthickness=2)
    stu_age_ent.place(x=5,y=305,width=180)
    #--------------------------------------------
    stu_phone_no=tk.Label(add_account,text="Enter Phone Number:",font=("bold", 15))
    stu_phone_no.place(x=5,y=360)
    #-----------------------------
    stu_phone_no_ent=tk.Entry(add_account,font=("bold", 15),highlightcolor="green",highlightbackground="gray",highlightthickness=2)
    stu_phone_no_ent.place(x=5,y=390,width=180)
    #--------------------------------------------
    stu_class_label=tk.Label(add_account,text="Enter Student Year:",font=("bold", 15))
    stu_class_label.place(x=5,y=445)
    #-------------------------------------------
    Select_year_button=Combobox(add_account, font=("bold", 15),state="readonly",values=year_list)
    Select_year_button.place(x=5,y=475,width=180,height=30)
    #------------------------------------------
    stu_id_no_label=tk.Label(add_account,text="Enter Student ID Number:",font=("bold", 15))
    stu_id_no_label.place(x=240,y=35)
    #-----------------------------
    stu_id=tk.Entry(add_account,font=("bold", 15),highlightcolor="green",highlightbackground="gray",highlightthickness=2)
    stu_id.place(x=240,y=80,width=180)
    #------------------------------------------
    student_email=tk.Label(add_account,text="Enter Student Email Address:",font=("bold", 15))
    student_email.place(x=240,y=130)
    #-----------------------------
    student_email_ent=tk.Entry(add_account,font=("bold", 11),highlightcolor="green",highlightbackground="gray",highlightthickness=2)
    student_email_ent.place(x=240,y=160,width=180)
    #-----------------------------------------------------
    stu_dept_label=tk.Label(add_account,text="Enter Student Branch:",font=("bold", 15))
    stu_dept_label.place(x=240,y=220)
    #-----------------------------------------------------
    Select_department_button=Combobox(add_account, font=("bold", 15),state="readonly",values=department_list)
    Select_department_button.place(x=240,y=250,width=180,height=30)
    #-------------------------------------------------------------
    student_Password=tk.Label(add_account,text="Create Student Password:",font=("bold", 15))
    student_Password.place(x=240,y=290)
    #---------------------------------------------------
    student_Password_ent=tk.Entry(add_account,font=("bold", 11),highlightcolor="green",highlightbackground="gray",highlightthickness=2,show="*")
    student_Password_ent.place(x=240,y=320,width=180)
    #----------------------------------------------------------------------
    home_button = tk.Button(add_account, text="Home", font=("bold", 14),bg=bg_colour, fg="white",command=backward_home_fn)
    home_button.place(x=250,y=360,width=80,height=40)
    #----------------------------------------------------------------------
    Submit_button = tk.Button(add_account, text="Submit", font=("bold", 14),bg=bg_colour, fg="white",command=forward_choosing_page)
    Submit_button.place(x=350,y=360,width=80,height=40)
    #------------------------------------------------------------------------
    add_account.pack(pady=5)
    add_account.pack_propagate(False)
    add_account.configure(width=550,height=580)
    #---------------------------------------------------
   
    
    
    
    global age
    age=stu_age_ent.get()
    global phone_number
    global ID_No
    global Year
    global department
    global email
    global password

    
    phone_number=stu_phone_no_ent.get()
    ID_No=stu_id.get()
    Year=Select_year_button.get()
    department=Select_department_button.get()
    email=student_email_ent.get()
    password=student_Password_ent.get()

    print("THE NAME:",name)
    
hostel_list=['a','b','c','d','e']
academic_list=['a','b','c','d','e','f']
def create():
    creation1_page=tk.Frame(panel,highlightbackground=bg_colour,highlightthickness=3)
    heading_label=tk.Label(creation1_page,text="Choose",font=("bold", 15),bg=bg_colour,fg="white")
    heading_label.place(x=0,y=0,width=400)
    #---------------------------------------------------------------------------------------------
    stu_aca_label=tk.Label(creation1_page,text="ACADEMIC:",font=("bold", 15))
    stu_aca_label.place(x=125,y=80)
    #-------------------------------------------------------------------------------------------
    Select_academic_button=Combobox(creation1_page, font=("bold", 15),state="readonly",values=academic_list)
    Select_academic_button.place(x=125,y=120,width=180,height=30)
    #---------------------------------------------------------------------------------
    stu_hostel_label=tk.Label(creation1_page,text="HOSTEL:",font=("bold", 15))
    stu_hostel_label.place(x=125,y=190)
    #-------------------------------------------------------------------------------
    Select_hostel_button=Combobox(creation1_page, font=("bold", 15),state="readonly",values=hostel_list)
    Select_hostel_button.place(x=125,y=225,width=180,height=30)
    #------------------------------------------------------------------------------------
    query=tk.Label(creation1_page,text="Comment your Query:",font=("bold", 15))
    query.place(x=125,y=270)
    #---------------------------------------------------
    query_ent=tk.Text(creation1_page, font=("bold", 11),highlightcolor="green",highlightbackground="gray",highlightthickness=2)
    query_ent.place(x=125,y=300,width=400,height=200)

    #-------------------------------------------------------------------------------------
    global academic_choosen
    academic_choosen=Select_academic_button.get()
    #---------------------------------------------------------------------------------
    global hostel_choosen
    hostel_choosen=Select_hostel_button.get()
    #------------------------------------------------------------------------------------
    """global comment
    comment=query_ent.get()"""
    #-------------------------------------------------------------------------------------
    creation1_page.pack(pady=5)
    creation1_page.pack_propagate(False)
    creation1_page.configure(width=550,height=880)

def display():
    display_data=tk.Frame(panel,highlightbackground=bg_colour,highlightthickness=3)
    heading_label=tk.Label(display_data,text="Student",font=("algerian", 15),bg=bg_colour,fg="white")
    heading_label.place(x=0,y=0,width=400)
    #-------------------------------------------------------------------------
    label=tk.Label (display_data,text="Enter Label:",font=("bold", 15))
    label.place(x=5,y=130)
    #------------------------------------------------
    label=tk.Entry(display_data,font=("bold", 15),highlightcolor=bg_colour,highlightbackground="gray",highlightthickness=2)
    label.place(x=5,y=160,width=180) 
    #-----------------------------------------------
    global labell

    labell=label.get()
    
    #--------------------------------------------------
    print("NAME:",name)
    print("AGE:",name)
    print("ID NUMBER:",name)
    print("DEPARTMENT:",name)
    print("YEAR:",name)
    print("LABEL:",label)
    
    #-------------------------------------------------
    
    display_data.pack(pady=5)
    display_data.pack_propagate(False)
    display_data.configure(width=550,height=580)



import tkinter as tk

def ticket_generation_page_fn():
    def forward_to_creation_page():
        welcome.pack_forget()
        panel.update()
        create()
        
    def forward_to_display_page():
        welcome.pack_forget()
        panel.update()
        display()

    


    welcome=tk.Frame(panel,highlightbackground=bg_colour,highlightthickness=3)
    heading=tk.Label(welcome,text="Your Choice",font=("bold", 15),bg=bg_colour,fg="white")
    heading.place(x=0,y=0,width=400)
    #button
    create_but=tk.Button(welcome,text="Create Ticket",bg=bg_colour,font=("bold", 15),fg="white",bd=0,command=forward_to_creation_page)
    create_but.place(x=120,y=125,width=200)
    #icon
    create_image=tk.Button(welcome,image=create_icon,bd=0,command=forward_to_creation_page)
    create_image.place(x=60,y=100)
    #-----------------------------------------------------------------
    #button
    disp_but=tk.Button(welcome,text="Display Details",bg=bg_colour,font=("bold", 15),fg="white",bd=0,command=forward_to_display_page)
    disp_but.place(x=120,y=225,width=200)
    #icon
    disp_image=tk.Button(welcome,image=display_icon,bd=0,command=forward_to_display_page)
    disp_image.place(x=60,y=200)
    #-----------------------------------------------
    #button
    addstudent_but=tk.Button(welcome,text="Add Student",bg=bg_colour,font=("bold", 15),fg="white",bd=0)
    addstudent_but.place(x=120,y=325,width=200)
    #icon
    addstudent_image=tk.Button(welcome,image=add_persn_icon,bd=0)
    addstudent_image.place(x=60,y=300)
    #-----------------------------------------------
    welcome.pack(pady=100)
    welcome.pack_propagate(False)
    welcome.configure(width=400,height=650)


#------------------- BACK END ----------------------------------
filename = "Student.csv"
#Set to store the unique label of the tickects
used_ids = set()
ticket_label = {}
ticket_obj = {}
array = []
#object of queue_adapter store the ticket objects
q = QueueAdapter()
#Queue for the  Issue regarding Academic
academic_queue = QueueAdapter()
academic_queue_high = QueueAdapter()
academic_queue_medium = QueueAdapter()
academic_queue_low = QueueAdapter()
#Queue for the issue regarding Hostel
hostel_queue = QueueAdapter()
hostel_queue_high = QueueAdapter()
hostel_queue_medium = QueueAdapter()
hostel_queue_low = QueueAdapter()
class Ticket:
    def __init__(self,category, name, regno, dept, year, email,  issue_regarding, ticket_id):
        self.category = category
        self.name = name
        self.regno = regno
        self.dept = dept
        self.year = year
        self.email = email
        self.status = "Open"
        self.priority = "High"
        self.issue_regarding = issue_regarding
        self.ticket_id = ticket_id

    
    #Method to display the ticket   
    def display_ticket(self):
        print("\n")
        print(f"Name: {self.name}\nRegister no: {self.regno}\nDepartment: {self.dept}\nYear: {self.year}\nLabel:{ticket_obj[self]} ")
        print(f"Status:{self.status}")
        print(f"Priority:{self.priority}")
        print(f"Issue:{self.issue_regarding}")
        print(f"Ticket Created successfully!!")
        print("\n")
#Function to generate the unique label for the tickets
def generate_ticket_id(length=4):
    characters = string.ascii_letters + string.digits 
    while True:
        ticket_id = ''.join(random.choice(characters) for _ in range(length))
        if ticket_id not in used_ids:
            used_ids.add(ticket_id)
            return ticket_id
def create_ticket(category, username, regno, dept, year, gmail , issue_regarding, comment):
    
    global id
    id = generate_ticket_id()
    t = Ticket( category, username, regno, dept, year, gmail, issue_regarding, id )
    t.ticket_id = id
    ticket_label[id] = t
    ticket_obj[t] = id
    data = {"ticket_id": id, "Category":f"{category}","username":f"{username}", "regno":f"{regno}", "dept":f"{dept}","year":f"{year}", 
            "gmail":f"{gmail}", "priority_level": "High", "issue_regarding":f"{issue_regarding}", "Comment":f"{comment}"}
    file = open("Student.csv", "a", newline="")
    fieldnames= ["ticket_id","Category", "username", "regno", "dept","year", "gmail", "priority_level", "issue_regarding", "Comment" ]
    file_exists = os.path.isfile("Student.csv")
    writer = csv.DictWriter(file, fieldnames)
    if file_exists and os.stat("Student.csv").st_size == 0:
            writer.writeheader()
    writer.writerow(data)

    return t
#Method that read the ticket details from the csv file and create a ticket object and enqueue it into the stack
def read_tickets_from_csv(filename):
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["Category"]
            username = row['username']
            regno = row['regno']
            dept = row['dept']
            year = row['year']
            gmail = row['gmail']
            issue_regarding = row["issue_regarding"]
            priority = row["priority_level"]
            ticket_id = row["ticket_id"]
            #print("###", ticket_id)
            ticket = Ticket(category, username, regno, dept, year, gmail,priority, issue_regarding , ticket_id)
            if category == "academic":
                academic_queue.enqueue(ticket)
            elif category == "hostel":
                hostel_queue.enqueue(ticket)
            q.enqueue(ticket)
            ticket_label[row['ticket_id']] = ticket
            ticket_obj[ticket] = row['ticket_id']
    return q
  

add_account_fn()
panel.mainloop()


