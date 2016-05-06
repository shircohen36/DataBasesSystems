
# coding: utf-8

# In[68]:

import csv
import os


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
                if valueTypeArray[i]==0:
                    valueTypeArray[i]=1
                valueTypeArray[i]=max(valueTypeArray[i],len(item)) 
    return valueTypeArray


# In[70]:

# write the sql file from data file
def writeDataSqlFile(f,data,tableName,valueTypeArray):
    
    f.write("CREATE TABLE %s (\n" % tableName)
    headline=data.pop(0)
        
    # create table
    for i in range (0,len(headline)):
        item=headline[i]
        item=item.replace(" ","_")
        if valueTypeArray[i]==0:
            f.write("\t%s INT,\n" % item)
        else:
            if "comment" in item or "discription" in item or valueTypeArray[i]>1500:
                f.write("\t%s TEXT,\n" % item)
            elif item=="name":
                valueTypeArray[i]+=16
                f.write("\t{0} VARCHAR({1}) NOT NULL,\n".format(item,valueTypeArray[i]))
            else:
                valueTypeArray[i]+=16
                f.write("\t{0} VARCHAR({1}),\n".format(item, valueTypeArray[i]))
    f.write("\tPRIMARY KEY (ID)\n")
    f.write(");\n")
        
    # insert values to table
    for row in data:
        f.write("INSERT INTO %s VALUES (" % tableName)
        for i in range (0,len(row)):
            item=row[i]
            item=item.replace("\'","\''")
            if valueTypeArray[i]==0:
                item=int(item)
                f.write("%d" % item)
            else:
                f.write('\'')
                f.write("%s" % item)
                f.write('\'')
            if i<len(headline)-1:
                f.write(",")
        f.write(");\n")


# In[ ]:

# write the sql file from match file
def writeMatchSqlFile(f,data,tableName,valueTypeArray):
   
    f.write("CREATE TABLE %s (\n" % tableName)
    headline=data.pop(0)
        
    # create table
    for i in range (0,len(headline)):
        item=headline[i]
        item=item.replace(" ","_")
        f.write("\t%s INT\n" % item)
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
            item=int(item)
            f.write("%d" % item)
            if i<len(headline)-1:
                f.write(",")
        f.write(");\n")


# In[71]:

# create tables from dir
def createDataTable(f,dirpath):
    for filename in os.listdir(dirpath):
        filepath=dirpath+'/'+filename
        tableName=filename.split('.csv')[0]
        with open(filepath) as f2:
            data = list(csv.reader(f2))
            data.reverse
            f2.close
        valueTypeArray=checkType(data)
        writeDataSqlFile(f,data,tableName,valueTypeArray)                  


# In[ ]:

# create tables from dir
def createMatchTable(f,dirpath):
    for filename in os.listdir(dirpath):
        filepath=dirpath+'/'+filename
        tableName=filename.split('.csv')[0]
        with open(filepath) as f2:
            data = list(csv.reader(f2))
            data.reverse
            f2.close
        valueTypeArray=checkType(data)
        writeMatchSqlFile(f,data,tableName,valueTypeArray)    


# In[ ]:

# write index file
def createIndex(f,dirpath):
        for filename in os.listdir(dirpath):
            tableName=filename.split('.csv')[0]
            f.write("CREATE INDEX nameIndex ON %s(name);\n" % tableName)       


# In[ ]:

# write all DB building queries into one SQL_DB file
def createSQLTables(dir1, dir2,dir3):
    outputPath="SQL_DB/AllTablesDB.sql"
    with open(outputPath,'w') as f:
    #    f.write("DROP SCHEMA IF EXISTS music\n");
    #    f.write("CREATE SCHEMA music\n");
    #    f.write("USE music\n");
    #   f.write("\n")
    #    f.write("set global innodb_file_format = Barracuda;\n")
    #    f.write("set global innodb_file_per_table = 1;\n")
    #    f.write("\n")
        createDataTable(f,dir1)
        f.write("\n")
        createMatchTable(f,dir2)
        f.write("\n")
        createIndex(f,dir3)
        f.close

