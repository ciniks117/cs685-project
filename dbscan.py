import numpy as np 
from sklearn.cluster import DBSCAN 
from sklearn import metrics 
from sklearn.datasets.samples_generator import make_blobs 
from sklearn.preprocessing import StandardScaler 
from sklearn import datasets 

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

filename="Locations.csv"
filename="Farmer-TweetsLat_Lon_Sent.csv"
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
    #print(location)
    #region.append(c.find('region/name').text)

import numpy as np
XX=[list(x) for x in LAT_LON_Dict];
X=np.array(XX)
from sklearn.cluster import DBSCAN


db = DBSCAN(eps=5, min_samples=10).fit(X)
cluster_labels = db.labels_
Cluster_Dict={}
for label in cluster_labels:
    Cluster_Dict[label]=[];
for i in range(len(X)):
    Cluster_Dict[cluster_labels[i]]+=[list(X[i])]
#print(Cluster_Dict)

# Plot result 
import matplotlib.pyplot as plt 


#y=np.array(Cluster_Dict[0])
#plt.plot(y[:,1],y[:,0], 'o',markeredgecolor='k',markersize=1)
#plt.show() 

for d in Cluster_Dict:
    if d==-1:
        continue
    y=np.array(Cluster_Dict[d])
    plt.plot(y[:,1], y[:,0], 'o',markeredgecolor='k',markersize=1)
    print(d)
plt.show() 


def CreateCluster(LAT_LON_Dict,e,m):
    import numpy as np
    import matplotlib.pyplot as plt
    XX=[list(x) for x in LAT_LON_Dict];
    X=np.array(XX)
    from sklearn.cluster import DBSCAN
    db = DBSCAN(eps=e, min_samples=m).fit(X)
    cluster_labels = db.labels_
    Cluster_Dict={}
    for label in cluster_labels:
        Cluster_Dict[label]=[];
    for i in range(len(X)):
        Cluster_Dict[cluster_labels[i]]+=[list(X[i])]
    for cluster in Cluster_Dict:
        if cluster==-1:
            continue;
        cluster_cords=np.array(Cluster_Dict[cluster]);
        plt.plot(cluster_cords[:,1],cluster_cords[:,0],'o')
    plt.ylim((-90,90))
    plt.xlim((-180,180))
    plt.savefig("Cluster.png")


"""    
# #############################################################################
# Generate sample data
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
                            random_state=0)

X = StandardScaler().fit_transform(X)


import numpy as np
XX=[list(x) for x in LAT_LON_Dict];
X=np.array(XX)
from sklearn.cluster import DBSCAN
db = DBSCAN(eps=0.3, min_samples=10).fit(X)
# #############################################################################
# Compute DBSCAN
print(X)
# Load data in X 
db = DBSCAN(eps=0.3, min_samples=10).fit(X) 
core_samples_mask = np.zeros_like(db.labels_, dtype=bool) 
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_ 

# Number of clusters in labels, ignoring noise if present. 
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0) 

print(labels) 

# Plot result 
import matplotlib.pyplot as plt 

# Black removed and is used for noise instead. 
unique_labels = set(labels) 
colors = ['y', 'b', 'g', 'r'] 
print(colors) 
for k, col in zip(unique_labels, colors): 
	if k == -1: 
		# Black used for noise. 
		col = 'k'

	class_member_mask = (labels == k) 

	xy = X[class_member_mask & core_samples_mask]
	plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, 
									markeredgecolor='k', 
									markersize=6) 

	xy = X[class_member_mask & ~core_samples_mask] 
	plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, 
									markeredgecolor='k', 
									markersize=6) 

plt.title('number of clusters: %d' %n_clusters_) 
plt.show() 
"""
