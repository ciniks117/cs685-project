#Clustering
cluestes_mean={1:(0,0),2:(1,1),3:(2,2),4:(3,3),5:(4,4)};
no_change=True;
while no_change:
    for row in rows:
        dis={}
        for k in cluestes_mean:
           dis[k]=math.sqrt((row[20]-cluestes_mean[k][0])*2+(row[21]-cluestes_mean[k][1])*2)
        break;
    break;
