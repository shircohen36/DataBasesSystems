# coding: utf-8

import csv
import os
import unicodecsv
from sets import Set

# remove comma from the tables
def cleanData(data):
    idKeys=Set() #list of wiki page IDs
    headline=data[0]
    for row in data:
        if (row[0] in idKeys) or (len(row)!=len(headline)): #delete double values and defected rows
            row[0]="NULL"
        else:
            idKeys.add(row[0])
    return data

def fixClassicalMusic(filePath,outputPath):
    with open(filePath) as f:
        data = list(csv.reader(f))
        f.close
    headline=data[0]
    urlIdx=-1
    cIdx=-1
    for i in range (0,len(headline)):
        item=headline[i]
        if item=="url":
            urlIdx=i
        if item=="cname":
            cIdx=i
    if urlIdx<0 or cIdx<0:
        print("Error: headline not as expected!\n")
        print(headline)
        exit(0)
    data[0][cIdx]="name"
    with open(outputPath,'w') as f:
        for j in range (0,len(data)):
            row=data[j]
            if j>0:
                newname=row[urlIdx].split("/")[-1]
                newname=newname.replace("_"," ")
                row[cIdx]=newname
            for i in range (0,len(row)):
                f.write("{0}".format(row[i]))
                if i<len(row)-1:
                    f.write(',')
            f.write("\n")
        f.close()

# clean file in the dir
def cleanFunc(filePath,outputPath,withID,counter):
    with open(filePath) as f:
        data = list(csv.reader(f))
        f.close
    data=cleanData(data)
    headline=data[0]
    with open(outputPath,'w') as f:
        j=0
        for row in data:
            if row[0]!="NULL":
                for i in range(0,len(headline)-1):
                    item = row[i]
                    f.write("{0}".format(item))
                    if i<(len(headline)-2):
                        f.write(',')
                if withID:
                    if j==0:
                        f.write(',ID\n')
                    else:
                        f.write(',%d\n' % j)
                    j+=1
                else:
                    f.write('\n')
        if "MusicGenre.csv" in filePath and counter==1:
             f.write("-1,NULL,Classical music composition,NULL,%d\n" % j)
        f.close()

def cleanFile(fileName,withID):
    filePath="DataTables"+"/"+fileName+".csv"
    outputPath="DataTablesClean"+"/"+fileName+".csv"

    if fileName=="ClassicalMusicComposition":
        fixClassicalMusic(filePath,outputPath)
        filePath=outputPath

    cleanFunc(filePath,outputPath,withID,1)
    cleanFunc(outputPath,outputPath,withID,2)