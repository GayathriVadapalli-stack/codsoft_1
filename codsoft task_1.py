#To-Do List
def add_todolist(to_do_list):  #adding tasks in the to-do-list
    num_elements=int(input("Enter the number of tasks you want to add: "))
    print("Enter your tasks")
    for i in range(num_elements):
        to_do_list.append(input().lower())
    print("Your Tasks have been added")
def update_todolist(to_do_list):   #deleting the tasks that are done in the to-do-list
    show_todolist(to_do_list)
    task=int(input("Enter the index of the tasks you've already done: "))
    to_do_list.pop(task-1)
    print("Your list has been updated")
def show_todolist(to_do_list):   #show to-do-list
    for i,j in enumerate(to_do_list):
        print(f'{i+1}.{j}')
to_do_list=[]  #defining the empty to-do-list
print(5*'*'+"To-Do List"+5*'*')
print("Create your To-Do List now")
while True:
    print("1.Create Task \n2.Update Task \n3.Track your to-do list")
    user_choice= int(input('Enter your choice: '))
    # calling functions according to the task
    if user_choice == 1:
        add_todolist(to_do_list)
    elif user_choice ==2:
        if len(to_do_list) == 0:
            print("The to-do list is Empty")
        else:
            update_todolist(to_do_list)
    elif user_choice==3:
        if len(to_do_list) == 0:
            print("The to-do list is Empty")
        else:
            show_todolist(to_do_list)
    else:
        print("Enter Valid choice")
    #Knowing the interest to continue adding or deleting or tracking the to-do-list
    interest=input(("Do you want to make any changes in the to-do list?(Type 'Y' or 'N'): ")).lower()
    if interest=='n':
        print("Thank you ")
        break
    elif interest=='y':
        continue
    else:
        print("Enter a valid interest")