from fastkml import kml
import numpy as np
from math import cos,sin, sqrt
from datetime import timedelta,datetime
from SubCalculations.Timecalcu import TimeCalcu
import glob
files=glob.glob('folderpath containg kml files/*.kml')
filecount=0
for file in files:
    filename=file
    outputf = open("outputfile", "a")
   
    filecount=filecount+1
    with open(filename, 'rt') as myfile:
        doc=myfile.read().encode('UTF-8')
    k=kml.KML()

    k.from_string(doc)
    features= list(k.features())

    
    f2=list(features[0].features())
    outpt=TimeCalcu()
    

    for i in range(len(f2)):
    
        start=f2[i].begin
        last=f2[i].end
        
        try:
            print(f2[i].geometry)
        except:
            continue
        if "POINT" in str(f2[i].geometry):
            
            lon=f2[i].geometry.x
            lat=f2[i].geometry.y
            x1=6371*cos(lat)*cos(lon)
            y1=6371*cos(lat)*sin(lon)
            startsec=start.hour*3600+start.minute*60+start.second
            T=last-start
            lastsec=last.hour*3600+last.minute*60+start.second
            currsec=startsec
            if startsec%30 !=0:
                currsec=startsec+30-(startsec%30)
            currsec=currsec+30
            while currsec<=lastsec:
                #print(str(currsec)+" "+str(x1)+" "+str(y1))
                outputf.write(str(currsec)+" "+str(x1)+" "+str(y1)+"\n")
                currsec=currsec+30
        else:
            
            line=f2[i].geometry
            linelist=list(line.coords)
        
            x=0
            y=0
            di=0
            dist={}
            xyconv=[]
            sum=0
            for positions in linelist:
            
                lon=positions[0]
                lat=positions[1]
                x1=6371*cos(lat)*cos(lon)
                y1=6371*cos(lat)*sin(lon)
                tup=(x1,y1)
                xyconv.append(tup)
                if x==0 and y==0:
                    x=x1
                    y=y1
                    pass
                else:
                    dist[di]=sqrt((x-x1)**2+(y-y1)**2)
                    sum=sum+dist[di]
                    di=di+1
                    print(dist[di-1])
                    x=x1
                    y=y1
            
            
            T=last-start        
            startsec=start.hour*3600+start.minute*60+start.second
            if sum==0:
                lastsec=last.hour*3600+last.minute*60+start.second
                currsec=startsec
                if startsec%30 !=0:
                    currsec=startsec+30-(startsec%30)
                currsec=currsec+30
                while currsec<=lastsec:
                
                    outputf.write(str(currsec)+" "+str(x)+" "+str(y)+"\n")
                    currsec=currsec+30
                continue
            totsec=T.total_seconds()
            outpt.getfile(startsec,totsec,dist,xyconv,sum,outputf)
    outputf.close()
