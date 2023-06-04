# Task Manager

# options
# 1. add task
    #1.1  ask task title
# 2. delete task
# 3. show tasklist
# 4. sort
# 5. exit
from collections import OrderedDict
import numpy as np
import json
taskid = 0
tasklist = []


def add_task():
    global taskid, tasklist
    taskname = input("Enter the task title: ")
    taskid +=1
    taskpriority = input("Enter the task priority: ")
    if taskpriority =="":
        taskpriority="0"
    
    list_entry = {taskid:{"taskname":taskname,"priority":taskpriority}}
    print(f"[{taskid}] {taskname}")
    tasklist.append(list_entry)
    print(tasklist)

def save_and_exit():
    jsonoutput = json.dumps(tasklist)
    f = open("tasklist.txt","w")
    f.write(jsonoutput)
    f.close()
    exit()

def display_list():
    global tasklist,taskid

    print("================    TASKLIST    ===================\n")
    for taskitem in tasklist:
        for taskkey in taskitem:
            # print(type(taskitem[taskkey]))
            # print(f"[{taskkey}] {taskitem[taskkey]}")
            print(f"[{taskkey}] {taskitem[taskkey]['taskname']} [{taskitem[taskkey]['priority']}]")
            # print(f"[{taskkey}] {taskitem[taskkey]}")
            taskid = int(taskkey)

def read_tasklist_from_file():
    global tasklist
    f = open("tasklist.txt","r")
    jsoncontent = f.read()
    f.close()
    if jsoncontent == "":
        tasklist=[]
    else:    
        tasklist = json.loads(jsoncontent)
def edit_task():
    print("tasklist is :")
    for i in tasklist:
        print(i)
    task_id=int(input("enter the task id to be edited: "))
    print("\n\ntask in tasklist array is :")
    chosen_task_dict = tasklist[task_id-1]
    print(chosen_task_dict)
    print("chosen task is :")
    chosen_task=chosen_task_dict[str(task_id)]
    print(chosen_task)
    print("what do you want to edit?: ")
    print("1 priority")
    print("2 taskname")
    task_property = input("what do you want to edit?")
    match task_property:
        case "1":
            print(f"current priority is : {chosen_task['priority']}")
            chosen_task['priority']=input("enter new value for priority: ")
            
        case "2":
            print(f"current taskname is : {chosen_task['taskname']}")
            chosen_task['taskname'] = input("enter new taskname: ")
        # case "3":
        #     sort_by_priority()
        # case "4":
        #     edit_task()
        # case "5":
        #     delete_task()
        # case "6":
        #     save_and_exit() 
        case "":
            print("Invalid input .please select one of these options")     
        case _:
            print("invalid")
    

def display_menu():
        print("\n===============================")
        print("\tSelect your option")
        print("===============================")
        print("1 add task \n")
        print("2 display list \n")
        print("3 sort \n")
        print("4 edit task \n")
        print("5 delete task \n")
        print("6 Exit \n")
        print("===============================\n\n")
def sort_by_priority(): 
    unsortedkeys = []
    unsortedvalues = []
    unsortedtitle = []
    for taskitem in tasklist:
        # keys = list(taskitem.keys())
        # values = list(taskitem.values())
        # print(f"key is {keys}")
        # print(f"values is {values}")
        # print(f"taskitem is {taskitem}")

        for taskkey in taskitem:
            # print(f"[{taskkey}] {taskitem[taskkey]['taskname']} [{taskitem[taskkey]['priority']}]")
            output = int(taskitem[taskkey]['priority'])   
            tasknameoutput = taskitem[taskkey]['taskname']
            # print(f" [{taskitem[taskkey]['priority']}]")
            # values = list(dict.values())  
            print(f"priority output = {output}")
            unsortedvalues.append(output)
            print(f"task key output = {taskkey}")
            unsortedkeys.append(taskkey)
            unsortedtitle.append(tasknameoutput)
        print(f"unsorted keys = {unsortedkeys}")
        print(f"unsorted values = {unsortedvalues}")
        print(f"unsorted title = {unsortedtitle}")
        sorted_value_index = np.argsort(unsortedvalues)
        print(sorted_value_index)
        # print(type(sorted_value_index))
        # print(sorted_value_index.size)
        # rev_sorted_value_index = sorted_value_index.sort(reverse=True)
        # sorted_dict = {unsortedkeys[i]: unsortedvalues[i] for i in sorted_value_index}
        inc_sorted_dict = {unsortedkeys[i]: { "title" : unsortedtitle[i], "priority" : unsortedvalues[i] } for i in sorted_value_index}
        dec_sorted_dict = {unsortedkeys[i]: { "title" : unsortedtitle[i], "priority" : unsortedvalues[i] } for i in reversed(sorted_value_index)}

        # sorted_dict = {unsortedkeys[sorted_value_index.size - i]: { "title" : unsortedtitle[sorted_value_index.size - i], "priority" : unsortedvalues[sorted_value_index.size - i] } for i in sorted_value_index}

        print(f"high priority wise dictionary = {dec_sorted_dict}")
        print(f"low priority wise dictionary = {inc_sorted_dict}")
        print(f"priority wise sorted list")
        for k in dec_sorted_dict :
            # print(k)
            print(f" [{dec_sorted_dict[k]['priority']}] {dec_sorted_dict[k]['title']}[{k}]")


        # print("priority wise sorted tasklist")
        # for k in sorted_dict:
        #     print(tasklist[int(k)])

        # for taskkey in taskitem:
        #     # print(f"[{taskkey}] {taskitem[taskkey]['taskname']} [{taskitem[taskkey]['priority']}]")
        #     print(f" [{taskitem[taskkey]['priority']}] {taskitem[taskkey]['taskname']} ")
        #     # values = list(dict.values())  

def task_manager():
    read_tasklist_from_file()
    display_list()
    while(True):
        display_menu()
        user_choice=input("")
        match user_choice:
            case "1":
                add_task()
                # order_list()
            case "2":
                display_list()
            case "3":
                sort_by_priority()
            case "4":
                edit_task()
            case "5":
                delete_task()
            case "6":
                save_and_exit() 
            case "":
                print("Invalid input .please select one of these options")     
            case _:
                print("invalid")
if __name__=="__main__":
    task_manager()

