
# coding: utf-8

# In[36]:

import csv


# In[37]:

# load genre:id to dict

filepath ="ExcelOntologyTablesForDB/MusicGenre_withID.csv"
with open(filepath) as f:
    data = list(csv.reader(f))
    f.close
data.reverse
dict={}
headline=data.pop(0)
labelIndex=0
idIndex=0
for i in range (0,len(headline)):
    if headline[i]=="label":
        labelIndex=i
    if headline[i]=="ID":
        idIndex=i
for row in data:
    temp={row[labelIndex]:row[idIndex]}
    dict.update(temp)


# In[38]:

# write row to file 'f'
def writeRow (f,row,insertname,index):
    for i in range (0,len(row)):
        if (i<len(row)-1):
            f.write('%s,' % row[i])
        else:
            f.write('%s\n' % row[i]) 
        if i==index: #write the genre name that fits this ID
            f.write('%s,' % insertname)


# In[39]:

# write artist's genres by 'id' in split rows
filepath ="ExcelOntologyTablesClean/MusicalArtist.csv"
with open(filepath) as f:
    data = list(csv.reader(f))
    f.close
data.reverse
headline=data.pop(0)
for i in range (0,len(headline)):
    if headline[i]=="genre_label":
        gInx=i
        headline[i]="genre_ID"
filepath ="ExcelOntologyTablesForDB/MusicalArtist_genreByID.csv"
with open(filepath,'w') as f:
    writeRow(f,headline,"genre_name",gInx)
    for row in data:
        if row[gInx]!="NULL":
            genre=row[gInx]
            if "{" in genre:
                genre=genre.split("{")[1]
            if "}" in genre:
                genre=genre.split("}")[0]
            if "|" in genre:
                genre=genre.split("|")
                for item in genre:
                    tempRow=row
                    if item in dict:
                        idg=int(dict[item])
                    else:
                        idg=0
                    tempRow[gInx]=idg
                    writeRow(f,tempRow,item,gInx)
            else:
                tempRow=row
                if genre in dict:
                    idg=int(dict[genre])
                else:
                    idg=0
                tempRow[gInx]=idg
                writeRow(f,tempRow,genre,gInx)
        else:
            writeRow(f,row,"NULL",gInx)
    f.close


# In[ ]:



