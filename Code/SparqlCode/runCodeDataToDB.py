
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
# extractAPISparqlData.createCSVTables()
# extractAPISparqlRelation.createCSVTables()
#
# Clean tables
print ("Cleaning Tables...\n")
#
# cleanDataAddID.cleanFile("MusicGenre",True)
# cleanDataAddID.cleanFile("MusicalArtist",True)
# cleanDataAddID.cleanFile("Band",True)
# cleanDataAddID.cleanFile("Album",True)
# cleanDataAddID.cleanFile("ClassicalMusicComposition",True)
# cleanDataAddID.cleanFile("Single",False)
# cleanDataAddID.cleanFile("Song",False)
#
# # Combine tables
print ("Combining Tables...\n")

#combineTwoTablesToOne.combineTwoWithID("DataTablesClean","DataTablesClean","Song","Single","Songs")
#
#combineTwoTablesToOne.combineTwo("RelationTables","RelationTables","Song_Artists","Single_Artists","Songs_Artists")
#combineTwoTablesToOne.combineTwo("RelationTables","RelationTables","Song_MusicGenre","Single_MusicGenre","Songs_MusicGenre")

# Create ID relation tables
print ("Creating ID Relation Tables...\n")

# createRelationTablesByID.createByID("DataTablesClean","MusicalArtist","MusicGenre","RelationTables","MusicalArtist_MusicGenre","RelationTablesID","MusicalArtist_MusicGenre")
# createRelationTablesByID.createByID("DataTablesClean","Songs","MusicGenre","RelationTables","Songs_MusicGenre","RelationTablesID","Songs_MusicGenre")
# createRelationTablesByID.createByID("DataTablesClean","Album","MusicGenre","RelationTables","Album_MusicGenre","RelationTablesID","Album_MusicGenre")
# createRelationTablesByID.createByID("DataTablesClean","Band","MusicGenre","RelationTables","Band_MusicGenre","RelationTablesID","Band_MusicGenre")
#
# createRelationTablesByID.createByID("DataTablesClean","MusicGenre","MusicGenre","RelationTables","MusicGenre_MusicDerivativeGenre","RelationTablesID","MusicGenre_MusicDerivativeGenre")
# createRelationTablesByID.createByID("DataTablesClean","MusicGenre","MusicGenre","RelationTables","MusicGenre_MusicFusionGenre","RelationTablesID","MusicGenre_MusicFusionGenre")
# createRelationTablesByID.createByID("DataTablesClean","MusicGenre","MusicGenre","RelationTables","MusicGenre_MusicStylisticOriginGenre","RelationTablesID","MusicGenre_MusicStylisticOriginGenre")
# createRelationTablesByID.createByID("DataTablesClean","MusicGenre","MusicGenre","RelationTables","MusicGenre_MusicSubGenre","RelationTablesID","MusicGenre_MusicSubGenre")

# createRelationTablesByID.createByID("DataTablesClean","Songs","MusicalArtist","RelationTables","Songs_Artists","RelationTablesID","Songs_MusicalArtist")
# createRelationTablesByID.createByID("DataTablesClean","Songs","Band","RelationTables","Songs_Artists","RelationTablesID","Songs_Band")
# createRelationTablesByID.createByID("DataTablesClean","Album","MusicalArtist","RelationTables","Album_Artists","RelationTablesID","Album_MusicalArtist")
# createRelationTablesByID.createByID("DataTablesClean","Album","Band","RelationTables","Album_Artists","RelationTablesID","Album_Band")
#
# createRelationTablesByID.createByID("DataTablesClean","Band","MusicalArtist","RelationTables","Band_BandMembers","RelationTablesID","Band_MusicalArtist")
#
# # # # Create SQL schema and data
print ("Creating SQL files...\n")

# createMySQLTableFromCSV.createSQLTables("DataTablesClean","RelationTablesID","DataTablesClean")

print ("Process Successfully Finished!\n")




