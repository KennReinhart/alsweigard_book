#math, simulation
import datetime, random

from collections import Counter

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

def getAllMatches(birthdays):
    counts = Counter(birthdays)
    return {day: c for day, c in counts.items() if c > 1}
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
# match = getMatch(birthdays)
# # Display the results:
# print('In this simulation, ', end='')
# if match:
#     month = MONTHS[match.month - 1]
#     print(f"{count(match.day)} people have a birthday on {month} {match.day}")
# else:
#     print('There are no matching birthdays')

matches = getAllMatches(birthdays)
if matches:
    print()
    for day, count in matches.items():
        month = MONTHS[day.month - 1]
        print(f"  {count} people have a birthday on {month} {day.day}")
        probability = count / len(birthdays)
        print(f" it was {probability * 100:.2f}% of the time")
else:
    print('There are no matching birthdays')