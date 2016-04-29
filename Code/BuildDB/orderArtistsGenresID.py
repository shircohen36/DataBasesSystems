
# coding: utf-8

# In[13]:

import csv


# In[8]:

# add id to rows

filepath ="MusicGenre.csv"
with open(filepath) as f:
    data = list(csv.reader(f))
    f.close
data.reverse
newfile="MusicGenre_id.csv"
with open(newfile,'w') as f:
    i=0
    for row in data:
        for item in row:
            f.write('%s,' % item)
        f.write('%d\n' % i)
        i+=1
    f.close()


# In[22]:

# load genre:id to dict

filepath ="MusicGenre_id.csv"
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


# In[35]:

# write row to file 'f'
def writeRow (f,row):
    for i in range (0,len(row)):
        if (i<len(row)-1):
            f.write('%s,' % row[i])
        else:
            f.write('%s\n' % row[i])    


# In[36]:

# write artist's genres by 'id' in split rows
filepath ="MusicalArtist.csv"
with open(filepath) as f:
    data = list(csv.reader(f))
    f.close
data.reverse
headline=data.pop(0)
for i in range (0,len(headline)):
    if headline[i]=="genre_label":
        gInx=i
filepath ="MusicalArtist_id.csv"
with open(filepath,'w') as f:
    writeRow(f,headline)
    for row in data:
        if row[gInx]!="NULL":
            if "{" in row[gInx]:
                genre=row[gInx].split("{",1)[1]
            if "}" in genre:
                genre=genre.split("}",1)[0]
            if "|" in genre:
                genre=genre.split("|",1)
                for item in genre:
                    tempRow=row
                    if item in dict:
                        idg=int(dict[item])
                    else:
                        idg=0
                    tempRow[gInx]=idg
                    writeRow(f,tempRow)
        else:
            writeRow(f,row)
    f.close


# In[ ]:



