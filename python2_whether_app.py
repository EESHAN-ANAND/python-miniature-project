import requests
import json


city=input("Please enter the city:-")
k=city.split()
city="%20".join(k)
print(city)
url='https://api.tomorrow.io/v4/weather/forecast?location={city}&apikey=9OSbMeDPrcEcuNVJEsQ452kpgpY3DWaD'.format(city=city)

r=requests.get(url)
# print(r.text)
wdic=json.loads(r.text)
# print(wdic)

lis_avg=[]
for i in wdic['timelines']['daily']:
    lis_avg.append(i['values']['temperatureApparentAvg'])
print("The list of the temperature for the next 5 days are:-")
print(lis_avg)
