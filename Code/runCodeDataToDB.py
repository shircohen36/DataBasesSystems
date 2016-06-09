
# coding: utf-8

import extractAPISparqlData
import extractAPISparqlRelation
import cleanDataAddID
import combineTwoTablesToOne
import createRelationTablesByID
import findTopGenres
import createMySQLTableFromCSV

header="../Data/"


# Get DBPedia APIs and create CSV tables
print ("Extracting APIs Data...\n")

extractAPISparqlData.createCSVTables()
extractAPISparqlRelation.createCSVTables()


# Clean tables

print ("Cleaning Tables...\n")

cleanDataAddID.cleanFile("MusicGenre",True)
cleanDataAddID.cleanFile("MusicalArtist",True)
cleanDataAddID.cleanFile("Band",True)
cleanDataAddID.cleanFile("Album",True)
cleanDataAddID.cleanFile("ClassicalMusicComposition",True)
cleanDataAddID.cleanFile("Single",False)
cleanDataAddID.cleanFile("Song",False)

print ("Finding Top Genres...\n")
# find top genres
findTopGenres.createTopGenre()
cleanDataAddID.cleanFile("MusicGenreTop",True)

# Combine tables
print ("Combining Tables...\n")

combineTwoTablesToOne.combineTwoWithID(header+"DataTablesClean",header+"DataTablesClean","Song","Single","Songs")

combineTwoTablesToOne.combineTwo(header+"RelationTables",header+"RelationTables","Song_Artists","Single_Artists","Songs_Artists")
combineTwoTablesToOne.combineTwo(header+"RelationTables",header+"RelationTables","Song_MusicGenre","Single_MusicGenre","Songs_MusicGenre")

# Create ID relation tables
print ("Creating ID Relation Tables...\n")

createRelationTablesByID.createByID(header+"DataTablesClean","MusicalArtist","MusicGenre",header+"RelationTables","MusicalArtist_MusicGenre",header+"RelationTablesID","MusicalArtist_MusicGenre",False)
createRelationTablesByID.createByID(header+"DataTablesClean","Songs","MusicGenre",header+"RelationTables","Songs_MusicGenre",header+"RelationTablesID","Songs_MusicGenre",False)
createRelationTablesByID.createByID(header+"DataTablesClean","Album","MusicGenre",header+"RelationTables","Album_MusicGenre",header+"RelationTablesID","Album_MusicGenre",False)
createRelationTablesByID.createByID(header+"DataTablesClean","Band","MusicGenre",header+"RelationTables","Band_MusicGenre",header+"RelationTablesID","Band_MusicGenre",False)

createRelationTablesByID.createByID(header+"DataTablesClean","MusicGenre","MusicGenreTop",header+"RelationTables","MusicGenre_MusicGenreTop",header+"RelationTablesID","MusicGenre_MusicGenreTop",True)
createRelationTablesByID.createByID(header+"DataTablesClean","MusicGenre","MusicGenre",header+"RelationTables","MusicGenre_MusicDerivativeGenre",header+"RelationTablesID","MusicGenre_MusicDerivativeGenre",False)
createRelationTablesByID.createByID(header+"DataTablesClean","MusicGenre","MusicGenre",header+"RelationTables","MusicGenre_MusicFusionGenre",header+"RelationTablesID","MusicGenre_MusicFusionGenre",False)
createRelationTablesByID.createByID(header+"DataTablesClean","MusicGenre","MusicGenre",header+"RelationTables","MusicGenre_MusicStylisticOriginGenre",header+"RelationTablesID","MusicGenre_MusicStylisticOriginGenre",False)
createRelationTablesByID.createByID(header+"DataTablesClean","MusicGenre","MusicGenre",header+"RelationTables","MusicGenre_MusicSubGenre",header+"RelationTablesID","MusicGenre_MusicSubGenre",False)

createRelationTablesByID.createByID(header+"DataTablesClean","Songs","MusicalArtist",header+"RelationTables","Songs_Artists",header+"RelationTablesID","Songs_MusicalArtist",False)
createRelationTablesByID.createByID(header+"DataTablesClean","Songs","Band",header+"RelationTables","Songs_Artists",header+"RelationTablesID","Songs_Band",False)
createRelationTablesByID.createByID(header+"DataTablesClean","Album","MusicalArtist",header+"RelationTables","Album_Artists",header+"RelationTablesID","Album_MusicalArtist",False)
createRelationTablesByID.createByID(header+"DataTablesClean","Album","Band",header+"RelationTables","Album_Artists",header+"RelationTablesID","Album_Band",False)

createRelationTablesByID.createByID(header+"DataTablesClean","Band","MusicalArtist",header+"RelationTables","Band_BandMembers",header+"RelationTablesID","Band_MusicalArtist",False)

# Create SQL schema and data
print ("Creating SQL files...\n")

createMySQLTableFromCSV.createSQLTables(header+"DataTablesClean",header+"RelationTablesID")

print ("Process Successfully Finished!\n")




