import math
class Pont:
    def __init__(self,x: int,y: int):
        self.x=x
        self.y=y
    def tav(self,other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)

class Teglalap:
    '''A téglalap oldalait az óramutató járásával megegyezően vannak megadva'''
    def __init__(self,s1: Pont,s2: Pont,s3: Pont,s4: Pont):
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.s4=s4
    def oldalhosszak(self):
        return [self.s1.tav(self.s2),self.s1.tav(self.s4)]
    def kerulet(self):
        oldalhosszak=self.oldalhosszak()
        return oldalhosszak[0]+oldalhosszak[1]
    def terulet(self):
        oldalhosszak=self.oldalhosszak()
        return  oldalhosszak[0]*oldalhosszak[1]

class Negyzet(Teglalap):
    def __init__(self, s1: Pont, s2: Pont, s3: Pont, s4: Pont):
        super().__init__(s1,s2,s3,s4)
    def kerulet(self):
        return self.s1.tav(self.s2)*4
    def terulet(self):
        return self.s1.tav(self.s2)**2

'''
pl1=Pont(3,6)
pl2=Pont(5,21)
print("A p1 és p2 távolsága:",Pont.tav(pl1,pl2))
'''