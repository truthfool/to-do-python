#Usage :-
# $ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
# $ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
# $ ./task del INDEX            # Delete the incomplete item with the given index
# $ ./task done INDEX           # Mark the incomplete item with the given index as complete
# $ ./task help                 # Show usage
# $ ./task report 


import sys

def help_task():
    print("Usage :-")
    print("$ ./task add 2 hello world    # Add a new item with priority 2 and text \"hello world\" to the list")
    print("$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order")
    print("$ ./task del INDEX            # Delete the incomplete item with the given index")
    print("$ ./task done INDEX           # Mark the incomplete item with the given index as complete")
    print("$ ./task report               # Statistics")
        
def list_tasks():
    file1 = open("task.txt","r").readlines()
    i=1
    for task in file1:
        print("{}. {}[{}]".format(i,task[:-2],task.split()[-1]))
        i+=1

def list_tasks_completed():
    file1 = open("completed.txt","r").readlines()
    i=1
    for task in file1:
        print("{}. {}".format(i,task))
        i+=1

def report():
    file1=open("task.txt","r").readlines()
    file2=open("completed.txt","r").readlines()
    count1,count2=0,0
    for i in file1:
        if i:
            count1+=1
    for i in file2:
        if i:
            count2+=1

    print("Pending :{}".format(count1))
    list_tasks()
    print("Completed :{}".format(count2))
    list_tasks_completed()


def add(next_words):
    priority=int(next_words[0])
    task=str(next_words[2:])
    
    with open("task.txt","r") as f:
        lines=f.read().splitlines()
    
    i=0
    print(lines)
    for line in lines:
        print(line[-1])    
        if int(line[-1])<=int(priority):
            i+=1
        else:
            lines.insert(i, task+" "+str(priority))

    i=0
    with open("task.txt", "w") as f:
        for line in lines:
            if i<len(lines)-1:
                f.write(line+"\n")
                i+=1
            else:
                f.write(line)



def done(val):
    with open("task.txt", "r") as f:
        lines = f.readlines()

    if int(val)>len(lines):
        print("Error: no incomplete item with index {} exists.".format(val))
        return

    i,s=1,""
    with open("task.txt", "w") as f:
        for line in lines:
            if i!=int(val):
                f.write(line)
            else:
                s=line
                print("Marked item as done.")
            i+=1
    
    with open("completed.txt","a+") as f:
        f.write("\n"+s)

def delete(val):
    with open("task.txt", "r") as f:
        lines = f.readlines()

    if int(val)>len(lines):
        print("Error: item with index {} does not exist. Nothing deleted.".format(val))
        return

    i=1
    with open("task.txt", "w") as f:
        for line in lines:
            if i!=int(val):
                f.write(line)
            else:
                print("Deleted item with index {}".format(val))
            i+=1

def task(a):
    first_word = a[1]
    next_words=""
    
    for i in a[2:]:
        next_words+=i+" "

    if first_word=="help":
        help_task()
    elif first_word=="ls":
        list_tasks()
    elif first_word=="add":
        add(next_words)
    elif first_word=="del":
        delete(a[-1])
    elif first_word=="done":
        done(a[-1])
    elif first_word=="report":
        report()

if __name__== "__main__":
    task(sys.argv)