import os
from models.employee import Employee
from services.sql import *

def show_menu():
    os.system('clear' if os.name == 'posix' else 'cls')  # Cross-platform clear screen
    print("""
          1. Insert Employee
          2. Get Employee by ID
          3. Get Employee by Last Name
          4. Show All Employees
          e. Exit
          """)

def execute_insert_emp():
    print("\nInsert Employee")
    first = input("Enter First Name: ")
    last = input("Enter Last Name: ")
    try:
        pay = int(input("Salary: "))
        emp = Employee(first, last, pay)
        insert_emp(emp)
        print("Employee added successfully!")
    except ValueError:
        print("Invalid salary input. Please enter a number.")

def show_employees():
    employees = get_all_emps()
    if employees:
        show_table(employees)
    else:
        print("No employees found.")

def main():
    while True:
        show_menu()
        user_input = input("Select an option: ")
        if user_input == "1":
            execute_insert_emp()
        elif user_input == "2":
            try:
                emp_id = int(input("Enter ID: "))
                emp = get_emp_by_id(emp_id)
                if emp:
                    show_table([emp])
                else:
                    print("Employee not found.")
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif user_input == "3":
            last_name = input("Enter Last Name: ")
            emps = get_emp_by_last(last_name)
            if emps:
                show_table(emps)
            else:
                print("No employees found with that last name.")
        elif user_input == "4":
            show_employees()
        elif user_input.lower() == "e":
            os.system('clear' if os.name == 'posix' else 'cls')
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
