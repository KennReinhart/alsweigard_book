print('   |  0   1   2   3   4   5   6   7   8   9  10  11  12')
print('---+---------------------------------------------------')

#display each row of products:
for number1 in range(0, 13):
    # print vertical number
    print(str(number1).rjust(2), end='')

    # Print a separating bar
    print('|', end='')
    for number2 in range(0, 13):
        print(str(number1 * number2).rjust(4), end='')

    print()