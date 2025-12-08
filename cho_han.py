import random, sys
from importlib.resources.simple import TraversableReader

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5:'GO', 6:'ROKU'}

print('''Cho-han by AL Sweigart, 

In this traditional Japanese dice game, two dice are rolled.
The player must guess if the dice total to an even (cho) or odd (han) number.''')
attempts = 0
while True:
    print('How much money do you have? ')
    response = input('> ')
    if response.isdecimal():
        myMoney = int(response)
        break

    attempts += 1
    print('Only real money man!')

    if attempts >= 3:
        print('Come back when you have money!')
        sys.exit(1)

