import random, sys

JAPANESE_NUMBERS = {1:'ICHI', 2:'NI', 3:'SAN',
                    4:'SHI', 5:'GO', 6:'ROKU'}

print('''CHO (even) or HAN (odd)''')

attempts=0
#Saldo
while True:
    print('How much money do you have?')
    response = input('> ')
    if response.isdecimal():
        saldo = int(response)
        break

    attempts+=1
    print('We only accept money man')

    if attempts >=3:
        print('Come back when you have money')
        sys.exit(1)

while True:
    print('You have ', saldo , 'Place your bet. ALL IN or QUIT')
    while True:
        response = input('> ')
        if response.upper() == 'QUIT':
            print('Thank you for playing')
            sys.exit(1)
        elif not response.isdecimal():
            print('Only real money man')
        elif int(response) > saldo:
            print('Sorry, you do not have enough money')
        else:
            response = int(response)
            break

    #roll the dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the dice')
    print('CHO (even) or HAN (odd)')
    while True:
        bet = input('> ')
        if bet != 'CHO' and bet != 'HAN':
            print('You may choose CHO or HAN only')
            continue
        else:
            break

    #reveal the dice results
    print(' ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('     ', dice1, '       ', dice2)

    #determine if the player won:
    rollIsEven = (dice1+dice2)%2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    if playerWon:
        print('You won!', response, 'mon')
        saldo = saldo + response
        print('The house collects a', response // 10, 'fee')
        saldo = saldo - (response // 10)
    else:
        saldo = saldo - response
        print('Sorry, you lost', saldo, 'remains')

    if saldo == 0:
        print('You are broke, go find more money')
        sys.exit(1)


