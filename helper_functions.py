import random
import wizards

def generateDeathEater():
    r = random.randint(1,4)
    if (r == 1):
        enemy = wizards.Gryffindor("Death Eater")
    elif (r == 2):
        enemy = wizards.Slytherin("Death Eater")
    elif (r == 3):
        enemy = wizards.Hufflepuff("Death Eater")
    elif (r == 4):
        enemy = wizards.Ravenclaw("Death Eater")
    return enemy

#---------------------------------------------------------------

def generateStartingWizards(team):
    count = 0
    limit = 3 - len(team)
    while (count < limit):
        house = int(input("Choose a house: \n" +
        "Press 1 for Gryffindor \n" +
        "Press 2 for Slytherin \n" +
        "Press 3 for Hufflepuff \n" +
        "Press 4 for Ravenclaw \n"))
        
        match (house):
            case 1:
                name = input("Please give this new member of Gryffindor a name: \n")
                wiz = wizards.Gryffindor(name)
                team.append(wiz)
                count += 1
                print()
            case 2:
                name = input("Please give this new member of Slytherin a name: \n")
                wiz = wizards.Slytherin(name)
                team.append(wiz)
                count += 1
                print()
            case 3:
                name = input("Please give this new member of Hufflepuff a name: \n")
                wiz = wizards.Hufflepuff(name)
                team.append(wiz)
                count += 1
                print()
            case 4:
                name = input("Please give this new member of Ravenclaw a name: \n")
                wiz = wizards.Ravenclaw(name)
                team.append(wiz)
                count += 1
                print()
    return team

#---------------------------------------------------------------

def explorePrep(team):
        if len(team) < 3:
            print(f"It appears you only have {len(team)} wizards on your team to go exploring with. Please select more Wizards to start with \n")
            print("------------------------------")
            team = generateStartingWizards(team)
            print("\nGreat, here is your team: \n ")
            for wizard in team:
                print(f"{wizard.name} - House: {wizard.house}")
                print("--------------------------------")

        ready = input("Are you ready to explore? (Y/N)\n")
        if (ready.upper().strip() == "Y"):
            action = "Explore"
            return action, team
        elif (ready.upper().strip() == "N"):
            action = ""
            return action, team
        else:
            print("Please enter 'Y' if you are ready to explore and 'N' if you would like to stay in the main lobby \n")

#---------------------------------------------------------------

def viewTeam():
    print("This functionality has not been implemented yet. Please come back another time.")

#---------------------------------------------------------------

def mainLobby(team):
    options = ["Explore", "View Team"]

    print("Welcome to Hogwarts. Please select one of the following options by type its corresponding number value: \n")
    for option in  options:
        print(f"{options.index(option) + 1}). {option}")
    print()
    optionSelected = int(input())
    
    match (optionSelected):
        case 1: 
            return explorePrep(team)
        case 2:
            viewTeam()

#---------------------------------------------------------------

def startFight(team):
    enemy = generateDeathEater()
    print("A Death Eater has appeared...")
    print("Chose the team member you would like to fight with by typing their corresponding number")
    for character in team:
        print(f"{team.index(character) + 1}). {character.name}")
    selection = int(input())
    character = team[selection - 1]
    print("Choose a move to attack by entering it's number...")
    move = playerMove(character)
    print(f"You used {move}...")
    enemyMove = opponentMove(enemy)
    print(f"The Death Eater used {enemyMove}...")



#---------------------------------------------------------------

def playerMove(character):
    for move in character.moveSet:
        print(f"{character.moveSet.index(move) + 1}). {move}")
    selection = input().lower().strip()
    move = character.moveSet[selection]
    return move

#---------------------------------------------------------------

def opponentMove(enemy):
    r = random.randint(0,1)
    if (r == 0):
        move = enemy.moveSet[r]
    elif (r == 1):
        move = enemy.moveSet[r]
    return move