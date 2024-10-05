import random as r

pencils = input("How many pencils would you like to use:")
while True:
    try:
        pencils = int(pencils)    
    except ValueError:
        print("The number of pencils should be numeric")
        pencils = input()
    else:
        pencils = int(pencils)
        if pencils < 0:
            print("The number of pencils should be numeric")
            pencils = input()
        elif pencils == 0:
            print("The number of pencils should be positive")
            pencils = input()
        else:
            pencils = int(pencils)
            break  
name1 = 'Lisa'
name2 = 'Bot'
first_player = input(f"Who will be the first ({name1},{name2}):")
if first_player not in [name1, name2]:
    print(f"Choose between {name1} and {name2}")
    first_player = input()
print("|" * pencils)
if first_player == name1:
    list_of_players = [name1, name2]
elif first_player == name2:
    list_of_players = [name2, name1]
current_player = first_player
player_index = 0
while pencils > 0:
    print (f"{name1}'s turn:" if current_player == name1 else f"{name2}'s turn:")
    if current_player == name2:
        if pencils % 4 == 0:
            turn = 3
        elif pencils % 4 == 3:
            turn = 2
        elif pencils % 4 == 2:
            turn = 1
        else:
            if pencils != 1:
                turn = r.randint(1,3)
            else:
                turn = 1
        print(turn)
    else:
        turn = input()
        while True:
            try:
                turn = int(turn)    
            except ValueError:
                print("Possible values: '1', '2' or '3'")
                turn = input()
            else:
                turn = int(turn)
                if turn not in [1, 2, 3]:
                    print("Possible values: '1', '2' or '3'")
                    turn = input()
                elif turn > pencils:
                    print("Too many pencils were taken")
                    turn = int(input())
                else:
                    turn = int(turn)
                    break
    pencils -= turn
    print('|' * pencils)
    player_index += 1
    current_player = list_of_players[player_index % 2]
print(f"{current_player} won!")