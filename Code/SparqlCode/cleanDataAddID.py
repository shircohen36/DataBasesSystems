
# coding: utf-8

# In[7]:

import csv
import os
import unicodecsv


# In[6]:

# remove comma from the tables
def cleanData(data):
    for row in data:
        for i in range (0,len(row)): #clean the data
           # row[i]=row[i].replace(',', '-')
            try:
                row[i] = unicode(row[i], "utf-8")
            except:
                row[0]="NULL"
                break
    return data


# In[8]:

# clean file in the dir
def cleanFile (filename):
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
                    if (i<len(row)-1):
                        f.write(',')
                if j==0:
                    f.write('ID\n')    
                else:
                    f.write('%d\n' % j)
            j+=1
        f.close()


# In[ ]:



