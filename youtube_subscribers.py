import json
import requests
import datetime
import locale

date = datetime.datetime.now()
   
tries = 1
print(date.strftime("%c"))
   
search = input("youtube channel search:\n")
print ("searching " + search)

url ="https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+search+"&fields=items/statistics&key=YOUR_API_KEY" 
resp = requests.get(url)
data = resp.json()
subs = data['items'][0]['statistics']['subscriberCount']
datasubs = locale.format_string("%s", subs)
print('pewdiepie :'datasubs)

#Author R4yan
