import random, sys, time

input('Press enter to begin...')
while True:
    print('...')
    time.sleep(random.randint(20, 50) / 10.0)
    print('DRAW')
    drawTime = time.time()
    input()
    timeElapsed = time.time() - drawTime

    if timeElapsed < 0.01:
        print('You drew before "DRAW", you lose!')
    elif timeElapsed > 0.3:
        timeElapsed = round(timeElapsed, 4)
        print('You took', timeElapsed, 'seconds to draw!. Too slow!')
    else:
        timeElapsed = round(timeElapsed, 4)
        print('You took', timeElapsed, 'seconds to draw!.')
        print('You win!')

    print('Press enter to play again, or QUIT')
    response = input('> ').upper()
    if response == 'QUIT':
        print('Goodbye!')
        sys.exit(1)