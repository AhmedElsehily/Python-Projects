# print("%" * 60)
# print("  Welcom to To Do List  ".center(60,"%"))
# print("%" * 60)

# name = input ("What\'s your name? ").strip().capitalize()

# print(f"Welcom Back Mr: {name}.")

# # add task                    show task                    delete task
# operation = ["Add Task", "Show Tasks", "Delete Task","Exit"]
# taskList = []


# def addTask (taskName):
#     taskList.append(taskName)

# def showTasks():
#     print(f"Your Tasks are: {taskList}")

# def deleteTask(taskNum):
#     taskList.remove(taskList.index(taskNum))


# option = input(f"Choose the operation:  {operation} ").strip().capitalize()
# while option != "Exit":
#     option = input(f"Choose the operation:  {operation} ").strip().capitalize()
#     if option == "Add":
#         addT = input("Enter the task you want to add  ").strip().capitalize()
#         addTask(addT)
#         print("Added Success.")
#     elif option == "Show":
#         showTasks()
#     elif option == "Delete":
#         delT = input("Enter the task you want to delete  ").strip().capitalize()
#         deleteTask(delT)
#     elif option == "Exit":
#         break
#     else:
#         print("Try Again")

# else:
#     print("Your Work is done ..^ ^..")

#----------------------   To Do List -----------------#
# print("%" * 60)
# print(" Welcome to To Do List ".center(60, "%"))
# print("%" * 60)

# name = input("What's your name? ").strip().capitalize()
# print(f"Welcome Back Mr: {name}")

# tasks = []

# def add_task():
#     task = input("Enter task name: ").strip()
#     tasks.append(task)
#     print("Task added successfully.")

# def show_tasks():
#     if not tasks:
#         print("No tasks found.")
#     else:
#         print("Your Tasks:")
#         for i, task in enumerate(tasks, 1):
#             print(f"{i}. {task}")

# def delete_task():
#     show_tasks()
#     if tasks:
#         try:
#             num = int(input("Enter task number to delete: "))
#             tasks.pop(num - 1)
#             print("Task deleted successfully.")
#         except (ValueError, IndexError):
#             print("Invalid choice.")

# while True:
#     print("\nChoose an option:")
#     print("1 - Add Task")
#     print("2 - Show Tasks")
#     print("3 - Delete Task")
#     print("4 - Exit")

#     choice = input("Your choice: ").strip()

#     if choice == "1":
#         add_task()
#     elif choice == "2":
#         show_tasks()
#     elif choice == "3":
#         delete_task()
#     elif choice == "4":
#         print("Your work is done. Goodbye 👋")
#         break
#     else:
#         print("Invalid option. Try again.")


#------------------------  Login system  ------------------------#


# print("%" * 60)
# print(" Welcome to Login System ".center(60, "%"))
# print("%" * 60)
# userName = input("User Name: ").strip().lower()
# password = input("Password: ").strip()
# mainPassword = "@hmed"
# while password != mainPassword:
#     tries -=1
#     tries = int(input("Enter the number of tries you want? ").strip())
#     print("Incorrect Password.")
#     password = input("Password: ").strip()
#     print(f"Wrong password {"last" if tries == 1 else tries} chances left")
#     if tries == 0:
#         print("Incorrect Password.")
#         break 
# else:
#     print(f"...Welcome Back...Ms {userName.capitalize()}.")




# products = {
#     "Laptop": 1000,
#     "Keyboard": 30,
#     "Mouse":15,
#     "Mobile":800,
#     "Head Phone":50
# }

# print("%" * 60)
# print(" Welcome to Login System ".center(60, "%"))
# print("%" * 60)
# mainPassword = "@hmed"
# userName = input("User Name: ").strip().lower()
# tries = 3
# while tries > 0:
#     password = input("Password: ").strip()
#     if password == mainPassword:
#         print(f"..Welcome Back.. MR: {userName.upper()}")
#         print("Choose any products you want:" )
#         for i, product in enumerate(products, 1):
#             print(f"{i}- {product} price ==> {products.get(product)}")
#         item = int(input("Select the item: "))
#         num = int(input("Number of items:  "))
#         for j, items in enumerate(products,1):
#              if item == j:
#                  print("$" *50)
#                  print("   Your Bill Contant:  ".center(50,"$"))
#                  print("$" *50)
#                  total = products.get(items)* num
#                  print(f"Product Name:   {items}  ")
#                  print(f"Product Amount: {num}    ")
#                  print(f"Total price is: {total} EGP ")
#                  break
#         break
          
#     else:
#         tries -=1
#         print(f"Wrong password {'last' if tries == 1 else tries} chances left")        
#         if tries == 0:
#             print('Incorrect password')
#             break
    


products = {
    "Laptop": 1000,
    "Keyboard": 30,
    "Mouse": 15,
    "Mobile": 800,
    "Head Phone": 50
}

print("%" * 60)
print(" Welcome to Billing System ".center(60, "%"))
print("%" * 60)

mainPassword = "@hmed"
userName = input("User Name: ").strip().lower()
tries = 3

while tries > 0:
    password = input("Password: ").strip()

    if password == mainPassword:
        print(f"\n..Welcome Back.. MR: {userName.upper()}")
        print("\nAvailable Products:")

        for i, product in enumerate(products, 1):
            print(f"{i}- {product} ==> {products[product]} EGP")

        bill = []
        grand_total = 0

        while True:
            item = int(input("\nSelect product number: "))
            quantity = int(input("Enter quantity: "))

            for index, name in enumerate(products, 1):
                if item == index:
                    price = products[name]
                    total = price * quantity

                    bill.append((name, quantity, total))
                    grand_total += total

                    print(f"Added: {name} x{quantity} = {total} EGP")

            more = input("Do you want to buy another product? (y/n): ").strip().lower()
            if more != "y":
                break

        print("\n" + "$" * 50)
        print(" YOUR BILL ".center(50, "$"))
        print("$" * 50)

        for item in bill:
            print(f"{item[0]} x{item[1]} ==> {item[2]} EGP")

        print("-" * 50)
        print(f"Grand Total: {grand_total} EGP")
        print("$" * 50)

        break

    else:
        tries -= 1
        print(f"Wrong password {'last' if tries == 1 else tries} chances left")
        if tries == 0:
            print("Incorrect password. Access denied.")
