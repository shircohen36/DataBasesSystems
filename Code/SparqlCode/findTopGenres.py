
# coding: utf-8

# In[62]:

import numpy as np
import csv
import os
from collections import OrderedDict

dictDer=OrderedDict()
dictFus=OrderedDict()
dictOrg=OrderedDict()
dictSub=OrderedDict()

topGenres=['Pop','Rock','Classical','Metal','Hip hop','Rap','Reggae','Jazz','House','Folk','Country','Disco','Soul','Techno',
           'Blues','A cappella','Afro','African','Acid','New age','New wave']

def insertToDict (filepath,dict):
    with open(filepath) as f:
        data = list(csv.reader(f))
        f.close
    headline=data.pop(0)
    for row in data:
        try:
            name=row[0]
            match=row[1]
            if name not in dict:
                dict[name]=[match]
            else:
                dict[name].append(match)
        except:
            print ("Error: defected row!\n")
            print(row)
            exit(0)
    return dict


def addTopGenre(rowGenre):
    genStr='{'
    for genre in topGenres:
        addTG=False
        if genre in rowGenre: #genre in the name of the row's genre
            addTG=True
        elif rowGenre in dictOrg: # MusicalGenre->[OrgGenres]
            for value in dictOrg[rowGenre]:
                if genre in value: #if one of the origins has the genres name
                    addTG=True
                    break
        else:
            for key in dictSub: # MusicalGenre->[SubGenres]
                if genre in key and rowGenre in dictSub[key]: #if the genre in one of the Org, and the row in his childrens
                    addTG=True
                    break
        if addTG:
            genStr+=("{0}|".format(genre))

    genStr+='}'
    genStr=genStr.replace("|}","}")
    return genStr


def createTopGenre():
    filepath="DataTables\MusicGenre.csv"
    with open(filepath) as f:
        data = list(csv.reader(f))
        f.close
    headline=data.pop(0)

    insertToDict("RelationTables/MusicGenre_MusicDerivativeGenre.csv",dictDer)
    insertToDict("RelationTables/MusicGenre_MusicFusionGenre.csv",dictFus)
    insertToDict("RelationTables/MusicGenre_MusicStylisticOriginGenre.csv",dictOrg)
    insertToDict("RelationTables/MusicGenre_MusicSubGenre.csv",dictSub)

    nameIdx=-1
    for i in range(0,len(headline)):
        if headline[i]=="name":
            nameIdx=i
    if nameIdx<0:
        print("Error: headline not as expected!\n")
        print(headline)
        exit(0)

    filepath="DataTables\MusicGenreTop.csv"
    with open(filepath,'w') as f:
        for item in headline:
            f.write("{0},".format(item))
        f.write("topGenre,\n")
        for row in data:
            for item in row:
                f.write("{0},".format(item))
            topGenreRow=addTopGenre(row[nameIdx])
            f.write("{0}\n".format(topGenreRow))
        f.close

createTopGenre()