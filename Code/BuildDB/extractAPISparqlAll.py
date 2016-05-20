from SPARQLWrapper import SPARQLWrapper, JSON



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


def getTableFromQuery(typeTable,let,collist):
    headers=""
    const=""
    langconst=""
    for col in collist:
        colName=col.split("/")[-1]
        if "#" in colName:
            colName=colName.split("#")[-1]
        headers += "?"+colName+" "
        const += "?type <"+col+"> ?"+colName+". "
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
        SELECT ?type ?name """+headers+""" WHERE{
            ?type a dbo:"""+typeTable+""".
            ?type foaf:name ?name. """
            + const + """
            FILTER regex(?name,"""+let+""","i").
            FILTER langMatches(lang(?name),"en"). """+
            langconst+"""
            } ORDER BY ?type
     """)
    print (sparql.queryString)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

def createDataTable(tableName,tableType,columnlist):

    tavRange=[['a','z'],['1','9']]

    fileName="DataTables/"+tableName+".csv"
    with open(fileName,'w') as f:

        ## write headers ##
        f.write("label, name,")
        for col in columnlist:
            colName=col.split("/")[-1]
            if "#" in colName:
                colName=colName.split("#")[-1]
            f.write("{0},".format(colName))
        f.write("\n")

        for rng in tavRange:
            startR=ord(rng[0])
            endR=ord(rng[1])+1

            for tav in range(startR, endR):
                let="\""+"^"+chr(tav)+"\""
                results=getTableFromQuery(tableType,let,columnlist) #return query

                ## write rows ##
                for result in results["results"]["bindings"]:
                    rowlabel=result["type"]["value"]
                    rowname=result["name"]["value"]
                    try:
                        rowlabel=rowlabel.replace(",",";")
                        rowlabel=rowlabel.encode("utf-8")
                        rowname=rowname.replace(",",";")
                        rowname=rowname.encode("utf-8")
                        f.write("{0},{1},".format(rowlabel,rowname))
                    except: #don't print line if name encoding is bad
                        continue

                    for col in columnlist:
                        col=col.split("/")[-1]
                        if "#" in col:
                            col=col.split("#")[-1]

                        colvalue=result[col]["value"]
                        colvalue=colvalue.replace("_"," ")
                        colvalue=colvalue.replace(",",";")

                        if "resource" not in colvalue and "comment" not in col:
                            f.write("NULL,") #don't print if not in other tables or not a comment
                        else:
                            if "resource" in colvalue:
                                colvalue=colvalue.split("http://dbpedia.org/resource/")[1]
                            try:
                                colvalue=colvalue.encode("utf-8")
                                f.write("{0},".format(colvalue))
                            except:  #don't print if encoding is bad
                                f.write("NULL,")
                    f.write("\n")

        f.close()

def createRelationTable(tableName,tableType,columnlist):

    tavRange=[['a','z'],['1','9']]

    fileName="RelationTables/"+tableName+".csv"
    with open(fileName,'w') as f:

        ## write headers ##
        headers=tableName.split("_")
        f.write("{0},{1}\n".format(headers[0],headers[1]))

        for rng in tavRange:
            startR=ord(rng[0])
            endR=ord(rng[1])+1

            for tav in range(startR, endR):
                let="\""+"^"+chr(tav)+"\""

                for col in columnlist:
                    templist=[col] #results for only one col to match to
                    results=getTableFromQuery(tableType,let,templist) #return query

                ## write rows ##
                    for result in results["results"]["bindings"]:
                        rowname=result["name"]["value"]
                        try:
                            rowname=rowname.replace(",",";")
                            rowname=rowname.encode("utf-8")
                        except: #don't print line if name encoding is bad
                            continue
                        col=col.split("/")[-1]
                        if "#" in col:
                            col=col.split("#")[-1]
                        colvalue=result[col]["value"]
                        colvalue=splitString(colvalue)
                        for colName in colvalue:
                            if colName.isspace() or colName=='': #empty string
                                continue
                            if '\n' in colName:
                                colName=colName.split('\n')[0]
                            try:
                                colName=colName.replace(",",";")
                                colName=colName.encode("utf-8")
                                f.write("{0},{1}\n".format(rowname,colName))
                            except:  #don't print if encoding is bad
                                f.write("{0},NULL\n".format(rowname))

        f.close()


def createCSVTables():
    # tableName="MusicGenre"
    # tableType="MusicGenre"
    # columns=["http://www.w3.org/2000/01/rdf-schema#comment"]
    # createDataTable(tableName,tableType,columns)

    tableName="MusicGenre_MusicSubGenre"
    tableType="MusicGenre"
    columns=["http://dbpedia.org/property/subgenres"]
    createRelationTable(tableName,tableType,columns)

    #columns=["http://dbpedia.org/property/derivatives","http://dbpedia.org/property/fusiongenres","http://dbpedia.org/property/stylisticOrigins"]

createCSVTables()


