
# coding: utf-8

# In[7]:

import csv
import os
import unicodecsv


# remove comma from the tables
def cleanData(data):
    dict={} #list of wiki page IDs
    for row in data:
        for i in range (0,len(row)): #clean the data
           # row[i]=row[i].replace(',', '-')
            if row[0] in dict: #delete double values
                row[0]="NULL"
                break
            try:
                row[i] = unicode(row[i], "utf-8")
            except:
                row[0]="NULL"
                break
            if row[i]=="" or row[i]==" ": #clean out defected rows
                row[0]="NULL"
                break
            dict.update(row[0])
    return data


# clean file in the dir
def cleanFile (filename,withID):
    dirpath="DataTables"
    filepath=dirpath+"/"+filename
    with open(filepath) as f:
        data = list(csv.reader(f))
        f.close
    data=cleanData(data)
    data.reverse
    newdirpath="DataTablesClean"
    filepath=newdirpath+"/"+filename
    with open(filepath,'w') as f:
        j=0
        for row in data:
            if row[0]!="NULL":
                for i in range(0,len(row)):
                    item = row[i]
                    f.write(item.encode('utf8'))
                    f.write(',')
                if withID:
                    if j==0:
                        f.write('ID\n')    
                    else:
                        f.write('%d\n' % j)
                    j+=1
                else:
                    f.write('\n')
        f.close()



