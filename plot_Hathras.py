from geopy.geocoders import Nominatim
import pandas as pd
import requests
from xml.etree import ElementTree
import numpy as np
import folium
import csv
import re

geolocator = Nominatim(user_agent="Nikhil")
location = geolocator.geocode("varanasi")
filename="Hathras-TweetsLat_Lon_Sent.csv"
rows = []
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)


a=re.findall(r"'(.*?)'", rows[0][0], re.DOTALL)
#a=rows[0][0].split(",")

#print(a[-2])
#print(len(rows))
myrows=rows
print(len(rows))
#print(rows)
name = []
latitude = []
longitude = []
mylocs=rows[:25]

#mylocs = ['varanasi','kanpur','lucknow']
for c in myrows:
    a=re.findall(r"'(.*?)'", c[0], re.DOTALL)
    c1=a[-2]
    location = geolocator.geocode(c1)
    print(location)
    if location:
        name.append(c1)
        latitude.append(location.latitude)
        longitude.append(location.longitude)
    #region.append(c.find('region/name').text)

df_counters = pd.DataFrame(
    {'Name' : name,
     'latitude' : latitude,
     'longitude' : longitude
     #'region' : region
    })
df_counters.head()

locations = df_counters[['latitude', 'longitude']]
locationlist = locations.values.tolist()
print(len(locationlist))
print(locationlist[2])

#map1 = folium.Map(location=[25.8, 83.5], zoom_start=12)
#for point in range(0, len(locationlist)):
#    folium.Marker(locationlist[point], popup=df_counters['Name'][point]).add_to(map1)


## for india map
location = geolocator.geocode("jabalpur")
mapit = folium.Map( location=[location.latitude, location.longitude], zoom_start=5 )
for coord in locationlist:
    folium.Marker( location=[ coord[0], coord[1] ], fill_color='#43d9de', radius=8 ).add_to( mapit )

mapit.save( 'indiamap_hathras.html')


### for world map
location = geolocator.geocode("Niamey")
mapit = folium.Map( location=[location.latitude, location.longitude], zoom_start=3)
for coord in locationlist:
    folium.Marker( location=[ coord[0], coord[1] ], fill_color='#43d9de', radius=8 ).add_to( mapit )

mapit.save( 'worldmap_hathras.html')



