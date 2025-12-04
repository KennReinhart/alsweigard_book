#2D image with only two possible colors for each pixel

import sys

bitmap = """
 .....................................................................
     **************   *  *** **  *      ******************************
    ********************* ** ** *  * ****************************** *
   **      *****************       ******************************
            *************          **  * **** ** ************** *
             *********            *******   **************** * *
              ********           ***************************  *
     *        * **** ***         *************** ******  ** *
                 ****  *         ***************   *** ***  *
                   ******         *************    **   **  *
                   ********        *************    *  ** ***
                     ********         ********          * *** ****
                     *********         ******  *        **** ** * **
                     *********         ****** * *           *** *   *
                       ******          ***** **             *****   *
                       *****            **** *            ********
                      *****             ****              *********
                      ****              **                 *******   *
                      ***                                       *    *
                      **     *                    *
 ....................................................................."""

print('Enter the message to display with the bitmap.')
message = input('> ')
if message == '':
    sys.exit()

# loop over each line in the bitmap
for line in bitmap.splitlines():
    # loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            # Print an empty space since there's space in the bitmap
            print(' ', end='')
        else:
            # Print a character from the message
            print(message[i % len(message)], end='')
    print() # Print a newline

#1. What happens if the player enters a blank string for the message?
# exiting program
#2. Does it matter what the nonspace characters are in the bitmap variable’s string?
#
#3. What does the i variable created on line 45 represent?
#the i represent for each characters in message. we found it by % or modulus which in a sense trying to read each character in the message
#4. What bug happens if you delete or comment out print() on line 43
#its not a bug, its just not working as intended. it makes sures to print the value in the designated bitmap.
