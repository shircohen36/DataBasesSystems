
# coding: utf-8

# In[68]:

import csv
import os


# In[69]:

# check type of values in each coulumn
def checkType(data):
    newData=list(data)
    valueTypeArray=newData.pop(0)
    valueTypeArray=["int" for i in range (0,len(valueTypeArray))]
    for row in newData:
        for i in range (0,len(row)):
            item=row[i]
            try: 
                int(item)
            except ValueError:
                valueTypeArray[i]="string" 
    return valueTypeArray


# In[70]:

# write the sql file from data file
def writeDataSqlFile(data,tableName,valueTypeArray):
    dirpath="SQL_DB"
    filepath=dirpath+'/'+tableName+".sql"
    with open(filepath,'w') as f:
        f.write("CREATE TABLE %s (\n" % tableName)
        headline=data.pop(0)
        
        # create table
        for i in range (0,len(headline)):
            item=headline[i]
            item=item.replace(" ","_")
            if "int" in valueTypeArray[i]:
                f.write("\t%s INT,\n" % item)
            else:
                if "comment" in item or "discription" in item:
                    f.write("\t%s VARCHAR(8000) CHARACTER SET utf8,\n" % item)
                elif item=="name":
                    f.write("\t%s VARCHAR(2000) NOT NULL CHARACTER SET utf8,\n" % item)
                else:
                    f.write("\t%s VARCHAR(2000) CHARACTER SET utf8,\n" % item)
        f.write("\tPRIMARY KEY (ID),\n")
        f.write("\tUNIQUE (name)\n")
        f.write(");\n")
        
        # insert values to table
        for row in data:
            f.write("INSERT INTO %s VALUES (" % tableName)
            for i in range (0,len(row)):
                item=row[i]
                item=item.replace("\'","\''")
                if "int" in valueTypeArray[i]:
                    item=int(item)
                    f.write("%d" % item)
                else:
                    f.write('\'')
                    f.write("%s" % item)
                    f.write('\'')
                if i<len(headline)-1:
                    f.write(",")
            f.write(");\n")
        f.close


# In[ ]:

# write the sql file from match file
def writeMatchSqlFile(data,tableName,valueTypeArray):
    dirpath="SQL_DB"
    filepath=dirpath+'/'+tableName+".sql"
    with open(filepath,'w') as f:
        f.write("CREATE TABLE %s (\n" % tableName)
        headline=data.pop(0)
        
        # create table
        for i in range (0,len(headline)):
            item=headline[i]
            item=item.replace(" ","_")
            if "int" in valueTypeArray[i]:
                f.write("\t%s INT\n" % item)
            else:
                f.write("\t%s VARCHAR(2000) CHARACTER SET utf8\n" % item)
            refTable=item.split("_ID")[0]
            f.write("\t\tREFERENCES %s(ID)" % refTable)
            if i<len(headline)-1:
                 f.write (',\n')
            else:
                f.write ('\n')
        f.write(");\n")
        
        # insert values to table
        for row in data:
            f.write("INSERT INTO %s VALUES (" % tableName)
            for i in range (0,len(row)):
                item=row[i]
                item=item.replace("\'","\''")
                if "int" in valueTypeArray[i]:
                    item=int(item)
                    f.write("%d" % item)
                else:
                    f.write('\'')
                    f.write("%s" % item)
                    f.write('\'')
                if i<len(headline)-1:
                    f.write(",")
            f.write(");\n")
        f.close


# In[71]:

# create tables from dir
def createDataTable(dirpath):
    for filename in os.listdir(dirpath):
        filepath=dirpath+'/'+filename
        tableName=filename.split('.csv')[0]
        with open(filepath) as f:
            data = list(csv.reader(f))
            data.reverse
            f.close
        valueTypeArray=checkType(data)
        writeDataSqlFile(data,tableName,valueTypeArray)                  


# In[ ]:

# create tables from dir
def createMatchTable(dirpath):
    for filename in os.listdir(dirpath):
        filepath=dirpath+'/'+filename
        tableName=filename.split('.csv')[0]
        with open(filepath) as f:
            data = list(csv.reader(f))
            data.reverse
            f.close
        valueTypeArray=checkType(data)
        writeMatchSqlFile(data,tableName,valueTypeArray)    


# In[ ]:

# write index file
def createIndex(dirpath):
        indexpath="SQL_DB/TablesIndex.sql"
        with open(indexpath,'w') as f:
            for filename in os.listdir(dirpath):
                tableName=filename.split('.csv')[0]
                f.write("CREATE INDEX nameIndex ON %s(name);\n" % tableName)
            f.close       

