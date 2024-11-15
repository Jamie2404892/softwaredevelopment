#yet to add error handling

#Table to hold the tasks for each day of the week 
week = {
    "monday" : ["cleaning"],
    "tuesday" : [],
    "wednesday" : [],
    "thursday" : [],
    "friday" : [],
    "saturday" : [],
    "sunday" : [],
    }

#adds an item to a selected day
def addItem(): 
    day = input("what day?").lower()
    item = input("what task?").lower()
    week[day].append(item)

#removes an item from a selected day 
def removeItem():
    day = input("what day?").lower()
    item = input("what task?").lower()
    week[day].remove(item)

#view what tasks are on a selected day or all
def viewTasks():
    day = input("what day?").lower()
    if day == "all":
        print(week)
    else:
        print(week[day])

#loops until end is selected     
active = True
while active:
    instruction = int(input("\nadd item (1)  view tasks(2)\nremove item(3)  end(4)"))
    if instruction == 1:
        addItem()
    if instruction ==2:
        viewTasks()
    if instruction == 3:
        removeItem()
    if instruction == 4:
        active = False