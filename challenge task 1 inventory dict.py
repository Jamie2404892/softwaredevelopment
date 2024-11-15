inventory = {"apple" : 1}

def add_item(inventory,item_name,quantity):
    inventory[item_name] = inventory.get(item_name, 0) + quantity

def use_item(inventory,item_name):
    if inventory[item_name] >= 1:
        inventory[item_name] -= 1
        if inventory[item_name] == 0:
            del inventory[item_name]
    else:
        print("you have no more ",item_name)
    

add_item(inventory,"banana",1)
add_item(inventory,"banana",1)
use_item(inventory,"banana")
print(inventory)
