
# coding: utf-8

import extractAPISparqlData
import extractAPISparqlRelation
import cleanDataAddID
import combineTwoTablesToOne
import createRelationTablesByID
import findTopGenres
import createMySQLTableFromCSV


# Get DBPedia APIs and create CSV tables
print ("Extracting APIs Data...\n")
#
# # extractAPISparqlData.createCSVTables()
# # extractAPISparqlRelation.createCSVTables()
#
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
findTopGenres.createTopGenre()
cleanDataAddID.cleanFile("MusicGenreTop",True)

# Combine tables
print ("Combining Tables...\n")

combineTwoTablesToOne.combineTwoWithID("DataTablesClean","DataTablesClean","Song","Single","Songs")

combineTwoTablesToOne.combineTwo("RelationTables","RelationTables","Song_Artists","Single_Artists","Songs_Artists")
combineTwoTablesToOne.combineTwo("RelationTables","RelationTables","Song_MusicGenre","Single_MusicGenre","Songs_MusicGenre")

# Create ID relation tables
print ("Creating ID Relation Tables...\n")

createRelationTablesByID.createByID("DataTablesClean","MusicalArtist","MusicGenre","RelationTables","MusicalArtist_MusicGenre","RelationTablesID","MusicalArtist_MusicGenre",False)
createRelationTablesByID.createByID("DataTablesClean","Songs","MusicGenre","RelationTables","Songs_MusicGenre","RelationTablesID","Songs_MusicGenre",False)
createRelationTablesByID.createByID("DataTablesClean","Album","MusicGenre","RelationTables","Album_MusicGenre","RelationTablesID","Album_MusicGenre",False)
createRelationTablesByID.createByID("DataTablesClean","Band","MusicGenre","RelationTables","Band_MusicGenre","RelationTablesID","Band_MusicGenre",False)

createRelationTablesByID.createByID("DataTablesClean","MusicGenre","MusicGenreTop","RelationTables","MusicGenre_MusicGenreTop","RelationTablesID","MusicGenre_MusicGenreTop",True)
createRelationTablesByID.createByID("DataTablesClean","MusicGenre","MusicGenre","RelationTables","MusicGenre_MusicDerivativeGenre","RelationTablesID","MusicGenre_MusicDerivativeGenre",False)
createRelationTablesByID.createByID("DataTablesClean","MusicGenre","MusicGenre","RelationTables","MusicGenre_MusicFusionGenre","RelationTablesID","MusicGenre_MusicFusionGenre",False)
createRelationTablesByID.createByID("DataTablesClean","MusicGenre","MusicGenre","RelationTables","MusicGenre_MusicStylisticOriginGenre","RelationTablesID","MusicGenre_MusicStylisticOriginGenre",False)
createRelationTablesByID.createByID("DataTablesClean","MusicGenre","MusicGenre","RelationTables","MusicGenre_MusicSubGenre","RelationTablesID","MusicGenre_MusicSubGenre",False)

createRelationTablesByID.createByID("DataTablesClean","Songs","MusicalArtist","RelationTables","Songs_Artists","RelationTablesID","Songs_MusicalArtist",False)
createRelationTablesByID.createByID("DataTablesClean","Songs","Band","RelationTables","Songs_Artists","RelationTablesID","Songs_Band",False)
createRelationTablesByID.createByID("DataTablesClean","Album","MusicalArtist","RelationTables","Album_Artists","RelationTablesID","Album_MusicalArtist",False)
createRelationTablesByID.createByID("DataTablesClean","Album","Band","RelationTables","Album_Artists","RelationTablesID","Album_Band",False)

createRelationTablesByID.createByID("DataTablesClean","Band","MusicalArtist","RelationTables","Band_BandMembers","RelationTablesID","Band_MusicalArtist",False)

# Create SQL schema and data
print ("Creating SQL files...\n")

createMySQLTableFromCSV.createSQLTables("DataTablesClean","RelationTablesID")

print ("Process Successfully Finished!\n")




