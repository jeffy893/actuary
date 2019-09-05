import csv
with open('eggs.csv', 'rb') as csvfile:
    read = csv.reader(csvfile, delimiter=',', quotechar='"')
    count = 0
    for row in read:
        if(count > 0):
            print row[0] + ',' + row[1]
        count = count + 1
