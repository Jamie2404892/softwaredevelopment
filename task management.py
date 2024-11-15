#yet to add error handling
week = {
    "monday" : ["cleaning"],
    "tuesday" : [],
    "wednesday" : [],
    "thursday" : [],
    "friday" : [],
    "saturday" : [],
    "sunday" : [],
    }

def addItem(): 
    day = input("what day?").lower()
    item = input("what task?").lower()
    week[day].append(item)
    
def removeItem():
    day = input("what day?").lower()
    item = input("what task?").lower()
    week[day].remove(item)
    
def viewTasks():
    day = input("what day?").lower()
    if day == "all":
        print(week)
    else:
        print(week[day])
        
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