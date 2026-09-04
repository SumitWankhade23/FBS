from prettytable import PrettyTable 

emp_details = {}

def addEmp():

    id = int(input("Enter ID: "))
    nm = input("Enter name: ")
    dept = input("Enter department: ")
    sal = float(input("Enter salary: "))

    if(id not in emp_details):
        emp_details[id] = [id, nm, dept, sal]
        return 'Employee added successfully '
    else:
        return "Employee ID already available"

def showMenu():
    table = PrettyTable()

    table.field_names = ["Option", "Operation"]

    table.add_row(["1", "Add Employee"])
    table.add_row(["2", "Update Employee"])
    table.add_row(["3", "Delete Employee"])
    table.add_row(["4", "Search Employee"])
    table.add_row(["5", "Show All Employees"])
    table.add_row(["6", "Logout"])

    print(table)

def showAllEmp():
    if len(emp_details) == 0:
        print("No employee record found")
        return
    table = PrettyTable()

    table.field_names = ["ID","Name","Department","Salary"]
    for id in emp_details:
        employee = emp_details[id]

        table.add_row([
            employee[0],
            employee[1],
            employee[2],
            employee[3]
        ])
    print(table)    

def update():
    id = int(input("Enter employee ID to update: "))
    if id in emp_details:
        print("Emplyee is available in database")
        print(emp_details[id])

        nm = input("Enter name: ")
        dept = input("Enter department: ")
        sal = float(input("Enter salary: "))

        emp_details[id] =[id,nm,dept,sal]

        print("Employee updated success")
    else:
        print("Emplyoee is not available")    
        
def delEmp():
    id = int(input("Enter ID to delete: "))
    if id in emp_details:
        print("Employee is present in database",emp_details[id])

        choice = input("Are you really want to delete emplyee detail? (yes/no): ")

        if choice.lower() == "yes":
            del emp_details[id]
            print("Employee detail deleted successfully")
        else:
            print("Delete operation cancel")
    else:
        print("Employee ID is not found")    



def searchEmp():
    id = int(input("Enter ID to be search: "))
    if id in emp_details:
        
        print(f"{id} Employee is prenst")
       
    else:
        print(f"{id} is not found")    

def empMange():
    ch = "0"
    while( ch != '6'):
        print('----EMPlOYEE MANAGMENT----')
        print('''Please select option from below:
        1. Add emp
        2. Upd emp
        3. Del emp
        4. Search emp
        5. Show emp
        6. Logout
        ''')
        ch = input('Enter choice: ')
        if(ch == '1'):
            result = addEmp()
            print(result)
        elif(ch == '2'):
            update()
        elif(ch == '3'):
            delEmp()
        elif(ch == '4'):
            searchEmp()
        elif(ch == '5'):
            showAllEmp()
        elif(ch == '6'):
            print("#Logged out#")
        else:
            print("Enter valid choice")                        
        
#Login function   
def login():
    print('\n####LOGIN PAGE####')
    uid = 'admin'
    passw = '1234'
    username = input('Enter USERNAME:')
    password = input('Enter PASSWORD: ')
    if(uid == username and passw == password):
        empMange()
    else:
        print('Invalid credincial..')

#Main menu
ch = '0'
while(ch != '2'):
    print("""Please select option from below
    1. Login
    2. Exit
            """)
    ch = input("Enter choice: ")
    if(ch == '1'):
        login()
    elif(ch == '2'):
        print("Thank you for choosing us")
    else:
        print("Invalid choice")
