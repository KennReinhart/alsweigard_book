#famous math pattern
#begins with 0 and 1, and the next number is always the sum of the previous two numbers
import sys

attempts = 3

while True:
    print('Enter your number, so we can fibonacci or QUIT:')
    response = input('> ')

    if response == ['QUIT', 'quit']:
        print('aight, Goodbye!')
        sys.exit()
    elif response.isdecimal() and int(response) != 0:
        number = int(response)
    else:
        attempts -= 1
        print('{} more attempts'.format(attempts))

    if attempts == 0:
        print('aight, Goodbye!')
        sys.exit()

#handle the special cases
    if number == 1:
        print('0')
        print()
        print('The #1 Fibonacci number is 0.')
    elif number == 2:
        print('1')
        print()
        print('The #2 Fibonacci number is 1.')

    if number >= 10000:
        print('This would take a while')
        print('Press Ctrl-C to quit.')
        input('Press Enter to begin...')

    #Caluclate the Nth Fibonacci number
    secondToLastNumber = 0
    lastNumber = 1
    fibNumbersCalucalated = 2
    print('0, 1, ', end='') #display the first two Fibonacci numbers

    while True:
        nextNumber = secondToLastNumber + lastNumber
        fibNumbersCalucalated += 1
        print(nextNumber, end=' ')

        if fibNumbersCalucalated == number:
            print()
            print()
            print('The #', fibNumbersCalucalated, ' Fibonacci number is ', nextNumber, sep='')
            break

        print(', ', end='')

        secondToLastNumber = lastNumber
        lastNumber = nextNumber



