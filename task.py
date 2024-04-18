# employee management system 
import json

class Employee:
    def __init__(self,id,name,title,department):
        self.name = name
        self.id = id
        self.title = title
        self.department = department
    
    def display_employee_details(self):
        print(f" employee name:{self.name} and Id is {self.id}")
    

class Department:
    def __init__(self,department_name, employee_list =[]):
        self.department_name = department_name
        self.employee_list = employee_list

    def add_employee(self,employee):
        if employee in self.employee_list:
            print("this employee already added")
        else:
            self.employee_list.append(employee)
            print("employee has sucessfully added")
    
    def remove_employee(self,employee):
        if employee in self.employee_list:
            self.employee_list.remove(employee)
            print("employee has been removed successfully")
        else:
            print("Employee is not found inside the employee list")
    
    def display_all_employees(self):
        for employee in self.employee_list:
            print("Employee:",employee.name)


class Company:
    def __init__(self):
        self.company = {}

    def add_department(self, department):
        if department.department_name in self.company:
            print("department already exists")
        else:
            self.company[department.department_name] = department
            print("department is successfully to the added company")

    def remove_department(self, department):
        if department.department_name in self.company:
            self.company.pop(department.department_name)
            print("department has been removed successfully from the company")
        else:
            print("department was not found in the company")

    def display_departments(self):
        for department_name , department in self.company.items():
            for employee in department.employee_list:
                print(f"Department : {department_name}, employee_name: {employee.name}")

    def save_company_data(self,filename):
        company_data = []
        for department_name , department in self.company.items():
            data = {
                    "department name" : department_name,
                    "employee name" : [employee.name for employee in department.employee_list] 
                    }
            company_data.append(data)
        
        # save data to JSON
        with open(filename, 'w') as file:
            json.dump(company_data, file, indent=4)
        print(f"Data saved to {filename}.")



while True:
        print("\nmenu for the user to interact with the Employee Management System :")
        print("1. Create Employee ")
        print("2. Create Department")
        print("3. Add Employee from Department")
        print("4. Remove Employee from Department")
        print("5. List All Employee from Departments")
        print("6. Create Company")
        print("7. Add Department to Company")
        print("8. Removed Department from Company")
        print("9. Display Department Details")
        print("10. Save Company Data")
        print("11. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            emp_name = input("Enter employee name: ")
            emp_id = int(input("Enter employee ID: "))
            emp_title = input("Enter employee title: ")
            emp_dept = input("Enter department name: ")
            emp = Employee(emp_id,emp_name, emp_title,emp_dept)
        if choice == "2":
            department_name = input("Enter department name: ")
            Dept = Department(department_name)
        elif choice == "3":
            Dept.add_employee(emp)
        elif choice == "4":
            Dept.remove_employee(emp)
        elif choice == "5":
            Dept.display_all_employees()
        elif choice == "6":
            com = Company()
        elif choice == "7":
            com.add_department(Dept)
        elif choice == "8":
            com.remove_department(Dept)
        elif choice == "9":
            com.display_departments()
        elif choice == "10":
            file_name = input("Enter file name: ")
            com.save_company_data(file_name)
        elif choice == "11":
            exit()
        
        




# # Create employees
# employee1 = Employee(1,"raj","mr","IT")
# employee2 = Employee(2,"sen","mr","security")

# # Create departments
# department1 = Department("Engineerning")
# department2 = Department("Management")


# # Add 2 employees to departments
# department1.add_employee(employee1)
# department2.add_employee(employee2)


# # Remove an employee2 from department1

# # department1.remove_employee(employee2)


# # List employees of department1
# department1.display_all_employees()

# #Create company
# company = Company()

# # add department1 to the company

# company.add_department(department1)
# company.add_department(department2)



# # remove department1 from company

# # company.remove_department(department1)

# # display all departments details
# company.display_departments()
# # save company information
# company.save_company_data(r'E:\assigment\sample.json')


        