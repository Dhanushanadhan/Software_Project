global name
    global age
    global phone_number
    global ID_No
    global Year
    global department
    global email
    global password

    name=stu_name_ent.get()
    age=stu_age_ent.get()
    phone_number=stu_phone_no_ent.get()
    ID_No=stu_id.get()
    Year=Select_year_button.get()
    department=Select_department_button.get()
    email=student_email_ent.get()
    password=student_Password_ent.get()

hostel_list=['a','b','c','d','e']
academic_list=['a','b','c','d','e','f']
def create():
    creation1_page=tk.Frame(panel,highlightbackground=bg_colour,highlightthickness=3)
    heading_label=tk.Label(creation1_page,text="Choose",font=("bold", 15),bg=bg_colour,fg="white")
    heading_label.place(x=0,y=0,width=400)
    #---------------------------------------------------------------------------------------------
    Select_academic_button=Combobox(creation1_page, font=("bold", 15),state="readonly",values=academic_list)
    Select_academic_button.place(x=240,y=250,width=180,height=30)
    #---------------------------------------------------------------------------------
    Select_hostel_button=Combobox(creation1_page, font=("bold", 15),state="readonly",values=hostel_list)
    Select_hostel_button.place(x=240,y=250,width=180,height=30)
    #----------------------------------------------------------------------------
    global academic_choosen
    academic_choosen=Select_academic_button.get()
    #---------------------------------------------------------------------------------
    global hostel_choosen
    hostel_choosen=Select_hostel_button.get()
    #------------------------------------------------------------------------------------
    creation1_page.pack(pady=5)
    creation1_page.pack_propagate(False)
    creation1_page.configure(width=550,height=580)

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


def ticket_generation_page_fn():
    def forward_to_creation_page():
        creation_page.destroy()
        panel.update()
        create()
    def forward_to_display_page():
        creation_page.destroy()
        panel.update()
        display()

    creation_page=tk.Frame(panel,highlightbackground=bg_colour,highlightthickness=3)
    heading_label=tk.Label(creation_page,text="Choose",font=("bold", 15),bg=bg_colour,fg="white")
    heading_label.place(x=0,y=0,width=400)
    #----------------------------------------------------------------------
    create_button = tk.Button(creation_page, text="Create", font=("bold", 14),bg=bg_colour, fg="white",command=forward_to_creation_page)
    create_button.place(x=250,y=260,width=80,height=40)
    #-----------------------------------------------------------------------
    Display_button = tk.Button(creation_page, text="Display", font=("bold", 14),bg=bg_colour, fg="white",command=forward_to_display_page)
    Display_button.place(x=250,y=560,width=200,height=40)
    #-------------------------------------------------------------------------
    creation_page.pack(pady=5)
    creation_page.pack_propagate(False)
    creation_page.configure(width=550,height=580)

global name
    global age
    global phone_number
    global ID_No
    global Year
    global department
    global email
    global password

    name=stu_name_ent.get()
    age=stu_age_ent.get()
    phone_number=stu_phone_no_ent.get()
    ID_No=stu_id.get()
    Year=Select_year_button.get()
    department=Select_department_button.get()
    email=student_email_ent.get()
    password=student_Password_ent.get()

hostel_list=['a','b','c','d','e']
academic_list=['a','b','c','d','e','f']
def create():
    creation1_page=tk.Frame(panel,highlightbackground=bg_colour,highlightthickness=3)
    heading_label=tk.Label(creation1_page,text="Choose",font=("bold", 15),bg=bg_colour,fg="white")
    heading_label.place(x=0,y=0,width=400)
    #---------------------------------------------------------------------------------------------
    Select_academic_button=Combobox(creation1_page, font=("bold", 15),state="readonly",values=academic_list)
    Select_academic_button.place(x=240,y=250,width=180,height=30)
    #---------------------------------------------------------------------------------
    Select_hostel_button=Combobox(creation1_page, font=("bold", 15),state="readonly",values=hostel_list)
    Select_hostel_button.place(x=240,y=250,width=180,height=30)
    #----------------------------------------------------------------------------
    global academic_choosen
    academic_choosen=Select_academic_button.get()
    #---------------------------------------------------------------------------------
    global hostel_choosen
    hostel_choosen=Select_hostel_button.get()
    #------------------------------------------------------------------------------------
    creation1_page.pack(pady=5)
    creation1_page.pack_propagate(False)
    creation1_page.configure(width=550,height=580)

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


def ticket_generation_page_fn():
    def forward_to_creation_page():
        creation_page.destroy()
        panel.update()
        create()
    def forward_to_display_page():
        creation_page.destroy()
        panel.update()
        display()

    creation_page=tk.Frame(panel,highlightbackground=bg_colour,highlightthickness=3)
    heading_label=tk.Label(creation_page,text="Choose",font=("bold", 15),bg=bg_colour,fg="white")
    heading_label.place(x=0,y=0,width=400)
    #----------------------------------------------------------------------
    create_button = tk.Button(creation_page, text="Create", font=("bold", 14),bg=bg_colour, fg="white",command=forward_to_creation_page)
    create_button.place(x=250,y=260,width=80,height=40)
    #-----------------------------------------------------------------------
    Display_button = tk.Button(creation_page, text="Display", font=("bold", 14),bg=bg_colour, fg="white",command=forward_to_display_page)
    Display_button.place(x=250,y=560,width=200,height=40)
    #-------------------------------------------------------------------------
    creation_page.pack(pady=5)
    creation_page.pack_propagate(False)
    creation_page.configure(width=550,height=580)
welcome_page_fn
add_account_fn()
panel.mainloop()



