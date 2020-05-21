import json
settings_file = "settings_player.txt"
st_file = open(settings_file, "w")


Player1 = {
    "Nick Name": "Ivan",
    "Score": 345,
    "Life": 98,
    "Age": 49
}

Player2 = {
    "Nick Name": "Kuzma",
    "Score": 765,
    "Life": 70,
    "Age": 37
}

Players = []
Players.append(Player1)
Players.append(Player2)

json.dump(Players, st_file)
st_file.close()

new_file = open("settings_player.txt", "r")
restore_players = json.load(new_file)
for item in restore_players:
    print("Player Name is : " + item['Nick Name'])