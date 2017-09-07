import csv


def writeOnCSV(Array):
    with open('Inof.csv', 'a', newline='') as csvfile:

        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(Array)
        print('Write on .csv')

def checkLast():
    with open('Inof.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        lastUrl = []
        for row in spamreader:
            #print(row[0])
            #print("-------------------")
            lastUrl.append(row[0])
    return lastUrl
