import csv
Dfilename="Farmer-Tweets.csv";
Dfile=open(Dfilename,"r",encoding="utf-8");
Data=[];
Locations=[]
csvReader=csv.reader(Dfile);
for row in csvReader:
    Data.append(eval(row[0]));
