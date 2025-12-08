import datetime

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December')

print('Calendar maker')

while True:
    print('Enter the year of the calendar')
    responseCal = input('> ')

    if responseCal.isdecimal() and int(responseCal) > 0:
        year = int(responseCal)
        break
    else:
        print('Please enter a valid year, Ex: 2023')
        continue

while True:
    try:
        print('Enter the month of the calendar, 1-12')
        responseMon = input('> ')
        month = int(responseMon)

        if month in range(1, 13):
            break
        else:
            print('Please enter a valid month, Ex: 1 for January')
            continue
    except ValueError:
        print('Please enter a valid month, Ex: 1 for January')

def getCalendarFor(year, month):
    calText = '' #will contain the string of our calendar

    #put the month and year at the top of the calendar
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

    #add the days of the week labels to the calendar:
    calText += '.....SUN........MON.......TUE........WED........THD..........FR.......SAT.....\n'

    #The horizontal line string that separate weeks
    weekSeparator = ('+----------' * 7) + '+\n'

    #The blank rows have ten spaces in between the | day separators:
    blankRow = ('|          ' * 7) + '|\n'

    #Get the first date in the month
    currentDate = datetime.date(year, month, 1)

    #Roll back currentDate until it is Sunday
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:
        calText += weekSeparator

        #dayNumberRow is the row with the day number labels
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' '*8)
            currentDate += datetime.timedelta(days=1) # Go to next day
        dayNumberRow += '\n' #Add vertical line after Saturday

        #Add the day number row and 3 blank rows to the calendar text
        calText += dayNumberRow
        for i in range(3):
            calText += blankRow

        # check if we're done with the month
        if currentDate.month != month:
            break

    #add the horizonal line at the very bottom of the calendar
    calText += weekSeparator
    return  calText

calText = getCalendarFor(year, month)
print(calText) #Display the calendar

#Save the calendar to a text file:
calendarFilename = 'calendar_{}_{}.txt'.format(year, month)
with open(calendarFilename, 'w') as fileObject:
    fileObject.write(calText)

print('Saved to ' + calendarFilename)