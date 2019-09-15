from random import randrange

play = True
MAX = 100


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

    return 0


__main__()