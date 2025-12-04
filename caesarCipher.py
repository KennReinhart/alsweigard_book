#is an ancient encryption algorithm used by Julius Caesar.
#by shifting them over by a certain number of places in the alphabet.
#ex, if key is 3, then A is D, B becomes E, etc

#to be added in cyberSec project

try:
    import pyperclip
except ImportError:
    pass #if not installed, do nothing.

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Let the user enter if they are encrypting or decrypting
while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?:')
    response = input('> ').lower()
    if response == 'e':
        mode = 'encrypt'
        break
    elif response == 'd':
        mode = 'decrypt'
        break
    print('Please enter your choice (e/d):')

# Let the user enter the key to use
while True:
    maxKey = len(SYMBOLS) - 1
    print('Please enter the {} key (0 to {}) to use'.format(mode, maxKey))
    response = input('> ').lower()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# Let the user enter the message to encrypt/decrypt
print('Enter the message to {}.'.format(mode))
message = input('> ')

#Caesar cipher only works on uppercase letters
message = message.upper()

#Stores the encrypted/decrpyted form of the message:
translated = ''

#Encrypt/decrypt each symbol in the message
for symbol in message:
    if symbol in SYMBOLS:
        #Get the encrypted (or decrpyted) number for this symbol
        num = SYMBOLS.find(symbol) # Get the number of the symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        #SYMBOLS or less than 0
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        translated = translated + SYMBOLS[num]
    else:
        #Add the symbol without encrypting/decrypting
        translated = translated + symbol
print(translated)

try:
    pyperclip.copy(translated)
    print('{} Copied to clipboard.'.format(mode))
except:
    pass


