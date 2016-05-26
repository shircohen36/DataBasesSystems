
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
           'Blues','A cappella','Afro','African','Acid','New age','New wave','Gospel','Apala','Ambient','Hardcore','Latin',
           'Punc','Punk','Funk','Tradition','World','Electro','Swing','Industrial','Samba','Noise','Groov','Dance','Chant','Soca',
           'National','Thrash','Soundtrack','Lo-fi','Ancient','Religio','Prayer','Garage','Wedding','Experimental','Boogie',
           'Calypso','Celtic','Indie','Indo']

def insertToDict (filepath,dict):
    with open(filepath) as f:
        data = list(csv.reader(f))
        f.close
    headline=data.pop(0)
    for row in data:
        try:
            name=row[0].lower()
            match=row[1].lower()
            if name not in dict:
                dict[name]=[match]
            else:
                dict[name].append(match)
        except:
            print ("Error: defected row!\n")
            print(row)
            exit(0)
    return dict


def addTopGenre(rowGenre,rowComm):
    genStr=[]
    for genre in topGenres:
        addTG=False
        orgGenre=genre
        genre=genre.lower()
        rowGenre=rowGenre.lower()
        rowComm=rowComm.lower()
        if genre in rowGenre or genre in rowComm: #genre in the name of the row's genre
            addTG=True
        if addTG==False and rowGenre in dictOrg: # MusicalGenre->[OrgGenres]
            for value in dictOrg[rowGenre]:
                if genre in value : #if one of the origins has the genres name
                    addTG=True
                    break
        if addTG==False:
            for key in dictSub: # MusicalGenre->[SubGenres]
                if genre in key and rowGenre in dictSub[key]: #if the genre in one of the Org, and the row in his childrens
                    addTG=True
                    break
        if addTG==False:
            for key in dictDer:
                if (genre in key and rowGenre in dictDer[key]) or (rowGenre in key and genre in dictDer[key]):
                    addTG=True
                    break

        if addTG==False:
            for key in dictFus:
                if (genre in key and rowGenre in dictFus[key]) or (rowGenre in key and genre in dictFus[key]):
                    addTG=True
                    break
        if addTG:
            genStr.append(orgGenre)
    return genStr

def fixGenre(item):
    if item == "Groov":
        return "Groove"
    if item == "Tradition" or item == "Ancient" or item == "Wedding":
        return "Traditional"
    if item == "Lo-fi":
        return "Experimental"
    if item == "Religio" or item=="Prayer":
        return "Religious"
    if item == "Punc":
        return "Punk"
    if item=="Garage" or item == "Thrash":
        return "Rock"
    if item == "Afro":
        return "African"
    if item == "Elctro":
        return "Electronic"
    if item == "Indo":
        return "Indie"
    if item == "Soca":
        return "Caribbean"
    return item



def createTopGenre():

    filepath="DataTables/MusicGenreTop.csv"
    with open (filepath,'w') as f:
      f.write("name,\n")
      for genre in topGenres:
          genre=fixGenre(genre)
          f.write("{0},\n".format(genre))
    f.close()

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
        if headline[i]=="comment":
            commIdx=i
    if nameIdx<0 or commIdx<0:
        print("Error: headline not as expected!\n")
        print(headline)
        exit(0)

    # filepath="DataTables\MusicGenreTop.csv"
    # with open(filepath,'w') as f:
    #     for item in headline:
    #         f.write("{0},".format(item))
    #     f.write("topGenre,\n")
    #     for row in data:
    #         for item in row:
    #             f.write("{0},".format(item))
    #         topGenreRow=addTopGenre(row[nameIdx],row[commIdx])
    #         for item in topGenreRow:
    #           f.write("{0},".format(item))
    #           f.write("\n")
    #     f.close

    filepath="RelationTables\MusicGenre_MusicGenreTop.csv"
    with open(filepath,'w') as f:
        f.write("MusicGenre,TopGenre\n")
        for row in data:
            topGenreRow=addTopGenre(row[nameIdx],row[commIdx])
            if len(topGenres)==0:
                f.write("{0},International\n".format(row[nameIdx],item))
            for item in topGenreRow:
                item=fixGenre(item)
                f.write("{0},{1}\n".format(row[nameIdx],item))
        f.write("Classical music composition,Classical\n")
        f.close