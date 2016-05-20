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


def getTableFromQuery(typeTable,let,col,langlist,toGroup):
    headers="*"
    const=""
    langconst=""
    groupByconst=""
    sampleHeader="(Sample(?name) as ?name) "
    colName=col.split("/")[-1]
    if "#" in colName:
        colName=colName.split("#")[-1]
    const = "?type <"+col+"> ?"+colName+". "
    if toGroup:
        sampleHeader+="(Sample(?"+colName+") as ?"+colName+") "
    if toGroup:
        groupByconst="GROUP BY ?type"
        headers = "?type "+sampleHeader
    if colName in langlist:
        langconst += "FILTER langMatches(lang(?"+colName+"),"+"\"en\""+"). "

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
        SELECT """+headers+""" WHERE{
            ?type a dbo:"""+typeTable+""".
            ?type foaf:name ?name. """
            + const + """
            FILTER regex(?name,"""+let+""","i").
            """+ langconst+"""
            }"""+groupByconst+"""
            ORDER BY ?type
     """)
    #print (sparql.queryString)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

def createDataTable(tableName,tableType,columnlist,langlist):

    tavRange=[['a','z'],['1','9']]
    dataDict=OrderedDict()
    colDict=OrderedDict()
    colDict["name"]="NULL"

    for col in columnlist:
        colName=col.split("/")[-1]
        if "#" in colName:
            colName=colName.split("#")[-1]
        colDict[colName]="NULL"

    for col in columnlist:
        colName=col.split("/")[-1]
        if "#" in col:
            colName=colName.split("#")[-1]

        for rng in tavRange:
            startR=ord(rng[0])
            endR=ord(rng[1])+1
            for tav in range(startR, endR):
                let="\""+"^"+chr(tav)+"\""
                results=getTableFromQuery(tableType,let,col,langlist,True) #return query

                for result in results["results"]["bindings"]:
                    rowurl=result["type"]["value"]
                    rowurl=rowurl.replace(",",";")
                    rowname=result["name"]["value"]
                    rowname=rowname.replace(",",";")
                    iden=rowurl

                    if iden not in dataDict.keys():
                        dataDict[iden]=colDict.copy()
                    (dataDict[iden])["name"]=rowname

                    colvalue=result[colName]["value"]
                    colvalue=colvalue.replace(",",";")
                    (dataDict[iden])[colName]=colvalue

    print(len(dataDict.keys()))

    fileName="DataTables/"+tableName+".csv"
    with open(fileName,'w') as f:

        ## write headers ##
        f.write("url,name,")
        for col in columnlist:
            colName=col.split("/")[-1]
            if "#" in colName:
                colName=colName.split("#")[-1]
            f.write("{0},".format(colName))
        f.write("\n")

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
    # columns=["http://www.w3.org/2000/01/rdf-schema#comment"]
    # langlist=["name","comment"]
    # createDataTable(tableName,tableType,columns,langlist)
    # print ("Table: "+tableName+" Completed!\n")
    #

    # tableName="MusicalArtist"
    # tableType="MusicalArtist"
    # columns=["http://www.w3.org/2000/01/rdf-schema#comment","http://dbpedia.org/ontology/activeYearsStartYear",
    #          "http://dbpedia.org/ontology/activeYearsEndYear","http://dbpedia.org/property/background",
    #          "http://dbpedia.org/property/description","http://dbpedia.org/ontology/thumbnail"]
    # langlist=["name","description","comment","background"]
    # createDataTable(tableName,tableType,columns,langlist)
    # print ("Table: "+tableName+" Completed!\n")

    # tableName="Band"
    # tableType="Band"
    # columns=["http://www.w3.org/2000/01/rdf-schema#comment","http://dbpedia.org/ontology/activeYearsStartYear",
    #          "http://dbpedia.org/ontology/activeYearsEndYear","http://dbpedia.org/property/background",
    #          "http://dbpedia.org/ontology/thumbnail"]
    # langlist=["name","comment","background"]
    # createDataTable(tableName,tableType,columns,langlist)
    # print ("Table: "+tableName+" Completed!\n")

    # tableName="Single"
    # tableType="Single"
    # columns=["http://www.w3.org/2000/01/rdf-schema#comment","http://dbpedia.org/property/Album",
    #          "http://dbpedia.org/ontology/subsequentWork","http://dbpedia.org/ontology/previousWork",
    #          "http://dbpedia.org/ontology/thumbnail"]
    # langlist=["name","comment"]
    # createDataTable(tableName,tableType,columns,langlist)
    # print ("Table: "+tableName+" Completed!\n")
    #
    #
    # tableName="Song"
    # tableType="Song"
    # columns=["http://www.w3.org/2000/01/rdf-schema#comment","http://dbpedia.org/property/Album",
    #          "http://dbpedia.org/ontology/subsequentWork","http://dbpedia.org/ontology/previousWork",
    #          "http://dbpedia.org/ontology/thumbnail"]
    # langlist=["name","comment"]
    # createDataTable(tableName,tableType,columns,langlist)
    # print ("Table: "+tableName+" Completed!\n")

    tableName="Album"
    tableType="Album"
    columns=["http://www.w3.org/2000/01/rdf-schema#comment","http://dbpedia.org/ontology/subsequentWork",
             "http://dbpedia.org/ontology/previousWork"]
    langlist=["name","comment"]
    createDataTable(tableName,tableType,columns,langlist)
    print ("Table: "+tableName+" Completed!\n")

    tableName="ClassicalMusicComposition"
    tableType="ClassicalMusicComposition"
    columns=["http://www.w3.org/2000/01/rdf-schema#comment","http://dbpedia.org/property/composer",
             "http://dbpedia.org/property/year"]
    langlist=["name","comment"]
    createDataTable(tableName,tableType,columns,langlist)
    print ("Table: "+tableName+" Completed!\n")

    print ("\nAll Tables Were Successfully Created!\n")

createCSVTables()


