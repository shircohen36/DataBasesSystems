from SPARQLWrapper import SPARQLWrapper, JSON


def getTableFromQuery(typeTable,let,mustHaveList,optionalList,langlist):
    strOptional=""
    strMustHave=""
    sampleHeader="(Sample(?table) as ?table) (Sample(?comment) as ?comment)"

    if len(mustHaveList)>0:
         strMustHave+="{ "
    for i in range(0,len(mustHaveList)):
        col = mustHaveList[i]
        colName=col.split("/")[-1]
        if "#" in colName:
            colName=colName.split("#")[-1]
        strMustHave += "{ ?table <"+col+"> ?"+colName+". }"
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
        strOptional += "{ ?table <"+col+"> ?"+colName+". "
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
            ?table a dbo:"""+typeTable+""".
            ?table rdfs:comment ?comment.
            ?table <http://dbpedia.org/ontology/wikiPageID> ?id.
            """ + strMustHave + """
            OPTIONAL {
                """ + strOptional + """
                }
            FILTER langMatches(lang(?comment),"en").
            FILTER regex(?cname,"""+let+""","i").
            }"""+groupByconst+"""
            ORDER BY ?id
     """)
    # print (sparql.queryString)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

def createDataTable(tableName,tableType,mustHaveList,optionalList,langlist):

    tavRange=[['a','z'],['1','9']]

    constCol=["id","table","comment"]

    fileName="Data/DataTables/"+tableName+".csv"
    with open(fileName,'w') as f:

        ## write headers ##
        f.write("wikiPageID,url,comment,")
        for col in optionalList:
            colName=col.split("/")[-1]
            if "#" in colName:
                colName=colName.split("#")[-1]
            if colName=="thumbnail":
                f.write("imageLink,")
            else:
                f.write("{0},".format(colName))
        f.write("\n")

        for rng in tavRange: #write all columns for each letter
            startR=ord(rng[0])
            endR=ord(rng[1])+1

            for tav in range(startR, endR):
                let="\""+"^"+chr(tav)+"\""

                try:
                    results=getTableFromQuery(tableType,let,mustHaveList,optionalList,langlist) #return query

                    for result in results["results"]["bindings"]:

                        constEncoded=["","",""]
                        writeRow=True
                        for i in range (0,len(constCol)):
                           col=constCol[i]
                           colResult=result[col]["value"]
                           colResult=colResult.replace(",",";")
                           try:
                               constEncoded[i]=colResult.encode("utf-8")
                           except:
                               writeRow=False
                               break

                        if writeRow: #write encoded to "utf-8"
                           for colResult in constEncoded:
                                f.write("{0},".format(colResult))

                        else: #4 main can't be encoded -> don't write row
                            continue

                        edge=len(optionalList)-1
                        for i in range (0,len(optionalList)):
                            col=optionalList[i]
                            colName=col.split("/")[-1]
                            if "#" in col:
                                colName=colName.split("#")[-1]
                            try:
                                colResult=result[colName]["value"]
                                if colResult=="" or colResult==" ":
                                    f.write("NULL")
                                    if i<edge:
                                        f.write(',')
                                    continue
                                if "/" in colResult and colName!="thumbnail":
                                   colResult=colResult.split("/")[-1]
                                if "_" in colResult and colName!="thumbnail":
                                   colResult=colResult.replace("_"," ")
                                colResult=colResult.replace(",",";")
                                colResult=colResult.encode("utf-8")
                                f.write("{0}".format(colResult))
                                if i<edge:
                                    f.write(',')
                            except:
                                f.write("NULL")
                                if i<edge:
                                    f.write(',')

                        f.write("\n") #end line
                except:
                    print ("Server Error: continue to next search.\n")
                    continue
        f.close()

# create classical music table
def run_code():
    tableName="ClassicalMusicComposition"
    tableType="ClassicalMusicComposition"
    mustHaveList=[]
    optionalList=["http://dbpedia.org/property/cname","http://dbpedia.org/property/composer"]
    langlist=[]
    createDataTable(tableName,tableType,mustHaveList,optionalList,langlist)
    print ("Table: "+tableName+" Completed!\n")