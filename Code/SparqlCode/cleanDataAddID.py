# coding: utf-8

import csv
import os
import unicodecsv
from sets import Set

# remove comma from the tables
def cleanData(data):
    idKeys=Set() #list of wiki page IDs
    headline=data[0]
    for row in data:
        if (row[0] in idKeys) or (len(row)!=len(headline)): #delete double values and defected rows
            row[0]="NULL"
        else:
            idKeys.add(row[0])
    return data


# clean file in the dir
def cleanFunc(filePath,outputPath,withID):
    with open(filePath) as f:
        data = list(csv.reader(f))
        f.close
    data=cleanData(data)
    headline=data[0]
    with open(outputPath,'w') as f:
        j=0
        for row in data:
            if row[0]!="NULL":
                for i in range(0,len(headline)-1):
                    item = row[i]
                    f.write("{0}".format(item))
                    if i<(len(headline)-2):
                        f.write(',')
                if withID:
                    if j==0:
                        f.write(',ID\n')
                    else:
                        f.write(',%d\n' % j)
                    j+=1
                else:
                    f.write('\n')
        f.close()

def cleanFile(fileName,withID):
    filePath="DataTables"+"/"+fileName+".csv"
    outputPath="DataTablesClean"+"/"+fileName+".csv"
    cleanFunc(filePath,outputPath,withID)
    cleanFunc(outputPath,outputPath,withID)