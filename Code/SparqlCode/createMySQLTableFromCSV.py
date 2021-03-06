
# coding: utf-8

# In[68]:

import csv
import os
import unicodecsv


# In[69]:

# check type of values in each coulumn
def checkType(data):
    newData=list(data)
    valueTypeArray=newData.pop(0)
    valueTypeArray=[0 for i in range (0,len(valueTypeArray))]
    for row in newData:
        for i in range (0,len(row)):
            item=row[i]
            try: 
                int(item)
            except ValueError:
                try:
                    if valueTypeArray[i]==0:
                        valueTypeArray[i]=1
                    valueTypeArray[i]=max(valueTypeArray[i],len(item))
                except:
                    print("Error: defected row. row is too short!\n")
                    print(row)
                    exit(0)
    return valueTypeArray


# In[70]:

# write the sql file from data file
def writeDataSqlFile(fscheme,fdata,data,tableName,valueTypeArray):
    
    fscheme.write("CREATE TABLE {0} (\n".format(tableName))
    headline=data.pop(0)
        
    # create table
    fscheme.write("\tID INT NOT NULL AUTO_INCREMENT,\n")
    for i in range (0,len(headline)-1):
        item=headline[i]
        if valueTypeArray[i]==0:
            fscheme.write("\t{0} INT,\n".format(item))
        else:
            if "comment" in item or "discription" in item or valueTypeArray[i]>1500:
                fscheme.write("\t{0} TEXT,\n".format(item))
            elif item=="name":
                valueTypeArray[i]+=16
                fscheme.write("\t{0} VARCHAR({1}) NOT NULL,\n".format(item,valueTypeArray[i]))
            else:
                valueTypeArray[i]+=16
                fscheme.write("\t{0} VARCHAR({1}),\n".format(item, valueTypeArray[i]))
    fscheme.write("\tPRIMARY KEY (ID)\n")
    fscheme.write(");\n\n")
        
    # insert values to table    
    for row in data:
        printrow=True
        for item in row:
            try: # check encoding of row
                item.encode('utf8')
            except:
                printrow=False
                break
        if printrow:
            fdata.write("INSERT INTO {0} VALUES (NULL,".format(tableName))
            for i in range (0,len(row)-1):
                item=row[i]
                item=item.replace("\'","\''")
                if valueTypeArray[i]==0:
                    item=int(item)
                    fdata.write("%d" % item)
                else:
                    fdata.write('\'')
                    fdata.write(item.encode('utf8'))
                    fdata.write('\'')
                if i<len(headline)-2:
                    fdata.write(",")
            fdata.write(");\n")
    fdata.write("\n")


# In[ ]:

# write the sql file from match file
def writeMatchSqlFile(fscheme,fdata,data,tableName,valueTypeArray):
   
    fscheme.write("CREATE TABLE {0} (\n".format(tableName))
    headline=data.pop(0)
        
    # create table
    for i in range (0,len(headline)):
        item=headline[i]
        fscheme.write("\t{0} INT\n".format(item))
        refTable=tableName.split("_")[i]
        if "Genre" in refTable:
            refTable="MusicGenre"
        fscheme.write("\t\tREFERENCES {0}(ID)".format(refTable))
        if i<len(headline)-1:
            fscheme.write (',\n')
        else:
            fscheme.write ('\n')
    fscheme.write(");\n\n")
        
    # insert values to table

    for row in data:
        fdata.write("INSERT INTO {0} VALUES (".format(tableName))
        for i in range (0,len(row)):
            item=row[i]
            item=int(item)
            fdata.write("%d" % item)
            if i<len(headline)-1:
                fdata.write(",")
        fdata.write(");\n")
    fdata.write("\n")


# In[71]:

# create tables from dir
def createDataTable(fscheme,fdata,dirpath):
    for filename in os.listdir(dirpath):
        filepath=dirpath+'/'+filename
        tableName=filename.split('.csv')[0]
        with open(filepath) as f2:
            data = list(csv.reader(f2))
            data.reverse
            f2.close
        valueTypeArray=checkType(data)
        writeDataSqlFile(fscheme,fdata,data,tableName,valueTypeArray)                  


# In[ ]:

# create tables from dir
def createMatchTable(fscheme,fdata,dirpath):
    for filename in os.listdir(dirpath):
        filepath=dirpath+'/'+filename
        tableName=filename.split('.csv')[0]
        with open(filepath) as f2:
            data = list(csv.reader(f2))
            data.reverse
            f2.close
        valueTypeArray=checkType(data)
        writeMatchSqlFile(fscheme,fdata,data,tableName,valueTypeArray) 


# In[ ]:

# write index file
def createIndex(f,dirpath):
        for filename in os.listdir(dirpath):
            field="name"
            tableName=filename.split('.csv')[0]
            if "Classical" in filename:
                field="cname"
            f.write("CREATE INDEX nameIndex ON {0}({1});\n".format(tableName,field))


# In[ ]:

# write all DB building queries into one SQL_DB file
def createSQLTables(dir1 ,dir2 ,dir3):
    outputSchemePath="SQL_DB/musicDB_schema.sql"
    outputDataPath="SQL_DB/musicDB_data.sql"
    with open(outputSchemePath,'w') as fscheme:
        with open(outputDataPath,'w') as fdata:
            createDataTable(fscheme,fdata,dir1)
            createMatchTable(fscheme,fdata,dir2)
            createIndex(fscheme,dir3)
            fdata.close
        fscheme.close