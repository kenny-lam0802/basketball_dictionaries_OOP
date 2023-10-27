players = [
    {
        "name":"Nikola Jokic",
        "age":28,
        "position":"Center",
        "team":"Denver Nuggets"
    },
    {
        "name":"LeBron James",
        "age":38,
        "position":"Small Forward",
        "team":"Los Angeles Lakers"
    },
    {
        "name":"Stephen Curry",
        "age":35,
        "position":"Point Guard",
        "team":"Golden State Warriors"
    },
    {
        "name":"Jayson Tatum",
        "age":25,
        "position":"Small Foward",
        "team":"Boston Celtics"
    },
    {
        "name":"Jimmy Butler",
        "age":34,
        "position":"Small Foward",
        "team":"Miami Heat"
    }
]

#1) Constructors to accept dictionary
class Player:
    def __init__(self, player_dictionary):
        self.name = player_dictionary["name"]
        self.age = player_dictionary["age"]
        self.position = player_dictionary["position"]
        self.team = player_dictionary["team"]

#2) Create object instances using players
nikola = {
        "name":"Nikola Jokic",
        "age":28,
        "position":"Center",
        "team":"Denver Nuggets"
}
lebron = {
        "name":"LeBron James",
        "age":38,
        "position":"Small Forward",
        "team":"Los Angeles Lakers"
}

stephen = {
        "name":"Stephen Curry",
        "age":35,
        "position":"Point Guard",
        "team":"Golden State Warriors"
}

jayson = {
        "name":"Jayson Tatum",
        "age":25,
        "position":"Small Foward",
        "team":"Boston Celtics"
}

jimmy = {
        "name":"Jimmy Butler",
        "age":34,
        "position":"Small Foward",
        "team":"Miami Heat"
}

player_nikola = Player(nikola)
player_lebron = Player(lebron)
player_stephen = Player(stephen)
player_jayson = Player(jayson)
player_Jimmy = Player(jimmy)
print(player_nikola)
print(player_lebron)
print(player_stephen)
print(player_jayson)
print(player_Jimmy)

new_team = [] #empty list to store objects
for player_info in players:
    new_team.append(Player(player_info)) #add objects to the empty list

for player_info in new_team:
    print(f"{player_info.name} - {player_info.team}")
