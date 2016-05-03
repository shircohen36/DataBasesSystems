
# coding: utf-8

# In[31]:

import csv
dict={}


# In[32]:

# load genre:id to dict

#filepath ="ExcelOntologyTablesForDB/MusicGenre_withID.csv"

def createDictFromFirst (filepath):
    with open(filepath) as f:
        data = list(csv.reader(f))
        f.close
    data.reverse
    headline=data.pop(0)
    labelIndex=0
    idIndex=0
    for i in range (0,len(headline)):
        if headline[i]=="name":
            labelIndex=i
        if headline[i]=="ID":
            idIndex=i
    for row in data:
        temp={row[labelIndex]:row[idIndex]}
        dict.update(temp)


# In[33]:

# write row to new file 'f'
def writeRow (f,dictItem,matchedItem):
    f.write('%s,' % dictItem)
    f.write('%s\n' % matchedItem)


# In[34]:

# write artist's genres by 'id' in split rows

#filepath ="ExcelOntologyTablesClean/MusicalArtist.csv"

def writeMatchFromFileTwo(fileOne,fileTwo,DirOutput,labelsToMatch):
    
    firstname=fileOne.split("/")
    firstname=firstname[len(firstname)-1].split(".csv")[0]

    secondname=fileTwo.split("/")
    secondname=secondname[len(secondname)-1].split(".csv")[0]
    
    fileOutput=DirOutput+"/"+firstname+"_"+secondname+".csv" #output file
    
    firstname=firstname+"_ID"
    secondname=secondname+"_ID"
      
    with open(fileTwo) as f:
        data = list(csv.reader(f))
        f.close
        data.reverse
        headline=data.pop(0)
    
    with open(fileOutput,'w') as f:
        
        writeRow(f,firstname,secondname)
        
        for labelToMatch in labelsToMatch:
            for i in range (0,len(headline)):
                if headline[i]==labelToMatch: #item to match to in first file
                    matchInx=i
                if headline[i]=="ID": #id of row in second file
                    idIndex=i
                  
            for row in data:
                if row[matchInx]!="NULL":
                    match=row[matchInx]
                    if "{" in match:
                        match=match.split("{")[1]
                    if "}" in match:
                        match=match.split("}")[0]
                    if "|" in match:
                        match=match.split("|")
                        for item in match:
                        # if ignorePer: # [name (info)] -> take only name
                            # if " (" in item:
                             #  item=item.split(" (")[0]
                            if item in dict:
                                idmatch=int(dict[item]) #found item in second file take its ID
                            else:
                                idmatch=0 #no match found
                            writeRow(f,idmatch,row[idIndex])
                    else:
                        if match in dict:
                            idmatch=int(dict[match])
                        else:
                            idmatch=0
                        writeRow(f,idmatch,row[idIndex])
                else:
                    writeRow(f,"NULL",row[idIndex]) #NULL in the place to match
        f.close


# In[35]:

# create joined files

def createJoinTableByID(fileOne,fileTwo,DirOutput,labelsToMatch):
    createDictFromFirst(fileOne)
    writeMatchFromFileTwo(fileOne,fileTwo,DirOutput,labelsToMatch)


# In[ ]:



