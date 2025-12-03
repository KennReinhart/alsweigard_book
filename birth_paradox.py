#math, simulation
import datetime, random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

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


def visualize_heatmap(birthdays):
    '''Draws a heatmap (Month x Day) of all birthdays.'''
    grid = np.zeros((12,31))

    for b in birthdays:
        grid[b.month - 1][b.day - 1] += 1

    plt.figure(figsize=(14,6))
    img = plt.imshow(grid, cmap="viridis", aspect="auto")
    cbar = plt.colorbar(img)
    cbar.locator = ticker.MaxNLocator(integer=True)
    cbar.update_ticks()

    plt.title("Birthdays Heatmap")

    plt.xlabel("Day of Month")
    plt.xticks(
        ticks=range(31),
        labels=[str(d+1) for d in range(31)],
        rotation=90
    )
    plt.ylabel("Month")
    plt.yticks(np.arange(len(MONTHS)), MONTHS)
    plt.tight_layout()
    plt.show()

#Generate and display the birthdays
def main():
    while True:
        while True:
            print('How many birthdays shall i generate? (MAX 100)')
            response = input('> ')
            if response.isdecimal() and (0 < int(response) <= 100):
                numBDays = int(response)
                break  # User has entered a valid amount

        print('here are', numBDays, 'birthdays')
        birthdays = getBirthdays(numBDays)

        for i, birthday in enumerate(birthdays):
            month = MONTHS[birthday.month - 1]
            if i > 0:
                print(", ", end="")
            print(f"{month} {birthday.day}", end="")
        print("\n")

        print("Do you want to visualize these birthdays? (y/n)")
        if input('> ').lower().startswith('y'):
            visualize_heatmap(birthdays)

        matches = getAllMatches(birthdays)
        if matches:
            print()
            for day, count in matches.items():
                month = MONTHS[day.month - 1]
                print(f"    {count} people have a birthday on {month} {day.day}")
                probability = count / len(birthdays)
                print(f"    it was {probability * 100:.2f}% of the time \n")
        else:
            print('There are no matching birthdays')

        print('Do you want to play again? (y/n)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thankyou for playing!')

if __name__ == '__main__':
    main()