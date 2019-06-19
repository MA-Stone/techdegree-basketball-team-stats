from constants import TEAMS, PLAYERS

def balance_players_to_team():
    teams_data = {team:[] for team in TEAMS}
    team_index = 0
    for player in PLAYERS:
        teams_data[TEAMS[team_index]].append(
            {
                'name': player['name'],
                'guardians': player['guardians'],
                'experience': True if player['experience'] else False,
                'height': int(player['height'][0:3])
            }
        )
        team_index = (team_index + 1) % len(TEAMS)
    return teams_data

def display_team_stats(team_name, team_players):
    print()
    print("Team: {} Stats".format(team_name))
    print("-" * len("Team: {} Stats".format(team_name)))
    print("Total players: {}\n".format(len(team_players)))
    print("Players on Team:")
    print(" " + ", ".join([player['name'] for player in team_players]))
    print()

def start():
    teams_data = balance_players_to_team()

    print("BASKETBALL TEAM STATS TOOL")
    
    while(True):
        print()
        print("-------- MENU --------\n")
        print(" Here are your choices:")
        print("  1) Display Team Stats")
        print("  2) Quit\n")

        try:
            option = int(input("Enter an option > "))
            if (option == 1):
                print()
                for team_no, team_name in enumerate(TEAMS, start=1):
                    print("{}) {}".format(team_no, team_name))
                print()
                team_no = int(input("Enter an option > "))
                team_name = TEAMS[team_no-1]
                display_team_stats(team_name, teams_data[team_name])
            elif (option == 2):
                print()
                print("Good bye!")
                break
            else:
                raise ValueError
        except:
            print()
            print("You inputed wrong option!")
            
        input("Press Enter to continue...")

if __name__ == "__main__":
    start()
