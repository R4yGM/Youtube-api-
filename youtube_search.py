import json
import requests
import datetime
import locale


#url ="https://www.googleapis.com/youtube/v3/channels?part=statistics&" #forUsername=pewdiepie&fields=items/statistics/subscriberCount

date = datetime.datetime.now()
    #this needs random library  import random
     #number = random.randint(1,10)
tries = 1
print(date.strftime("%c"))
#print(date);      
search = input("youtube channel search:\n")
print ("searching " + search)
#arams = dict(
#    forUsername='pewdiepie&',
#    fields='items/statistics/subscriberCount',   
#    key='&key=AIzaSyC3hobIG7uMMPwGv2qIlNYlwfhJVoDGXJc'     viewCount
#)
#url = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=pewdiepie&fields=items/statistics/subscriberCount&key=AIzaSyC3hobIG7uMMPwGv2qIlNYlwfhJVoDGXJc'
#obj = json.load(url)
url ="https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+search+"&fields=items/statistics&key=AIzaSyC3hobIG7uMMPwGv2qIlNYlwfhJVoDGXJc" #/subscriberCount
resp = requests.get(url)
data = resp.json()
subs = data['items'][0]['statistics']['subscriberCount']
datasubs = locale.format_string("%s", subs)
#todos = json.loads(resp.text)
print(datasubs)
