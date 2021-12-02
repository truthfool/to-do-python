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
    file1=open("task.txt","r").read()
    pending = file1.split("\n")
    file2=open("completed.txt","r").read()
    completed = file2.split("\n")
    count1,count2=0,0
    for i in pending:
        if i:
            count1+=1
    for i in completed:
        if i:
            count2+=1

    print("Pending :{}".format(count1))
    list_tasks()
    print("Completed :{}".format(count2))
    list_tasks_completed()


def add(next_words):
    priority=int(next_words[0])
    task=str(next_words[1:])
    with open("task.txt","r+") as f:
        lines=f.readlines()
        for line in lines:
            if int(line[-1])>priority:
                lines[i] = lines[i].strip() + '2012\n'
                f.seek(0)
                for line in lines:
                    f.write(line)

def delete(val):
    s=""
    with open("task.txt", "r") as f:
        lines = f.readlines()
        if lines[-1]==val:
            s=lines[:-2]

    with open("task.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != s:
                f.write(line)
def done(val):
    s=""
    with open("task.txt", "r") as f:
        lines = f.readlines()
        if lines[-1]==val:
            s=lines[:-2]

    with open("task.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != s:
                f.write(line)
            else:
                add(s)

def task(a):
    first_word = a.split()[0]
    next_words=a[1:]

    if a=="help":
        help_task()
    elif a=="ls":
        list_tasks()
    elif a=="add":
        add(next_words)
    elif a=="del":
        delete(a[-1])
    elif a=="done":
        done(a[-1])
    elif a=="report":
        report()

if __name__== "__main__":
    task(sys.argv[1])