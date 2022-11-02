import requests
import json
lang =input('chois languge :\n\t 1 => english\n\t 2 => frensh \n\t')
title =input('enter a title for searsh :')
if lang =="1":
  x = requests.get('https://en.wikipedia.org/w/api.php?action=query&exintro=&explaintext=&format=json&prop=extracts&titles='+title)
else:
   x = requests.get('https://fr.wikipedia.org/w/api.php?action=query&exintro=&explaintext=&format=json&prop=extracts&titles='+title)
result = json.loads(x.text)
list_key=result['query']['pages']
a=[]
for y in list_key:
  a.append(y)
pageid=a[0]
title=result['query']['pages'][pageid]['title']
text=result['query']['pages'][pageid]['extract']
print('\t\t'+title+'\n\n'+text )
