def weightedGrade(gradeLst,weights=(0.3,0.3,0.4)):
    '''Expects 3 elements in gradeLst. Multiples each grade
    by its weight. Returns the sum.'''
    result = \
           (gradeLst[0]*weights[0])+\
           (gradeLst[1]*weights[1])+\
           (gradeLst[2]*weights[2])
    return result

def grade(fileLine):
    '''Expects a line of form last,first,exam1,exam2,final.
    returns first + last and a final grade.'''
    fieldLst = fileLine.split(',')
    name = fieldLst[1] + ' ' + fieldLst[0]
    grades = []
    for element in fieldLst[2:]:
        grades.append(int(element))
    theGrade = weightedGrade(grades)
    return name,theGrade

def main():
    '''Get a line from the file,print the final grade nicely'''
    fileName = raw_input('Open what file:')
    fileObj = open(fileName,'r')
    print '%-15s %-15s' % ('Name','Grade')
    print '-'*25
    for line in fileObj:
        line = line.strip()
        print '%-15s %7.2f' % grade(line)
