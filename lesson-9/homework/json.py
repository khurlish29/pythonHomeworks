import csv
import json
def load_tasks(file):
    with open(file, 'r') as f:
        return json.load(f)

def save_tasks(file, tasks):
    with open(file, 'w') as f:
        json.dump(tasks, f, indent=4)

def display_tasks(tasks):
    print("ID | Task | Completed | Priority")
    for task in tasks:
        print(f"{task['id']} | {task['task']} | {task['completed']} | {task['priority']}")

def calculate_task_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task['priority'] for task in tasks) / total_tasks
    print(f"Total tasks: {total_tasks}\nCompleted tasks: {completed_tasks}\nPending tasks: {pending_tasks}\nAverage priority: {avg_priority:.2f}")

def convert_json_to_csv(json_file, csv_file):
    tasks = load_tasks(json_file)
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])
