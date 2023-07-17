from queue_data_struct import QueueAdapter
from dynamic_array import  listADT
from LinkedList import *
import random
import string
import csv
import os.path 
import os
#-------------------------------------------------------------------------------
filename = "Student.csv"
#Set to store the unique label of the tickects
used_ids = set()
ticket_label = {}
ticket_obj = {}
#-------------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------------------
#class to create the ticket
class Ticket:
    def __init__(self, name, regno, dept, year, email, priority , issue_regarding, ticket_id):
        self.name = name
        self.regno = regno
        self.dept = dept
        self.year = year
        self.email = email
        self.status = "Open"
        self.priority = priority
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
#----------------------------------------------------------------------------------------------
#Function to generate the unique label for the tickets
def generate_ticket_id(length=4):
    characters = string.ascii_letters + string.digits 
    while True:
        ticket_id = ''.join(random.choice(characters) for _ in range(length))
        if ticket_id not in used_ids:
            used_ids.add(ticket_id)
            return ticket_id
#----------------------------------------------------------------------------------------

#To creat the ticket for the user
def create_ticket(category, username, regno, dept, year, gmail , priority_level, issue_regarding, comment):
    
    global id
    id = generate_ticket_id()
    t = Ticket( category, username, regno, dept, year, gmail, priority_level, issue_regarding, id )
    t.ticket_id = id
    ticket_label[id] = t
    ticket_obj[t] = id
    data = {"ticket_id": id, "Category":f"{category}","username":f"{username}", "regno":f"{regno}", "dept":f"{dept}","year":f"{year}", 
            "gmail":f"{gmail}", "priority_level": f"{priority_level}", "issue_regarding":f"{issue_regarding}", "Comment":f"{comment}"}
    file = open("Student.csv", "a", newline="")
    fieldnames= ["ticket_id","Category", "username", "regno", "dept","year", "gmail", "priority_level", "issue_regarding", "Comment" ]
    file_exists = os.path.isfile("Student.csv")
    writer = csv.DictWriter(file, fieldnames)
    if file_exists and os.stat("Student.csv").st_size == 0:
            writer.writeheader()
    writer.writerow(data)

    return t
#-------------------------------------------------------------------------------------------------
#Method that read the ticket details from the csv file and create a ticket object and enqueue it into the stack
def read_tickets_from_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            
            username = row['username']
            regno = row['regno']
            dept = row['dept']
            year = row['year']
            gmail = row['gmail']
            issue_regarding = row["issue_regarding"]
            priority = row["priority_level"]
            ticket_id = row["ticket_id"]
            ticket = Ticket( username, regno, dept, year, gmail,priority, issue_regarding , ticket_id)
             
            academic_queue.enqueue(ticket)
            
            q.enqueue(ticket)
            ticket_label[row['ticket_id']] = ticket
            ticket_obj[ticket] = row['ticket_id']
    
        
    return q
#---------------------------------------------------------------------------------------------------
#To retreive the object once the label is called 
def get_ticket_by_label(label):
    if label in ticket_label:
        return ticket_label[label]
    return None


#********************************Priority Module **********************************
    
academic_problems = {
'Assignment submission': 'High',
'Exam-related questions': 'Medium',
'Scholarship applications and queries': 'High',
'Grading inquiries': 'Medium',
'Doubts related to the subjects': 'High',
'Lab-related queries': 'Low'
        }


hostel_issues = {
'Room allocation and roommate conflicts': 'high',
'Maintenance and repairs': 'medium',
'Cleanliness and hygiene': 'medium',
'Safety and security': 'high',
'Food-related issues': 'medium',
'Outpass issues': 'low'
            }

#Methods to assign priority for academic issues
def select_priority_academic(selected_serial_number, issue_about):
    if issue_about == "academic":
        if selected_serial_number == 1:
            priority = academic_problems["Assignment submission"]
            return priority, "Assignment submission"
        elif selected_serial_number == 2:
            priority = academic_problems["Exam-related questions"]
            return priority, "Exam-related questions"
        elif selected_serial_number == 3:
            priority = academic_problems["Scholarship applications and queries"]
            return priority, "Scholarship applications and queries"
        elif selected_serial_number == 4:
            priority = academic_problems["Grading inquiries"]
            return priority, "Grading inquiries"
        elif selected_serial_number == 5:
            priority = academic_problems["Doubts related to the subjects"]
            return priority, "Doubts related to the subjects"
        elif selected_serial_number == 6:
            priority = academic_problems["Lab-related queries"]
            return priority, "Lab-related queries"
        else:
            print("Invalid serial number")
            return None, None
