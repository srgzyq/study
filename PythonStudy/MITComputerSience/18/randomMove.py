#coding=utf-8
#模拟无规则运用 (simolate random walk)
# 1.Location (喝酒醉的位置) 2.CompassPt (走向东南西北) 3.Field(场地,笛卡尔平面)
# 4.Drunk (醉汉)

import math, random, pylab

class Location(object):
    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)
    def move(self,xc,yc):
        return Location(self.x+float(xc), self.y+float(yc))
    def getCoords(self):
        return self.x, self.y
    def getDist(self,other):
        ox, oy = other.getCoords()
        xDist = self.x - ox
        yDist = self.y - oy
        return math.sqrt(xDist**2+yDist**2)

class CompassPt(object):
    # 北,南,东,西 
    possibles = ('N','S','E','W')
    def __init__(self,pt):
        if pt in self.possibles: self.pt = pt
        else: raise ValueError('in CompassPt.__init__')
    def move(self, dist):
        if self.pt == 'N': return(0,dist) 
        elif self.pt == "S": return(0,-dist)
        elif self.pt == "E": return(dist,0)
        elif self.pt == "W": return(-dist,0)
        else: raise ValueError("in CompassPt.move")

class Field(object):
    def __init__(self,drunk,loc):
        self.drunk = drunk
        self.loc = loc
    def move(self,cp,dist):
        oldLoc = self.loc
        xc, yc = cp.move(dist)
        self.loc = oldLoc.move(xc,yc)
    def getLoc(self):
        return self.loc
    def getDruck(self):
        return self.drunk

class Drunk(object): 
    def __init__(self,name):
        self.name = name
    def move(self,field,time = 1):
        if field.getDruck() != self:
            raise ValueError("Drunk, move called with")
        for i in range(time):
            pt = CompassPt(random.choice(CompassPt.possibles))
            field.move(pt,1)

#assert False

def firstTest():
    drunk = Drunk('srgzyq')
    for i in range(3):
        f = Field(drunk, Location(0, 0))
        distances = performTrial(500,f)
        pylab.plot(distances)

    pylab.title("srgzyq walk")
    pylab.xlabel('Time')
    pylab.ylabel('Distance from Origin')

def performTrial(time, f):
    start = f.getLoc()
    distances = [0.0]
    for t in range(1, time + 1):
        f.getDruck().move(f)
        newLoc = f.getLoc()
        distance = newLoc.getDist(start)
        distances.append(distance)
    return distances

def performSim(time,numTrials):
    distLists = []
    for trial in range(numTrials):
        d = Drunk("Drunk" + str(trial))
        f = Field(d,Location(0,0))
        distances = performTrial(time,f)
        distLists.append(distances)
    return distLists

def ansQuest(maxTime,numTrials):
    means = []
    distLists = performSim(maxTime,numTrials)
    for t in range(maxTime+1):
        tot = 0.0
        for distL in distLists:
            tot += distL[t]
        means.append(tot/len(distLists))
    pylab.figure()
    pylab.plot(means)
    pylab.title("test")
    pylab.xlabel('Time')
    pylab.ylabel('distLists')


#firstTest()
ansQuest(1000,200)
#ansQuest(1,5)

pylab.show()
assert False


