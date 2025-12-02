#math, simulation
import datetime, random
from http.cookiejar import MONTHS


def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(numberOfBirthdays):
        #The year is unimportant
        startOfYear = datetime.date(1994,1,1)

        randomNumberOfDays = datetime.timedelta(random.randrange(1,366))
        # birthdays = startOfYear + randomNumberOfDays
        # birthdays.append(birthdays)
        birthdays.append(startOfYear + randomNumberOfDays)
    return birthdays

def getMatch(birthdays):
    """Returns a list of number random date objects for birthdays."""
    if len(birthdays) == len(set(birthdays)):
        return None # All birthdays are uniques

    #compare each birthdays
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA #return the matching birthday

#Display the intro:
print('''Birthday Paradox, by AL Sweigart''')

# Set up tuple of month names in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('How many birthdays shall i generate? (MAX 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break # User has entered a valid amount
print()

#Generate and display the birthdays
print('here are', numBDays, 'birthdays')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, str(birthday))
    print(dateText, end='')
print()
print()

# Determine if there are two birthdays that match
match = getMatch(birthdays)

# Display the results:
print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dataText = '{} {}'.format(monthName, str(match.day))
    print('Multiple people have a birthday on ', dataText, end='')
else:
    print('There are no matching birthdays')
print()

# Run through 100 simulations
print('Generating', numBDays, 'random dates')
input('Press enter to begin..')

print('Lets run another simulation')
simMatch = 0
for i in range (100):
    if i % 10 == 0:
        print(i, 'simulations run...')
    birthdays = getBirthdays(numBDays)

    if getMatch(birthdays) != None:
        simMatch += 1
print('100 simulations run.')
# Display simulation results:
probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')