def kacsak():
    prefixes="JKLMNOPQ"
    suffix="ack"
    for i in range(len(prefixes)):
        print(prefixes[i]+suffix)
#kacsak()
def megtalal(karakter: str,szoveg: str)-> int:
    pozicio=-1
    for i in range(len(szoveg)):
        if pozicio==-1 and szoveg[i]==karakter:
            pozicio=i
    return pozicio
str="a"
str2="Hallgató"
print(str2.find(str),megtalal(str,str2))
def kacsak_tanar(prefixes: str,suffix: str) -> str: #vagy def kacsak_tanar(prefixes="JKLMNOPQ",suffix="ack")->str:
    nevek=""
    for prefix in prefixes:
        nevek+=prefix+suffix+", "
    return nevek[0:-2]
print(kacsak_tanar("JKLMNOPQ","ack"))