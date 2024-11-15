shop_items = {"tomato" : {"price" : 10, "stock" : 3},
              "carrot" : {"price" : 2, "stock" : 6},
              "lettuce" : {"price" : 5, "stock" : 8},
              }

def buy_items(shop_items, item_name, player_gold):
    if shop_items[item_name]["stock"] > 0:
        if player_gold >= shop_items[item_name]["price"]:
            player_gold -= shop_items[item_name]["price"]
        else:
            print("Not enough gold")
            
    else:
        print(f"The item {item_name} is out of stock.")
