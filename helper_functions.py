import random
import wizards
import moves

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
        while (True):
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

def viewTeam(team):
    for wizard in team:
        print(f"{wizard.name} - Species: {wizard.house}")
        print("--------------------------------")
    action = ""
    return action, team

#---------------------------------------------------------------

def mainLobby(team):
    options = ["Explore", "View Team"]

    print("Welcome to Hogwarts. Please select one of the following options by typing its corresponding number value: \n")
    for option in  options:
        print(f"{options.index(option) + 1}). {option}")
    print()
    try:
        optionSelected = int(input())
        
        match (optionSelected):
            case 1: 
                return explorePrep(team)
            case 2:
                return viewTeam(team)
    except ValueError:
        print("Please enter a valid integer corresponding to a valid option")
        return "", team

#---------------------------------------------------------------

def startFight(team, fight):
        enemy = generateDeathEater()
        print(f"A Death Eater has appeared...")
        print("------------------------------")
        print("Chose the wizard you would like to fight with by typing their corresponding number")
        for character in team:
            print(f"{team.index(character) + 1}). {character.name}")
        selection = int(input())
        character = team[selection - 1]
        print(f"{character.name}'s health: {character.health}")
        print(f"Death Eater's health: {enemy.health}")
        print("------------------------------")

        while(fight):
            print("Choose a move to attack by entering it's number...")
            move = playerMove(character)
            enemyMove = opponentMove(enemy)
            enemy.calculateDamage(move, character.attack, character.name)
            character.calculateDamage(enemyMove, enemy.attack, enemy.name)
            print(f"{character.name}'s health: {character.health}")
            print(f"Death Eater's health: {enemy.health}")
            print("------------------------------")
            if (character.health == 0 and enemy.health == 0):
                print("Both parties have lost the fight...")
                team.remove(character)
                fight = False
                result = "lost"
            elif (enemy.health == 0):
                print("Enemy has been defeated...")
                print(f"You have saved a new wizard of house {enemy.house}. Please give this new teammate a nickname:")
                name = input()
                wiz = acquireWizard(enemy, name)
                team.append(wiz)
                fight = False
                result = "won"
            elif (character.health == 0):
                print("You have been defeated...")
                team.remove(character)
                fight = False
                result = "lost"
        return result



#---------------------------------------------------------------

def playerMove(character):
    for move in character.moveSet:
        print(f"{character.moveSet.index(move) + 1}). {move}")
    selection = int(input())
    if (selection in range(len(character.moveSet) + 1)):
        move = getattr(moves, character.moveSet[selection - 1])
    else:
        print(f"Value entered is out of range of available move options. Defaulting to basic move...")
        move = getattr(moves, character.moveSet[0])
    return move(character.strength)

#---------------------------------------------------------------

def opponentMove(enemy):
    r = random.randint(0, len(enemy.moveSet) - 1)
    move = getattr(moves, enemy.moveSet[r])
    return move(enemy.strength)

#---------------------------------------------------------------

def acquireWizard(enemy, name):
    wiz = getattr(wizards, enemy.house)
    return wiz(name)