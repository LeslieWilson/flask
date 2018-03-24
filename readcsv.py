import csv
import collections import Counter

with open ('Data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    array = []
    for row in reader:
        for column in row:
            array.append(column)
    c = Counter(array)
csvfile.close()
data = open('Data.txt', 'w')
data.write('%d\nName %d\nDepartment %d\nEthnicity %d\nGender %d\nEducation Level %n\nUniversity %d\nMajor %d\n1990 %d\n1991 %d\n1992 %d\n1993 %d\n2000 %d\n2001) % (c['1990'] (c['1991'] c['1992'] c['1993'] c['2000']),c['2001']))
data.close()
