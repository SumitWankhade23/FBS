# Python Assignment – (Pickling and Unpickling)
# 1. Create a class Emp (eid,ename,basic)
# 2. WAP a menu driven program to perform following operations using
# files :

# a. Add a record
# b. Search for a record using id
# c. Delete a record using id
# d. Edit a record using id.
# e. Display all records.
import pickle
class Emp:
    def __init__(self, eid=0, ename="Unknown", basic=0.0):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def display(self):
        print(f"ID: {self.eid:<6} Name: {self.ename:<15} Basic: {self.basic}")

    def __str__(self):
        return f"Emp[ID={self.eid}, Name={self.ename}, Basic={self.basic}]"


def load_all():
    records = []
    try:
        with open("emp.dat", "rb") as f:
            while True:
                try:
                    records.append(pickle.load(f))      
                except EOFError:                        
                    break
    except FileNotFoundError:
        pass                                            
    return records


def save_all(records):
    with open("emp.dat", "wb") as f:
        for emp in records:
            pickle.dump(emp, f)                      


def read_id(message="Enter employee id: "):
    try:
        return int(input(message))
    except ValueError:
        print("Invalid id. Please enter a whole number.")
        return None



def add_record():
    eid = read_id()
    if eid is None:
        return
    if any(e.eid == eid for e in load_all()):
        print("An employee with this id already exists.")
        return
    try:
        ename = input("Enter name: ").strip()
        basic = float(input("Enter basic salary: "))
    except ValueError:
        print("Invalid salary. Please enter a number.")
        return
    with open("emp.dat", "ab") as f:                    
        pickle.dump(Emp(eid, ename, basic), f)
    print("Record added.")


def search_record():
    eid = read_id()
    if eid is None:
        return
    for emp in load_all():
        if emp.eid == eid:
            print("Record found:")
            emp.display()
            return
    print("Record not found.")



def delete_record():
    eid = read_id()
    if eid is None:
        return
    records = load_all()
    remaining = [e for e in records if e.eid != eid]
    if len(remaining) == len(records):
        print("Record not found.")
        return
    save_all(remaining)
    print("Record deleted.")


def edit_record():
    eid = read_id()
    if eid is None:
        return
    records = load_all()
    for emp in records:
        if emp.eid == eid:
            print("Current record:")
            emp.display()
            new_name = input("Enter new name (press Enter to keep): ").strip()
            new_basic = input("Enter new basic (press Enter to keep): ").strip()
            try:
                if new_name:
                    emp.ename = new_name
                if new_basic:
                    emp.basic = float(new_basic)
            except ValueError:
                print("Invalid salary. Record not changed.")
                return
            save_all(records)
            print("Record updated.")
            return
    print("Record not found.")


def display_all():
    records = load_all()
    if not records:
        print("No records available.")
        return
    print("\n--- All Employees ---")
    for emp in records:
        emp.display()

def main():
    while True:
        print("\n===== Employee Menu =====")
        print("1. Add a record")
        print("2. Search a record by id")
        print("3. Delete a record by id")
        print("4. Edit a record by id")
        print("5. Display all records")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_record()
        elif choice == "2":
            search_record()
        elif choice == "3":
            delete_record()
        elif choice == "4":
            edit_record()
        elif choice == "5":
            display_all()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 to 6.")


if __name__ == "__main__":
    main()
