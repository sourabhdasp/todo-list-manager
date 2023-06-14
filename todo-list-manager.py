# --------------------------------------------- import ----------------------------------------------------------------------------  
from rich.console import Console
from rich.text import Text
from collections import OrderedDict
import json


# --------------------------------------------- global variables ----------------------------------------------------------------------------  

task_id = 0
task_list = []
task_name = ""
task_dictionary = {}
console = Console()

# ---------------------------------------------Save & Exit----------------------------------------------------------------------------

def save_and_exit():
    global task_list
    tasks_json = json.dumps(task_list)
    # print(tasks_json)
    try:
        f = open("tasks.json","w")
        f.write(tasks_json)
        print("file saved successfully")
        f.close()
    except FileNotFoundError:
            print("backup file not found")
    exit()

# ---------------------------------------------Import Tasks----------------------------------------------------------------------------

def import_tasks():
    global task_list
    print("importing tasks from backup file")
    try:
        f = open("tasks.json","r")
        task_json = f.read()
        # print("task_json is :")
        # print(task_json)
        f.close()
        if task_json == "":
                # print("task_json is empty")
                task_list = []
        else:
                task_list = json.loads(task_json)
                # print(task_list)
    except FileNotFoundError:
            print_error("Backup file not found. Starting with an empty task list")
            task_list = []

# ---------------------------------------------Display Main Menu----------------------------------------------------------------------------

def display_menu():
        # print_format("WHAT DO YOU WANT TO DO ?")
        print_g("------------------------------------------------------------------------------------------------------------")
        # print(f"[n] ADD         [e] EDIT        [d] DELETE      [x] DONE \n[p] PENDING          [i] PRIORITY            [a] ALL         [q] EXIT")
        print ("{:<22} {:<22} {:<22} {:<22}".format("[a] ADD TASK", "[e] EDIT TASK", "[d] DELETE TASK", "[x] MARK AS DONE"))
        print ("{:<22} {:<22} {:<22} {:<22}".format("[p] SHOW PENDING", "[i] SHOW PRIORITY", "[t] SHOW ALL", "[q] QUIT"))
        # print_y("1 Add New Task [n]\n")
        # print_y("2 Edit Task [e]\n")
        # print_y("3 Delete Task [d]\n")
        # print_y("4 Mark as Done [x]\n")
        # print_y("5 Show Pending Tasks [p]\n")
        # print_y("6 Show Priority Tasks [i]\n")
        # print_y("7 Show All Tasks [a]\n")
        # print_y("8 Exit [q]\n")
        print_g("------------------------------------------------------------------------------------------------------------")
        # print_y("===============================\n\n")

# --------------------------------------------- display taskList ----------------------------------------------------------------------------

def show_all_tasks():
    global task_list
    print_format("ALL TASKS")
    print_b("{:<8} {:<60} {:<10} {:<10}".format('ID','Title','Priority','Status'))
    print_g("------------------------------------------------------------------------------------------------------------")
    for task in task_list:
        # print(task)
        task_id = task_list.index(task) + 1
        print_db ("{:<8} {:<60} {:<10} {:<10}".format(task_id, task['title'], task['priority'], task['status']))
        # for k, v in task.items():
        #     # print(f"{k} --------- {v}")
        #     # taskname, priority, status = v
        #     # print ("{:<8} {:<15} {:<10} {:<10}".format(k,k[v]))
        #     # print_db ("{:<8} {:<60} {:<10} {:<10}".format(k, v['title'], v['priority'], v['status']))
        #     print_db ("{:<8} {:<60} {:<10} {:<10}".format(k, task['title'], v['priority'], v['status']))
            # task_id = int(k)

# --------------------------------------------- Add New Task----------------------------------------------------------------------------

def add_task():
    global task_id, task_list,task_name,task_priority
    try:
        print_p("Enter the task title:\n ")
        task_name = input("=> ")
        task_status = 'pending'  
        add_priority()
        task_id +=1
        new_entry = {"uid":task_id, "title":task_name,"priority":task_priority,"status":task_status}
        # print(f"[{taskid}] {taskname}")
        task_list.append(new_entry)
    except ValueError:
        print_error("Enter the Integer value between 1-5")
        task_priority = 0
        print(f"task priority  {task_priority}")
    except KeyError:
        print_error("Please choose with in the range (Shown above)")
        # task_priority = 0
        add_priority()



# ---------------------------------------------Adding Priority----------------------------------------------------------------------------  


def add_priority():
    global task_priority
    try:
        print_p("Enter the task priority: \n")
        task_priority = int(input("=> "))
        if task_priority =="":
            task_priority="0"
        elif task_priority > 5:
            print_error("Enter value between 1-5")
            task_priority = 0
            add_priority()
        elif task_priority < 0:
            print_error("Enter value between 1-5")
            task_priority = 0
            add_priority()
        # list_entry = {taskid:{"taskname":taskname,"priority":taskpriority,"status":taskstatus}}
        # print(f"[{taskid}] {taskname}")
        # tasklist.append(list_entry)
        # print(tasklist)
    except ValueError:
        print_error("Enter a value between 1-5 or Enter 0 to skip ")
    except KeyError:
        print_error("Please choose with in the range (Shown above)")
        add_priority()

# --------------------------------------------- display list ----------------------------------------------------------------------------  

# def display_list():
#     global tasklist,taskid

#     print_format("TASKLIST")
#     for taskitem in tasklist:
#         for taskkey in taskitem:
#             print(f"[{taskkey}] {taskitem[taskkey]['taskname']} [{taskitem[taskkey]['priority']}] {taskitem[taskkey]['status']}")
#             taskid = int(taskkey)

# ---------------------------------------------Editing TaskList----------------------------------------------------------------------------

def show_task_info(task_id):
    global user_choice
    try:
        user_choice = task_list[task_id]
        print_g(f"\n---> {user_choice['title']} [{user_choice['priority']}] [{user_choice['status']}] ")
    except KeyError:
        print_error("Please choose with in the range (Shown above)")

def edit_task():
    global user_choice
    try:
        # print_format("TASKLIST")
        show_all_tasks()
        print_p("\nenter the task id to be edited:\n")
        task_id = int(input("=> ")) - 1
        show_task_info(task_id)
        # task_id=int(input("\nenter the task id to be edited: "))
        # print(task_dictionary)
        # print_g(f"{task_dictionary[task_id]} {task_dictionary[task_id]['taskname']} {task_dictionary[task_id]['priority']}")
        # chosen_task_dict = tasklist[task_id-1]
        # chosen_task=chosen_task_dict[str(task_id)]
        # print(f"\n---> {chosen_task['taskname']} [{chosen_task['priority']}] ")
        print_p("\nwhat do you want to edit ? : ")
        print_g("[1] Priority")
        print_g("[2] Title")
        task_property = input("=> ")
        match task_property:
            case "1":
                print_g(f"current priority is : {user_choice['priority']}")
                print_p("enter new value for priority:\n")
                user_choice['priority']=int(input("=> "))
                
            case "2":
                print_g(f"current title is : {user_choice['title']}")
                print_p("enter new title :\n")
                user_choice['title'] = input("=> ")
                print("")
            case "":
                print_error("Invalid input .please select one of these options")     
            case _:
                print_error("invalid")
    except IndexError:
                print_error("Please choose with in the range (Shown above)")
                # print("Please choose with in the range (Shown above)")
    except KeyError:
                print_error("Please choose with in the range (Shown above)")

# ---------------------------------------------Sorted Priority----------------------------------------------------------------------------  

def sort_by_priority(): 
    unsorted_dictionary = {}
    
    # for i in tasklist:
    #     task_dictionary.update(i)
    # print(task_dictionary)

    for task in task_list:
            new_key = task_list.index(task)
            unsorted_dictionary[new_key] = task['priority']
    print(unsorted_dictionary)
    arranged = sorted(unsorted_dictionary.items(),key=lambda x: x[1],reverse=True)
    print_format("TASKLIST")
    print_b("{:<8} {:<60} {:<10} {:<10}".format('ID','Title','Priority','Status'))
    print_g("------------------------------------------------------------------------------------------------------------")
    for i in arranged:
        new_key = i[0]
        # print(task_dictionary[new_key])
        if task_list[new_key]['status'] == "pending":
                print_db ("{:<8} {:<60} {:<10} {:<10}".format(new_key,task_list[new_key]['title'], task_list[new_key]['priority'],task_list[new_key]['status']))
    # for taskitem in tasklist:
    #     for k, v in taskitem.items():
    #             # index = index(k)
    #             # index = index + 1

# ---------------------------------------------Deleting Tasks----------------------------------------------------------------------------  


def delete_task():
    try:
        print_format("tasklist")
        show_all_tasks()
        print_p("\nenter the task id to be deleted: \n")
        task_id = int(input("=> ")) - 1
        user_choice = task_list[task_id]
        print_g(f"\n---> {user_choice['title']} [{user_choice['priority']} [{user_choice['status']}] ")
        print_p("\nare you sure want to delete?")
        print_y("\n[y] to delete or [n] to cancel \n")
        delete_item = input("=> ")
        print("")
        if delete_item == "y":
            del task_list[task_id]

    except IndexError:
        print_error("Please choose with in the range (Shown above)")
    except KeyError:
        print_error("Please choose with in the range (Shown above)")

# ---------------------------------------------Deleting Tasks----------------------------------------------------------------------------  

