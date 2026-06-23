tasks = []
# for load the task:
def load_tasks():
    file = open("tasks.txt", "r")
    for line in file:
        tasks.append(line.strip())
    file.close()
# for save the task:  
def save_tasks():
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()
# for add the task:
def add_task():
    task = input("Enter your task: ")
    tasks.append(task)
    save_tasks()
    print("Task added successfully")
# for see the task:
def view_tasks():
    if len(tasks) == 0:
        print("No tasks available")
    else:
        for i in range(len(tasks)):
            print(i+1, ".", tasks[i])
# for remove the task from list:
def delete_task():
    view_tasks()
    number = int(input("Enter task number to delete: "))
    tasks.pop(number-1)
    save_tasks()
    print("Task deleted")
load_tasks()

print("----------------------------------")
print("   SHIVAM'S TO DO LIST MANAGER   ")
print("----------------------------------")

while True:
    print("\n ** TO DO LIST **")
    print("1. Add Your Task:")
    print("2. View Task:")
    print("3. Delete Task:")
    print("4. Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Thank you")
        break
    else:
        print("Invalid choice")