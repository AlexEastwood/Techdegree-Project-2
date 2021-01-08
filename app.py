import constants


def clean_data(players):

    new_players = []

    for player in players:
        new_players.append(player)

    for player in new_players:
        height_whole = player["height"]
        height_digits = []
        for i in range(len(height_whole)):
            if height_whole[i].isnumeric() == True:
                height_digits.append(height_whole[i])
            else:
                player["height"] = int(("".join(map(str, height_digits))))
                break

        if player["experience"] == "YES":
            player["experience"] = True
        else:
            player["experience"] = False
            
        player_guardians = player["guardians"].split(" and ")
        player["guardians"] = player_guardians
            
    return new_players

def player_teams(player_list):
    num_players_team = int(len(player_list) / len(constants.TEAMS))


    experienced_on_team = [{"team": constants.TEAMS[0], "experienced": 0, "inexperienced": 0}, 
                           {"team": constants.TEAMS[1], "experienced": 0, "inexperienced": 0}, 
                           {"team": constants.TEAMS[2], "experienced": 0, "inexperienced": 0}]
    
    j = 0
    
    for player in player_list:
        if player["experience"] == True:
            while True:
                if experienced_on_team[j]["experienced"] < num_players_team / 2:
                    player["team"] = constants.TEAMS[j]
                    experienced_on_team[j]["experienced"] += 1
                    j = 0
                    break
                else:
                    j += 1
                    continue
        else:
            while True:
                if experienced_on_team[j]["inexperienced"] < num_players_team / 2:
                    player["team"] = constants.TEAMS[j]
                    experienced_on_team[j]["inexperienced"] += 1
                    j = 0 
                    break
                else:
                    j += 1
                    continue

    return player_list

def team_stats(team):
    if team not in ["A", "B", "C"]:
        while team.upper() not in ["A", "B", "C"]:
            team = input("Please choose A, B or C\n")
        team = team.upper()

        print("\n\nTeam: {}".format(list_of_teams[team]))
        print("Total Players: {}".format(int(len(list_of_players) / len(constants.TEAMS))))
        print("Players on Team:")
        players_one_string = []
        experienced = 0
        inexperienced = 0
        
        for player in list_of_players:
            if player["team"] == list_of_teams[team]:
                player_name = player["name"]
                players_one_string.append(player_name)
            
                if player["experience"] == True:
                    experienced += 1
                else:
                    inexperienced += 1
                
        print(", ".join(players_one_string))
        print("Experienced: {}".format(experienced))
        print("Inexperienced: {}".format(inexperienced))
        
        
        print("Press Enter to continue")
        input()
        return

if __name__ == "__main__":
    list_of_players = clean_data(constants.PLAYERS)
    list_of_players = player_teams(list_of_players)
    list_of_teams = {"A": constants.TEAMS[0], "B": constants.TEAMS[1], "C": constants.TEAMS[2]} 

for player in list_of_players:
    print(player)


while True:
    print("\n\nBASKETBALL TEAM STATS TOOL")
    print("\n\n----MENU----\n\n")
    print("""Here are your choices:\nA) Display Team Stats\nB) Quit\n""")

    while True:
        choice = input()
        choice = choice.upper()
        if choice == "A":
            choice = input("A) Panthers\nB) Bandits\nC) Warriors\n")
            team_stats(choice)
            break    
        elif choice == "B":
            print("Goodbye")
            exit()
        else:
            print("Please choose A or B\n")
            continue
