from geopy.geocoders import Nominatim
import folium
import csv
#################################################
geolocator = Nominatim(user_agent="Nikhil")
#location = locator.geocode(“Howrah,Kolkata,India”)
location = geolocator.geocode("kanpur")
#print(location.address)
#print((location.latitude, location.longitude))
#print(location.raw)
location = geolocator.geocode("varanasi")
#print(location.address)
#print((location.latitude, location.longitude))
################################################

filename="USElection-TweetsLat_Lon_Sent.csv"
rows = []
with open(filename, 'r',encoding="utf-8") as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(eval(row[0]))


myrows=rows


LAT_LON_Dict={}
for c in myrows:
    location = (c[20],c[21])
    if location not in LAT_LON_Dict:
        LAT_LON_Dict[location]=[[c[22],c[24],c[25]]]
    else:
        LAT_LON_Dict[location]+=[[c[22],c[24],c[25]]]
    print(location)
    #region.append(c.find('region/name').text)

## for india map
location = geolocator.geocode("jabalpur")
mapit = folium.Map( location=[location.latitude, location.longitude], zoom_start=5 )
for coord in LAT_LON_Dict:
    #sent=LAT_LON_Dict[coord][0][1]
    sent=sum([x[1]for x in LAT_LON_Dict[coord]])/len(LAT_LON_Dict[coord])
    if sent>0 and sent<=0.25:
        folium.Circle( location=[ coord[0], coord[1] ], color='darkred', fill_color='darkred', radius=50*len(LAT_LON_Dict[coord])).add_to( mapit )
    elif sent>0.25 and sent<=0.5:
        folium.Circle( location=[ coord[0], coord[1] ], color='red', fill_color='red', radius=50*len(LAT_LON_Dict[coord]) ).add_to( mapit )
    elif sent>0.5 and sent<=0.75:
        folium.Circle( location=[ coord[0], coord[1] ], color='green', fill_color='green', radius=00*len(LAT_LON_Dict[coord]) ).add_to( mapit )
    elif sent>0.75 and sent<=1:
        folium.Circle( location=[ coord[0], coord[1] ], color='darkgreen', fill_color='darkgreen', radius=50*len(LAT_LON_Dict[coord]) ).add_to( mapit )

mapit.save( 'indiamap_uselection.html')

"""
### for world map
location = geolocator.geocode("Niamey")
mapit = folium.Map( location=[location.latitude, location.longitude], zoom_start=3)
for coord in LAT_LON_Dict:
    folium.Marker( location=[ coord[0], coord[1] ], fill_color='#43d9de', radius=8 ).add_to( mapit )
mapit.save( 'worldmap_uselection.html')
"""

ind_coord = geolocator.geocode("India")
### for world map
location = geolocator.geocode("Niamey")
mapit = folium.Map( location=[location.latitude, location.longitude], zoom_start=3)
for coord in LAT_LON_Dict:
    sent=sum([x[1]for x in LAT_LON_Dict[coord]])/len(LAT_LON_Dict[coord])
    if (ind_coord.latitude,ind_coord.longitude) == coord:
        print(coord)
        continue
    if sent>0 and sent<=0.25:
        folium.Circle( location=[ coord[0], coord[1] ], color='darkred', fill_color='darkred', radius=1000).add_to(mapit)
    elif sent>0.25 and sent<=0.5:
        folium.Circle( location=[ coord[0], coord[1] ], color='red', fill_color='red', radius=1000 ).add_to( mapit )
    elif sent>0.5 and sent<=0.75:
        folium.Circle( location=[ coord[0], coord[1] ], color='green', fill_color='green', radius=1000).add_to( mapit )
    elif sent>0.75 and sent<=1:
        folium.Circle( location=[ coord[0], coord[1] ], color='darkgreen', fill_color='darkgreen', radius=1000 ).add_to( mapit )
    #folium.Marker( location=[ coord[0], coord[1] ], fill_color='#43d9de', radius=8 ).add_to( mapit )

mapit.save( 'worldmap_uselection.html')

ind_coord = geolocator.geocode("India")
### for world map
location = geolocator.geocode("Denver")
mapit = folium.Map( location=[location.latitude, location.longitude], zoom_start=3)
for coord in LAT_LON_Dict:
    sent=sum([x[1]for x in LAT_LON_Dict[coord]])/len(LAT_LON_Dict[coord])
    if (ind_coord.latitude,ind_coord.longitude) == coord:
        print(coord)
        continue
    if sent>0 and sent<=0.25:
        folium.Circle( location=[ coord[0], coord[1] ], color='darkred', fill_color='darkred', radius=40000).add_to(mapit)
    elif sent>0.25 and sent<=0.5:
        folium.Circle( location=[ coord[0], coord[1] ], color='red', fill_color='red', radius=40000 ).add_to( mapit )
    elif sent>0.5 and sent<=0.75:
        folium.Circle( location=[ coord[0], coord[1] ], color='green', fill_color='green', radius=40000).add_to( mapit )
    elif sent>0.75 and sent<=1:
        folium.Circle( location=[ coord[0], coord[1] ], color='darkgreen', fill_color='darkgreen', radius=40000 ).add_to( mapit )
    #folium.Marker( location=[ coord[0], coord[1] ], fill_color='#43d9de', radius=8 ).add_to( mapit )

mapit.save( 'usmap_uselection.html')

