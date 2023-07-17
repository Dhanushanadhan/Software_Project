import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox, Grid
from queue_data_struct import QueueAdapter
from LinkedList import *
from hash import *
import random
import string
import csv
import os.path
import os
import smtplib

panel = tk.Tk()
panel.geometry("1300x700")
panel.title("SSN HELPDESK MANAGEMENT")

details = []
bg_colour = "#273b7a"

login_icon = tk.PhotoImage(file="login_student_img.png")
admin_icon = tk.PhotoImage(file="admin_img.png")
add_persn_icon = tk.PhotoImage(file="add_student_.png")
locked_icon = tk.PhotoImage(file="locked.png")
unlocked_icon = tk.PhotoImage(file="unlocked.png")
add_account_icon = tk.PhotoImage(file="add_image.png")
create_icon = tk.PhotoImage(file="new_create.gif")
display_icon = tk.PhotoImage(file="new_disp.gif")
metadata = {}
name = tk.StringVar()
age = tk.StringVar()
email = tk.StringVar()
id_no = tk.StringVar()
department = tk.StringVar()
year = tk.StringVar()
academic_choosen = ""
comment = tk.StringVar()
ticket_result = None
move_var = None
assign_var = None
complt = None
stu_id = None
passw = tk.StringVar()
pwd = tk.StringVar()
academic_problems = {
    "Assignment submission": "High",
    "Exam-related questions": "Medium",
    "Scholarship applications and queries": "High",
    "Grading inquiries": "Medium",
    "Doubts related to the subjects": "High",
    "Lab-related queries": "Low",
}

# Create an instance of the HashTable
size = 10  # Choose an appropriate size for your use case
hash_table = HashTable(size)
# ------------------------------------------------------------
# Insert key-value pairs into the hash table
hash_table.insert("Assignment submission", "High")
hash_table.insert("Exam-related questions", "Medium")
hash_table.insert("Scholarship applications and queries", "High")
hash_table.insert("Grading inquiries", "Medium")
hash_table.insert("Doubts related to the subjects", "High")
hash_table.insert("Lab-related queries", "Low")
# ----------------------------------------------------------------


def confirm_fn(message):
    answer = tk.BooleanVar()
    answer.set(False)

    def action(ans):
        answer.set(ans)
        confirm_box.destroy()

    confirm_box = tk.Frame(panel, highlightbackground=bg_colour, highlightthickness=3)
    msg_label = tk.Label(confirm_box, text=message, font=("bold", 15))
    msg_label.pack(pady=20)
    cancel_button = tk.Button(
        confirm_box,
        text="CANCEL",
        font=("bold", 14),
        bg=bg_colour,
        fg="white",
        command=lambda: action(False),
        bd=0,
    )
    cancel_button.place(x=50, y=160)
    yes_button = tk.Button(
        confirm_box,
        text="YES",
        font=("bold", 14),
        bg=bg_colour,
        fg="white",
        command=lambda: action(True),
    )
    yes_button.place(x=190, y=160, width=80)
    confirm_box.place(x=100, y=120, width=320, height=220)

    panel.wait_window(confirm_box)
    return answer.get()


def msg_fn(message):
    msg_box = confirm_box = tk.Frame(
        panel, highlightbackground=bg_colour, highlightthickness=3
    )
    close_btn = tk.Button(
        confirm_box,
        text="X",
        font=("bold", 14),
        bg=bg_colour,
        fg=bg_colour,
        command=lambda: msg_box.destroy(),
        bd=0,
    )
    close_btn.place(x=290, y=5)
    msg_label = tk.Label(msg_box, text=message, font=("bold", 15))
    msg_label.pack(pady=50)
    msg_box.place(x=100, y=120, width=320, height=220)


import tkinter as tk
from tkinter import messagebox

import tkinter as tk
from tkinter import messagebox


def welcome_page_fn():
    def forward_student():
        welcome.destroy()
        panel.update()
        student_log_page_fn()

    def forward_admin():
        welcome.destroy()
        panel.update()
        admin_login_page_fn()

    welcome = tk.Frame(panel, highlightbackground="blue", highlightthickness=3)
    heading = tk.Label(welcome, text="Login", font=("bold", 15), bg="blue", fg="white")
    heading.place(x=0, y=0, width=400)
    # button
    student_login_but = tk.Button(
        welcome,
        text="Student Login",
        bg="blue",
        font=("bold", 15),
        fg="white",
        bd=0,
        command=forward_student,
    )
    student_login_but.place(x=120, y=125, width=200)
    # icon
    student_login_image = tk.Button(
        welcome, image=login_icon, bd=0, command=forward_student
    )
    student_login_image.place(x=60, y=100)
    # -----------------------------------------------------------------
    # button
    admin_login_but = tk.Button(
        welcome,
        text="Admin Login",
        bg="blue",
        font=("bold", 15),
        fg="white",
        bd=0,
        command=forward_admin,
    )
    admin_login_but.place(x=120, y=225, width=200)
    # icon
    admin_login_image = tk.Button(
        welcome, image=admin_icon, bd=0, command=forward_admin
    )
    admin_login_image.place(x=60, y=200)
    # -----------------------------------------------
    # button
    # -----------------------------------------------
    welcome.pack(pady=100)
    welcome.pack_propagate(False)
    welcome.configure(width=400, height=650)


def student_log_page_fn():
    def show_hide_pass():
        if passw["show"] == "*":
            passw.config(show="")
            show_password.config(image=unlocked_icon)
        else:
            passw.config(show="*")
            show_password.config(image=locked_icon)

    def forward_create():
        student_login_page.destroy()
        panel.update()
        add_account_fn()

    def backward_fn():
        student_login_page.destroy()
        panel.update()
        welcome_page_fn()

    student_login_page = tk.Frame(
        panel, highlightbackground="blue", highlightthickness=3
    )
    heading_lab = tk.Label(
        student_login_page,
        text="Student Login Page",
        font=("bold", 15),
        bg="blue",
        fg="white",
    )
    heading_lab.place(x=0, y=0, width=400)
    # ----------------------------------
    back_button = tk.Button(
        student_login_page, text="←", fg=bg_colour, bd=0, command=backward_fn
    )
    back_button.place(x=5, y=40)
    # ------------------------------
    stu_page_icon = tk.Label(student_login_page, image=login_icon)
    stu_page_icon.place(x=150, y=40)
    # -------------------------------------------
    id_no = tk.Label(
        student_login_page,
        text="Enter Student ID Number:",
        font=("bold", 15),
        fg="blue",
    )
    id_no.place(x=80, y=140)
    # -----------------------------
    id_no_stu = tk.Entry(
        student_login_page,
        font=("bold", 15),
        justify=tk.CENTER,
        highlightcolor="light blue",
        highlightbackground="gray",
        highlightthickness=2,
    )
    id_no_stu.place(x=80, y=190)
    # ----------------------------
    stu_name_lab = tk.Label(
        student_login_page, text="Enter Student Name:", font=("bold", 15)
    )
    stu_name_lab.place(x=80, y=250)
    # ------------------------------------------------
    student_name = tk.Entry(
        student_login_page,
        font=("bold", 15),
        textvariable=name,
        highlightcolor=bg_colour,
        highlightbackground="gray",
        highlightthickness=2,
    )
    student_name.place(x=80, y=300, width=180)

    # -------------------------------------------------------------------------------------------
    def valid_stu_id():
        global stu_id
        stu_id = id_no_stu.get()
        if not stu_id.isdigit() or int(stu_id) < 0 or stu_id == "":
            messagebox.showerror("Invalid", "Please enter a valid ID number")

    def valid_pass():
        global passw
        pwd = student_name.get()
        if not pwd.isalpha() or pwd == "":
            messagebox.showerror("Invalid Name", "Please enter a valid Name")

    # -----------------------------------------------------------------------------------------
    def submit():
        valid_stu_id()
        valid_pass()

    # --------------------------------------------------------------------------------------------

    # ------------------------
    show_password = tk.Button(
        student_login_page, image=locked_icon, bd=0, command=show_hide_pass
    )
    show_password.place(x=310, y=280)
    # ---------------------------
    login_button = tk.Button(
        student_login_page,
        text="Login",
        font=("bold", 14),
        bg=bg_colour,
        fg="white",
        command=forward_create,
    )
    login_button.place(x=95, y=340, width=200, height=40)
    # ------------------------------
    forgot_password_button = tk.Button(
        student_login_page, text="🗝️\nForgot Password", fg=bg_colour, bd=0
    )
    forgot_password_button.place(x=150, y=390)
    # ------------------------------------------------------------------
    submit_button = tk.Button(
        student_login_page,
        text="Submit",
        font=("bold", 14),
        bg=bg_colour,
        fg="white",
        command=submit,
    )
    submit_button.place(x=95, y=400, width=200, height=40)
    # ----------------------------------
    # ----------------------------
    student_login_page.pack(pady=100)
    student_login_page.pack_propagate(False)
    student_login_page.configure(width=400, height=450)
    # ------------------------------------------------


def admin_login_page_fn():
    def forward_admin():
        admin_login_page.destroy()
        panel.update()
        agent()

    def show_hide_pass():
        if password_ent["show"] == "*":
            password_ent.config(show="")
            show_password.config(image=unlocked_icon)
        else:
            password_ent.config(show="*")
            show_password.config(image=locked_icon)

    def backward_fn():
        admin_login_page.destroy()
        panel.update()
        welcome_page_fn()

    admin_login_page = tk.Frame(
        panel, highlightbackground=bg_colour, highlightthickness=3
    )

    heading_label = tk.Label(
        admin_login_page,
        text="Admin Login Page",
        font=("bold", 15),
        bg=bg_colour,
        fg="white",
    )
    heading_label.place(x=0, y=0, width=400)
    back_button = tk.Button(
        admin_login_page, text="←", fg=bg_colour, bd=0, command=backward_fn
    )
    back_button.place(x=5, y=40)
    # ------------------------------

    admin_page_icon = tk.Label(admin_login_page, image=admin_icon)
    admin_page_icon.place(x=150, y=40)
    # --------------------------------------
    username = tk.Label(
        admin_login_page, text="Enter admin Name:", font=("bold", 15), fg="blue"
    )
    username.place(x=80, y=140)
    # -----------------------------
    username_ent = tk.Entry(
        admin_login_page,
        font=("bold", 15),
        justify=tk.CENTER,
        highlightcolor="light blue",
        highlightbackground="gray",
        highlightthickness=2,
    )
    username_ent.place(x=80, y=190)
    # ----------------------------
    password = tk.Label(
        admin_login_page, text="Enter Password:", font=("bold", 15), fg=bg_colour
    )
    password.place(x=80, y=240)
    # -----------------------------
    password_ent = tk.Entry(
        admin_login_page,
        font=("bold", 15),
        justify=tk.CENTER,
        highlightcolor="green",
        highlightbackground="gray",
        highlightthickness=2,
        show="*",
    )
    password_ent.place(x=80, y=290)
    # ------------------------
    show_password = tk.Button(
        admin_login_page, image=locked_icon, bd=0, command=show_hide_pass
    )
    show_password.place(x=310, y=280)
    # ---------------------------
    login_button = tk.Button(
        admin_login_page,
        text="Login",
        font=("bold", 14),
        bg=bg_colour,
        fg="white",
        command=forward_admin,
    )
    login_button.place(x=95, y=340, width=200, height=40)
    # ----------------------------------
    submit_button = tk.Button(
        admin_login_page,
        text="Submit",
        font=("bold", 14),
        bg=bg_colour,
        fg="white",
        command=forward_admin,
    )
    submit_button.place(x=95, y=400, width=200, height=40)
    # ----------------------------------
    admin_login_page.pack(pady=30)
    admin_login_page.pack_propagate(False)
    admin_login_page.configure(width=400, height=480)
    # ---------------------------------------------------------------------------------------------------


def agent():
    def backward_fn():
        agent_data.destroy()
        panel.update()
        admin_login_page_fn()

    agent_data = tk.Frame(panel, highlightbackground=bg_colour, highlightthickness=3)
    agent_data.pack(pady=5)
    agent_data.pack_propagate(False)
    agent_data.configure(width=1050, height=680)
    label_frame = tk.Frame(agent_data)
    label_frame1 = tk.Frame(agent_data)

    heading_label = tk.Label(
        agent_data, text="Student", font=("algerian", 15), bg=bg_colour, fg="white"
    )
    heading_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    move_button = tk.Button(
        agent_data,
        text="TICKET AVAILABLE MOVE TO AGENT QUEUE",
        width=40,
        font=("bold", 14),
        bg=bg_colour,
        fg="white",
        command=lambda: my_func(),
    )
    move_button.grid(row=1, column=0, padx=10, pady=10)

    assigned_button = tk.Button(
        agent_data,
        text="ASSIGNED TICKET TO AGENT",
        font=("bold", 14),
        width=40,
        bg=bg_colour,
        fg="white",
        command=lambda: my_func1(),
    )
    assigned_button.grid(row=1, column=1, padx=10, pady=10)

    complete_button = tk.Button(
        agent_data,
        text="Complete",
        font=("bold", 14),
        bg=bg_colour,
        fg="white",
        command=lambda: my_func2(),
    )

    complete_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

    back_button = tk.Button(
        agent_data, text="←", fg=bg_colour, bd=0, command=backward_fn
    )
    back_button.grid(row=0, column=0, padx=10, pady=10, sticky="W")

    def my_func2():
        if checker("Assigned.csv") == 1:
            complete_button.config(state="disabled")
        else:
            global complt
            for child in label_frame.winfo_children():
                child.destroy()

            complt = finish()
            label_frame.grid(row=3, column=1, padx=10, pady=10, sticky="W")
            Name = tk.Label(
                label_frame, text=f"Student Name: {complt.name}", font=("bold", 15)
            )
            Name.grid(row=3, column=0, padx=5, pady=5, sticky="W")
            Dept = tk.Label(
                label_frame, text=f"Department: {complt.dept}", font=("bold", 15)
            )
            Dept.grid(row=4, column=0, padx=5, pady=5, sticky="W")
            yr = tk.Label(label_frame, text=f"Year: {complt.year}", font=("bold", 15))
            yr.grid(row=5, column=0, padx=5, pady=5, sticky="W")
            tracking = tk.Label(
                label_frame, text=f"Ticket Status: {complt.status}", font=("bold", 15)
            )
            tracking.grid(row=6, column=0, padx=5, pady=5, sticky="W")
            lab = tk.Label(
                label_frame, text=f"Ticket Label: {complt.ticket_id}", font=("bold", 15)
            )
            lab.grid(row=7, column=0, padx=5, pady=5, sticky="W")

    def my_func():
        if checker("Student.csv") == 1:
            move_button.config(state="disabled")
        else:
            global move_var
            move_var = move()

    def my_func1():
        if checker("Agent.csv") == 2:
            assigned_button.config(state="disabled")
        else:
            global assign_var
            assign_var = assign_to_agent()
            for child in label_frame1.winfo_children():
                child.destroy()

            label_frame1.grid(row=4, column=0, padx=10, pady=10, sticky="W")
            Name = tk.Label(
                label_frame1,
                text=f"Student Name: {assign_var[1].name}",
                font=("bold", 15),
            )
            Name.grid(row=0, column=0, padx=5, pady=5, sticky="W")
            Dept = tk.Label(
                label_frame1,
                text=f"Department: {assign_var[1].dept}",
                font=("bold", 15),
            )
            Dept.grid(row=1, column=0, padx=5, pady=5, sticky="W")
            yr = tk.Label(
                label_frame1, text=f"Year: {assign_var[1].year}", font=("bold", 15)
            )
            yr.grid(row=2, column=0, padx=5, pady=5, sticky="W")
            tracking = tk.Label(
                label_frame1,
                text=f"Ticket Status: {assign_var[1].status}",
                font=("bold", 15),
            )
            tracking.grid(row=3, column=0, padx=5, pady=5, sticky="W")
            lab = tk.Label(
                label_frame1,
                text=f"Ticket Label: {assign_var[1].ticket_id}",
                font=("bold", 15),
            )
            lab.grid(row=4, column=0, padx=5, pady=5, sticky="W")

            label_frame2 = tk.Frame(agent_data)
            label_frame2.grid(row=3, column=0, padx=10, pady=10, sticky="W")
            Name = tk.Label(
                label_frame2,
                text=f"Agent Name: {assign_var[0].name}",
                font=("bold", 15),
            )
            Name.grid(row=0, column=0, padx=5, pady=5, sticky="W")
            Dept = tk.Label(
                label_frame2, text=f"Agent ID: {assign_var[0].id}", font=("bold", 15)
            )
            Dept.grid(row=1, column=0, padx=5, pady=5, sticky="W")
            yr = tk.Label(
                label_frame2,
                text=f"Category: {assign_var[0].agent_category}",
                font=("bold", 15),
            )
            yr.grid(row=2, column=0, padx=5, pady=5, sticky="W")
            tracking = tk.Label(
                label_frame2,
                text=f"Agent Designation: {assign_var[0].designation}",
                font=("bold", 15),
            )
            tracking.grid(row=3, column=0, padx=5, pady=5, sticky="W")
            lab = tk.Label(
                label_frame2,
                text=f"Agent Workload: {assign_var[0].workload}",
                font=("bold", 15),
            )
            lab.grid(row=4, column=0, padx=5, pady=5, sticky="W")

    agent_data.pack(pady=5)
    agent_data.pack_propagate(False)
    agent_data.configure(width=1050, height=680)


student_gender = tk.StringVar()
# --------------------------------------
year_list = [
    "1",
    "2",
    "3",
    "4",
]
# --------------------------------------------------------------------------------------
department_list = ["IT", "CSE", "ECE", "EEE", "CHEM", "CIVIL", "MECH", "BME"]
# ---------------------------------------------------------------------------------------





# ---------------------------------------------------------------------------------------------


