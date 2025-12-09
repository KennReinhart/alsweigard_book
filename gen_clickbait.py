#string manipulation and text generation
import random

#set up the constants
OBJECT_PRONOUNS = ['Her','Him', 'Them']
POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
          'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
          'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
          'Plastic Straw','Serial Killer', 'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
           'Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']

def main():
    print('Clickbait headline generator')
    print('By Al Sweigart')
    print()

    while True:
        print('Enter the number of clickbait headlines to generate:')
        response = input('> ')
        # if response.isdecimal() and (0 < int(response) <= 100):
        if not response.isdecimal():
            print('Please enter a valid number of clickbait headlines')
        else:
            numClickbait = int(response)
            break

    for i in range(numClickbait):
        clickbaitType = random.randint(1, 8)

        if clickbaitType == 1:
            headline = generateAreMillenisKillingHeadline()
        if clickbaitType == 2:
            headline = generateWhatYouDontKnowHeadline()
        if clickbaitType == 3:
            headline = generateBigCompaniesHateHerHeadline()
        if clickbaitType == 4:
            headline = generateYouWontBelieveHeadline()
        if clickbaitType == 5:
            headline = generateDontWantYouToKnowHeadline()
        if clickbaitType == 6:
            headline = generateGiftIdeaHeadline()
        if clickbaitType == 7:
            headline = generateReasonsWhyHeadline()
        if clickbaitType == 8:
            headline = generateJobAutomatedHeadline()

        print(headline)
    print()

    website = random.choice(['Wobsite', 'Blog', 'Facebook', 'Googles',
                            'X',' Tweedie','Instagram'])
    when = random.choice(WHEN).lower()
    print('Post these to our', website, when, 'or you\'re fired!')

#each of these functions returns a different type of headline
def generateAreMillenisKillingHeadline():
    noun = random.choice(NOUNS)
    return 'Are Millennials killing the {} Industry?'.format(noun)

def generateWhatYouDontKnowHeadline():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return 'Without this {}, {} Could kill you {}'.format(noun, pluralNoun, when)

def generateBigCompaniesHateHerHeadline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return 'Big Companies hate {}! See how this {} {} Invented a cheaper {}'.format(pronoun, state, noun1, noun2)

def generateYouWontBelieveHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESIVE_PRONOUNS)
    place = random.choice(PLACES)
    return 'You won\'t believe what this {} {} found in {} {}'.format(state, noun, pronoun, place)

def generateDontWantYouToKnowHeadline():
    pluralNoun1 = random.choice(NOUNS) + 's'
    pluralNoun2 = random.choice(NOUNS) + 's'
    return 'What {} don\'t want you to know about {}'.format(pluralNoun1, pluralNoun2)

def generateGiftIdeaHeadline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return '{} gift ideas to give your {} from {}'.format(number, noun, state)

def generateReasonsWhyHeadline():
    number1 = random.randint(3, 19)
    pluralNoun = random.choice(NOUNS) + 's'
    #number 2 should be no larger than number 1
    number2 = random.randint(1, number1)
    return '{} Reasons why {} are more interesting than you think (Number {} will surprise you!'.format(number1, pluralNoun, number2)

def generateJobAutomatedHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0, 2)
    pronoun1 = POSSESIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]

    if pronoun1 == 'Their':
        return 'This {} {} didn\'t think robots would take {} job. {} were wrong.'.format(state, noun, pronoun1, pronoun2)
    else:
        return 'This {} {} didn\'t think robots would take {} job. {} was wrong.'.format(state, noun, pronoun1, pronoun2)

if __name__ == '__main__':
    main()

