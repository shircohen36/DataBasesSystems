from SPARQLWrapper import SPARQLWrapper, JSON
from collections import OrderedDict

def splitString (st):
    if '**' in st:
        st=st.split("**")
        return st
    if '*' in st:
        st=st.split("*")
        return st
    if ',' in st:
        st=st.split(",")
        return st
    if ' - ' in st:
        st=st.split(" - ")
        return st
    if '|' in st:
        st=st.split("|")
        return st
    return [st]


def getTableFromQuery(typeTable,let,mustHaveList,optionalList,langlist):
    strOptional=""
    strMustHave=""
    sampleHeader="(Sample(?type) as ?type) (Sample(?name) as ?name) (Sample(?comment) as ?comment)"

    if len(mustHaveList)>0:
         strMustHave+="{ "
    for i in range(0,len(mustHaveList)):
        col = mustHaveList[i]
        colName=col.split("/")[-1]
        if "#" in colName:
            colName=colName.split("#")[-1]
        strMustHave += "{ ?type <"+col+"> ?"+colName+". }"
        if i<len(mustHaveList)-1:
            strMustHave += " UNION "
        if i==len(mustHaveList)-1:
            strMustHave+=" }"

    for i in range(0,len(optionalList)):
        col = optionalList[i]
        colName=col.split("/")[-1]
        if "#" in colName:
            colName=colName.split("#")[-1]
        sampleHeader+="(Sample(?"+colName+") as ?"+colName+") "
        strOptional += "{ ?type <"+col+"> ?"+colName+". "
        if colName in langlist:
            strOptional += "FILTER langMatches(lang(?"+colName+"),"+"\"en\""+"). }"
        else:
            strOptional+="} "
        if i<len(optionalList)-1:
            strOptional += " UNION "

    groupByconst="GROUP BY ?id"
    headers = "?id "+sampleHeader

    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX dc: <http://purl.org/dc/elements/1.1/>
        PREFIX : <http://dbpedia.org/resource/>
        PREFIX dbpedia2: <http://dbpedia.org/property/>
        PREFIX dbpedia: <http://dbpedia.org/>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        SELECT """+headers+"""
        WHERE{
            ?type a dbo:"""+typeTable+""".
            ?type foaf:name ?name.
            ?type rdfs:comment ?comment.
            ?type <http://dbpedia.org/ontology/wikiPageID> ?id.
            """ + strMustHave + """
            OPTIONAL {
                """ + strOptional + """
                }
            FILTER langMatches(lang(?name),"en").
            FILTER langMatches(lang(?comment),"en").
            FILTER regex(?name,"""+let+""","i").
            }"""+groupByconst+"""
            ORDER BY ?name
     """)
   # print (sparql.queryString)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

def createDataTable(tableName,tableType,mustHaveList,optionalList,langlist):

    tavRange=[['a','z'],['1','9']]
    dataDict=OrderedDict()
    colDict=OrderedDict()
    colDict["type"]="NULL"
    colDict["name"]="NULL"
    colDict["comment"]="NULL"

    fileName="DataTables/"+tableName+".csv"
    with open(fileName,'w') as f:

        ## write headers ##
        f.write("wikiPageID,url,name,comment,")
        for col in optionalList:
            colName=col.split("/")[-1]
            if "#" in colName:
                colName=colName.split("#")[-1]
            f.write("{0},".format(colName))
        f.write("\n")


        for rng in tavRange: #write all columns for each letter
            startR=ord(rng[0])
            endR=ord(rng[1])+1

            for tav in range(startR, endR):
                dataDict.clear()
                let="\""+"^"+chr(tav)+"\""

                results=getTableFromQuery(tableType,let,mustHaveList,optionalList,langlist) #return query

                for result in results["results"]["bindings"]:
                    rowID=result["id"]["value"]
                    rowurl=result["type"]["value"]
                    rowurl=rowurl.replace(",",";")
                    rowname=result["name"]["value"]
                    rowname=rowname.replace(",",";")
                    comname=result["comment"]["value"]
                    comname=comname.replace(",",";")
                    iden=rowID

                    if iden not in dataDict.keys():
                        dataDict[iden]=colDict.copy()
                        (dataDict[iden])["type"]=rowurl
                        (dataDict[iden])["name"]=rowname
                        (dataDict[iden])["comment"]=comname

                    for col in optionalList:
                        colName=col.split("/")[-1]
                        if "#" in col:
                            colName=colName.split("#")[-1]
                        try:
                            colvalue=result[colName]["value"]
                            colvalue=colvalue.replace(",",";")
                            (dataDict[iden])[colName]=colvalue
                        except:
                            (dataDict[iden])[colName]="NULL"


                for iden in dataDict.keys():
                    try:
                        rowurl=iden.encode("utf-8")
                        f.write("{0},".format(rowurl))
                    except: #don't print line if name encoding is bad
                        continue
                    for col in dataDict[iden].keys():
                        colvalue=(dataDict[iden])[col]
                        try:
                            colvalue=colvalue.encode("utf-8")
                            f.write("{0},".format(colvalue))
                        except:  #don't print if encoding is bad
                            f.write("NULL,")
                    f.write("\n")
        f.close()


def createCSVTables():

    print ("Creating Tables...\n\n")

    # tableName="MusicGenre"
    # tableType="MusicGenre"
    # mustHaveList=[]
    # optionalList=[]
    # langlist=[]
    # createDataTable(tableName,tableType,mustHaveList,optionalList,langlist)
    # print ("Table: "+tableName+" Completed!\n")
    #
    # tableName="MusicalArtist"
    # tableType="MusicalArtist"
    # mustHaveList=["http://dbpedia.org/property/genre"]
    # optionalList=["http://dbpedia.org/ontology/activeYearsStartYear","http://dbpedia.org/ontology/activeYearsEndYear",
    #          "http://dbpedia.org/property/background","http://dbpedia.org/property/description",
    #          "http://dbpedia.org/ontology/thumbnail"]
    # langlist=["description","background"]
    # createDataTable(tableName,tableType,mustHaveList,optionalList,langlist)
    # print ("Table: "+tableName+" Completed!\n")
    #
    # tableName="Band"
    # tableType="Band"
    # mustHaveList=["http://dbpedia.org/property/genre"]
    # optionalList=["http://dbpedia.org/ontology/activeYearsStartYear","http://dbpedia.org/ontology/activeYearsEndYear"
    #          "http://dbpedia.org/property/background","http://dbpedia.org/ontology/thumbnail"]
    # langlist=["background"]
    # createDataTable(tableName,tableType,mustHaveList,optionalList,langlist)
    # print ("Table: "+tableName+" Completed!\n")

    # tableName="Single"
    # tableType="Single"
    # mustHaveList=["http://dbpedia.org/property/genre","http://dbpedia.org/ontology/musicalBand",
    #              "http://dbpedia.org/ontology/musicalArtist"]
    # optionalList=["http://dbpedia.org/property/year",
    #               "http://dbpedia.org/property/Album","http://dbpedia.org/ontology/subsequentWork",
    #              "http://dbpedia.org/ontology/previousWork","http://dbpedia.org/ontology/thumbnail"]
    #
    # langlist=[]
    # createDataTable(tableName,tableType,mustHaveList,optionalList,langlist)
    # print ("Table: "+tableName+" Completed!\n")


    # tableName="Song"
    # tableType="Song"
    # mustHaveList=["http://dbpedia.org/property/genre","http://dbpedia.org/property/artist"]
    # optionalList=["http://dbpedia.org/property/year",
    #             "http://dbpedia.org/property/Album","http://dbpedia.org/ontology/subsequentWork",
    #              "http://dbpedia.org/ontology/previousWork","http://dbpedia.org/ontology/thumbnail"]
    # langlist=[]
    # createDataTable(tableName,tableType,mustHaveList,optionalList,langlist)
    # print ("Table: "+tableName+" Completed!\n")

    # tableName="Album"
    # tableType="Album"
    # columns=["http://www.w3.org/2000/01/rdf-schema#comment","http://dbpedia.org/property/type",
    #          "http://dbpedia.org/property/year","http://dbpedia.org/property/released",
    #          "http://dbpedia.org/property/lastAlbum","http://dbpedia.org/property/nextAlbum"]
    # langlist=["name","comment"]
    # createDataTable(tableName,tableType,columns,langlist)
    # print ("Table: "+tableName+" Completed!\n")
    # #
    # tableName="ClassicalMusicComposition"
    # tableType="ClassicalMusicComposition"
    # columns=["http://www.w3.org/2000/01/rdf-schema#comment","http://dbpedia.org/property/composer",
    #          "http://dbpedia.org/property/year"]
    # langlist=["name","comment"]
    # createDataTable(tableName,tableType,columns,langlist)
    # print ("Table: "+tableName+" Completed!\n")

    print ("\nAll Tables Were Successfully Created!\n")

createCSVTables()