#Methods to assign priority to the hostel issues     
def select_priority_hostel(selected_serial_number, issue_about):
    if issue_about == "hostel":
        if selected_serial_number == 1:
            priority = hostel_issues["Room allocation and roommate conflicts"]
            return [priority, "Room allocation and roommate conflicts"]
        elif selected_serial_number == 2:
            priority = hostel_issues["Maintenance and repairs"]
            return priority, "Maintenance and repairs"
        elif selected_serial_number == 3:
            priority = hostel_issues["Cleanliness and hygiene"]
            return priority, "Cleanliness and hygiene"
        elif selected_serial_number == 4:
            priority = hostel_issues["Safety and security"]
            return priority, "Safety and security"
        elif selected_serial_number == 5:
            priority = hostel_issues["Food-related issues"]
            return priority, "Food-related issues"
        elif selected_serial_number == 6:
            priority = hostel_issues["Outpass issues"]
            return priority, "Outpass issues"
        else:
            print("Invalid serial number")
            return None, None
        
def academic_tickets_prioritization(academic_tickets):
    for ticket in academic_tickets:
        if (ticket.priority).lower() == "high":
            academic_queue_high.enqueue(ticket)
        elif (ticket.priority).lower() == "medium":
            academic_queue_medium.enqueue(ticket)
        elif (ticket.priority).lower() == "low":
            academic_queue_low.enqueue(ticket)

def hostel_tickets_prioritization(hostel_tickets):
    for ticket in hostel_tickets:
        if (ticket.priority).lower() == "high":
            hostel_queue_high.enqueue(ticket)
        elif (ticket.priority).lower() == "medium":
            hostel_queue_medium.enqueue(ticket)
        elif (ticket.priority).lower() == "low":
            hostel_queue_low.enqueue(ticket)
#----------------------------- over ----------------------------------------------

#*************Agent Creation  Module********************************
academic_agents = LinkedList()
hostel_agents = LinkedList()
class Academic_Agent:
    def __init__(self, name, id, designation, dept, agent_category ):
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
'''
class Hostel_Agent:
    def __init__(self, name, id, designation):
        self.name = name
        self.id = id 
        self.designation = designation
        self.agents_tickets = QueueAdapter()
        self.agent_tickets_high = QueueAdapter()
        self.agent_tickets_medium = QueueAdapter()
        self.agent_tickets_low = QueueAdapter()
        self.workload = 0
    def display(self):
        print("\n")
        print(f"Name: {self.name}") 
        print(f"id: {self.id}")
        print(f"Designation: {self.designation}")
        print(f"Workload: {self.workload}" ) '''

def find_least_workload_agent(head):
    if head is None:
        raise ValueError("The linked list is empty.")
    
     # Initialize with positive infinity
    min_agent = head.next.item
    minimum = head.next.item.workload

    current = head.next
    while current is not None:
        if current.item.workload <=minimum:
            minimum = current.item.workload
            min_agent = current.item
        current = current.next

    return min_agent


def academic_ticket_assignment( academic_queue_high, 
                               academic_queue_medium, academic_queue_low, option = None):
    print("Hello academic")
    available_agent = find_least_workload_agent(academic_agents.head)
    if len(academic_queue) != 0:
        if len(academic_queue_high) != 0:
            ticket = academic_queue_high.dequeue()
            available_agent.agent_tickets_high.enqueue(ticket)
            ticket.status = "Assigned"
            available_agent.workload += 1
        elif len(academic_queue_medium) != 0:
            ticket = academic_queue_medium.dequeue()
            available_agent.agent_tickets_medium.enqueue(ticket)
            ticket.status = "Assigned"
            available_agent.workload += 1
        elif len(academic_queue_low) != 0:
            ticket = academic_queue_low.dequeue()
            available_agent.agent_tickets_low.enqueue(ticket)
            ticket.status = "Assigned"
            available_agent.workload += 1
        t = academic_queue.dequeue()
        print(t.ticket_id)
    else:
        print("No More Tickets To Add")
        return None
