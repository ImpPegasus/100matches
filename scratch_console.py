
play = True
MAX = 100


def PlayerControl(plr: int, op: int):
    n = int
    if op == 1:
        n = 2
    elif op == 2:
        n = 2
    elif op == 3:
        n = 3
    elif op == 4:
        n = 4
    else:
        print("Some bugs in there")
    if plr > n: plr = 1
    return plr

def AIturn():
    nonlocal Num, Count
    if Num > Count:
        Num = Count;
    else:
        Num = randrange(0, 10)
    return 0


def start(NumOfPlayers: int):
    nonlocal names
    print("Please, enter names of all players")
    for name in range(0, NumOfPlayers):
        input(names[name])
    for name in range(4, 1 + NumOfPlayers):
        names[name] = 'AI ' + str(name)
    return 0


def game(plr: int, NumOfPlayers: int, op: int):
    nonlocal names, Num, Count
    if plr == 1:
        print("It's ", names[1], " turn!")
        print('Table has ', Count, ' matches, how much would you take?')
        input(Num)
        if type(Num) != int:
            print('Incorrect value, please try again')
    elif plr == 2:
        print("It's ", names[2], " turn!")
        print('Table has ', Count, ' matches, how much would you take?')
        input(Num)
        if type(Num) != int:
            print('Incorrect value, please try again')

    elif plr == 3:
        print("It's ", names[3], " turn!")
        print('Table has ', Count, ' matches, how much would you take?')
        input(Num)
        if type(Num) != int:
            print('Incorrect value, please try again')

    elif plr == 4:
        print("It's ", names[4], " turn!")
        print('Table has ', Count, ' matches, how much would you take?')
        input(Num)
        if type(Num) != int:
            print('Incorrect value, please try again')

    print(names[plr], "take ", Num, "Matches")
    if Num >= 1 and Num <= 10 and Num <= Count:
        Count = Count - int(Num)
    else:
        print('You must use 1-10 range, try again')
    while Count > 0:
        game(plr, NumOfPlayers, op)
    return plr
def __main__():
    Num = 0
    Count = MAX
    names = ['Player 1', 'Player 2', 'Player 3', 'Player 4']
    NumOfPlayers = int


    AIturn()
    while play:
        print('Number of opponents')
        print('')
        input(NumOfPlayers)
        start(NumOfPlayers)
        game(0, 0, 0)

    return 0


__main__()