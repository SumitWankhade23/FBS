from hr import Hr
from dev import Dev
class EmpMange:
    #Static object Empdetail={}
    Empdeatil = {} #It should be independant because it has only one copy It is for all HR,Dev,emp
    def addEmp(self):
        eid = input("Enter Emp Id = ")
        if eid in EmpMange.Empdeatil:
            print("Employee alredy exist")
            return
        else:
            ename = input("Enter the Emp Name = ")
            esal = float(input("Enter salary = "))
            print("1.Hr")
            print("2.Devloper")
            ch = int(input("Enter the choice: "))
            if ch == 1:
                ecom = float(input("Enter the commition of Hr: "))
                emp = Hr(eid,ename,esal,ecom)
            elif ch == 2:
                ebonus = float(input("Enter the bonus of dev: "))
                emp = Dev(eid,ename,esal,ebonus)
            else:
                print("Invalid choice") 
                return 

            EmpMange.Empdeatil[eid] = emp
            print("Emp added successfully")  
                

    def displayEmp(self):
        if len(EmpMange.Empdeatil) == 0:
            print("Emp is not exist")
        else:
            for var in EmpMange.Empdeatil.values():
                print(var) 

    def searchEmp(self):
        eid = input("Enter the id of employee to be secrched: ")
        if eid in EmpMange.Empdeatil:
            print(EmpMange.Empdeatil[eid])
            return
        else:
            print("Employee is not exist")    
    def updateEmp(self):
        eid = input("Enter the id of employee to be update: ")
        if eid not in EmpMange.Empdeatil:
            print("Employee id is not exist")
        else:
            emp = EmpMange.Empdeatil[eid]
            print("1.Update Dev")
            print("2.Update HR")
            ch = int(input("Enter the choice: "))
            if ch == 1 and isinstance(emp,Dev):
                newname = input("Enter new name of Dev: ")
                emp.setName(newname)
            elif ch == 2 and isinstance(emp,Hr):
                newname = input("Enter new name of HR: ")
                emp.setName(newname)
            else:
                print("Invalid input")    

            
    def deleteEmp(self):
        eid = input("Enter the id of employee: ")
        if eid in EmpMange.Empdeatil:
            del EmpMange.Empdeatil[eid]
            print("Employee deleted successfuly..")
        else:
            print("Employe is not available")    
        
                    
