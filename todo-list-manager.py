# --------------------------------------------- import ----------------------------------------------------------------------------  
from rich.console import Console
from rich.text import Text
from collections import OrderedDict
import json


# --------------------------------------------- global variables ----------------------------------------------------------------------------  

taskid = 0
tasklist = []
taskname = ""
task_dictionary = {}
console = Console()

# ---------------------------------------------Displaying menu----------------------------------------------------------------------------  


def display_menu():
        # print("\n===============================")
        # print("\tSelect your option")
        # print("===============================")
        print_format("SELECT YOUR OPTION")
        # print(f"[1] ADD [2] LIST [3] EDIT [4] DELETE [5] COMPLETE [6] PENDING [7] PRIORITY [8] EXIT")
        print_y("1 Add Task \n")
        print_y("2 display List \n")
        print_y("3 Sort \n")
        print_y("4 Edit Task \n")
        print_y("5 Delete Task \n")
        print_y("6 Complete Task \n")
        print_y("7 Pending Task \n")
        print_y("8 Exit \n")
        print_y("===============================\n\n")
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

    header_line_1 = Text(text="\n===========-------------===========", style="#00FFFF")
    console.print(header_line_1)
    header_text = Text(text=f"             {i}            ", style="#7FFF00")
    console.print(header_text)
    # print(f"          {i}          ")
    header_line_2 = Text(text="===========-------------===========\n", style="#00FFFF")
    console.print(header_line_2)
# --------------------------------------------- formated error----------------------------------------------------------------------------  

def print_error(i):
    header_line_1 = Text(text="\n===========---ERROR----===========\n", style="#DC143C")
    console.print(header_line_1)
    header_text = Text(text=f" ❌❌--- {i} ---❌❌  ", style="#8B0000")
    console.print(header_text)
    header_line_1 = Text(text="\n===========---ERROR----===========", style="#DC143C")
    console.print(header_line_1)
# --------------------------------------------- display taskList ----------------------------------------------------------------------------


def display_list():
    global taskid, task_dictionary
    print_b("{:<8} {:<60} {:<10} {:<10}".format('ID','Title','Priority','Status'))
    print_g("------------------------------------------------------------------------------------------------------------")
    for taskitem in tasklist:
        for taskkey in taskitem:
            task_dictionary[taskkey] = taskitem[taskkey]
        for k, v in taskitem.items():
            # print(f"{k} --------- {v}")
            # taskname, priority, status = v
            # print ("{:<8} {:<15} {:<10} {:<10}".format(k,k[v]))
            print_db ("{:<8} {:<60} {:<10} {:<10}".format(k, v['taskname'], v['priority'], v['status']))
            taskid = int(k)


# --------------------------------------------- Add New Task----------------------------------------------------------------------------  

def add_task():
    global taskid, tasklist,taskname,taskpriority
    try:
        print_p("Enter the task title:\n ")
        taskname = input("")
        task_status = 'pending'  
        add_priority()
        taskid +=1
        list_entry = {taskid:{"taskname":taskname,"priority":taskpriority,"status":task_status}}
        # print(f"[{taskid}] {taskname}")
        tasklist.append(list_entry)
    except ValueError:
        print_error("Enter the Integer value between 1-99")
    except KeyError:
        print_error("Please choose with in the range (Shown above)")
        add_priority()



# ---------------------------------------------Adding Priority----------------------------------------------------------------------------  


def add_priority():
    global taskpriority
    try:
        print_p("Enter the task priority: \n")
        taskpriority = int(input(""))
        if taskpriority =="":
            taskpriority="0"
        elif taskpriority > 99:
            print_p("Enter value between 1-99")
        elif taskpriority < 0:
            print_p("Enter value between 1-99")
        # list_entry = {taskid:{"taskname":taskname,"priority":taskpriority,"status":taskstatus}}
        # print(f"[{taskid}] {taskname}")
        # tasklist.append(list_entry)
        # print(tasklist)
    except ValueError:
        print_error("Enter a value between 1-100 or Enter 0 to skip ")
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


# ---------------------------------------------Save & exit----------------------------------------------------------------------------  



def save_and_exit():
    jsonoutput = json.dumps(tasklist)
    f = open("tasklist.txt","w")
    f.write(jsonoutput)
    f.close()
    exit()


# ---------------------------------------------Importing TaskList----------------------------------------------------------------------------  

def read_tasklist_from_file():
    global tasklist
    f = open("tasklist.txt","r")
    jsoncontent = f.read()
    f.close()
    if jsoncontent == "":
        tasklist=[]
    else:    
        tasklist = json.loads(jsoncontent)

# ---------------------------------------------Editing TaskList----------------------------------------------------------------------------  

def edit_task():
    try:
        print_format("TASKLIST")
        print_b ("{:<8} {:<60} {:<10} {:<10}".format('ID','Title','Priority','Status'))
        print_g("------------------------------------------------------------------------------------------------------------")
        for taskitem in tasklist:
            for k, v in taskitem.items():
                # index = index(k)
                # index = index + 1
                print_db("{:<8} {:<60} {:<10} {:<10}".format(k, v['taskname'], v['priority'], v['status']))
        # for taskitem in tasklist:
        #         for taskkey in taskitem:
        #             index = tasklist.index(taskitem)
        #             index = index + 1
        #             print(f"[{index}] {taskitem[taskkey]['taskname']} [{taskitem[taskkey]['priority']}]")
        print_p("\nenter the task id to be edited:\n")
        task_id=input(" ")
        # task_id=int(input("\nenter the task id to be edited: "))
        # print(task_dictionary)
        print_g(f"{task_dictionary[task_id]} {task_dictionary[task_id]['taskname']} {task_dictionary[task_id]['priority']}")
        # chosen_task_dict = tasklist[task_id-1]
        # chosen_task=chosen_task_dict[str(task_id)]
        # print(f"\n---> {chosen_task['taskname']} [{chosen_task['priority']}] ")
        print_p("\nwhat do you want to edit?: ")
        print_g("1 priority")
        print_g("2 taskname")
        task_property = input("what do you want to edit?")
        match task_property:
            case "1":
                print_g(f"current priority is : {task_dictionary[task_id]['priority']}")
                print_p("enter new value for priority:\n")
                task_dictionary[task_id]['priority']=input(" ")
                
            case "2":
                print_g(f"current taskname is : {task_dictionary[task_id]['taskname']}")
                print_p("enter new taskname:\n")
                task_dictionary[task_id]['taskname'] = input(" ")
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

    for taskitem in tasklist:
        for taskkey in taskitem:
            task_dictionary[taskkey] = taskitem[taskkey]
            unsorted_dictionary[taskkey]=int(taskitem[taskkey]['priority'])
    arranged=sorted(unsorted_dictionary.items(),key=lambda x: x[1],reverse=True)
    print_format("TASKLIST")
    print_b("{:<8} {:<60} {:<10} {:<10}".format('ID','Title','Priority','Status'))
    print_g("------------------------------------------------------------------------------------------------------------")
    for i in arranged:
        new_key = i[0]
        # print(task_dictionary[new_key])
        print_db ("{:<8} {:<60} {:<10} {:<10}".format(new_key,task_dictionary[new_key]['taskname'], task_dictionary[new_key]['priority'],task_dictionary[new_key]['status']))
    # for taskitem in tasklist:
    #     for k, v in taskitem.items():
    #             # index = index(k)
    #             # index = index + 1

# ---------------------------------------------Deleting Tasks----------------------------------------------------------------------------  


def delete_task():
    try:
        print_format("TASKLIST")
        for taskitem in tasklist:
                for taskkey in taskitem:
                    index = tasklist.index(taskitem)
                    index = index + 1
                    print(f"[{index}] {taskitem[taskkey]['taskname']} [{taskitem[taskkey]['priority']}]")  
        print_p("\nenter the task id to be deleted: \n")
        task_id=int(input(""))
        chosen_task_dict = tasklist[task_id-1]
        chosen_task=chosen_task_dict[str(task_id)]
        print_g(f"\n---> {chosen_task['taskname']} [{chosen_task['priority']}] ")
        print_p("\nAre you sure want to delete?")
        print_y("\n[y] to delete or [n] to cancel ")
        delete_item = input("\nconfirm ? : ")
        if delete_item == "y":
            del tasklist[task_id-1]

    except IndexError:
        print_error("Please choose with in the range (Shown above)")
    except KeyError:
        print_error("Please choose with in the range (Shown above)")

# ---------------------------------------------Deleting Tasks----------------------------------------------------------------------------  

def complete_task():
    try:
        print_format("TASKLIST")
        print_b ("{:<8} {:<60} {:<10} {:<10}".format('ID','Title','Priority','Status'))
        print_g("------------------------------------------------------------------------------------------------------------")
        for taskitem in tasklist:
            for k, v in taskitem.items():
                print_db("{:<8} {:<60} {:<10} {:<10}".format(k, v['taskname'], v['priority'], v['status']))
        print_p("\nenter the task id to be completed: \n")            
        task_id=int(input(""))
        chosen_task_dict = tasklist[task_id-1]
        chosen_task=chosen_task_dict[str(task_id)]
        print(f"\n---> {chosen_task['taskname']} [{chosen_task['priority']}] {chosen_task['status']}")                                                                                                                                                                                                                                                                                                                                                 
        chosen_task['status']="completed"
        print(f"\n---> {chosen_task['taskname']} [{chosen_task['priority']}] {chosen_task['status']}")                                                                                                                                                                                                                                                                                                                                                 

    except IndexError:
        print_error("Please choose with in the range (Shown above)")
    except KeyError:
        print_error("Please choose with in the range (Shown above)")

# ---------------------------------------------pending task----------------------------------------------------------------------------  


def pending_task():
    global taskid
    pending = 0
    completed = 0
    print_b("{:<8} {:<60} {:<10} {:<10}".format('ID','Title','Priority','Status'))
    print_g("------------------------------------------------------------------------------------------------------------")
    for taskitem in tasklist:
        for k, v in taskitem.items():
            if v['status'] == "pending":
                print_y("{:<8} {:<60} {:<10} {:<10}".format(k, v['taskname'], v['priority'], v['status']))
                pending = pending + 1
            else:
                completed = completed + 1   
    if pending == 0:
        print_g("\n                 <--------- Every thing is completed ---------->")



# ---------------------------------------------Main menu----------------------------------------------------------------------------  
# [1] add []

def task_manager():
    read_tasklist_from_file()
    print_format("TASKS")
    display_list()
    # mytext = Text(text="Todo List", style="#00FFFF")
    # console.print(mytext)
    # print_format ("sourabh")
    # print_format ("appu")
    # print_format ("apple")
    # print_format ("mango")
    while(True):
        display_menu()
        user_choice=input("")
        match user_choice:
            case "1":
                add_task()
            case "2":
                display_list()
            case "4":
                edit_task()
            case "5":
                delete_task()
            case "6":
                complete_task() 
            case "7":
                pending_task()
            case "3":
                sort_by_priority()                
            case "8":
                save_and_exit() 
            case "":
                print_error("Invalid input .please select one of these options")     
            case _:
                print_error("invalid")

if __name__=="__main__":
    task_manager()
