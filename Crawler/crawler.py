'''
Project KESJ python crawler

python in visual studio
https://pytools.codeplex.com/wikipage?title=PTVS%20Installation
install python
https://www.python.org/download
install neo4j 
http://neo4j.com/download/
install neo4jrestclient
Now Windows open terminal pip.exe en install $ pip install neo4jrestclient
Example NEo4j with python
https://pypi.python.org/pypi/neo4jrestclient/1.3.3
more examples
https://neo4j-rest-client.readthedocs.org/en/latest/info.html

'''

import re, urllib
import requests
from neo4jrestclient.client import GraphDatabase

gdb = GraphDatabase("http://localhost:7474/db/data/")

def get_page(url):       
    r = requests.get(url)
    content = r.text.encode('utf-8', 'ignore')
    content = str(content)
    ## set first block pattern
    content_pattern = re.compile('<div class="listRow">(.*?)<div class="clear">')
    ## find first block
    result = re.findall(content_pattern, content)
    ## set oms pattern from first block
    omschrijving_pattern = re.compile('<span class="pic" title="(.*?)"')
    #set price pattern from block
    prijs_pattern = re.compile('&euro; (.*?)</sup>')
    result = str(result)
    ## findall prijs en omschrijving
    omschrijving = re.findall(omschrijving_pattern, result)
    prijs = re.findall(prijs_pattern, result)
    
    ## TODO if statement and fill neo4j with labels and relationship
    i = 0 
    for item in omschrijving:
            item = item.replace("&nbsp;", '')
            
            data = prijs[i]
            data = data.replace("*", '')
            data = data.replace("<sup>", '')
            
            ## fill database neo4j
            #ddr3 = gdb.nodes.create(name="ddr3", omschrijving=item, prijs=data)
            
            i = i + 1
            
            ## test output
            print(data)
            
 
#alle moederborden
url1 = 'http://www.alternate.nl/html/product/listing.html?navId=11622&tk=7&lk=9419&size=500'

#Alle DDR3 geheugen 
#met size=40 kan je de reultaten vergroten
url2 = 'http://www.alternate.nl/html/product/listing.html?navId=11556&tk=7&lk=9326&size=40'

## for running internal
get_page(url2)
    
## TODO IMPLEMENT UDATE OR DELETE
## Delete ddr3 from database
#query2 = """MATCH (n { name: "ddr3" })
#OPTIONAL MATCH (n)-[r]-()
#DELETE n, r"""
#print (gdb.query(query2).get_response())

## DELETE everything
#query2 = """MATCH (n)
#OPTIONAL MATCH (n)-[r]-()
#DELETE n,r"""
#print (gdb.query(query2).get_response())
