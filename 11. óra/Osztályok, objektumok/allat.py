class Macska:
    """macskák osztálya"""
    def __init__(self,nev: str,fajta: str):
        self.nev=nev
        self.fajta=fajta
        self.kaja=100
        self.ihatnek=100
        self.kedv=100

    def jatek(self, idotartam: int):
        self.kedv+=idotartam
        if self.kedv>100:
            self.kedv=100
        self.ihatnek-=10
        if self.ihatnek<0:
            self.ihatnek=0
        self.kaja-=20
        if self.kaja<0:
            self.kaja=0

    def allapot(self):
        print(self.nev,"jóllakottsága:",self.kaja,"szomjúsága:",self.ihatnek,"kedve:",self.kedv)

