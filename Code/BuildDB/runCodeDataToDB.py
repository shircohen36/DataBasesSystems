
# coding: utf-8

# In[1]:

import cleanDataAddID
import createFileMatchByID


# In[2]:

cleanDataAddID.cleanFile("MusicGenre.csv")
cleanDataAddID.cleanFile("MusicalWork.csv")
cleanDataAddID.cleanFile("MusicalArtist.csv")
cleanDataAddID.cleanFile("Band.csv")
cleanDataAddID.cleanFile("Single.csv")
cleanDataAddID.cleanFile("Song.csv")


# In[12]:

#createFileMatchByID

fileOne="ExcelOntologyTablesClean/MusicGenre.csv"
#fileTwo="ExcelOntologyTablesClean/MusicalWork.csv"
#fileTwo="ExcelOntologyTablesClean/MusicalArtist.csv"
#fileTwo="ExcelOntologyTablesClean/Band.csv"
#fileTwo="ExcelOntologyTablesClean/Single.csv"
#fileTwo="ExcelOntologyTablesClean/Song.csv"
DirOutput="ExcelOntologyTablesForDB"

labelsToMatch=list()
labelsToMatch.append("genre label")

#createFileMatchByID.createJoinTableByID(fileOne,fileTwo,DirOutput,labelsToMatch,True)


# In[14]:

createFileMatchByID

fileOne="ExcelOntologyTablesClean/MusicalArtist.csv"
fileTwo="ExcelOntologyTablesClean/MusicalWork.csv"
DirOutput="ExcelOntologyTablesForDB"

labelsToMatch=list()
labelsToMatch.append("musicalArtist label")
labelsToMatch.append("bandMember label")
labelsToMatch.append("artist label")

createFileMatchByID.createJoinTableByID(fileOne,fileTwo,DirOutput,labelsToMatch,True)


# In[16]:

createFileMatchByID

fileOne="ExcelOntologyTablesClean/Band.csv"
fileTwo="ExcelOntologyTablesClean/MusicalWork.csv"
DirOutput="ExcelOntologyTablesForDB"

labelsToMatch=list()
labelsToMatch.append("musicalBand label")
labelsToMatch.append("associatedBand label")
labelsToMatch.append("artist label")

createFileMatchByID.createJoinTableByID(fileOne,fileTwo,DirOutput,labelsToMatch,True)


# In[17]:

createFileMatchByID

fileOne="ExcelOntologyTablesClean/MusicalArtist.csv"
fileTwo="ExcelOntologyTablesClean/Band.csv"
DirOutput="ExcelOntologyTablesForDB"

labelsToMatch=list()
labelsToMatch.append("bandMember label")
labelsToMatch.append("currentMember label")
labelsToMatch.append("formerBandMember label")
labelsToMatch.append("pastMember label")
labelsToMatch.append("associatedMusicalArtist label")

createFileMatchByID.createJoinTableByID(fileOne,fileTwo,DirOutput,labelsToMatch,True)


# In[18]:

createFileMatchByID

fileOne="ExcelOntologyTablesClean/MusicalWork.csv"
fileTwo="ExcelOntologyTablesClean/Single.csv"
DirOutput="ExcelOntologyTablesForDB"

labelsToMatch=list()
labelsToMatch.append("label")

createFileMatchByID.createJoinTableByID(fileOne,fileTwo,DirOutput,labelsToMatch,False)


# In[19]:

createFileMatchByID

fileOne="ExcelOntologyTablesClean/MusicalWork.csv"
fileTwo="ExcelOntologyTablesClean/Song.csv"
DirOutput="ExcelOntologyTablesForDB"

labelsToMatch=list()
labelsToMatch.append("label")

createFileMatchByID.createJoinTableByID(fileOne,fileTwo,DirOutput,labelsToMatch,False)


# In[ ]:



