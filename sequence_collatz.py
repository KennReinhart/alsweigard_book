#oldest math problem in the book
#rules
#if n is even, the next number n is n / 2
#if n is odd, the next number n is n*3+1
#if n is either 0 or 1, stop. Otherwise repeat

import sys, time

print('''Collatz Sequence''')
def collatz(n):
    print(n, end='', flush=True)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
            if n % 3 == 0:
                n = n // 3

        print(', ', str(n), end='', flush=True)
        time.sleep(0.1)
    print()

for start in range(1, 1000):
    print(f"Start: {start}")
    collatz(start)


#original
# print('Enter a starting number (greater than zero): or QUIT')
# response = input('> ')

# if not response.isdecimal() or response == '0':
#     print('Invalid input')
#     sys.exit()

# n = int(response)
# print(n, end='', flush=True)
#     while n != 1:
#         if n % 2 == 0:
#             n = n // 2
#         else:
#             n = 3 * n + 1
#             if n % 3 == 0:
#                 n = n // 3
#
#         print(', ', str(n), end='', flush=True)
#         time.sleep(0.1)
#     print()