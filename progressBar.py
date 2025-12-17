#it simulates a downloading file

import random, time

BAR = chr(9608)

def main():
    print('Progress Bar simulation')
    bytesDownloaded = 0
    downloadSize = 4096
    while bytesDownloaded < downloadSize:
        bytesDownloaded += random.randint(0, 100)

        barStr = getProgressBar(bytesDownloaded, downloadSize)

        print(barStr, end='', flush=True)
        time.sleep(0.2)

        print('\b' * len(barStr), end='', flush=True)

def getProgressBar(progress, total, barWidth=40):
    progressBar = '' #The progress bar will b e string value
    progressBar += '[' #create the left end of the progress bar

    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    numberOfBars = int((progress/ total)* barWidth)

    progressBar += BAR * numberOfBars #add the progress bar
    progressBar += ' ' * (barWidth - numberOfBars) #add empty space
    progressBar += ']' #add the right end of the progress bar

    percentComplete = round(progress / total * 100, 1)
    progressBar += ' ' + str(percentComplete) + '%'

    #add the numbers:
    progressBar += ' ' + str(progress) + '/' + str(total)

    return progressBar

if __name__ == '__main__':
    main()