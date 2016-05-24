
# coding: utf-8

import csv
import os
import unicodecsv


# remove comma from the tables
def cleanData(data):
    for row in data:
        for i in range (0,len(row)): #clean the data
          #  row[i]=row[i].replace(',', '-')
            try:
                row[i] = unicode(row[i], "utf-8")
            except:
                row[0]="NULL"
                break
    return data


# create one table with ID
def combineTwoWithID(dirpath,outputPath,filename1,filename2,newfilename):
    filepath1=dirpath+"/"+filename1+".csv"
    filepath2=dirpath+"/"+filename2+".csv"
    with open(filepath1) as f:
        data1 = list(csv.reader(f))
        f.close
    with open(filepath2) as f:
        data2 = list(csv.reader(f))
        f.close
    data1=cleanData(data1)
    data2=cleanData(data2)
    data1.reverse
    data2.reverse
    data2.pop(0)
    filepath=outputPath+"/"+newfilename+".csv"
    with open(filepath,'w') as f:
        j=0
        for row in data1:
            if row[0]!="NULL":
                for i in range(0,len(row)):
                    item = row[i]
                    f.write(item.encode('utf8'))
                    if (i<len(row)-1):
                        f.write(',')
                if j==0:
                    f.write('ID\n')
                else:
                    f.write('%d\n' % j)
                j+=1
        for row in data2:
            if row[0]!="NULL":
                for i in range(0,len(row)):
                    item = row[i]
                    f.write(item.encode('utf8'))
                    if (i<len(row)-1):
                        f.write(',')
                f.write('%d\n' % j)
                j+=1
        f.close()

# create one table without ID
def combineTwo(dirpath,outputPath,filename1,filename2,newfilename):
    filepath1=dirpath+"/"+filename1+".csv"
    filepath2=dirpath+"/"+filename2+".csv"
    with open(filepath1) as f:
        data1 = list(csv.reader(f))
        f.close
    with open(filepath2) as f:
        data2 = list(csv.reader(f))
        f.close
    data1=cleanData(data1)
    data2=cleanData(data2)
    data1.reverse
    data2.reverse
    data2.pop(0)
    filepath=outputPath+"/"+newfilename+".csv"
    with open(filepath,'w') as f:
        for row in data1:
            if row[0]!="NULL":
                for i in range(0,len(row)):
                    item = row[i]
                    f.write(item.encode('utf8'))
                    if (i<len(row)-1):
                        f.write(',')
        for row in data2:
            if row[0]!="NULL":
                for i in range(0,len(row)):
                    item = row[i]
                    f.write(item.encode('utf8'))
                    if (i<len(row)-1):
                        f.write(',')
        f.close()
# In[ ]:



