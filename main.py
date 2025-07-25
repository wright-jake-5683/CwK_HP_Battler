import wizards 
import moves
import helper_functions as hf

play = True
team = []

while (play == True):
    action, team = hf.mainLobby(team)
    match (action):
        case "Explore":
            result = hf.startFight(team)
    