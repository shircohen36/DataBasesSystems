
# coding: utf-8

# In[30]:

import csv
import os


# In[31]:

# remove comma from the tables
def cleanData(data):
    for row in data:
        for i in range (0,len(row)): #clean the data
            row[i]=row[i].replace(',', '-')
    return data


# In[32]:

# clean all files in the given dir
dirpath="ExcelOntologyTables"
for filename in os.listdir(dirpath):
    filepath=dirpath+"/"+filename
    with open(filepath) as f:
        data = list(csv.reader(f))
        f.close
    data=cleanData(data)
    data.reverse
    if "MusicGenre" in filename:
        filepath="ExcelOntologyTablesForDB/MusicGenre_withID.csv"
    else:
        newdirpath="ExcelOntologyTablesClean"
        filepath=newdirpath+"/"+filename
    with open(filepath,'w') as f:
        j=0
        for row in data:
            for item in row:
                f.write('%s,' % item)
            if j==0:
                f.write('ID\n')
            else:
                f.write('%d\n' % j)
            j+=1
        f.close()


# In[ ]:



