import math
#gömb térfogat
def f1():
    r=int(input("Kérem a gömb sugarát cm-ben: "))
    pi=math.pi
    v=(4*r**3*pi)/3
    print("%.2f cm^3 a gömb térfogata" %v)
#2 koordináta közti táv
def f2():
    k1_1=int(input("Kérem az első pont első koordánátáját: "))
    k1_2=int(input("Kérem az első pont második koordánátáját: "))
    k2_1=int(input("Kérem az második pont első koordánátáját: "))
    k2_2=int(input("Kérem az második pont második koordánátáját: "))
    tav=math.sqrt((k2_1-k1_1)**2+(k2_2-k1_2)**2)
    print("A 2 megadott pont távolsága %.2f egység" %tav)
#szavak hossza kiírva ha 10 karakternél hosszabbak
def f3():
    be=open("EP2_3.txt","r")
    for sor in be:
        if len(sor)>10:
            print("%s hossza: %d\n" %(sor,len(sor)-1))
#nem tudom hova tűnt a 4. feladat
#szobafestes
def f5():
    szoba=75
    festek_lefed=15
    festek_ara=4300
    festo_ido=13
    festo_oraber=2100
    festek_kell=szoba*2//festek_lefed*festek_ara
    print("%d Ft értékben kell vegyen festéket" %festek_kell)
    netto=szoba*2*festo_ido*festo_oraber/60
    print("Nettó %d Ft-ért festi ki a festő a szobát" %netto)
    print("Bruttó %d Ft-ért festi ki a festő a szobát" %(netto*1.27))
#-----------------------------------------
f1()
f2()
f3()
f5()