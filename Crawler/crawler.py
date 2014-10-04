#!/Python34/pyton
'''
Project KESJ python crawler

TODO Make POSTJSON and GETJSON config file seperate py
'''

import urllib.request
import json
import codecs
import requests
import re, urllib
import requests

#Json config File
requestconfigfile = 'http://127.0.0.1/test.json'

#Get the Json file and read patterns and url config for crawling
file = urllib.request.urlopen(requestconfigfile)
charset = file.info().get_param('charset', 'utf8')
data = file.read()
jsondata = json.loads(data.decode(charset))

#make a empty list
list = [] 

#loop for each item in data configfile
for item in jsondata['data']:
   url = item['url']
   pattern = item["pattern"]
   subpatternprijs = item["subpatternprijs"]
   subpatternomschrijving = item["subpatternomschrijving"]
   category = item["category"]
  
   #Get url for crawling
   r = requests.get(url)
   content = r.text.encode('utf-8', 'ignore')
   content = str(content)
   ## set first block pattern
   content_pattern = re.compile(pattern)
   ## find first block pattern
   result = re.findall(content_pattern, content)
   ## set oms pattern from first block
   omschrijving_pattern = re.compile(subpatternomschrijving)
   #set price pattern from block
   prijs_pattern = re.compile(subpatternprijs)
   result = str(result)
   ## findall prijs en omschrijving
   omschrijving = re.findall(omschrijving_pattern, result)
   prijs = re.findall(prijs_pattern, result)
   
   ## loop statement for each product
   i = 0 
   for item in omschrijving:
           # Clean up some code from omschrijving
           item = item.replace("&nbsp;", '')
           #Get prijs
           itemprijs = prijs[i]
           #Filter out extra for alternate prijs to make prijs float
           itemprijs = itemprijs.replace("*", '')
           itemprijs = itemprijs.replace(",", '.')
           itemprijs = itemprijs.replace(".-", '')
           itemprijs = float(itemprijs.replace("<sup>", ''))
           
           i = i + 1
           #Make a json file for posting
           #list.append(json.dumps({'category': category , 'omschrijving': item, 'prijs' : itemprijs},indent=0))
           list.append({'category': category , 'omschrijving': item, 'prijs' : itemprijs})
           
           

#make new list and put in json file  
list2 = []
list2.extend(list)           
     
#post the list to API
posturl = 'http://localhost:49990/GetJson.aspx'
#headers = {'content-type': 'application/json'}
headers = {'content-type': 'text/plain'}

response = requests.post(posturl, data=json.dumps(list2), headers=headers)

#test      
print(response)











