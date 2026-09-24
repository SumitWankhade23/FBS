from empmange import EmpMange
class Main:
    @staticmethod
    def login():
        eid = input("Enter user id: ")
        epass = input("Enter pssword: ")
        if eid == "admin" and epass == "1234":
            print("Log in is done")
            return True
        else:
            print("Invalid credencials")

    def menu(self):
        em = EmpMange()
        while True:
            print("""
                1. Add Employee
                2. Display Employee
                3. Search Emplyee  
                4. Update Employee
                5. Delete Employee
                6. Exit """) 
            choice = int(input("Enter choice: "))
            if choice == 1:
                em.addEmp()
            elif choice == 2:
                em.displayEmp()    
            elif choice == 3:
                em.searchEmp()
            elif choice == 4:
                em.updateEmp()
            elif choice == 5:
                em.deleteEmp()
            elif choice == 6:
                print("Thank you visit again")
                break
            else:
                print("Invalid choice")


result = Main.login()
if result:
    m = Main()
    m.menu()               