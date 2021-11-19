def menu_options():
    print("Kérem válasszon az alábbi menüpontokból:\n\t"
          "0 - Kilépés""\n\t"
          "1 - Új fa regisztálása\n\t"
          "2 - Adott koordinátán lévő fafaj regisztálása\n\t"
          "3 - Fák és koordinták listázása\n\t"
          "4 - Fafajták listázása\n\t"
          "5 - <Nem elérhető>\n\t"
          "6 - Fafajta alapján koordináták kilistázása")
def egesz_szam_bekerese(koordinata: str)->int:
    szam=""
    while szam=="":
        try:
            szam=int(input(f"Kérem adja meg {koordinata} koordinátát"))
        except ValueError:
            print('Nem pozitív egész számot adott meg.')
    return szam
def fa_regisztalasa(fak: dict):
    x=egesz_szam_bekerese('x')
    y=egesz_szam_bekerese('y')
    hely=(x,y)
    if hely not in fak:
        fafajta=input("Kérem adja meg a fa fajtáját: ")
        fak[hely]=fafajta
    else:
        print("Itt már áll egy fa, ide nem regisztálhat új fát")
def fafaj_lekerese(fak: dict):
    x = egesz_szam_bekerese('x')
    y = egesz_szam_bekerese('y')
    hely = (x, y)
    if hely not in fak:
        print("Ezen a helyen {} fajta fa áll".format(fak[hely]))
    else:
        print("Ezen a koordinátán nincs fa")
def fafajtak_kiiratasa(fak: dict):
    fafajtak=[]
    for i in fak:
        if fak[i] not in fafajtak:
            fafajtak.append(fak[i])
    print("Fafaják:"+fafajtak)
def f5():
    print("<Nem elérhető>")
def fafajta_koordinatak(fak: dict):
    fajta=input("Milyen fafajta koordinátákra kíváncsi: ")
    koordinatak=""
    for i in fak:
        if fak[i]==fajta:
            koordinatak+=str(i)
    if koordinatak=="":
        print("Ilyen fa nincs a kertben!")
    else:
        print("Ezen koordinátákon vannak {} fák:: {}".format(fajta,koordinatak))
def szotar_kiiratasa(fak: dict):
    file = open("fak.csv", "w")
    for i in fak:
        file.write(str(i))
        file.write("\t")
        file.write(fak[i])
        file.write("\n")
    file.close()

menu=""
fak={}
while menu!="0":
    menu_options()
    menu=input()
    if menu=="1":
        fa_regisztalasa(fak)
    elif menu=="2":
        fafaj_lekerese(fak)
    elif menu=="3":
        print(fak)
    elif menu=="4":
        fafajtak_kiiratasa(fak)
    elif menu=="5":
        print("Még nincs kész")
    elif menu=="6":
        fafajta_koordinatak(fak)
szotar_kiiratasa()