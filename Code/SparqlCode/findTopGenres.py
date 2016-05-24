
# coding: utf-8

# In[62]:

import numpy as np
import csv
import os


# In[63]:

filepath="ExcelOntologyTables\MusicGenre.csv"
with open(filepath) as f:
    data = list(csv.reader(f))
    f.close


# In[64]:

data.reverse
headline=data.pop(0)
i=0
for title in headline:
    if title=='name':
        nameplace=i
    if title =='stylisticOrigin':
        orgplace=i
    if title=='topGenre':
        toplace=i
    i+=1      


# In[65]:

topGenres=['Pop','Rock','Classical','Metal','Hip hop','Rap','Reggae','Jazz','House','Folk','Country','Disco','Soul','Techno',
           'Blues','A cappella','Afro','African','Acid','New age','New wave']


# In[66]:

for row in data:
    row[toplace]='{'
    for genre in topGenres:
        if genre in row[nameplace] or genre in row[orgplace] or genre.lower() in row[nameplace] or genre.lower() in row[orgplace]:
            row[toplace]=row[toplace]+genre+"|"
    row[toplace]=row[toplace]+"}"
    row[toplace]=row[toplace].replace("|}","}")


# In[67]:

filepath="ExcelOntologyTables\MusicGenreTop.csv"
with open(filepath,'w') as f:
    for item in headline:
        f.write("%s," % item)
    f.write("\n")
    for row in data:
        for item in row:
            f.write("%s," % item)
        f.write("\n")
    f.close