def add_account_fn():
    def valid_name():
        global name
        name = stu_name_ent.get()
        if not name.isalpha() or name == "":
            messagebox.showerror("Invalid Name", "Please enter a valid name")

    def valid_age():
        global age
        age = stu_age_ent.get()
        if not age.isdigit() or int(age) < 0 or age == "":
            messagebox.showerror("Invalid", "Please enter a valid age")

    def valid_id_no():
        global id_no
        id_no = stu_id.get()
        if not id_no.isdigit() or int(id_no) < 0 or id_no == "":
            messagebox.showerror("Invalid", "Please enter a valid admission number")

    def valid_department():
        global department
        department = Select_department_button.get()
        if not department.isalpha() or department == "":
            messagebox.showerror("Invalid", "Please enter a valid department")

    def valid_Year():
        global year
        year = Select_year_button.get()
        if not year.isdigit() or int(year) < 0 or int(year) > 4 or year == "":
            messagebox.showerror("Invalid", "Please enter a valid year")

    def valid_gmail():
        global email
        email = student_email_ent.get()
        if (
            "@" not in email
            or "." not in email
            or not email.endswith("@gmail.com")
            or email == ""
        ):
            messagebox.showerror("Invalid", "Please enter a valid email")

    """def valid_password():
        global pwd
        pwd = student_Password_ent.get()
        if len(pwd) < 8:
            messagebox.showerror("Invalid", "Please enter a valid password with at least 8 characters")"""

    def backward_home_fn():
        ans = messagebox.askyesno("Confirmation", "Do you want to leave?")
        if ans:
            add_account.destroy()
            panel.update()
            welcome_page_fn()

    def forward_choosing_page():
        add_account.pack_forget()
        panel.update()
        ticket_generation_page_fn()

    def backward_fn():
        add_account.destroy()
        panel.update()
        student_log_page_fn()

    def submit():
        valid_name()
        valid_age()
        valid_id_no()
        valid_department()
        valid_Year()
        valid_gmail()


    # ----------------------------------------------------------------------------------

    add_account = tk.Frame(panel, highlightbackground=bg_colour, highlightthickness=3)
    add_pic = tk.Frame(add_account, highlightbackground=bg_colour, highlightthickness=2)
    add_pic_button = tk.Button(add_pic, image=add_account_icon, bd=0)
    add_pic_button.pack()
    add_pic.place(x=5, y=5, width=105, height=105)
    # ------------------------------------------------
    stu_name_lab = tk.Label(add_account, text="Enter Student Name:", font=("bold", 15))
    stu_name_lab.place(x=5, y=130)
    # ------------------------------------------------
    stu_name_ent = tk.Entry(
        add_account,
        font=("bold", 15),
        textvariable=name,
        highlightcolor=bg_colour,
        highlightbackground="gray",
        highlightthickness=2,
    )
    stu_name_ent.place(x=5, y=160, width=180)
    # -----------------------------------------------------
    stu_gender_lab = tk.Label(
        add_account, text="Enter Student Gender:", font=("bold", 15)
    )
    stu_gender_lab.place(x=5, y=210)
    # ------------------------------------------------
    male_button = tk.Radiobutton(
        add_account,
        text="Male",
        font=("bold", 15),
        variable=student_gender,
        value="male",
    )
    male_button.place(x=5, y=235)
    # --------------------------------------------------
    female_button = tk.Radiobutton(
        add_account,
        text="Female",
        font=("bold", 15),
        variable=student_gender,
        value="female",
    )
    female_button.place(x=75, y=235)
    # ----------------------------------------------------
    student_gender.set("male")
    # ---------------------------------------------------
    stu_age = tk.Label(add_account, text="Enter Student Age:", font=("bold", 15))
    stu_age.place(x=5, y=275)
    # -----------------------------
    stu_age_ent = tk.Entry(
        add_account,
        font=("bold", 15),
        textvariable=age,
        highlightcolor="green",
        highlightbackground="gray",
        highlightthickness=2,
    )
    stu_age_ent.place(x=5, y=305, width=180)
    # --------------------------------------------
    stu_phone_no = tk.Label(add_account, text="Enter Phone Number:", font=("bold", 15))
    stu_phone_no.place(x=5, y=360)
    # -----------------------------
    stu_phone_no_ent = tk.Entry(
        add_account,
        font=("bold", 15),
        highlightcolor="green",
        highlightbackground="gray",
        highlightthickness=2,
    )
    stu_phone_no_ent.place(x=5, y=390, width=180)
    # --------------------------------------------
    stu_class_label = tk.Label(
        add_account, text="Enter Student Year:", font=("bold", 15)
    )
    stu_class_label.place(x=5, y=445)
    # -------------------------------------------
    Select_year_button = Combobox(
        add_account, font=("bold", 15), state="readonly", values=year_list
    )
    Select_year_button.place(x=5, y=475, width=180, height=30)
    # ------------------------------------------
    stu_id_no_label = tk.Label(
        add_account, text="Enter Student ID Number:", font=("bold", 15)
    )
    stu_id_no_label.place(x=240, y=35)
    # -----------------------------
    stu_id = tk.Entry(
        add_account,
        font=("bold", 15),
        highlightcolor="green",
        highlightbackground="gray",
        highlightthickness=2,
    )
    stu_id.place(x=240, y=80, width=180)
    # ------------------------------------------
    student_email = tk.Label(
        add_account, text="Enter Student Email Address:", font=("bold", 15)
    )
    student_email.place(x=240, y=130)
    # -----------------------------
    student_email_ent = tk.Entry(
        add_account,
        font=("bold", 11),
        highlightcolor="green",
        highlightbackground="gray",
        highlightthickness=2,
    )
    student_email_ent.place(x=240, y=160, width=180)
    # -----------------------------------------------------
    stu_dept_label = tk.Label(
        add_account, text="Enter Student Branch:", font=("bold", 15)
    )
    stu_dept_label.place(x=240, y=220)
    # -----------------------------------------------------
    Select_department_button = Combobox(
        add_account, font=("bold", 15), state="readonly", values=department_list
    )
    Select_department_button.place(x=240, y=250, width=180, height=30)
    # -------------------------------------------------------------
    student_Password = tk.Label(
        add_account, text="Create Student Password:", font=("bold", 15)
    )
    student_Password.place(x=240, y=290)
    # ---------------------------------------------------
    student_Password_ent = tk.Entry(
        add_account,
        font=("bold", 11),
        highlightcolor="green",
        highlightbackground="gray",
        highlightthickness=2,
        show="*",
    )
    student_Password_ent.place(x=240, y=320, width=180)
    # ----------------------------------------------------------------------
    home_button = tk.Button(
        add_account,
        text="Home",
        font=("bold", 14),
        bg=bg_colour,
        fg="white",
        command=lambda: [backward_home_fn()],
    )
    home_button.place(x=250, y=360, width=80, height=40)
    # ----------------------------------------------------------------------
    Submit_button = tk.Button(
        add_account,
        text="Submit",
        font=("bold", 14),
        bg=bg_colour,
        fg="white",
        command=lambda: [submit()],
    )
    Submit_button.place(x=350, y=360, width=80, height=40)
    # ------------------------------------------------------------------------
    back_button = tk.Button(
        add_account, text="←", fg=bg_colour, bd=0, command=backward_fn
    )
    back_button.place(x=5, y=40)
    # ----------------------------------------------------------------------------
    next_button = tk.Button(
        add_account,
        text="Next",
        font=("bold", 14),
        bg=bg_colour,
        fg="white",
        command=lambda: [forward_choosing_page()],
    )
    next_button.place(x=300, y=460, width=80, height=40)
    # -------------------------------------------------------------------------
    add_account.pack(pady=5)
    add_account.pack_propagate(False)
    add_account.configure(width=550, height=580)
    # ---------------------------------------------------


academic_list = [
    "Assignment submission",
    "Exam-related questions",
    "Scholarship applications and queries",
    "Grading inquiries",
    "Doubts related to the subjects",
    "Lab-related queries",
]


def tempory_details():
    creation2_page = (tk.Toplevel(panel),)
    creation2_page = tk.Frame(
        panel, highlightbackground=bg_colour, highlightthickness=3
    )
    heading_label = tk.Label(
        creation2_page, text="DETAILS", font=("bold", 15), bg=bg_colour, fg="white"
    )
    heading_label.place(x=0, y=0, width=400)

    # ----------------------------------------------------------------------------------------------
    Name = tk.Label(creation2_page, text=f"Student Name:{name}", font=("bold", 15))
    Name.place(x=5, y=130)
    # ---------------------------------------------------------------------------------------------
    Dept = tk.Label(creation2_page, text=f"Department:{department}", font=("bold", 15))
    Dept.place(x=5, y=170)
    # -----------------------------------------------------------------------------------------------
    yr = tk.Label(creation2_page, text=f"Year:{year}", font=("bold", 15))
    yr.place(x=5, y=200)
    # ------------------------------------------------------------------------------------------------
    label = tk.Label(creation2_page, text=f"Label:{ticket_result}", font=("bold", 15))
    yr.place(x=5, y=200)
    # -------------------------------------------------------------------------------------------------
    creation2_page.pack(pady=5)
    creation2_page.pack_propagate(False)
    creation2_page.configure(width=550, height=580)


def create():
    def forward_details_page():
        creation1_page.destroy()
        panel.update()
        tempory_details()

    def backward_fn():
        creation1_page.destroy()
        panel.update()
        ticket_generation_page_fn()

    # ------------------------------------------------------------------------------------------------
    creation1_page = tk.Frame(
        panel, highlightbackground=bg_colour, highlightthickness=3
    )
    heading_label = tk.Label(
        creation1_page, text="Choose", font=("bold", 15), bg=bg_colour, fg="white"
    )
    heading_label.place(x=0, y=0, width=400)

    # ----------------------------------------------------------------------------------------------
    stu_aca_label = tk.Label(creation1_page, text="ACADEMIC:", font=("bold", 15))
    stu_aca_label.place(x=125, y=80)
    # -------------------------------------------------------------------------------------------
    Select_academic_button = Combobox(
        creation1_page,
        font=("bold", 15),
        state="readonly",
        values=academic_list,
    )
    Select_academic_button.place(x=125, y=120, width=180, height=30)
    # ---------------------------------------------------------------------------------

    query = tk.Label(creation1_page, text="Comment your Query:", font=("bold", 15))
    query.place(x=125, y=270)
    # ---------------------------------------------------
    # --------------------------------------------------------
    global comment
    query_ent = tk.Entry(
        creation1_page,
        font=("bold", 11),
        highlightcolor="green",
        highlightbackground="gray",
        highlightthickness=2,
        textvariable=comment,
    )
    query_ent.place(x=125, y=300, width=400, height=200)

    # ---------------------------------------------------------------------------------------------
    back_button = tk.Button(
        creation1_page, text="←", fg=bg_colour, bd=0, command=backward_fn
    )
    back_button.place(x=5, y=40)
    # ----------------------------------------------------------------------------------------------

    # -------------------------------------------------------------------------------------

    def submit_button_click():
        global ticket_result
        # Call the create_ticket function and store the return value
        ticket_result = create_ticket(
            name,
            id_no,
            department,
            year,
            email,
            select_priority_academic(Select_academic_button.get()),
            Select_academic_button.get(),
            query_ent.get(),
        )
        # Access and use the ticket_result value as needed

    # ------------------------------------------------------------------------------------------------------
    Submit_button = tk.Button(
        creation1_page,
        text="Submit",
        font=("bold", 14),
        bg=bg_colour,
        fg="white",
        # username, regno, dept, year, gmail , priority_level, issue_regarding, comment
        command=lambda: [submit_button_click()],
    )
    Submit_button.place(x=350, y=660, width=80, height=40)
    # -------------------------------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------------------------------
    print("meow")
    Details_button = tk.Button(
        creation1_page,
        text="Details",
        font=("bold", 14),
        bg=bg_colour,
        fg="white",
        command=forward_details_page,
    )
    Details_button.place(x=150, y=660, width=80, height=40)
    # ---------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------------
    # global issue
    # issue = Select_academic_button.get()

    creation1_page.pack(pady=5)
    creation1_page.pack_propagate(False)
    creation1_page.configure(width=550, height=880)


def tempory_details():
    def backward_fn():
        creation2_page.destroy()
        panel.update()
        ticket_generation_page_fn()

    creation2_page = (tk.Toplevel(panel),)
    creation2_page = tk.Frame(
        panel, highlightbackground=bg_colour, highlightthickness=3
    )
    heading_label = tk.Label(
        creation2_page, text="DETAILS", font=("bold", 15), bg=bg_colour, fg="white"
    )
    heading_label.place(x=0, y=0, width=400)

    # ----------------------------------------------------------------------------------------------
    Name = tk.Label(creation2_page, text=f"Student Name:{name}", font=("bold", 15))
    Name.place(x=5, y=130)
    # ---------------------------------------------------------------------------------------------
    Dept = tk.Label(creation2_page, text=f"Department:{department}", font=("bold", 15))
    Dept.place(x=5, y=170)
    # -----------------------------------------------------------------------------------------------
    yr = tk.Label(creation2_page, text=f"Year:{year}", font=("bold", 15))
    yr.place(x=5, y=200)
    # ------------------------------------------------------------------------------------------------
    tracking = tk.Label(
        creation2_page, text=f"Ticket_Status:{ticket_result.status}", font=("bold", 15)
    )
    tracking.place(x=5, y=230)
    # -------------------------------------------------------------------------------------------------
    lab = tk.Label(
        creation2_page,
        text=f"Ticket_label:{ticket_result.ticket_id }",
        font=("bold", 15),
    )
    lab.place(x=5, y=260)

    # -------------------------------------------------------------------------------------------------
    prior = tk.Label(
        creation2_page,
        text=f"Ticket_Priority:{ticket_result.priority }",
        font=("bold", 15),
    )
    prior.place(x=5, y=260)
    # ------------------------------------------------------------------------------------------------
    query = tk.Label(
        creation2_page, text=f"Issue:{ticket_result.issue_regarding}", font=("bold", 15)
    )
    query.place(x=5, y=290)
    # ------------------------------------------------------------------------------------------------
    back_button = tk.Button(
        creation2_page, text="←", fg=bg_colour, bd=0, command=backward_fn
    )
    back_button.place(x=5, y=40)
    # ------------------------------------------------------------------------------------------------
    creation2_page.pack(pady=5)
    creation2_page.pack_propagate(False)
    creation2_page.configure(width=550, height=580)


def display():
    def forward_permanent_page():
        display_data.destroy()
        panel.update()
        permanent_details()

    display_data = tk.Frame(panel, highlightbackground=bg_colour, highlightthickness=3)
    heading_label = tk.Label(
        display_data, text="Student", font=("algerian", 15), bg=bg_colour, fg="white"
    )
    heading_label.place(x=0, y=0, width=400)
    # -------------------------------------------------------------------------
    label = tk.Label(display_data, text="Enter Label:", font=("bold", 15))
    label.place(x=5, y=130)
    # ------------------------------------------------
    label = tk.Entry(
        display_data,
        font=("bold", 15),
        highlightcolor=bg_colour,
        highlightbackground="gray",
        highlightthickness=2,
    )
    label.place(x=5, y=160, width=180)

    # -------------------------------------------------------------------------------------------------------
    def show_details():
        if label.get() in ticket_label:
            global output
            output = get_ticket_by_label(label.get())
        else:
            Details_button.config(state="disabled")
        # Access and use the ticket_result value as needed

    # ------------------------------------------------------------------------------------------------------
    store_button = tk.Button(
        display_data,
        text="Store",
        font=("bold", 14),
        bg=bg_colour,
        fg="white",
        # username, regno, dept, year, gmail , priority_level, issue_regarding, comment
        command=lambda: [show_details()],
    )
    store_button.place(x=150, y=260, width=80, height=40)
    # ---------------------------------------------------------------------------------------------
    Details_button = tk.Button(
        display_data,
        text="Details",
        font=("bold", 14),
        bg=bg_colour,
        fg="white",
        command=forward_permanent_page,
    )
    Details_button.place(x=220, y=360, width=80, height=40)
    # --------------------------------------------------------------------------------------------
    display_data.pack(pady=5)
    display_data.pack_propagate(False)
    display_data.configure(width=550, height=580)


def permanent_details():
    details = (tk.Toplevel(panel),)
    details = tk.Frame(panel, highlightbackground=bg_colour, highlightthickness=3)
    heading_label = tk.Label(
        details, text="DETAILS", font=("bold", 15), bg=bg_colour, fg="white"
    )
    heading_label.place(x=0, y=0, width=400)
    """ self.name = name
        self.regno = regno
        self.dept = dept
        self.year = year
        self.email = email
        self.status = "Open"
        self.priority = priority
        self.issue_regarding = issue_regarding
        self.ticket_id = ticket_id"""

    # ----------------------------------------------------------------------------------------------
    Name = tk.Label(details, text=f"Student Name:{output.name}", font=("bold", 15))
    Name.place(x=5, y=130)
    # ---------------------------------------------------------------------------------------------
    Dept = tk.Label(details, text=f"Department:{output.dept}", font=("bold", 15))
    Dept.place(x=5, y=170)
    # -----------------------------------------------------------------------------------------------
    yr = tk.Label(details, text=f"Year:{output.year}", font=("bold", 15))
    yr.place(x=5, y=200)
    # ------------------------------------------------------------------------------------------------
    tracking = tk.Label(
        details, text=f"Ticket_Status:{output.status}", font=("bold", 15)
    )
    tracking.place(x=5, y=230)
    # -------------------------------------------------------------------------------------------------
    lab = tk.Label(details, text=f"Ticket_label:{output.ticket_id }", font=("bold", 15))
    lab.place(x=5, y=260)

    # -------------------------------------------------------------------------------------------------
    prior = tk.Label(
        details, text=f"Ticket_Priority:{output.priority }", font=("bold", 15)
    )
    prior.place(x=5, y=290)
    # ---------------------------------------------------------------------------------------------------
    query = tk.Label(details, text=f"Issue:{output.issue_regarding}", font=("bold", 15))
    query.place(x=5, y=260)
    # ---------------------------------------------------------------------------------------------------
    details.pack(pady=5)
    details.pack_propagate(False)
    details.configure(width=550, height=580)


def ticket_generation_page_fn():
    def forward_to_creation_page():
        welcome.pack_forget()
        panel.update()
        create()

    def forward_to_display_page():
        welcome.pack_forget()
        panel.update()
        display()

    def backward_fn():
        welcome.destroy()
        panel.update()
        add_account_fn()

    welcome = tk.Frame(panel, highlightbackground=bg_colour, highlightthickness=3)
    heading = tk.Label(
        welcome, text="Your Choice", font=("bold", 15), bg=bg_colour, fg="white"
    )
    heading.place(x=0, y=0, width=400)

    # button
    create_but = tk.Button(
        welcome,
        text="Create Ticket",
        bg=bg_colour,
        font=("bold", 15),
        fg="white",
        bd=0,
        command=forward_to_creation_page,
    )
    create_but.place(x=120, y=125, width=200)
    # icon
    create_image = tk.Button(
        welcome, image=create_icon, bd=0, command=forward_to_creation_page
    )
    create_image.place(x=60, y=100)
    # -----------------------------------------------------------------
    # button
    disp_but = tk.Button(
        welcome,
        text="Display Details",
        bg=bg_colour,
        font=("bold", 15),
        fg="white",
        bd=0,
        command=forward_to_display_page,
    )
    disp_but.place(x=120, y=225, width=200)
    # icon
    disp_image = tk.Button(
        welcome, image=display_icon, bd=0, command=forward_to_display_page
    )
    disp_image.place(x=60, y=200)
    # -----------------------------------------------
    # -----------------------------------------------
    back_button = tk.Button(welcome, text="←", fg=bg_colour, bd=0, command=backward_fn)
    back_button.place(x=5, y=40)
    # ------------------------------------------
    welcome.pack(pady=100)
    welcome.pack_propagate(False)
    welcome.configure(width=400, height=650)


# --------------------------------------------------------------------------------------
# Methods to assign priority for academic issues
def select_priority_academic(issue):
    # print(issue)
    return hash_table.get(issue)
    # return academic_problems[issue]
    # return "Low"


# ----------------------------------------------------------------------------------------------

filename = "Student.csv"
# Set to store the unique label of the tickects
used_ids = set()
ticket_label = {}
ticket_obj = {}
array = []
# object of queue_adapter store the ticket objects
q = QueueAdapter()
# Queue for the  Issue regarding Academic
academic_queue = QueueAdapter()
academic_queue_high = QueueAdapter()
academic_queue_medium = QueueAdapter()
academic_queue_low = QueueAdapter()
# Queue for the issue regarding Hostel
hostel_queue = QueueAdapter()
hostel_queue_high = QueueAdapter()
hostel_queue_medium = QueueAdapter()
hostel_queue_low = QueueAdapter()
# Linked_list
academic_agents = LinkedList()


# -----------------------------------------------------------------------
class Academic_Agent:
    def __init__(self, name, id, designation, dept, agent_category):
        self.name = name
        self.id = id
        self.designation = designation
        self.workload = 0
        self.agent_tickets = QueueAdapter()
        self.agent_tickets_high = QueueAdapter()
        self.agent_tickets_medium = QueueAdapter()
        self.agent_tickets_low = QueueAdapter()
        self.dept = dept
        self.agent_category = agent_category

    def display(self):
        print("\n")
        print(f"Name: {self.name}")
        print(f"id: {self.id}")
        print(f"Agent Category: {self.agent_category}")
        print(f"Department: {self.dept}")
        print(f"Designation: {self.designation}")
        print(f"WorkLoad: {self.workload}")


# --------------------------------------------------------
def find_least_workload_agent(head):
    if head is None:
        raise ValueError("The linked list is empty.")

    # Initialize with positive infinity
    min_agent = head.next.item
    minimum = head.next.item.workload

    current = head.next
    while current is not None:
        if current.item.workload <= minimum:
            minimum = current.item.workload
            min_agent = current.item
        current = current.next

    return min_agent


# ---------------------------------------------------------
def checker(csv_file2):
    size = count_csv_lines(csv_file2)
    return size


# --------------------------------------------------------
def delete_first_row_and_append(csv_file1, csv_file2):
    # Read the first CSV file and delete the first row
    with open(csv_file1, "r") as file1:
        csv_reader = csv.reader(file1)
        rows = list(csv_reader)
        deleted_row = rows.pop(1)  # Delete the first row
    is_new_file_empty = os.stat(csv_file2).st_size == 0
    # Append the deleted row to the second CSV file
    with open(csv_file2, "a", newline="") as file2:
        csv_writer = csv.writer(file2)
        if is_new_file_empty:  # Write header if the file is empty
            csv_writer.writerow(
                [
                    "ticket_id",
                    "username",
                    "regno",
                    "dept",
                    "year",
                    "gmail",
                    "priority_level",
                    "issue_regarding",
                    "Comment",
                ]
            )
        csv_writer.writerow(deleted_row)

    # Write the remaining rows (without the first row) back to the first CSV file
    with open(csv_file1, "w", newline="") as file1:
        csv_writer = csv.writer(file1)
        csv_writer.writerows(rows)


# -------------------------------------------------------------
# class to create the ticket
# ------------ Agent Object-----------------------------------------
def count_csv_lines(file_path):
    with open(file_path, "r") as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)

        # Count the number of lines in the CSV file
        line_count = sum(1 for row in csv_reader)

        return line_count


# -------------------------------------------------------------------
def move():
    delete_first_row_and_append("Student.csv", "Agent.csv")


# ----------------------------------------------------------------------------
def assign_to_agent():
    filename_new = "Agent.csv"
    with open(filename_new, "r") as file:
        reader = csv.DictReader(file)
        row_index = 1
        for i, row in enumerate(reader):
            if i == row_index:
                username = row["username"]
                regno = row["regno"]
                dept = row["dept"]
                year = row["year"]
                gmail = row["gmail"]
                issue_regarding = row["issue_regarding"]
                priority = row["priority_level"]
                ticket_id = row["ticket_id"]
                ticket = Ticket(
                    username,
                    regno,
                    dept,
                    year,
                    gmail,
                    priority,
                    issue_regarding,
                    ticket_id,
                )
                ticket_label[row["ticket_id"]] = ticket
                ticket_obj[ticket] = row["ticket_id"]
                break
    available_agent = find_least_workload_agent(academic_agents.head)
    print(ticket.priority)
    if ticket.priority == "High":
        available_agent.agent_tickets_high.enqueue(ticket)
        available_agent.agent_tickets.enqueue(ticket)
        ticket.status = "Assigned"
        available_agent.workload += 1
    elif ticket.priority == "Medium":
        available_agent.agent_tickets_medium.enqueue(ticket)
        ticket.status = "Assigned"
        available_agent.agent_tickets.enqueue(ticket)
        available_agent.workload += 1
    elif ticket.priority == "Low":
        available_agent.agent_tickets_medium.enqueue(ticket)
        ticket.status = "Assigned"
        available_agent.agent_tickets.enqueue(ticket)
        available_agent.workload += 1

    delete_first_row_and_append("Agent.csv", "Assigned.csv")
    return [available_agent, ticket]


# ----------------------------------------------------------------------------
def assigned_automatic():
    filename_new = "Assigned.csv"
    with open(filename_new, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            username = row["username"]
            regno = row["regno"]
            dept = row["dept"]
            year = row["year"]
            gmail = row["gmail"]
            issue_regarding = row["issue_regarding"]
            priority = row["priority_level"]
            ticket_id = row["ticket_id"]
            ticket = Ticket(
                username, regno, dept, year, gmail, priority, issue_regarding, ticket_id
            )
            ticket_label[row["ticket_id"]] = ticket
            ticket_obj[ticket] = row["ticket_id"]
            available_agent = find_least_workload_agent(academic_agents.head)
            if ticket.priority == "High":
                available_agent.agent_tickets_high.enqueue(ticket)
                available_agent.agent_tickets.enqueue(ticket)
                ticket.status = "Assigned"
                available_agent.workload += 1
            elif ticket.priority == "Medium":
                available_agent.agent_tickets_medium.enqueue(ticket)
                ticket.status = "Assigned"
                available_agent.agent_tickets.enqueue(ticket)
                available_agent.workload += 1
            elif ticket.priority == "Low":
                available_agent.agent_tickets_medium.enqueue(ticket)
                ticket.status = "Assigned"
                available_agent.agent_tickets.enqueue(ticket)
                available_agent.workload += 1
            ##available_agent.display()
            # ticket.display_ticket()


# -----------------------------------------------------------------------------------------------
class Ticket:
    def __init__(
        self, name, regno, dept, year, email, priority, issue_regarding, ticket_id
    ):
        self.name = name
        self.regno = regno
        self.dept = dept
        self.year = year
        self.email = email
        self.status = "Open"
        self.priority = priority
        self.issue_regarding = issue_regarding
        self.ticket_id = ticket_id

    # Method to display the ticket
    def display_ticket(self):
        print("\n")
        print(
            f"Name: {self.name}\nRegister no: {self.regno}\nDepartment: {self.dept}\nYear: {self.year}\nLabel:{ticket_obj[self]} "
        )
        print(f"Status:{self.status}")
        print(f"Priority:{self.priority}")
        print(f"Issue:{self.issue_regarding}")
        print(f"Ticket Created successfully!!")
        print("\n")


# Function to generate the unique label for the tickets
def generate_ticket_id(length=4):
    characters = string.ascii_letters + string.digits
    while True:
        ticket_id = "".join(random.choice(characters) for _ in range(length))
        if ticket_id not in used_ids:
            used_ids.add(ticket_id)
            return ticket_id


# To creat the ticket for the user
def create_ticket(
    username, regno, dept, year, gmail, priority_level, issue_regarding, comment
):
    global id
    id = generate_ticket_id()
    t = Ticket(username, regno, dept, year, gmail, priority_level, issue_regarding, id)
    t.ticket_id = id
    ticket_label[id] = t
    ticket_obj[t] = id
    data = {
        "ticket_id": id,
        "username": f"{username}",
        "regno": f"{regno}",
        "dept": f"{dept}",
        "year": f"{year}",
        "gmail": f"{gmail}",
        "priority_level": f"{priority_level}",
        "issue_regarding": f"{issue_regarding}",
        "Comment": f"{comment}",
    }
    file = open("Student.csv", "a", newline="")
    fieldnames = [
        "ticket_id",
        "username",
        "regno",
        "dept",
        "year",
        "gmail",
        "priority_level",
        "issue_regarding",
        "Comment",
    ]
    file_exists = os.path.isfile("Student.csv")
    writer = csv.DictWriter(file, fieldnames)
    if file_exists and os.stat("Student.csv").st_size == 0:
        writer.writeheader()
    writer.writerow(data)
    return t


# Method that read the ticket details from the csv file and create a ticket object and enqueue it into the stack
def read_tickets_from_csv(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            username = row["username"]
            regno = row["regno"]
            dept = row["dept"]
            year = row["year"]
            gmail = row["gmail"]
            issue_regarding = row["issue_regarding"]
            priority = row["priority_level"]
            ticket_id = row["ticket_id"]
            # print("###", ticket_id)
            ticket = Ticket(
                username, regno, dept, year, gmail, priority, issue_regarding, ticket_id
            )
            academic_queue.enqueue(ticket)
            q.enqueue(ticket)
            ticket_label[row["ticket_id"]] = ticket
            ticket_obj[ticket] = row["ticket_id"]
    return q


# To retreive the object once the label is called
def get_ticket_by_label(label):
    if label in ticket_label:
        return ticket_label[label]


# -------------------------------------------------------------------------------------
def finish():
    csv_file1 = "Assigned.csv"
    csv_file2 = "Recycle.csv"
    with open(csv_file1, "r") as file1:
        csv_reader = csv.reader(file1)
        rows = list(csv_reader)
        deleted_row = rows.pop(1)
        # Write the second row to the output file
        username = deleted_row[1]
        regno = deleted_row[2]
        dept = deleted_row[3]
        year = deleted_row[4]
        gmail = deleted_row[5]
        issue_regarding = deleted_row[7]
        priority = deleted_row[6]
        ticket_id = deleted_row[0]
        ticket = Ticket(
            username, regno, dept, year, gmail, priority, issue_regarding, ticket_id
        )
        ticket.status = "Completed"
        ticket_label[deleted_row[0]] = ticket
        ticket_obj[ticket] = deleted_row[0]
    is_new_file_empty = os.stat(csv_file2).st_size == 0
    # Append the deleted row to the second CSV file
    with open(csv_file2, "a", newline="") as file2:
        csv_writer = csv.writer(file2)
        if is_new_file_empty:  # Write header if the file is empty
            csv_writer.writerow(
                [
                    "ticket_id",
                    "username",
                    "regno",
                    "dept",
                    "year",
                    "gmail",
                    "priority_level",
                    "issue_regarding",
                    "Comment",
                ]
            )
        csv_writer.writerow(deleted_row)
    with open(csv_file1, "w", newline="") as file1:
        csv_writer = csv.writer(file1)
        csv_writer.writerows(rows)

    return ticket


# --------------------------------------------------------------------------


# Methods to assign priority for academic issues


if __name__ == "__main__":
    read_tickets_from_csv("Student.csv")
    welcome_page_fn()
    a1 = Academic_Agent(
        "Sundararajan",
        "A1",
        "Assistant Professor",
        "Information Technology",
        "Academic",
    )
    a2 = Academic_Agent(
        "Saravanan", "A2", "Asssistant Professor", "Information Technology", "Academic"
    )
    a3 = Academic_Agent(
        "Dilli Babu", "A3", "Assistant Professor ", "Information Technology", "Academic"
    )
    a4 = Academic_Agent(
        "Manish", "A4", "Assistant Professor", "Information Technology", "Academic"
    )
    a5 = Academic_Agent(
        "Vijayasekar",
        "A5",
        "Associative Professor",
        "Information Technology",
        "Academic",
    )
    a6 = Academic_Agent(
        "Sripriya", "A6", "Associative  Professor", "Information Technology", "Academic"
    )
    a7 = Academic_Agent(
        "C Aravind", "A7", "Head of Department", "Information Technology", "Academic"
    )
    lst = [a1, a2, a3, a4]
    for i in lst:
        academic_agents.append(i)
    assigned_automatic()
    panel.mainloop()
