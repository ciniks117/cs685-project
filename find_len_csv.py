import csv
file1="tweet_12:19:53.281742_.csv"
file1="Tweet_2020-09-30_Nikhil.csv"
file1="Tweet_#HathrasCase_2020-10-04_Nikhil.csv"
file1="Tweet_#HathrasTruthExposed_2020-10-04_Nikhil.csv"
file1="Tweet_#FranceBeheading_2020-10-29_Nikhil.csv"
file1="Tweet_#ViennaTerrorAttack_2020-11-03_Nikhil.csv"
file1="Tweet_#ViennaTerrorAttack_2020-11-02_Nikhil.csv"
#file1="Tweet_#USElection2020_2020-11-04_Nikhil.csv"
file1="Tweet_#ViennaAttack_2020-11-03_Nikhil.csv"
with open(file1,"r") as f:
    reader = csv.reader(f,delimiter = ",")
    data = list(reader)
    row_count = len(data)
    print(row_count)

