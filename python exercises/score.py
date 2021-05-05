import secrets # Random module is not random enough
def randGame():
    d1, d2 = secrets.randbelow(6)+1, secrets.randbelow(6)+1
    if d1 == d2:
        print( 'Dice 1:', str(d1), '| Dice 2:', str(d2), '\n  Score:', str((d1+d2)*2) )
    else:
        print( 'Dice 1:', str(d1), '| Dice 2:', str(d2), '\n  Score:', str(d1+d2) )
randGame()
