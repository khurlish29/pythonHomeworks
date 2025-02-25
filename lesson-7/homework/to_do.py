import csv
import json

class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __repr__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def update_task(self, task_id, **kwargs):
        for task in self.tasks:
            if task.task_id == task_id:
                for key, value in kwargs.items():
                    setattr(task, key, value)

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]

    def filter_tasks(self, status):
        return [task for task in self.tasks if task.status == status]

    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Task ID", "Title", "Description", "Due Date", "Status"])
            for task in self.tasks:
                writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])

    def load_from_csv(self, filename):
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            self.tasks = []
            for row in reader:
                self.tasks.append(Task(row[0], row[1], row[2], row[3], row[4]))

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def load_from_json(self, filename):
        with open(filename, 'r') as file:
            tasks_dict = json.load(file)
            self.tasks = [Task(**task) for task in tasks_dict]

def main():
    todo_list = ToDoList()

    while True:
        print("\nWelcome to the To-Do Application!")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Load tasks")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD): ")
            status = input("Enter Status (Pending/In Progress/Completed): ")
            todo_list.add_task(Task(task_id, title, description, due_date, status))
            print("Task added successfully!")

        elif choice == "2":
            print("\nTasks:")
            todo_list.view_tasks()

        elif choice == "3":
            task_id = input("Enter Task ID to update: ")
            title = input("Enter new Title (leave blank to keep unchanged): ")
            description = input("Enter new Description (leave blank to keep unchanged): ")
            due_date = input("Enter new Due Date (leave blank to keep unchanged): ")
            status = input("Enter new Status (Pending/In Progress/Completed, leave blank to keep unchanged): ")
            update_data = {key: value for key, value in [("title", title), ("description", description), ("due_date", due_date), ("status", status)] if value}
            todo_list.update_task(task_id, **update_data)
            print("Task updated successfully!")

        elif choice == "4":
            task_id = input("Enter Task ID to delete: ")
            todo_list.delete_task(task_id)
            print("Task deleted successfully!")

        elif choice == "5":
            status = input("Enter Status to filter by (Pending/In Progress/Completed): ")
            filtered_tasks = todo_list.filter_tasks(status)
            print("\nFiltered Tasks:")
            for task in filtered_tasks:
                print(task)

        elif choice == "6":
            filename = input("Enter filename to save (with extension .csv or .json): ")
            if filename.endswith('.csv'):
                todo_list.save_to_csv(filename)
            elif filename.endswith('.json'):
                todo_list.save_to_json(filename)
            else:
                print("Unsupported file format.")
            print("Tasks saved successfully!")

        elif choice == "7":
            filename = input("Enter filename to load (with extension .csv or .json): ")
            if filename.endswith('.csv'):
                todo_list.load_from_csv(filename)
            elif filename.endswith('.json'):
                todo_list.load_from_json(filename)
            else:
                print("Unsupported file format.")
            print("Tasks loaded successfully!")

        elif choice == "8":
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
