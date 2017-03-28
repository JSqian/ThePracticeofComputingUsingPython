import csv
readFileObj = open('grades.csv','rU')
csvReader = csv.reader(readFileObj)

sheet = []
for row in csvReader:
    sheet.append(row)
readFileObj.close()

sheet[3][3] = '100.00'

theSum = 0
for fieldStr in sheet[3][1:-1]:
    theSum += float(fieldStr)
avg = theSum/3
sheet[3][4] = '%.2f' % avg

theSum = 0
for row in sheet[1:-2]:
    theSum += float(row[-1])
gradeAverage = theSum / 4
sheet[-1][-1] = '%.2f' % gradeAverage

writeFileObj = open('NewGrades.csv','w')
writer = csv.writer(writeFileObj)
for row in sheet:
    writer.writerow(row)
writeFileObj.close()
