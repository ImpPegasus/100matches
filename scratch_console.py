from random import randrange

play = True
vMax = 100


def AIturn():
    nonlocal Num, Count
    if Num > Count:
        Num = Count;
    else:
        Num = randrange(0, 10)

def __main__():
    Num = 0
    Count = vMax
    AIturn()
    while play:
        print('Number of opponents')

    return 0


__main__()
