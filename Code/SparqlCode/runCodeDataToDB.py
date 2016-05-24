
# coding: utf-8

import extractAPISparqlData
import extractAPISparqlRelation
import cleanDataAddID
import combineTwoTablesToOne
import createRelationTablesByID
import findTopGenres
import createMySQLTableFromCSV


# Get DBPedia APIs and create CSV tables
# print ("Extracting APIs Data...\n")
#
# #extractAPISparqlData.createCSVTables()
# #extractAPISparqlRelation.createCSVTables()
#
# Clean tables
print ("Cleaning Tables...\n")

# cleanDataAddID.cleanFile("MusicGenre.csv")
# cleanDataAddID.cleanFile("MusicalArtist.csv")
# cleanDataAddID.cleanFile("Band.csv")
# cleanDataAddID.cleanFile("Album.csv")
# cleanDataAddID.cleanFile("ClassicalMusicComposition.csv")
#
# # Combine tables
# print ("Combining Tables...\n")
#
# combineTwoTablesToOne.combineTwoWithID("DataTables","DataTablesClean","Single","Song","Songs")
#
# combineTwoTablesToOne.combineTwo("RelationTables","RelationTables","Single_Artists","Song_Artists","Songs_Artists")
# combineTwoTablesToOne.combineTwo("RelationTables","RelationTables","Single_MusicGenre","Song_MusicGenre","Songs_MusicGenre")

# Create ID relation tables
print ("Creating ID Relation Tables...\n")

#createRelationTablesByID.createByID("DataTablesClean","MusicalArtist","MusicGenre","RelationTables","MusicalArtist_MusicGenre","RelationTablesID","MusicalArtist_MusicGenre")
#createRelationTablesByID.createByID("DataTablesClean","Songs","MusicGenre","RelationTables","Songs_MusicGenre","RelationTablesID","Songs_MusicGenre")
# createRelationTablesByID.createByID("DataTablesClean","Album","MusicGenre","RelationTables","Album_MusicGenre","RelationTablesID","Album_MusicGenre")
# createRelationTablesByID.createByID("DataTablesClean","Band","MusicGenre","RelationTables","Band_MusicGenre","RelationTablesID","Band_MusicGenre")
#
# createRelationTablesByID.createByID("DataTablesClean","MusicGenre","MusicGenre","RelationTables","MusicGenre_MusicDerivativeGenre","RelationTablesID","MusicGenre_MusicDerivativeGenre")
# createRelationTablesByID.createByID("DataTablesClean","MusicGenre","MusicGenre","RelationTables","MusicGenre_MusicFusionGenre","RelationTablesID","MusicGenre_MusicFusionGenre")
# createRelationTablesByID.createByID("DataTablesClean","MusicGenre","MusicGenre","RelationTables","MusicGenre_MusicStylisticOriginGenre","RelationTablesID","MusicGenre_MusicStylisticOriginGenre")
# createRelationTablesByID.createByID("DataTablesClean","MusicGenre","MusicGenre","RelationTables","MusicGenre_MusicSubGenre","RelationTablesID","MusicGenre_MusicSubGenre")
#
# createRelationTablesByID.createByID("DataTablesClean","Songs","MusicalArtist","RelationTables","Songs_Artists","RelationTablesID","Songs_Artists")
# createRelationTablesByID.createByID("DataTablesClean","Songs","Band","RelationTables","Songs_Artists","RelationTablesID","Songs_Band")
# createRelationTablesByID.createByID("DataTablesClean","Album","MusicalArtist","RelationTables","Album_Artists","RelationTablesID","Album_Artists")
# createRelationTablesByID.createByID("DataTablesClean","Album","Band","RelationTables","Album_Artists","RelationTablesID","Album_Band")
#
# createRelationTablesByID.createByID("DataTablesClean","Band","MusicalArtist","RelationTables","Band_BandMembers","RelationTablesID","Band_BandMembers")
#
# # Create SQL schema and data
# print ("Creating SQL files...\n")

#createMySQLTableFromCSV.createSQLTables("DataTablesClean","RelationTablesID","DataTablesClean")

print ("Process Successfully Finished!\n")




