print('Ctrl - C to quit')

while True:
    response = input('Enter a number to start > ')
    if response == '':
        response = 0
        break
    if response.isdecimal():
        break
    print('Please enter a number greater than or equal to 0.')
start = int(response)

while True:
    response = input('Enter how many numbers to display > ')
    if response == '':
        response = 100
        break
    if response.isdecimal():
        break
    print('Please enter a number greater than start')
amount = int(response)

for number in range(start, start + amount): #main program
    hexNumber = hex(number)[2:]
    binNumber = bin(number)[2:]

    print('DEC:', number, ' HEX:', hexNumber, ' BIN:', binNumber)

#hex(number)[2:].upper() changed the a into A and so forth eg, 90 Hex is 5A instead of 5a
#response would be automatically have str or string type