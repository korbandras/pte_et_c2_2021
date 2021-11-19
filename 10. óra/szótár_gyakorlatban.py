#rgb kóódok
def beolvasas(filepath: str):
    szinek={}
    try:
        fileobject=open(filepath,'r')
        for sor in fileobject:
            sor_adat=sor.split()
            szinek[sor_adat[1]]=(sor_adat[3],sor_adat[4],sor_adat[5])
        fileobject.close()
    except FileNotFoundError:
        print("Nem találom a filet!")
    return szinek

szin_szotar=beolvasas("color.csv")
print(szin_szotar)
print(type(szin_szotar))