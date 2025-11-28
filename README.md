This is where i answers the given questions from the projects

1. Guessing game (practice with constants)
   
   a. What happens when you change the NUM_DIGITS constant?
   
        The number of digits would increases or decreases, initial number was 3.
   
   b. What happens when you change the MAX_GUESSES constant?
   
        The number of tries to guess the correct number would increase or decrease.
   
   c. What happens if you set NUM_DIGITS to a number larger than 10?
   
         List index out of range.
   
   d. What happens if you replace secretNum = getSecretNum() on line 30 with secretNum = '123'?
   
        The correct number will always be '123'
   
   e. What error message do you get if you delete or comment out numGuesses = 1 on line 34?
   
        "cannot access local variable 'numGuesses' since its not define first. By declaring numGuesses as 1 for starter, then loop until numGuesses reaches 3 times with numGuesses += 1 at the end of the 'while loop'
   
   f. What happens if you delete or comment out random.shuffle(numbers) on line 62?
   
        The correct number would always be the first 3 digit of the initial list of numbers (numbers = list('012...')
   
   g. What happens if you delete or comment out if guess == secretNum: on line 74 and return 'You got it!' on line 75?

         The program would not tell if you guess it right, it would straight to go to prompt do you want to play again or not.
   
   h. What happens if you comment out numGuesses += 1 on line 44?
   
        We will stuck until we guess the right digits
