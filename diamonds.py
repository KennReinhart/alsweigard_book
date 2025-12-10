def main():
    print('Diamonds by AL Sweigart')

    for diamondSize in range(0,6):
        displayOutlineDiamond(diamondSize)
        print()
        displayFilledDiamond(diamondSize)
        print()

def displayOutlineDiamond(size):
     # Display the top half of the diamond:
    for i in range(size):
         print(' ' * (size - i - 1), end='')  # Left side space.
         print('/', end='')  # Left side of diamond.
         print(' ' * (i * 2), end='')  # Interior of diamond.
         print('\\')  # Right side of diamond.

     # Display the bottom half of the diamond:
    for i in range(size):
         print(' ' * i, end='')  # Left side space.
         print('\\', end='')  # Left side of diamond.
         print(' ' * ((size - i - 1) * 2), end='')  # Interior of diamond.
         print('/')  # Right side of diamond.


def displayFilledDiamond(size):
    # Display the top half of the diamond:
    for i in range(size):
        print(' ' * (size - i - 1), end='')  # Left side space.
        print('/' * (i + 1), end='')  # Left half of diamond.
        print('\\' * (i + 1))  # Right half of diamond.
     # Display the bottom half of the diamond:
    for i in range(size):
        print(' ' * i, end='')  # Left side space.
        print('\\' * (size - i), end='')  # Left side of diamond.
        print('/' * (size - i))  # Right side of diamond.

if __name__ == '__main__':
    main()