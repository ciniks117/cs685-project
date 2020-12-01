# importing csv module 
import csv 

# csv file name 
filename = "Tweet_2020-09-22_Nikhil.csv"

# initializing the titles and rows list 
fields = [] 
rows = [] 

# reading csv file 
with open(filename, 'r') as csvfile: 
	# creating a csv reader object 
	csvreader = csv.reader(csvfile) 
	
	# extracting field names through first row 
	#fields = next(csvreader) 

	# extracting each data row one by one 
	for row in csvreader: 
		rows.append(row) 

	# get total number of rows 
	print("Total no. of rows: %d"%(csvreader.line_num)) 


# printing the field names 
#print('Field names are:' + ', '.join(field for field in fields)) 

# printing first 5 rows 
print('\nFirst 5 rows are:\n') 
for row in rows: 
        # parsing each column of a row 
        #for col in row: 
        #    print("%10s"%col), 
        #print("%10s"%col), 
        #try:
        print(row)
        if row:
            print(row[1])
