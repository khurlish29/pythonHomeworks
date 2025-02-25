class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.filename = filename
        self.employees = self.load_employees()

    def load_employees(self):
        employees = []
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    employee_id, name, position, salary = line.strip().split(", ")
                    employees.append(Employee(employee_id, name, position, float(salary)))
        except FileNotFoundError:
            pass  # File does not exist yet
        return employees

    def save_employees(self):
        with open(self.filename, "w") as file:
            for emp in self.employees:
                file.write(str(emp) + "\n")

    def add_employee(self, employee):
        self.employees.append(employee)
        self.save_employees()

    def view_all_employees(self):
        for emp in self.employees:
            print(emp)

    def search_employee(self, employee_id):
        for emp in self.employees:
            if emp.employee_id == employee_id:
                return emp
        return None

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        emp = self.search_employee(employee_id)
        if emp:
            if name: emp.name = name
            if position: emp.position = position
            if salary: emp.salary = float(salary)
            self.save_employees()
            return True
        return False

    def delete_employee(self, employee_id):
        emp = self.search_employee(employee_id)
        if emp:
            self.employees.remove(emp)
            self.save_employees()
            return True
        return False

def main():
    manager = EmployeeManager()

    while True:
        print("\nWelcome to the Employee Records Manager!")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            employee_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            position = input("Enter Position: ")
            salary = input("Enter Salary: ")
            manager.add_employee(Employee(employee_id, name, position, float(salary)))
            print("Employee added successfully!")

        elif choice == "2":
            print("\nEmployee Records:")
            manager.view_all_employees()

        elif choice == "3":
            employee_id = input("Enter Employee ID to search: ")
            emp = manager.search_employee(employee_id)
            if emp:
                print("\nEmployee Found:")
                print(emp)
            else:
                print("Employee not found.")

        elif choice == "4":
            employee_id = input("Enter Employee ID to update: ")
            name = input("Enter new Name (leave blank to keep unchanged): ")
            position = input("Enter new Position (leave blank to keep unchanged): ")
            salary = input("Enter new Salary (leave blank to keep unchanged): ")
            updated = manager.update_employee(employee_id, name or None, position or None, salary or None)
            if updated:
                print("Employee updated successfully!")
            else:
                print("Employee not found.")

        elif choice == "5":
            employee_id = input("Enter Employee ID to delete: ")
            deleted = manager.delete_employee(employee_id)
            if deleted:
                print("Employee deleted successfully!")
            else:
                print("Employee not found.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
