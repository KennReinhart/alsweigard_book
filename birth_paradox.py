#math, simulation
import datetime, random

def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    start = datetime.date(1994, 1, 1)
    for i in range(numberOfBirthdays):
        offset = datetime.timedelta(random.randrange(1,365))
        # birthdays = startOfYear + randomNumberOfDays
        # birthdays.append(birthdays)
        birthdays.append(start + offset)
    return birthdays

def getMatch(birthdays):
    seen = set()
    for b in birthdays:
        if b in seen:
            return b
        seen.add(b)
    return None

#Display the intro:
print('''Birthday Paradox, by AL Sweigart''')

# Set up tuple of month names in order:
MONTHS = ('January', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('How many birthdays shall i generate? (MAX 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break # User has entered a valid amount

#Generate and display the birthdays
print('here are', numBDays, 'birthdays')
birthdays = getBirthdays(numBDays)

for i, birthday in enumerate(birthdays):
    month = MONTHS[birthday.month - 1]
    if i > 0:
        print(", ", end="")
    print(f"{month} {birthday.day}", end="")
print("\n")

# Determine if there are two birthdays that match
match = getMatch(birthdays)

# Display the results:
print('In this simulation, ', end='')
if match:
    month = MONTHS[match.month - 1]
    print(f"Multiple people have a birthday on {month} {match.day}")
else:
    print('There are no matching birthdays')
print()

# Run through 100 simulations
print('Generating', numBDays, 'random dates')
input('Press enter to begin..')

print('Lets run another simulation')
simMatch = 0
SIMS = 100_000

for i in range (SIMS):
    if i % 10_000 == 0:
        print(i, 'simulations run...')
    if getMatch(birthdays = getBirthdays(numBDays)):
        simMatch += 1
# Display simulation results:
probability = simMatch / SIMS * 100

print("\n100,000 simulations complete.")
print(f"Out of {SIMS} simulations of groups of {numBDays} people:")
print(f"- {simMatch} had matching birthdays.")
print(f"- Estimated probability: {probability:.2f}%")