import math, sys

while True:
    print('Enter a positive whole number to factor (or QUIT):')
    response = input('> ')
    if response.upper() == 'QUIT':
        sys.exit()

    if not (response.isdecimal() and int(response) > 0):
        continue
    number = int(response)

    factors = []

    #find the factors
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0: #if theres no remainder, it is a factor
            factors.append(i)
            factors.append(number // i)

    #convert to a set to get rid of duplicate
    factors = list(set(factors))
    factors.sort()

    for i, factor in enumerate(factors):
        factors[i] = str(factor)
    print(', '.join(factors))