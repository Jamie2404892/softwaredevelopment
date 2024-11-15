default_player_stats = {"level" : 0, "health" : 1, "experience" : 0}

players = {"player1" : {
            "level" : 0,
            "health" : 100,
            "experience" : 0,
            }}

def level_up(player_name):
    players[player_name]["level"] += 1


level_up(1,"player1")

print(players["player1"])

#would pull from default_player_stats to make a new player but it wasnt specified so leaving as is
