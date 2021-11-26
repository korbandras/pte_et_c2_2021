def ismetlodesek(list: list[float])->list[float]:
    ismetlodo_szamok=[]
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]==list[j] and list[j] not in ismetlodo_szamok:
                ismetlodo_szamok.append(list[i])
    return ismetlodo_szamok
def kisebb(list: list[float],limit: float)->int:
    kisebbek=0
    for szam in list:
        if szam<limit:
            kisebbek+=1
    return kisebbek
def primek(szam:int)->None:
    maradek=szam
    oszto=2
    while maradek>1:
        if maradek%oszto==0:
            maradek=maradek//oszto
            print(oszto)
        else:
            oszto+=1