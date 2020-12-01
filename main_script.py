#---IMPORTS-----#
import csv
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

#------Variable declartion-----#
geolocator = Nominatim(user_agent="Vishal")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
Dfilename="Farmer-Tweets.csv";
#Dfilename="Test_Data.csv";
Dfile=open(Dfilename,"r",encoding="utf-8");
Data=[];
Locations=[]
csvReader=csv.reader(Dfile);

#Reading tweets into variable Data
for row in csvReader:
    Data.append(eval(row[0]));

#Collecting all tweet loactions beacuse we need to find their address, Lat and Long
for row in Data:
    if row[9] not in Locations:
        Locations.append(row[9])

#Sorting all Tweet locatons
Locations.sort()
#------------------------------------------------------------------------------#
"""
--->Creating Dictonary where keys are tweet location present in tweet
---> Values contains 3 entry:
        1.Latitude e.g 22.02
        2.Longitute e.g 75.44
        3.Corresponding Correct Adress.[Will be used to find City and state]
                                e.g Bahadurgarh, Jhajjar, Haryana, India
"""
LocationLatLon={};
for loc in Locations:
    #Get the lat,Lon, and Address of that loc
    locationD =geocode(loc)
    #If location has found, then    
    if locationD is not None:
        #locationD[1][0] : Lat of that location, locationD[1][1] : Lon of that location, locationD[0]: Correspondance Address of that loc
        LocationLatLon[loc]=[locationD[1][0],locationD[1][1],locationD[0]]
        print(locationD)
#------------------------------------------------------------------------------#
"""
---> Creating New Cleared Data which will be used for final Processing.
---> Removing those Data for which we couldn't able to find location.
---> Here we are not removing those Tweets which are not tweeted from india i.e tweeted from other county, because that we will use in our analysis, also we are not removng those indian tweets
     for which we dont have city or state mentioned
"""
NewData=[];
for row in Data:
    loc=row[9];
    if loc in LocationLatLon.keys():
        d=list(row);
        d.append(LocationLatLon[loc][0])
        d.append(LocationLatLon[loc][1])
        d.append(LocationLatLon[loc][2]);
        dT=tuple(d);
        NewData.append(dT);