def complete_task():
    try:
        print_format("TASKLIST")
        # print_b ("{:<8} {:<60} {:<10} {:<10}".format('ID','Title','Priority','Status'))
        # print_g("------------------------------------------------------------------------------------------------------------")
        show_pending_tasks()
        print_p("\nenter the task id to be completed: \n")
        task_id=int(input("=> "))
        user_choice = task_list[task_id-1]
        # chosen_task=chosen_task_dict[str(task_id)]
        print(f"\n---> {user_choice['title']} [{user_choice['priority']}] {user_choice['status']}")
        user_choice['status']="done"
        print(f"\n---> {user_choice['title']} [{user_choice['priority']}] {user_choice['status']}")
        # print(f"\n---> {chosen_task['taskname']} [{chosen_task['priority']}] {chosen_task['status']}")

    except IndexError:
        print_error("Please choose with in the range (Shown above)")
    except KeyError:
        print_error("Please choose with in the range (Shown above)")

# ---------------------------------------------pending task----------------------------------------------------------------------------  


def show_pending_tasks():
    global task_list
    pending = 0
    completed = 0
    print_format("PENDING TASKS")
    print_b("{:<8} {:<60} {:<10} {:<10}".format('ID','Title','Priority','Status'))
    print_g("------------------------------------------------------------------------------------------------------------")
    for task in task_list:
        if task['status'] == "pending":
           task_id = task_list.index(task) + 1
           print_y("{:<8} {:<60} {:<10} {:<10}".format(task_id, task['title'], task['priority'], task['status']))
           pending = pending + 1
        else:
           completed = completed + 1
    if pending == 0:
        print_g("\n                 <--------- Looks like you have no more pending tasks !!! ---------->")

    # for task in task_list:
    #     for k, v in taskitem.items():
    #         if task['status'] == "pending":
    #             print_y("{:<8} {:<60} {:<10} {:<10}".format(k, v['taskname'], v['priority'], v['status']))
    #             pending = pending + 1
    #         else:
    #             completed = completed + 1
    # if pending == 0:
    #     print_g("\n                 <--------- Every thing is completed ---------->")


# --------------------------------------------- formated printstatment ----------------------------------------------------------------------------

def print_y(i):
    header_text = Text(text=f"{i}", style="#ffa500")
    console.print(header_text)
def print_b(i):
    header_text = Text(text=f"{i}", style="#6a5acd")
    console.print(header_text)
def print_db(i):
    header_text = Text(text=f"{i}", style="#00719c")
    console.print(header_text)
def print_g(i):
    header_text = Text(text=f"{i}", style="#00f100")
    console.print(header_text)
def print_p(i):
    header_text = Text(text=f"{i}", style="#ff10be")
    console.print(header_text)
# --------------------------------------------- formated header ----------------------------------------------------------------------------

def print_format(i):

    header_line_1 = Text(text="\n------------------------------------------------------------------------------------------------------------", style="#00FFFF")
    # header_line_1 = Text(text="\n===========-------------===========", style="#00FFFF")
    console.print(header_line_1)
    header_text = Text(text=f" {i} ", style="#7FFF00")
    console.print(header_text)
    # print(f"          {i}          ")
    header_line_2 = Text(text="------------------------------------------------------------------------------------------------------------", style="#00FFFF")
    console.print(header_line_2)

# --------------------------------------------- formated error----------------------------------------------------------------------------

def print_error(i):
    header_line_1 = Text(text="\n===========---ERROR----===========\n", style="#DC143C")
    console.print(header_line_1)
    header_text = Text(text=f" ❌❌--- {i} ---❌❌  ", style="#8B0000")
    console.print(header_text)
    header_line_1 = Text(text="\n===========---ERROR----===========", style="#DC143C")
    console.print(header_line_1)

# ---------------------------------------------Main Application Logic----------------------------------------------------------------------------

def task_manager():
    import_tasks()
    # print_format("TASKS")
    show_pending_tasks()
    # mytext = Text(text="Todo List", style="#00FFFF")
    # console.print(mytext)
    # print_format ("sourabh")
    # print_format ("appu")
    # print_format ("apple")
    # print_format ("mango")
    while(True):
        display_menu()
        user_choice=input("=> ")
        match user_choice:
            case "1" | "a":
                add_task()
                # print_format("TASKS")
                show_pending_tasks()
            case "2" | "e":
                edit_task()
                show_all_tasks()
            case "3" | "d":
                delete_task()
                show_all_tasks()
            case "4" | "x":
                complete_task()
                show_pending_tasks()
            case "5" | "p":
                show_pending_tasks()
            case "6" | "i":
                sort_by_priority()
            case "7" | "t":
                show_all_tasks()
            case "8" | "q":
                save_and_exit()
            case "":
                print_error("Input is empty. Please select one from the list below")
            case _:
                print_error("That is an invalid option. Please select one from the list below")

if __name__=="__main__":
    task_manager()
