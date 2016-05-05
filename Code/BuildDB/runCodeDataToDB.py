
# coding: utf-8

# In[1]:

import cleanDataAddID
import createFileMatchByID
import createMySQLTableFromCSV


# In[3]:

#cleanDataAddID.cleanFile("MusicGenre.csv")
#cleanDataAddID.cleanFile("MusicalWork.csv")
#cleanDataAddID.cleanFile("MusicalArtist.csv")
#cleanDataAddID.cleanFile("Band.csv")
#cleanDataAddID.cleanFile("Single.csv")
#cleanDataAddID.cleanFile("Song.csv")


# In[ ]:

#createFileMatchByID

fileOne="ExcelOntologyTablesClean/MusicGenre.csv"
#fileTwo="ExcelOntologyTablesClean/MusicalWork.csv"
#fileTwo="ExcelOntologyTablesClean/MusicalArtist.csv"
#fileTwo="ExcelOntologyTablesClean/Band.csv"
#fileTwo="ExcelOntologyTablesClean/Single.csv"
#fileTwo="ExcelOntologyTablesClean/Song.csv"
DirOutput="ExcelOntologyTablesMatch"

labelsToMatch=list()
labelsToMatch.append("genre")

#createFileMatchByID.createJoinTableByID(fileOne,fileTwo,DirOutput,labelsToMatch)


# In[9]:

#createFileMatchByID

fileOne="ExcelOntologyTablesClean/MusicalArtist.csv"
fileTwo="ExcelOntologyTablesClean/MusicalWork.csv"
DirOutput="ExcelOntologyTablesMatch"

labelsToMatch=list()
labelsToMatch.append("musicalArtist")
labelsToMatch.append("artist")
labelsToMatch.append("musicalBand")
labelsToMatch.append("bandMember")
labelsToMatch.append("associatedBand")

#createFileMatchByID.createJoinTableByID(fileOne,fileTwo,DirOutput,labelsToMatch)


# In[10]:

#createFileMatchByID

fileOne="ExcelOntologyTablesClean/Band.csv"
fileTwo="ExcelOntologyTablesClean/MusicalWork.csv"
DirOutput="ExcelOntologyTablesMatch"

labelsToMatch=list()
labelsToMatch.append("musicalArtist")
labelsToMatch.append("artist")
labelsToMatch.append("musicalBand")
labelsToMatch.append("bandMember")
labelsToMatch.append("associatedBand")


#createFileMatchByID.createJoinTableByID(fileOne,fileTwo,DirOutput,labelsToMatch)


# In[11]:

#createFileMatchByID

fileOne="ExcelOntologyTablesClean/MusicalArtist.csv"
fileTwo="ExcelOntologyTablesClean/Band.csv"
DirOutput="ExcelOntologyTablesMatch"

labelsToMatch=list()
labelsToMatch.append("bandMember")
labelsToMatch.append("currentMember")
labelsToMatch.append("formerBandMember")
labelsToMatch.append("pastMember")
labelsToMatch.append("associatedMusicalArtist")
labelsToMatch.append("associatedMusicalBand")

#createFileMatchByID.createJoinTableByID(fileOne,fileTwo,DirOutput,labelsToMatch)


# In[18]:

#createFileMatchByID

#fileOne="ExcelOntologyTablesClean/MusicalWork.csv"
#fileTwo="ExcelOntologyTablesClean/Single.csv"
#DirOutput="ExcelOntologyTablesMatch"

#labelsToMatch=list()
#labelsToMatch.append("name")

#createFileMatchByID.createJoinTableByID(fileOne,fileTwo,DirOutput,labelsToMatch)


# In[19]:

#createFileMatchByID

#fileOne="ExcelOntologyTablesClean/MusicalWork.csv"
#fileTwo="ExcelOntologyTablesClean/Song.csv"
#DirOutput="ExcelOntologyTablesMatch"

#labelsToMatch=list()
#labelsToMatch.append("name")

#createFileMatchByID.createJoinTableByID(fileOne,fileTwo,DirOutput,labelsToMatch)


# In[5]:

createMySQLTableFromCSV

createMySQLTableFromCSV.createDataTable("ExcelOntologyTablesClean")
createMySQLTableFromCSV.createMatchTable("ExcelOntologyTablesMatch")

#createMySQLTableFromCSV.createDataTable("test1")
#createMySQLTableFromCSV.createMatchTable("test2")


# In[ ]:



