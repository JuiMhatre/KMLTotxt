'''
Created on 01-Dec-2018

@author: juimh
'''
from math import atan,cos,sin, sqrt, floor, radians
class TimeCalcu(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def getfile(self,startsec,totsec,dist,xyconv,sum,file):
        totsec=int(totsec)
        
        totspeed=sum/totsec
        dist30=totspeed*30
        currdis=0
        currsec=startsec
        prevtup=()
        index=0
        for tup in xyconv:
            if prevtup==():
                prevtup=tup
                continue
            else:
                currtup=tup
                if currsec%30==0:
                    file.write(str(currsec)+" "+str(tup[0])+" "+str(tup[1])+"\n")
                    currsec=currsec+30
                    currdis=dist30
                    newx=prevtup[0]
                    newy=prevtup[1]
                    x1=prevtup[0]
                    y1=prevtup[1]
                    x2=currtup[0]
                    y2=currtup[1]
                    try:
                        slope=(y1-y2)/(x1-x2)
                    except:
                        slope=radians(90)
                        pass
                    theta=atan(slope)
                else:
                    tempsec=30-(startsec%30)
                    tempdis=totspeed/tempsec
                    x1=prevtup[0]
                    y1=prevtup[1]
                    x2=currtup[0]
                    y2=currtup[1]
                    try:
                        slope=(y1-y2)/(x1-x2)
                    except:
                        slope=radians(90)
                        pass
                    theta=atan(slope)
                    p=tempdis*cos(theta)
                    q=tempdis*sin(theta)
                    newx=x1+p
                    newy=y1+q
                    currsec=currsec+tempsec
                    currdis=tempdis
                    #print(str(currsec)+" "+str(newx)+" ,"+str(newy))
                    file.write(str(currsec)+" "+str(newx)+" "+str(newy)+"\n")
                    
                p=dist30*cos(theta)
                q=dist30*sin(theta)
                linesec=(dist[index]/dist30)*30
                #print("---------"+str(dist[index])+" "+str(dist30)+" "+str(currsec-startsec))
                while currsec-startsec <linesec:                        
                    newx=newx+p
                    newy=newy+q
                    currsec=currsec+30
                    currdis=currdis+30
                    totdis=sqrt((newx-prevtup[0])**2+(newy-prevtup[1])**2)
                    if totdis>=dist[index]:
                        continue
                    #print(str(currsec)+" "+str(newx)+" "+str(newy))
                    file.write(str(currsec)+" "+str(newx)+" "+str(newy)+"\n")
            index=index+1
