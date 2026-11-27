"""Beginner-friendly Employee Management command-line application."""
from employee_service import EmployeeService

def show_menu():
    print("\n=== Employee Management ===")
    print("1. Add employee")
    print("2. List employees")
    print("3. Search employee")
    print("4. Update department")
    print("5. Delete employee")
    print("6. List employees by department")
    print("7. Exit")

def print_employees(employees, empty_message):
    if not employees:
        print(empty_message)
    for employee in employees:
        print(employee)

def main():
    service = EmployeeService()
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            employee_id = input("Employee ID: ").strip()
            name = input("Name: ").strip()
            department = input("Department: ").strip()
            try:
                service.add_employee(employee_id, name, department)
                print("Employee added.")
            except ValueError as error:
                print("Error:", error)
        elif choice == "2":
            employees = service.list_employees()
            print_employees(employees, "No employees found.")
        elif choice == "3":
            term = input("Enter employee ID or name: ").strip()
            matches = service.search_employees(term)
            print_employees(matches, "No matching employees.")
        elif choice == "4":
            employee_id = input("Employee ID: ").strip()
            department = input("New department: ").strip()
            try:
                service.update_department(employee_id, department)
                print("Department updated.")
            except ValueError as error:
                print("Error:", error)
        elif choice == "5":
            employee_id = input("Employee ID to delete: ").strip()
            print("Employee deleted." if service.delete_employee(employee_id) else "Employee not found.")
        elif choice == "6":
            department = input("Department: ").strip()
            employees = service.list_by_department(department)
            print_employees(employees, "No employees found in that department.")
        elif choice == "7":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please select 1 to 7.")

if __name__ == "__main__":
    main()

