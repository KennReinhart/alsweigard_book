while True:
    print('Do you want to know a secret y/n ?')
    response = input('> ')
    if response in ('y', 'yes', 'YES,' 'Yes'):
        print('aight, do you want to know a secret y/n ?')
        continue
    elif response in ('n', 'no', 'NO,', 'No'):
        print('bye')
        break
    else:
        print('sorry, {} is not a valid response'.format(response))
