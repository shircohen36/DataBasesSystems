
# coding: utf-8

# In[1]:

import cleanDataAddID
import createFileMatchByID
import createMySQLTableFromCSV


# In[6]:

cleanDataAddID.cleanFile("MusicGenre.csv")
cleanDataAddID.cleanFile("MusicalArtist.csv")
cleanDataAddID.cleanFile("Band.csv")
cleanDataAddID.cleanFile("Single.csv")
cleanDataAddID.cleanFile("Song.csv")
cleanDataAddID.cleanFile("Album.csv")
cleanDataAddID.cleanFile("ClassicalMusicComposition.csv")


# In[7]:

# find genres in fileTwo

createFileMatchByID

fileOne="ExcelOntologyTablesClean/MusicGenre.csv"
nameOne="MusicGenre"
DirOutput="ExcelOntologyTablesMatch"

labelsToMatch=list()
labelsToMatch.append("genre")

filesToMatch=list()
filesToMatch.append("MusicalArtist")
filesToMatch.append("Band")
filesToMatch.append("Single")
filesToMatch.append("Song")
filesToMatch.append("Album")
filesToMatch.append("ClassicalMusicComposition")

for filename in filesToMatch:
    fileTwo="ExcelOntologyTablesClean/"+filename+".csv"
    nameTwo=filename
    createFileMatchByID.createJoinTableByID(fileOne,fileTwo,DirOutput,labelsToMatch,nameOne,nameTwo)


# In[8]:

# connect genre to genre categories

createFileMatchByID

fileOne="ExcelOntologyTablesClean/MusicGenre.csv"
fileTwo="ExcelOntologyTablesClean/MusicGenre.csv"
nameOne="MusicGenre"
DirOutput="ExcelOntologyTablesMatch"

nameTwo="MusicSubGenre"
labelsToMatch=list()
labelsToMatch.append("musicSubgenre")

createFileMatchByID.createJoinTableByID(fileOne,fileTwo,DirOutput,labelsToMatch,nameOne,nameTwo)

nameTwo="MusicStylisticOriginGenre"
labelsToMatch=list()
labelsToMatch.append("stylisticOrigin")

createFileMatchByID.createJoinTableByID(fileOne,fileTwo,DirOutput,labelsToMatch,nameOne,nameTwo)

nameTwo="MusicDerivativeGenre"
labelsToMatch=list()
labelsToMatch.append("derivative")

createFileMatchByID.createJoinTableByID(fileOne,fileTwo,DirOutput,labelsToMatch,nameOne,nameTwo)

nameTwo="MusicFusionGenre"
labelsToMatch=list()
labelsToMatch.append("musicFusionGenre")

createFileMatchByID.createJoinTableByID(fileOne,fileTwo,DirOutput,labelsToMatch,nameOne,nameTwo)


# In[5]:

# find artists/bands in Single

createFileMatchByID

fileTwo="ExcelOntologyTablesClean/Single.csv"
nameTwo="Single"
DirOutput="ExcelOntologyTablesMatch"

labelsToMatch=list()
labelsToMatch.append("musicalArtist")
labelsToMatch.append("artist")
labelsToMatch.append("musicalBand")

filesToMatch=list()
filesToMatch.append("MusicalArtist")
filesToMatch.append("Band")

for filename in filesToMatch:
    fileOne="ExcelOntologyTablesClean/"+filename+".csv"
    nameOne=filename
    createFileMatchByID.createJoinTableByID(fileOne,fileTwo,DirOutput,labelsToMatch,nameOne,nameTwo)


# In[6]:

# find artists/bands/composers in Song

createFileMatchByID

fileTwo="ExcelOntologyTablesClean/Song.csv"
nameTwo="Song"
DirOutput="ExcelOntologyTablesMatch"

labelsToMatch=list()
labelsToMatch.append("artist")
labelsToMatch.append("composer")

filesToMatch=list()
filesToMatch.append("MusicalArtist")
filesToMatch.append("Band")

for filename in filesToMatch:
    fileOne="ExcelOntologyTablesClean/"+filename+".csv"
    nameOne=filename
    createFileMatchByID.createJoinTableByID(fileOne,fileTwo,DirOutput,labelsToMatch,nameOne,nameTwo)


# In[7]:

# find artists/bands/composers in Album

createFileMatchByID

fileTwo="ExcelOntologyTablesClean/Album.csv"
nameTwo="Album"
DirOutput="ExcelOntologyTablesMatch"

labelsToMatch=list()
labelsToMatch.append("artist")
labelsToMatch.append("associatedBand")
labelsToMatch.append("associatedMusicalArtist")
labelsToMatch.append("bandMember")
labelsToMatch.append("compiler")
labelsToMatch.append("formerBandMember")
labelsToMatch.append("musicalArtist")
labelsToMatch.append("musicalBand")

filesToMatch=list()
filesToMatch.append("MusicalArtist")
filesToMatch.append("Band")

for filename in filesToMatch:
    fileOne="ExcelOntologyTablesClean/"+filename+".csv"
    nameOne=filename
    createFileMatchByID.createJoinTableByID(fileOne,fileTwo,DirOutput,labelsToMatch,nameOne,nameTwo)


# In[8]:

# find Album in fileTwo

createFileMatchByID

fileOne="ExcelOntologyTablesClean/Album.csv"
nameOne="Album"
DirOutput="ExcelOntologyTablesMatch"

labelsToMatch=list()
labelsToMatch.append("album")

filesToMatch=list()
filesToMatch.append("Single")
filesToMatch.append("Song")

for filename in filesToMatch:
    fileTwo="ExcelOntologyTablesClean/"+filename+".csv"
    nameTwo=filename
    createFileMatchByID.createJoinTableByID(fileOne,fileTwo,DirOutput,labelsToMatch,nameOne,nameTwo)


# In[9]:

#connect band to artists

createFileMatchByID

fileOne="ExcelOntologyTablesClean/MusicalArtist.csv"
nameOne="MusicalArtist"
fileTwo="ExcelOntologyTablesClean/Band.csv"
nameTwo="Band"
DirOutput="ExcelOntologyTablesMatch"

labelsToMatch=list()
labelsToMatch.append("bandMember")
labelsToMatch.append("currentMember")
labelsToMatch.append("formerBandMember")
labelsToMatch.append("pastMember")
labelsToMatch.append("associatedMusicalArtist")
labelsToMatch.append("associatedMusicalBand")

createFileMatchByID.createJoinTableByID(fileOne,fileTwo,DirOutput,labelsToMatch,nameOne,nameTwo)


# In[2]:

createMySQLTableFromCSV

createMySQLTableFromCSV.createSQLTables("ExcelOntologyTablesClean","ExcelOntologyTablesMatch","ExcelOntologyTablesClean")


# In[ ]:



