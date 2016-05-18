from SPARQLWrapper import SPARQLWrapper, JSON
from collections import OrderedDict

def udpateNamesFromQuery(typeTable,let):
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
        SELECT ?name WHERE{
            ?type a dbo:"""+typeTable+"""  .
            ?type foaf:name ?name .
            FILTER regex(?name,"""+let+""","i")
            } Group by ?name
             Order by ?name
     """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

def updateColFromQuery(typeTable,let,colURL):
    colName=colURL.split("/")[-1]
    colURL="<"+colURL+">"
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
        SELECT ?name ?"""+colName+""" WHERE{
            ?type a dbo:"""+typeTable+"""  .
            ?type foaf:name ?name .
            ?type """+colURL+""" ?"""+colName+""" .
            FILTER regex(?name,"""+let+""","i")
            } Order by ?name
     """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

def createTableDict(tableName,columnlist):
     dict=OrderedDict()
     for tav in range(ord('a'), ord('z')+1):
        let="\""+"^"+chr(tav)+"\""
        results=udpateNamesFromQuery(tableName,let)
        for result in results["results"]["bindings"]: #update all the rows names
            keyname=result["name"]["value"]
            keyname=keyname.encode('utf-8')
            dict.update({keyname:OrderedDict()})
            for col in columnlist:
                col=col.split("/")[-1]
                colvallist={col:[]}
                dict[keyname].update(colvallist)
        for col in columnlist: #update each column values for each row
            results=updateColFromQuery(tableName,let,col) #return query fot current col
            for result in results["results"]["bindings"]:
                keyname=result["name"]["value"]
                keyname=keyname.encode('utf-8')
                col=col.split("/")[-1]
                colvalue=result[col]["value"]
                if "resource" in colvalue:
                    colvalue=colvalue.split("http://dbpedia.org/resource/")[1]
                colvalue=colvalue.encode('utf-8')
                (dict[keyname])[col].append(colvalue)
     return dict


def printTable(tableName,columns,tableDict):
    fileName="DataTables/"+tableName+".csv"
    with open(fileName,'w') as f:
        f.write("name,")
        for col in columns:
            col=col.split("/")[-1]
            f.write("%s," % col)
        f.write("\n")
        for namekey in tableDict:
            namekey=namekey.replace(",",";")
            #namekey=namekey.encode('utf-8')
            f.write("{0},".format(namekey))
            for colkey in tableDict[namekey]:
                if not (tableDict[namekey])[colkey]:
                    f.write("NULL,")
                else:
                    f.write("{")
                    for item in (tableDict[namekey])[colkey]:
                        item=item.replace(",","|")
                        item=item.replace("_"," ")
                        #item=item.encode('utf-8')
                        f.write("{0}|".format(item))
                    f.write("},")
            f.write("\n")
        f.close()



def createCSVTables():
    tablename="MusicGenre"
    #"http://www.w3.org/2000/01/rdf-schema#comment"
    columns=["http://dbpedia.org/property/derivatives","http://dbpedia.org/property/fusiongenres","http://dbpedia.org/property/subgenres","http://dbpedia.org/property/stylisticOrigins"]
    tabledict=createTableDict(tablename,columns)
    printTable(tablename,columns,tabledict)


createCSVTables()