'''
def hostel_ticket_assignment( hostel_queue_high, hostel_queue_medium, hostel_queue_low, option = None):
    print("Hello hostel")
    available_agent = find_least_workload_agent(hostel_agents.head)
    if len(hostel_queue) != 0:
        if len(hostel_queue_high) != 0:
            ticket = hostel_queue_high.dequeue()
            available_agent.agent_tickets_high.enqueue(ticket)
            ticket.status = "Assigned"
            available_agent.workload += 1
        elif len(hostel_queue_medium) != 0:
            ticket = hostel_queue_medium.dequeue()
            available_agent.agent_tickets_medium.enqueue(ticket)
            ticket.status = "Assigned"
            available_agent.workload += 1
        elif len(hostel_queue_low) != 0:
            ticket = hostel_queue_low.dequeue()
            available_agent.agent_tickets_low.enqueue(ticket)
            ticket.status = "Assigned"
            available_agent.workload += 1
        ticket = hostel_queue.dequeue()
        if option == None:
          delete_row_by_ticket_id(ticket.ticket_id)
        return available_agent
    else:
        print("No More Tickets To Add")
        return None '''







#------------------------------ care-------------------------------
def delete_row_by_ticket_id( ticket_id):
    # Step 1: Open the source CSV file and create an empty list
    source_file = "Student.csv"
    with open(source_file,'r') as file:
        rows = list(csv.reader(file))
    
    deleted_row = None  # Store the deleted row
    
    # Step 2: Remove the row based on the ticket ID and write it to a new list
    new_rows = []
    for row in rows:
        if row[0] == ticket_id:  # Assuming ticket ID is in the first column
            deleted_row = row
        else:
            new_rows.append(row)
    
    # Step 5: Open the source CSV file in write mode
    with open(source_file, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Step 6: Write the remaining rows back to the source CSV file
        writer.writerows(new_rows)
    
    # Step 8: Check if the new CSV file is empty
    destination_file = "Agent.csv"
    is_new_file_empty = (os.stat(destination_file).st_size == 0)
    
    # Step 9: Open the new CSV file in append mode
    with open(destination_file, 'a', newline='') as dest_file:
        writer = csv.writer(dest_file)
        
        # Step 10: Write the deleted row to the new CSV file
        if is_new_file_empty:  # Write header if the file is empty
            writer.writerow(["ticket_id", "username", "regno", "dept","year", "gmail", "priority_level", "issue_regarding", "Comment" ])  # Replace with your header
        writer.writerow(deleted_row)


#----------------------------------------------------------------------------------------



def delete_first_row_and_append(csv_file1, csv_file2 ):
    # Read the first CSV file and delete the first row
    with open(csv_file1, 'r') as file1:
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
        ticket = Ticket( username, regno, dept, year, gmail,priority, issue_regarding , ticket_id)
        ticket_label[deleted_row['ticket_id']] = ticket
        ticket_obj[ticket] = deleted_row['ticket_id']
    is_new_file_empty = (os.stat(csv_file2).st_size == 0)
    # Append the deleted row to the second CSV file
    with open(csv_file2, 'a', newline='') as file2:
        csv_writer = csv.writer(file2)
        if is_new_file_empty:  # Write header if the file is empty
            csv_writer.writerow(["ticket_id", "username", "regno", "dept","year", "gmail", "priority_level", "issue_regarding", "Comment" ])
        csv_writer.writerow(deleted_row)
        

    # Write the remaining rows (without the first row) back to the first CSV file
    with open(csv_file1, 'w', newline='') as file1:
        csv_writer = csv.writer(file1)
        csv_writer.writerows(rows)




#-----------------------------------------------------------------------------------------------


def asign():
    while True:
        
        assign = input("Do you want to assign the ticket the agent Yes or No : ").lower()   
        if assign == "yes":
            choice = input("Academic or Hostel: ").lower()
            if choice == "academic":
               a =  academic_ticket_assignment( academic_queue_high, academic_queue_medium, academic_queue_low)
            
    
        else:
            
            break 
def auto_assign():
    
    #Information Technology Staffs
    a1 = Academic_Agent("Sundararajan", "A1", "Assistant Professor","Information Technology", "Academic")
    a2 = Academic_Agent("Saravanan", "A2", "Asssistant Professor", "Information Technology" ,"Academic")
    a3 = Academic_Agent("Dilli Babu","A3", "Assistant Professor ", "Information Technology", "Academic")
    a4 = Academic_Agent("Manish", "A4", "Assistant Professor", "Information Technology", "Academic")
    a5 = Academic_Agent("Vijayasekar", "A5", "Associative Professor","Information Technology","Academic"  )
    a6 = Academic_Agent("Sripriya", "A6", "Associative  Professor", "Information Technology", "Academic")
    a7 =Academic_Agent("C Aravind", "A7", "Head of Department", "Information Technology", "Academic")
    lst = [a1, a2, a3, a4]
    for i in lst:
        academic_agents.append(i)
    #for agent in academic_agents:
        #agent.display()
    #Non_faculty agents

   
    #Agent.csv file    
    

    with open("Agent.csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["Category"]
            if category == "academic":
               academic_ticket_assignment( academic_queue_high, academic_queue_medium, academic_queue_low, 1)
            
'''         
    current = academic_agents.head.next
    while current:
        current.item.display()
        current = current.next'''
#------------------------------------------------------------------------
def count_csv_lines(file_path):
    with open(file_path, 'r') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)
        
        # Count the number of lines in the CSV file
        line_count = sum(1 for row in csv_reader)
        
        return line_count
#----------------------------------------------------------
def move():
    count = count_csv_lines("Student.csv")
    while count > 1:
        op = input("Do you want to move the ticket yes / no: ").lower()
        if op == "yes":
            delete_first_row_and_append("Student.csv","Agent.csv" )
        else:
            break

def assign_to_agent():

    filename_new = "Agent.csv"
    with open(filename_new, 'r') as file:
        reader = csv.DictReader(file)
        row_index = 1
        for i, row in enumerate(reader):
            if i == row_index:
                
                username = row['username']
                regno = row['regno']
                dept = row['dept']
                year = row['year']
                gmail = row['gmail']
                issue_regarding = row["issue_regarding"]
                priority = row["priority_level"]
                ticket_id = row["ticket_id"]
                ticket = Ticket( username, regno, dept, year, gmail,priority, issue_regarding , ticket_id)
                ticket_label[row['ticket_id']] = ticket
                ticket_obj[ticket] = row['ticket_id']
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
    available_agent.display()  
    ticket.display_ticket()  
    delete_first_row_and_append("Agent.csv", "Assigned.csv" )







def finish(): 
    csv_file1 = "Assigned.csv"
    csv_file2 = "Recycle.csv"
    with open(csv_file1, 'r') as file1:
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
        ticket = Ticket( username, regno, dept, year, gmail,priority, issue_regarding , ticket_id)
        ticket.status = "Completed" 
        ticket_label[deleted_row[0]] = ticket
        ticket_obj[ticket] = deleted_row[0]
    is_new_file_empty = (os.stat(csv_file2).st_size == 0)
    # Append the deleted row to the second CSV file
    with open(csv_file2, 'a', newline='') as file2:
        csv_writer = csv.writer(file2)
        if is_new_file_empty:  # Write header if the file is empty
            csv_writer.writerow(["ticket_id", "username", "regno", "dept","year", "gmail", "priority_level", "issue_regarding", "Comment" ])
        csv_writer.writerow(deleted_row)
    with open(csv_file1, 'w', newline='') as file1:
        csv_writer = csv.writer(file1)
        csv_writer.writerows(rows)

    return ticket








#**********************main **************************
if __name__ == "__main__":
     

    
    print("Welcome to the Helpdesk Management System")
    read_tickets_from_csv(filename)
    academic_tickets_prioritization(academic_queue)
    hostel_tickets_prioritization(hostel_queue)
    #auto_assign()
   

    a1 = Academic_Agent("Sundararajan", "A1", "Assistant Professor","Information Technology", "Academic")
    a2 = Academic_Agent("Saravanan", "A2", "Asssistant Professor", "Information Technology" ,"Academic")
    a3 = Academic_Agent("Dilli Babu","A3", "Assistant Professor ", "Information Technology", "Academic")
    a4 = Academic_Agent("Manish", "A4", "Assistant Professor", "Information Technology", "Academic")
    a5 = Academic_Agent("Vijayasekar", "A5", "Associative Professor","Information Technology","Academic"  )
    a6 = Academic_Agent("Sripriya", "A6", "Associative  Professor", "Information Technology", "Academic")
    a7 =Academic_Agent("C Aravind", "A7", "Head of Department", "Information Technology", "Academic")
    lst = [a1, a2, a3, a4]
    for i in lst:
       academic_agents.append(i)
    def assigned_automatic():
        filename_new = "Assigned.csv"
        with open(filename_new, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                    username = row['username']
                    regno = row['regno']
                    dept = row['dept']
                    year = row['year']
                    gmail = row['gmail']
                    issue_regarding = row["issue_regarding"]
                    priority = row["priority_level"]
                    ticket_id = row["ticket_id"]
                    ticket = Ticket( username, regno, dept, year, gmail,priority, issue_regarding , ticket_id)
                    ticket_label[row['ticket_id']] = ticket
                    ticket_obj[ticket] = row['ticket_id']
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
                    available_agent.display()
                    ticket.display_ticket()
    assigned_automatic()
    
    while True:
        op = input("Do you want to close the ticket : ").lower()
        if op == "yes":
           t =  finish()
           t.display_ticket()
        else:
            break
    
    move()
    
    '''
    print("1) Create aTicket")
    print("2)Dispaly the Ticket Details")
    choice = int(input("Select :"))
    if choice == 1:
        flag = True
        username = input("Enter username: ")
        regno = input("Enter registration number: ")
        dept = input("Enter department: ")
        year = input("Enter year: ")
        gmail = input("Enter Gmail: ")
        ticket_is_for = input("Ticket is regrading Academic or Hostel: ").lower()
        if ticket_is_for == "academic":
            i = 1
            for issue in academic_problems:
                print(f"{i} {issue}")
                i += 1
            select_issue = int(input("Select the issue: "))
            comment = input("You can briefly Explain Your problem here: ")
            priority_list = select_priority_academic(select_issue, ticket_is_for )
            print(priority_list)


        elif ticket_is_for == "hostel":
            i = 1
            for issue in hostel_issues:
                print(f"{i} {issue}")
                i += 1
            select_issue = int(input("Select the issue: "))
            comment = input("You can briefly Explain Your problem here: ")
            priority_list = select_priority_hostel(select_issue, ticket_is_for)
            print(priority_list)
            
        else:
            flag = False         
            print("Inavalid selection")

        if flag:
            issue_regarding = priority_list[1]
            t = create_ticket( ticket_is_for, username, regno, dept, year, gmail, priority_list[0],issue_regarding , comment)
            read_tickets_from_csv(filename)
            academic_tickets_prioritization(academic_queue)
            hostel_tickets_prioritization(hostel_queue)
            t.display_ticket()
    
    elif choice == 2:
        label = input("Enter ticket label to access user information: ")
        ticket = get_ticket_by_label(label)
        if ticket:
            ticket.display_ticket()
        else:
            print("Invalid ticket label.") 
    else:
        print("Invalid Selection")  '''
    

    #*************************************************************
    '''
    for i in range(len(academic_queue_high)):
        academic_queue_high[i].display_ticket()
    for i in range(len(academic_queue_medium)):
        academic_queue_medium[i].display_ticket()
    for i in range(len(academic_queue_low)):
        academic_queue_low[i].display_ticket()
    print("**********************************************************")
    for i in range(len(hostel_queue_high)):
        hostel_queue_high[i].display_ticket()
    for i in range(len(hostel_queue_medium)):
        hostel_queue_medium[i].display_ticket()
    for i in range(len(hostel_queue_low)):
        hostel_queue_low[i].display_ticket() '''
    #print(academic_queue)
    #
    #-----------------------------------------------------------------
    '''
    #Information Technology Staffs
    a1 = Academic_Agent("Sundararajan", "A1", "Assistant Professor","Information Technology", "Academic")
    a2 = Academic_Agent("Saravanan", "A2", "Asssistant Professor", "Information Technology" ,"Academic")
    a3 = Academic_Agent("Dilli Babu","A3", "Assistant Professor ", "Information Technology", "Academic")
    a4 = Academic_Agent("Manish", "A4", "Assistant Professor", "Information Technology", "Academic")
    a5 = Academic_Agent("Vijayasekar", "A5", "Associative Professor","Information Technology","Academic"  )
    a6 = Academic_Agent("Sripriya", "A6", "Associative  Professor", "Information Technology", "Academic")
    a7 =Academic_Agent("C Aravind", "A7", "Head of Department", "Information Technology", "Academic")
    lst = [a1, a2, a3, a4]
    for i in lst:
        academic_agents.append(i) '''
#--------------------------------------------------------------------------------
    #for agent in academic_agents:
        #agent.display()
    #Non_faculty agents

   
    #------------------------------------------------------------------------------
    #assign
    

    #for i in academic_queue:
       # i.display()

    
    











    
    
    

    
      




    


    


