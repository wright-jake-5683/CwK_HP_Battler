import wizards 
import moves
import helper_functions as hf

play = True
team = []

while (play == True):
    action, team = hf.mainLobby(team)

    match (action):
        case "Explore":
            while (action == "Explore"):
                if not team:
                    print("You have no wizards left on your team, returning to Hogwarts...")
                    action = ""
                else:
                    hf.startFight(team, True)
                    answer = int(input("Press 1 to keep Exploring or any other button to return to the Hogwarts: \n"))
                    if (answer == 1):
                        action = "Explore"
                    elif (isinstance(answer, int)):
                        action = ""
                    else:
                        print("Please enter a valid integer")
    